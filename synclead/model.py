
from langchain_community.document_loaders import PyPDFLoader, DirectoryLoader
from langchain.prompts import PromptTemplate
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.llms import CTransformers
from langchain.chains import RetrievalQA
import re

import json 

# Chemin de la base de données FAISS
DB_FAISS_PATH = 'vectorstore1/db_faiss1'
LOG_FILE_PATH = 'Output/llm_interaction_log.json'


# Modèle de langage et base de données FAISS chargés une seule fois
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2",
                                   model_kwargs={'device': 'cpu'})
db = FAISS.load_local(DB_FAISS_PATH, embeddings)
llm = CTransformers(
    model = "mistral-7b-instruct-v0.1.Q4_0.gguf",
    #model_type="llama",
    max_new_tokens = 2000 ,
    temperature = 0.5,
    config = {'context_length' : 2048}
)

# Template de prompt
custom_prompt_template = """
You are the call assistant of the real estate agency "light". Use the following pieces of information to answer the user's question or provide information.
If the question cannot be answered with the information provided and if the question doesn't revolve around real estate , answer with "I don't know".
For example, if the client says : "I am Searching for an appartment"
Answer : "Sure, I'll search in our database what is available, are you searching for anaything in particular"
In the case where additional information is provided by the user for example and apartment he is searching for , propose a product based on the information provided.
If nothing corresponds, point out that you do not have something as close as what the user described, but you should still propose apartments (for example as close as 40 percent of what was asked)
Ask questions based on what the user said before.
Here is an example of a conversation : 


"Client:Goodmorning,I'm interested in finding a studio apartment to rent in the
downtown area.Can you assist me ?

You:Goodmorning! Certainly,I'd be happy to help you with your
search.Could you please provide me with some details about your preferences ? For
instance,do you have a specific budget in mind,any amenities you prioritize,or a
preferred move-indate?


"
Context: {context}
Question: {question}

Only return the helpful answer below and nothing else.
Helpful answer:
"""

def set_custom_prompt():
    """
    Prompt template for QA retrieval for each vectorstore
    """
    prompt = PromptTemplate(template=custom_prompt_template,
                            input_variables=['context', 'question'])
    return prompt

def retrieval_qa_chain(llm, prompt, db):
    qa_chain = RetrievalQA.from_chain_type(llm=llm,
                                           chain_type='stuff',
                                           retriever=db.as_retriever(search_kwargs={'k': 2}),
                                           return_source_documents=True,
                                           chain_type_kwargs={'prompt': prompt}
                                           )
    return qa_chain

def qa_bot(prompt, db, llm):
    qa = retrieval_qa_chain(llm, prompt, db)
    return qa

def final_result(query, qa):
    response = qa({'query': query})
    log_interaction(query, response["result"]) 

    return response["result"]  # Retourner uniquement la réponse



def clean_text(text):
    """
    Nettoie le texte en supprimant les sauts de ligne et les espaces excédentaires.
    Peut être étendu pour inclure d'autres nettoyages.
    """
    # Suppression des sauts de ligne et réduction des espaces multiples à un seul espace
    text = re.sub(r'\s+', ' ', text, flags=re.MULTILINE).strip()
    # Assurez-vous que la première lettre est en majuscule et que le texte se termine par un point.
    text = text[0].upper() + text[1:]
    if not text.endswith('.'):
        text += '.'
    return text

def log_interaction(input_text, output_text):
    """
    Enregistre les interactions utilisateur-modèle dans un fichier JSON après nettoyage.
    """
    # Nettoyage des textes d'entrée et de sortie
    cleaned_input = clean_text(input_text)
    cleaned_output = clean_text(output_text)

    interaction = {'input': cleaned_input, 'output': cleaned_output}
    try:
        with open(LOG_FILE_PATH, 'r+', encoding='utf-8') as file:
            data = json.load(file)
            data.append(interaction)
            file.seek(0)
            json.dump(data, file, indent=4)
    except FileNotFoundError:
        with open(LOG_FILE_PATH, 'w', encoding='utf-8') as file:
            json.dump([interaction], file, indent=4)

if __name__ == "__main__":
    print("Je suis l'avatar de real estate agency, comment puis-je vous aider ? Tapez 'quit' pour quitter.")

    prompt = set_custom_prompt()
    qa = qa_bot(prompt, db, llm)

    while True:
        user_input = input("Votre question: ")
        if user_input.lower() == 'quit':
            break
        answer = final_result(user_input, qa)
        print("Réponse:", answer)
