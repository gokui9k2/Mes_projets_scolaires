## French Version:
# SYNCLEAD

Ce projet était un projet entrepreneurial. L'objectif de ce projet était d'implémenter un LLM (modèle de langage) dans une boîte vocale téléphonique. Pour cela, nous avons utilisé Twilio, qui permet de créer des boîtes vocales personnalisées avec sa bibliothèque Python. Le résumé de l'appel est ensuite transféré dans un tableau de bord via une application utilisant Django.

## Scénario et contexte du projet

Il est généralement assez frustrant de tomber sur une boîte vocale en appelant une agence immobilière, surtout lorsque l'on doit déménager pour des raisons diverses. Par exemple, pour moi, étudiant d'outre-mer, il a été difficile de trouver un logement à Paris : j'ai passé de nombreux appels sans obtenir de réponse ni de suivi. C'est là que SYNCLEAD intervient. Notre projet permet à toute entreprise disposant d'un service client téléphonique d'intégrer un chatbot dans son répondeur. Ce dernier peut répondre aux appels en l'absence de personnel, puis un compte rendu de l'appel est envoyé à un conseiller commercial, etc.

## Guide utilisateur

Pour lancer notre projet, vous aurez besoin d'un fichier .env contenant un numéro Twilio (que vous pouvez acheter en ligne) ainsi que votre clé API Twilio. Il vous faudra aussi une clé API Ngrok afin de déployer le serveur sur Internet. Enfin, une clé API AssemblyAI est nécessaire pour la transcription des appels. Une fois le fichier .env configuré, il suffit d’appeler votre numéro Twilio et d’attendre la messagerie :)) Avant cela, lancez l’application avec la commande suivante :

```python
python main.py
```

## Comment ça fonctionne ?

La première étape a été de créer une base de données dans laquelle notre LLM pourrait puiser pour formuler ses réponses. Pour cela, nous avons créé le fichier `ingest.py`, qui génère une base de données vectorielle représentant les informations de notre agence immobilière. Lorsqu'une question est posée à un LLM, la phrase est vectorisée, puis une projection linéaire est effectuée sur ce vecteur afin de créer une matrice d'attention, ce qui permet au LLM de répondre de manière pertinente.

Dans le fichier `modele.py`, nous avons construit notre LLM. Nous avons testé Mistral AI et LLaMA, mais avons finalement choisi de poursuivre avec Mistral AI, qui nous paraissait plus robuste. Ce fichier contient également les réglages du modèle, notamment le nombre maximal de tokens en entrée et sortie, le prompt engineering, etc.

Dans `transcribe.py`, nous avons créé une classe `TwilioTranscriber`, qui réalise les transcriptions des appels afin d'envoyer ces données au LLM. Pour le moment, nous nous concentrons sur les transcriptions en anglais, mais dans le futur, il serait souhaitable de les étendre à d’autres langues.

La méthode `on_open` est utilisée pour initier une session de chat, ce qui pourrait être utile à l’avenir si nous voulons permettre plusieurs sessions en simultané avec le même numéro. C’est plus coûteux, mais réalisable avec Twilio. La méthode `on_data` est appelée à chaque réception de données vocales : une fois la phrase de l'utilisateur terminée, AssemblyAI détecte les fins de phrase avec un délai de 2 secondes, puis envoie les informations au LLM. Pendant le traitement des informations par le modèle, les autres données vocales ne sont pas enregistrées pour éviter tout dysfonctionnement. Cette classe inclut également une fonction pour gérer les erreurs, etc.

Le fichier `main.py` contient notre application. Nous avons décidé d'utiliser WebSocket, car avec un protocole HTTP classique, il n’était pas possible de créer ce type de projet. La communication avec WebSocket s’effectue via des fichiers JSON, et les informations reçues sont décodées pour être traitées par notre classe de transcription.

Voici un aperçu de notre application web avec le tableau de bord :
![Texte alternatif](images/Screenshot%20from%202024-11-14%2018-55-34.png)


## Conclusion

Ce projet a été très enrichissant techniquement. Nous avons découvert de nouvelles technologies comme WebSocket et les transformers. C’est l'un des projets les plus complexes auxquels j'ai été confronté, car la gestion des WebSocket ainsi que l'intégration avec Twilio n'étaient pas simples. Pour améliorer ce projet, nous pourrions essayer de le déployer sur le web via AWS, perfectionner le chatbot, qui comporte encore des erreurs, ou encore dockeriser l'application.

## English Version:

# SYNCLEAD

This project was an entrepreneurial initiative. The goal was to implement an LLM (language model) in a voicemail system. For this, we used Twilio, which allows you to create custom voicemail systems with its Python library. The call summary is then transferred to a dashboard via an application built with Django.

## Project Scenario and Context

It is often quite frustrating to reach a voicemail when calling a real estate agency, especially when moving for various reasons. For example, as an international student, finding accommodation in Paris was challenging: I made many calls without receiving any response or follow-up. This is where SYNCLEAD comes in. Our project enables any company with a telephone customer service to integrate a chatbot into their voicemail system. The bot can answer calls in the absence of staff, and then a summary of the call is sent to a sales advisor, etc.

## User Guide

To launch our project, you will need a `.env` file containing a Twilio number (which you can purchase online) along with your Twilio API key. You will also need an Ngrok API key to deploy the server online. Finally, an AssemblyAI API key is necessary for call transcription. Once the `.env` file is configured, just call your Twilio number and wait for the voicemail :) Before that, run the application with the following command:

```python
python main.py
```

## How does it work?

The first step was to create a database where our LLM could draw from to formulate its responses. To do this, we created the `ingest.py` file, which generates a vector database representing the information from our real estate agency. When a question is posed to the LLM, the sentence is vectorized, then a linear projection is made on this vector to create an attention matrix, which allows the LLM to provide relevant answers.

In the `modele.py` file, we built our LLM. We tested Mistral AI and LLaMA, but ultimately decided to go with Mistral AI, which we found to be more robust. This file also contains model settings, such as the maximum number of tokens for input and output, prompt engineering, etc.

In `transcribe.py`, we created a class called `TwilioTranscriber`, which handles the transcription of calls to send this data to the LLM. Currently, we are focusing on English transcriptions, but in the future, we plan to expand to other languages.

The `on_open` method is used to initiate a chat session, which could be useful in the future if we want to allow multiple sessions simultaneously with the same number. This is more costly but feasible with Twilio. The `on_data` method is called each time vocal data is received: once the user's sentence is finished, AssemblyAI detects sentence breaks with a 2-second delay, and then sends the information to the LLM. During the model's data processing, other voice data is not recorded to avoid any malfunction. This class also includes a function to handle errors, etc.

The `main.py` file contains our application. We decided to use WebSocket because with a standard HTTP protocol, it was not possible to build this type of project. Communication with WebSocket occurs via JSON files, and the received information is decoded for processing by our transcription class.

Here is a preview of our web application with the dashboard:

![Alt Text](images/Screenshot%20from%202024-11-14%2018-55-34.png)

## Conclusion

This project has been very rewarding technically. We discovered new technologies like WebSocket and transformers. It’s one of the most complex projects I’ve worked on, as managing WebSocket communication and integrating with Twilio was challenging. To improve the project, we could try deploying it on the web via AWS, refine the chatbot (which still has some errors), or even containerize the application.
