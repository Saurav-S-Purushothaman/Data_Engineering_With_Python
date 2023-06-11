"""
Streaming data through pubsub into bigquery 
Architecture diagram given below 
website >> purchases topic >> dataflow >> bigquery analysis
mock data create through mockaroo.com 

"""

import json
import csv 
from google.cloud import pubsub_v1

project_name = "playground-s-11-ff3159aa"
topic_name = "purchases"
file = "MOCK_DATA.csv"

publisher = pubsub_v1.PublisherClient()
topic_path = publish.topic_path(project_name, topic_name) 

with open("MOCK_DATA.csv","r") as file : 
    rd = csv.Dictreader(file, delimiter = ",")
    for row in rd:
        data = json.dumps(dict(row))
        publisher.publish(topic_path, data = data.encode("utf-8")) 

