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
