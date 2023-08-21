from datetime import datetime 
from datetime import timedelta

from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator  

import pandas as pd 


def CSVtoJSON():
    df = pd.read_csv("tmp/mycsv.csv")
    for i, r in df.iterrows():
        print(r["name"])
    df.to_JSON("fromAirflow.json",orient="records")

# arguments to be passed to the DAG
yesterday = datetime.now() - timedelta(days=1)
default_args = {
        "owner":"saurav",
        "start_date": yesterday,
        "retries":1,
        "retry_delay": timedelta(minutes=5)
        }

with DAG("mycsv_dag",default_args=default_args, schedule_interval=timedelta(minutes=5) )as dag:
    print_starting= BashOperator(task_id="starting",
            bash_command="echo 'Reading csv'")

    csv_to_json = PythonOperator(task_id="convertCSVtoJson",python_callable=CSVtoJSON)


    print_starting >> csv_to_json
