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

