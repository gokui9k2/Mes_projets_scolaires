# PARK & SEE

Fictitious project for managing a car park in a French metropolitan area

## Project Scenario and Context

Your company has responded to a public tender for a large metropolitan area in France. This contract concerns the management of parking spaces, parking payment, and their monitoring.

This will allow for the study of usage, verification of user payments, and the management of parking violations (e.g., parking on sidewalks).

In the long run, this will help improve traffic flow and adapt parking habits, especially for the "last mile". The solutions will also need to be compatible with new low-emission zones for both circulation and parking. It will also be necessary to account for new regulations concerning paid parking for two-wheelers (2 and 3-wheel vehicles).

There is also a concern regarding the use of new modes of transport, such as electric scooters and "Uberized" electric scooters, which are often parked improperly. The contract requires several studies and tools to support the evolution of the metropolitan area's information system:

- Implementing a real-time tracking tool for used parking spaces.
- Recording (via sensors and/or video identification of license plates, vehicle type, electric or not, etc.) for studying data and usage (time and occupation of parking spaces).
- Deploying mobile terminals for municipal service providers (delegated by the city hall) and the police, responsible for monitoring parking payment (either remotely or on-site).
- Interface for users of parking spaces for remote tracking and payment (within the time limits defined by the city hall and parking zone laws).

## How does it work?

To start the project, simply run the following commands:

```bash
docker-compose build
docker-compose up
```

For this project, we decided to use AWS RDS (Relational Database Service) to gain experience with the cloud tools offered by AWS. The database and host configuration can be found in our `db_config.py` file. In the `CreerDB.py` file, you will find the database creation scripts. For a better understanding of the database architecture, here is an ER diagram:

![Database ER Diagram](images/Database%20ER%20diagram%20(crow's%20foot).png)

In the `app.py` file, you will find various endpoints that allow us to access the login, account creation, etc. We also added a function to send a notification when a vehicle's parking time is about to end, so our users can be more responsive.

### Templates:

#### Login:

![Screenshot](images/Screenshot%20from%202024-11-14%2015-02-14.png)

#### Register:

![Screenshot](images/Screenshot%20from%202024-11-14%2015-02-33.png)

#### Administrator Views:

![Administrator Views](images/Screenshot%20from%202024-11-14%2015-04-19.png)

![Administrator Tools](images/Screenshot%20from%202024-11-14%2015-04-45.png)

![Administrator Reports](images/Screenshot%20from%202024-11-14%2015-05-18.png)

#### Agent Views:

![Admin Dashboard](images/Screenshot%20from%202024-11-14%2015-05-51.png)

![User Profile](images/Screenshot%20from%202024-11-14%2015-06-26.png)

![User Settings](images/Screenshot%20from%202024-11-14%2015-06-43.png)

#### User Views:

![Admin Dashboard Overview](images/Screenshot%20from%202024-11-14%2015-07-03.png)

![Admin Settings](images/Screenshot%20from%202024-11-14%2015-07-41.png)

![Admin Tools](images/Screenshot%20from%202024-11-14%2015-07-56.png)

![User Management](images/Screenshot%20from%202024-11-14%2015-08-12.png)

#### Confirmation Email:

![Confirmation Email](images/Screenshot%20from%202024-11-14%2015-08-35.png)

#### Reservation Confirmation:

![Reservation Confirmation](images/Screenshot%20from%202024-11-14%2015-08-51.png)

#### 30 Minutes Before Reservation Ends:

![30 Minutes Before Reservation Ends](images/Screenshot%20from%202024-11-14%2015-09-07.png)

## TestDB.py

We also took care to add unit tests. Unfortunately, we couldn't automate them. It would be a good improvement to use tools like Jenkins to perform tests automatically. Another improvement would be to use SQL DBT to ensure the quality of the data entering the database.

# Conclusion

This project has been very educational. We were able to experiment with AWS cloud services and improve our database knowledge. For containerization, we chose to use a well-known framework. Among future improvements, we could automate the tests and verify data quality. Other features could also be added.

Any feedback on this project would be appreciated.
