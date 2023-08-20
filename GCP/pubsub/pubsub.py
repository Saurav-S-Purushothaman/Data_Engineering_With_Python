from google.cloud import pubsub_v1
import requests 
import time 

project_name = "playground-s-11-ff3159aa"
topic_name ="mytopic"

api = "https://www.boredapi.com/api/activity"

publisher = pubsub_v1.PublisherClient()
topic_path = publisher.topic_path(project_name, topic_name)


while True:
  response = requests.get(api).text
  publisher.publish(topic_path , data = response.encode("utf-8"))
  time.sleep(10)

  