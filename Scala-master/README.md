## French Version:
# Scala 

Ce projet est un projet Scala où nous avons recréé une SQL Kernel Engine, ce qui est un projet très enrichissant pour la connaissance de Scala. Pour rendre ce projet réalisable, nous avons décidé de n'utiliser que des fichiers CSV afin d'insérer les données. Nous n'avons pas réalisé tous les nœuds d'une vraie base de données dans ce projet, mais nous avons recréé le SELECT, WHERE, les fonctions d'agrégation, ainsi que UNION. Dans le futur, nous essaierons aussi de recréer une jointure, même si ces algorithmes sont très complexes.

## Architecture

![Architecture Diagram](img)

## Guide du Développeur

- **Langage** : Scala
- **Framework** : sbt
- **IDE recommandé** : Visual Studio Code ou IntelliJ 

## Guide Utilisateur

Pour lancer ce projet, exécutez les commandes suivantes :

```
sbt compile
sbt run
```

### Comment cela fonctionne ?

Afin de commencer ce projet, nous devions créer un KVStore, c'est là que nous stockerons nos données. Pour cela, nous avons décidé de créer une classe KVStore avec 5 fonctions principales : 
- put : qui permet d'insérer des données via un CSV 
- get : la fonction get recherche la valeur depuis la map en mémoire, si elle n'est pas trouvée, elle cherche le fichier CSV correspondant 
- remove : cette méthode permet de supprimer la clé de la map 
- contains : vérifie si la clé existe dans la map 

Afin de réduire la mutabilité de ce code, nous avons décidé d'utiliser la déclaration `val` et les collections immuables de Scala, ce qui peut poser des problèmes lors de la gestion des données, mais offre des avantages en termes de sécurité et de prévisibilité du code.

Nous avons une deuxième classe Database. La première fonction est `serializeTable` qui permet de convertir l'objet en chaîne de caractères séparée, ce qui nous donne un format plutôt simple, et `deserializeTable`, la fonction inverse. Ce sont ces fonctions centrales qui nous permettent de créer les nœuds nécessaires pour effectuer les différentes opérations qui nous permettront de faire des requêtes.

Avant de parler des nœuds que nous avons créés, nous avons deux manières de créer des tables :
- `createTable` permet de créer une table vide en donnant en argument le nom de la table ainsi que les différentes colonnes.
- `loadTableFromCSV` qui nous permet de convertir un CSV en table SQL.

Les différents nœuds :
Les différents nœuds sont basés sur notre fonction `getTable` qui va chercher dans le KVStore la clé correspondante, la désérialise via `deserializeTable`, puis avec un `.map` nous récupérons les données. Ceci est utilisé dans :
- `projectTable` (c'est un SELECT) qui nous projette une ou plusieurs colonnes dans une nouvelle table.
- Notre fonction `filterTable` ou le WHERE nous permet, en fonction d'un opérateur choisi et d'une colonne, de ne retourner uniquement les lignes qui répondent à la condition initiale.
- `unionTables` vérifie d'abord si les deux tables ont le même schéma avant d'effectuer l'union des deux tables.

Pour aller un peu plus loin dans ce projet, nous avons créé un petit parser en utilisant du langage Regex afin de pouvoir faire de vraies commandes SQL que vous pouvez tester. Il y a un script de code pour cela.

## Conclusion

Ce projet de SQL Kernel Engine en Scala nous a permis d'explorer en profondeur les concepts de base de données relationnelles tout en utilisant les fonctionnalités avancées de Scala. Nous avons réussi à implémenter les opérations fondamentales SQL comme SELECT, WHERE, et UNION, ainsi qu'un parser simple pour interpréter les requêtes SQL. 

Bien que notre implémentation soit basique comparée à un système de gestion de base de données complet, elle fournit une base solide pour comprendre les mécanismes sous-jacents des bases de données SQL. Les défis rencontrés, notamment dans la gestion de l'immuabilité et la création d'un système de stockage basé sur CSV, ont renforcé notre compréhension des compromis en conception de systèmes.

Pour l'avenir, l'implémentation de jointures et l'optimisation des performances seraient des axes d'amélioration.

## English Version:
# Scala

This project is a Scala project where we recreated a SQL Kernel Engine, which is a very enriching project for learning Scala. To make this project feasible, we decided to use only CSV files for data insertion. We didn't implement all the nodes of a real database in this project, but we recreated the SELECT, WHERE, aggregation functions, and UNION. In the future, we will also try to recreate a JOIN operation, although these algorithms are quite complex.

## Architecture

![Architecture Diagram](img)

## Developer Guide

- **Language:** Scala  
- **Framework:** sbt  
- **Recommended IDE:** Visual Studio Code or IntelliJ  

## User Guide

To launch this project, run the following commands:

```
sbt compile
sbt run
```

### How it works

To start this project, we had to create a KVStore, where we would store our data. To do this, we created a `KVStore` class with 5 main functions:
- `put`: which inserts data from a CSV
- `get`: the `get` function searches for the value in the in-memory map, and if it's not found, it looks for the corresponding CSV file
- `remove`: this method deletes the key from the map
- `contains`: checks if the key exists in the map

To reduce the mutability of this code, we decided to use the `val` declaration and Scala's immutable collections, which can cause challenges when managing data, but offer benefits in terms of code safety and predictability.

We also have a second class, `Database`. The first function is `serializeTable`, which converts the object into a string-separated format, giving us a rather simple format, and `deserializeTable`, the inverse function. These core functions allow us to create the necessary nodes to perform the different operations required for executing queries.

Before discussing the nodes we created, we have two ways to create tables:
- `createTable`: creates an empty table by passing the table name and column details as arguments.
- `loadTableFromCSV`: converts a CSV file into a SQL table.

### The various nodes:
The nodes are based on our `getTable` function, which looks for the corresponding key in the KVStore, deserializes it using `deserializeTable`, and then, with `.map`, we retrieve the data. This is used in:
- `projectTable` (which is a SELECT) that projects one or more columns into a new table.
- Our `filterTable` function, or WHERE clause, which allows us to return only the rows that satisfy the initial condition based on a chosen operator and column.
- `unionTables` first checks if the two tables have the same schema before performing the union of the two tables.

To take this project a step further, we created a small parser using Regex to allow for real SQL commands, which you can test. There’s a code script for that.

## Conclusion

This SQL Kernel Engine project in Scala allowed us to deeply explore the concepts of relational databases while utilizing Scala’s advanced features. We successfully implemented fundamental SQL operations such as SELECT, WHERE, and UNION, as well as a simple parser to interpret SQL queries.

Although our implementation is basic compared to a complete database management system, it provides a solid foundation for understanding the underlying mechanisms of SQL databases. The challenges we faced, particularly with immutability and the creation of a CSV-based storage system, strengthened our understanding of trade-offs in system design.

For the future, implementing joins and optimizing performance would be areas for improvement.
