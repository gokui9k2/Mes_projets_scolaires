import os
import json
import assemblyai as aai
from dotenv import load_dotenv
from model import set_custom_prompt, qa_bot, final_result, db, llm
import time
from threading import Timer, Lock
from twilio.twiml.voice_response import VoiceResponse
from pathlib import Path
load_dotenv()

aai.settings.api_key = os.getenv('ASSEMBLYAI_API_KEY')

TWILIO_SAMPLE_RATE = 8000  # Hz

class TwilioTranscriber(aai.RealtimeTranscriber):
    def __init__(self):
        super().__init__(
            on_data=self.on_data,
            on_error=self.on_error,
            on_open=self.on_open,
            on_close=self.on_close,
            sample_rate=TWILIO_SAMPLE_RATE,
            encoding=aai.AudioEncoding.pcm_mulaw
        )
        self.llm_call_in_progress = False
        self.errors = []
        self.final_transcript = ""  # To store the final transcript
        self.timer = None
        self.delay_seconds = 2  # Buffer to prevent immediate processing

    def on_open(self, session_opened):
        print("Session ID:", session_opened.session_id)

    def on_data(self, transcript):
        if not transcript.text or self.llm_call_in_progress:
            return

        if isinstance(transcript, aai.RealtimeFinalTranscript):
            self.final_transcript = transcript.text  # Store the final transcript
            if self.timer:  # Cancel any existing timer
                self.timer.cancel()
            self.timer = Timer(self.delay_seconds, self.process_final_transcript)
            self.timer.start()

    def process_final_transcript(self):
        if self.final_transcript:
            print("Final Transcript:", self.final_transcript)
            response = self.generate_ai_response(self.final_transcript)
            print(response)

            # Définition du chemin du fichier JSON
            json_file_path = Path('interactions.json')
            
            # Vérification si le fichier existe pour charger les données existantes
            if json_file_path.exists() and json_file_path.stat().st_size != 0:
                with open(json_file_path, 'r') as file:
                    try:
                        data = json.load(file)
                    except json.JSONDecodeError:  # Si le fichier est vide ou corrompu
                        data = {"user": [], "ia": []}
            else:
                data = {"user": [], "ia": []}
            
            # Ajout des nouvelles interactions
            data["user"].append(self.final_transcript)
            data["ia"].append(response)
            
            # Sauvegarde de la mise à jour des données dans le fichier JSON
            with open(json_file_path, 'w') as file:
                json.dump(data, file, indent=4)

            self.final_transcript = ""

    def on_error(self, error):
        self.errors.append(str(error))

    def on_close(self):
        if self.errors:
            print("Errors occurred during the session:")
            for error in self.errors:
                print(error)
        else:
            print("No errors occurred during the session.")

    def generate_ai_response(self, transcript):
        self.llm_call_in_progress = True
        prompt = set_custom_prompt()
        qa = qa_bot(prompt, db, llm)
        response = final_result(transcript, qa)
        self.llm_call_in_progress = False
        return response
