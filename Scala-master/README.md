# Scala

This project is a Scala project where we recreated an SQL Kernel Engine, which is a very enriching project for learning Scala. To make this project feasible, we decided to use only CSV files to insert the data. We did not implement all the nodes of a real database in this project, but we recreated the SELECT, WHERE, aggregation functions, as well as UNION. In the future, we will also attempt to recreate a join, although these algorithms are very complex.

## Developer Guide

- **Language**: Scala
- **Framework**: sbt
- **Recommended IDE**: Visual Studio Code or IntelliJ

## User Guide

To launch this project, run the following commands:

```
sbt compile
sbt run
```

### How does it work?

To start this project, we needed to create a KVStore, which is where we store our data. To do this, we decided to create a `KVStore` class with 5 main functions:
- `put`: allows data insertion via a CSV file.
- `get`: the `get` function searches for the value from the in-memory map; if not found, it searches the corresponding CSV file.
- `remove`: this method removes the key from the map.
- `contains`: checks if the key exists in the map.

To reduce mutability in the code, we decided to use the `val` declaration and Scala’s immutable collections. While this can present challenges when managing data, it offers advantages in terms of security and predictability of the code.

We have a second class, `Database`. The first function is `serializeTable`, which converts an object into a delimited string, giving us a simple format, and `deserializeTable`, the inverse function. These central functions allow us to create the necessary nodes for performing the various operations that will enable us to run queries.

Before discussing the nodes we created, we have two ways to create tables:
- `createTable` allows us to create an empty table by specifying the table name and columns.
- `loadTableFromCSV` allows us to convert a CSV into an SQL table.

The various nodes:
The different nodes are based on our `getTable` function, which searches the KVStore for the corresponding key, deserializes it via `deserializeTable`, and then uses `.map` to retrieve the data. This is used in:
- `projectTable` (a SELECT), which projects one or more columns into a new table.
- Our `filterTable` function or the WHERE clause, which, depending on the chosen operator and column, returns only the rows that meet the initial condition.
- `unionTables` first checks if the two tables have the same schema before performing the union of the two tables.

To take this project further, we created a simple parser using Regex to enable real SQL commands that you can test. There is a script for this.

## Conclusion

This SQL Kernel Engine project in Scala allowed us to explore relational database concepts in depth while using advanced Scala features. We successfully implemented fundamental SQL operations such as SELECT, WHERE, and UNION, as well as a simple parser to interpret SQL queries.

Although our implementation is basic compared to a full-fledged database management system, it provides a solid foundation for understanding the underlying mechanisms of SQL databases. The challenges we encountered, particularly in managing immutability and creating a CSV-based storage system, enhanced our understanding of the trade-offs in system design.

In the future, implementing joins and optimizing performance would be areas for improvement.
