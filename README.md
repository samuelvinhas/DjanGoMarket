# DjanGoMarket

## Models

The models were inspired in a supermarket management project we made in the second year of our degree
Many M:N relationships were transformed into tables because the relationships had attributes

## Admin
The admin interface was used to manage the data in the database, and to test the models and relationships
- **User**: admin
- **Email**: admin@gmail.com
- **Password**: adminpass123!

## Populate DB
The `populate_db.py` script was used to populate the database with some initial data for testing purposes. It creates instances of the models and saves them to the database.
The script `migrate.sh` was used to run the migrations so we don't have to run the commands manually every time we make changes to the models