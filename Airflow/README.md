# Airflow DAGS pipeline for data transformation.

1. DAG to read file from local system. Make transformation and convert the format
  - simple_dag.py : read csv file as input and output json file  
  - mycsv.csv : input csv file 
  - fromAirflow.json : output json file
   
2. DAG that orchestrate a pipeline that takes data from postgresDB to MongoDB 
  - postgres.py : This class connects to postgresDB in localhost 
    - Using a class for Postgres connection makes it simpler to write airflow dag code
  - postgres_to_mongodb.py : Data pipeline that transfer data from postgres database to MongoDB 
    - Airflow DAG reads data from Postgres database and stores it in a csv file locally
    - This csv file is read and inserted into MongoDB database
