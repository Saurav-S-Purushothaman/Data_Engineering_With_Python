from datetime import datetime 
from datetime import timedelta

from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator

import pymongo
import csv
import os
import pandas as pd

from postgres import Postgres

def queryPostgresSql():
    """ Queries postgres db, stores the result in csv file """ 
    database = Postgres()
    database.connect()
    database.cursor()

    # Query to select all records from table 
    query = "SELECT * FROM users ORDER BY name DESC"

    database.curr.execute(query)
    query_result = database.curr.fetchall()
    with open("query_result.csv", "w") as f:
        csv_writer = csv.writer(f)
        header=[("id","name","age","street_address","city")]
        csv_writer.writerows(header)
        csv_writer.writerows(query_result)

def insertToMongoDb():
    """ Inserts the extracted csv file Postgres db into MongoDb """
    client = pymongo.MongoClient("localhost",27017)
    db = client["demo"]
    collection = db["demo"]
    file_path = "/home/saurav/query_result.csv"
    data = pd.read_csv(file_path)
    data_dict = data.to_dict(orient="records")
    collection.insert_many(data_dict)


yesterday = datetime.now() - timedelta(days=1)
default_args = {
        "owner":"saurav",
        "start_date":yesterday,
        "retries":1,
        "retry_delay":timedelta(minutes=5),
        "schedule_interval":None
        }

with DAG("postgres_to_mongo",default_args=default_args) as dag:

    get_data_from_postgres = PythonOperator(
            task_id="get_data_from_postgres",
            python_callable=queryPostgresSql
    )

    bash_operator = BashOperator(
    task_id="print_current_directory",
    bash_command="pwd"
    )

    insertToMongoDb = PythonOperator(
            task_id="insert_data_to_mongo_db",  
            python_callable=insertToMongoDb
    )

    bash_operator>>get_data_from_postgres>>insertToMongoDb 
