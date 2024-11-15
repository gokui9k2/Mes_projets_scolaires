# Utiliser une image de base Python officielle
FROM python:3.8-slim

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier le fichier des dépendances et installer les dépendances
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copier les fichiers JSON et le reste de l'application dans le répertoire de travail
# Make sure to update the JSON filenames if you rename them
COPY ufc_database.ufc_fighters.json ./
COPY ufc_database.ufc_fight_1.json ./  
COPY init-mongo.sh ./
# Copier le reste de l'application dans le répertoire de travail
COPY . .

# Exposer le port sur lequel l'application va s'exécuter
EXPOSE 8050

# Utiliser Gunicorn pour exécuter l'application
CMD ["gunicorn", "-b", "0.0.0.0:8050", "--timeout", "120", "app:server"]
