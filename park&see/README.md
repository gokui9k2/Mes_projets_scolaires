# PARK & SEE 

Projet fictif de gestion d'un parc automobile pour une agglomération française

[![](https://github.com/soyerg/it_equipe_4/raw/Eric/MaquetteCap/imagesReadme/landingscreen.png)](https://github.com/soyerg/it_equipe_4/blob/Eric/MaquetteCap/imagesReadme/landingscreen.png)

## Scénario et contexte du projet

Votre société a répondu à un appel d'offre public pour une très grande agglomération en France. Ce marché concerne la gestion des places de parking, le paiement du stationnement et le suivi de celles-ci.

Cela permettra l’étude des usages, la vérification du paiement des usagers et la gestion des délits de stationnement (stationnement sur trottoir, etc.).

À terme, cela permettra d’améliorer la fluidité du trafic et d'adapter les habitudes de stationnement, notamment pour le "dernier kilomètre". Les solutions devront être compatibles avec les nouvelles zones à faibles émissions pour la circulation et le stationnement. Il faudra également prendre en compte la nouvelle réglementation concernant le stationnement payant des deux-roues (2 et 3 roues).

Il y a aussi un enjeu concernant l'usage des nouveaux modes de transport, tels que les trottinettes électriques et les scooters électriques "uberisés", qui sont souvent mal stationnés. Le marché nécessite plusieurs études et outils permettant l'évolution du système d’information de l'agglomération :

- Mise en place d’un outil de suivi en temps réel des places de parking utilisées.
- Enregistrement (par capteur et/ou identification par vidéo des plaques d'immatriculation, type de véhicule, électrique ou non, etc.) pour l’étude des données et des usages (temps et occupation des places de parking).
- Mise en place de terminaux mobiles pour les prestataires municipaux (ayant délégation par la mairie) et la police, chargés du contrôle du paiement du stationnement (à distance ou non).
- Interface pour les usagers des places de parking pour le suivi et paiement à distance (dans la limite de temps définie par la mairie et les lois sur les zones de stationnement).

## Comment ça fonctionne ? 

Pour lancer le projet, il suffit d'exécuter les commandes suivantes : 

```bash
docker-compose build
docker-compose up
```

Pour ce projet, nous avons décidé d'utiliser AWS RDS (Relational Database Service) afin d'avoir une première expérience avec les outils cloud proposés par AWS. La configuration de la base de données et de l'hôte se trouve dans notre fichier de configuration `db_config.py`. Dans le fichier `CreerDB.py`, vous trouverez les scripts de création de la base de données. Pour une meilleure compréhension de l'architecture de notre base de données, voici un diagramme ER : 

![Diagramme ER](chemin/vers/ton/image)

Dans le fichier `app.py`, vous trouverez les différents endpoints qui nous permettent d’accéder au login, à la création de compte, etc. Nous avons également ajouté une fonction permettant d’envoyer une notification lorsque la fin du stationnement du véhicule approche, afin que nos utilisateurs soient plus réactifs.

## TestDB.py

Nous avons aussi pris soin d'ajouter des tests unitaires. Malheureusement, nous n'avons pas pu les automatiser. Ce serait une bonne amélioration d'utiliser des outils comme Jenkins pour effectuer des tests automatiquement. Une autre amélioration serait d'utiliser SQL DBT afin d'assurer la qualité des données qui entrent dans la base de données.

# Conclusion 

Ce projet a été très éducatif. Nous avons pu expérimenter avec les services cloud d’AWS et améliorer nos connaissances en matière de base de données. Pour la conteneurisation, nous avons choisi d'utiliser un framework bien connu. Parmi les améliorations futures, nous pourrions automatiser les tests et vérifier la qualité des données. D’autres fonctionnalités pourraient également être ajoutées.

Tout retour sur ce projet serait apprécié.
