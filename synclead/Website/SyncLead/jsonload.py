import sys
import os
import json
import mysql.connector
import datetime  

def insert_json_data(user_id, file_path):
    if not os.path.exists(file_path):
        print("Le fichier JSON spécifié n'existe pas.")
        return

    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="Synclead"
        )
    except mysql.connector.Error as err:
        print("Erreur de connexion à la base de données MySQL:", err)
        return

    with open(file_path, 'r') as file:
        json_content = json.load(file)

    file_name, _ = os.path.splitext(os.path.basename(file_path)) 
    created_at = datetime.datetime.now()  
    caller = "+000000000000"
    emergency = "Non urgent"

    cursor = conn.cursor()
    insert_query = "INSERT INTO auth_app_jsonfile (user_id, json_content, file_name, created_at, caller, emergency) VALUES (%s, %s, %s, %s, %s, %s)"
    json_data = json.dumps(json_content)  
    cursor.execute(insert_query, (user_id, json_data, file_name, created_at, caller, emergency))
    conn.commit()
    conn.close()

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python jsonload.py <user_id> <file_path>")
        sys.exit(1)

    user_id = sys.argv[1]
    file_path = sys.argv[2]

    insert_json_data(user_id, file_path)