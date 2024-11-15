# init-mongo.sh
mongoimport --host mongodb --db ufc_database --collection ufc_fighters --type json --file /data/ufc_database.ufc_fighters.json --jsonArray
mongoimport --host mongodb --db ufc_database --collection ufc_fight --type json --file /data/ufc_database.ufc_fight_1.json --jsonArray
