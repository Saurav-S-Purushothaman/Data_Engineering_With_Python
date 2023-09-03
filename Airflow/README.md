# Airflow DAGS pipeline for data transformation.

##1. simple_dag.py : read csv file as input and output json file \n 
   mycsv.csv : input csv file 
   fromAirflow.json : output json file
   
##2. postgres.py : This class connects to postgresDB in localhost \n
   Using a class for Postgres connection makes it simpler to write airflow dag code

##3. postgres_to_mongodb.py : Data pipeline that transfer data from postgres database to MongoDB \n
   Airflow DAG reads data from Postgres database and stores it in a csv file locally
   This csv file is read and inserted into MongoDB database
