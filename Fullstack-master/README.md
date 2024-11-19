# FULL STACK DATA

This application uses Dash, a Python framework, with Flask and Docker for containerization.

## Developer Guide

- **Language:** Python  
- **Framework:** Dash  
- **Recommended IDE:** Visual Studio Code or PyCharm

## User Guide

To launch this project, run the following command:

```bash
docker-compose up --build
```

Here’s a preview of our application:

[Voir la vidéo](https://youtu.be/4NgM59sO4DM)

### How does it work?

### Backend:

#### `insert_data.py`

At the start of the project, we focused on inserting data into our PostgreSQL database. To do this, we first defined the types of various variables in the CSV file to avoid any type issues when using this database. To prevent duplication errors, we decided to delete the existing tables before each insertion. Then, we loaded the data in batches of 1000 rows.

#### `main.py`

In this file, we have initialized various functions to secure access to the API routes using JWT tokens. To ensure confidentiality, we use JWT tokens. How does it work? The user logs in with their credentials, and a request is then sent to the API to load the data. The data is subsequently retrieved through SQL queries using SQLAlchemy.

To avoid formatting errors, we defined a data schema with classes, notably `FighterData`, which makes it easier to manage the data as a list. While we could have used a dictionary, this format is more convenient for creating dataframes.


### Frontend:

For the front-end, we decided to create a fairly simple login and registration interface. This information is then sent to the users table, which stores all emails and passwords, which are hashed.
#### `request.py`

This file contains the functions necessary to access the API.

#### `data_process.py`

This file contains all the functions needed to process the data and create the charts.

#### `app.py`

This file initializes the Flask application and passes the processed data to the `index.html` page for dynamic rendering in JavaScript.

elastic_ingestion.py:

In this file, we process the data to create a dataframe containing information about different fighters. Then, we insert this data into an Elasticsearch container to enable searches in the dashboard.

### Docker:

Regarding Docker, we have three services:

- PostgreSQL database
- API
- Web application

## Conclusion

This project allowed us to explore Docker in more depth and manage a distributed application, which is different from simply running it locally. We had to carefully orchestrate our services to ensure smooth operation without errors. We also experimented with the JavaScript library Chart.js and considered a React version.

We would be happy to receive your feedback on our work!
