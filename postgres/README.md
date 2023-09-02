# Connecting to postgres database and reading/writing data

## postgres.py 
File for postgres Class
This class takes care of postgres database connection.
Methods for reading and writing data are available.

## insert_data.py
This file uses the Postgres class to connect to database and 
uses the faker library to insert 1000s of mock data to postgres database

## get_data.py
This file uses the Postgres class to connect to database.
Queries the database and stores the result in a csv file 

## read_with_pandas.py
This file uses the Postgres class to connect to database. 
Queries the database and stores the result in a Pandas DataFrame
