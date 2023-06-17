from faker import Faker    # library used to generate random data
from google.cloud import pubsub_v1
import random
import json
from datetime import datetime
import time

PROJECT_ID = "playground-s-11-4bdc2db4"
TOPIC = "tweep"

# create the details

username = []
faker = Faker()
publisher = pubsub_v1.PublisherClient()
topic_path = publisher.topic_path(PROJECT_ID, TOPIC)

def publish(publisher, topic, message):
    """
    Function to publish message, encode it in utf-8
    :params = publisher- pubsub publisher client, topic - pubsub topic, message
    :return = publish object to topic
    """
    data = message.encode("utf-8")
    return publisher.publish(topic_path, data=data)

def generate_tweep():
    """
    Function to generate random tweeps
    :return data
    :rtype string
    """
    data = {}
    data["created_at"] = datetime.now().strftime("%d/%b/%Y:%H:%S")
    data["tweep_id"] = faker.uuid4()
    data["text"] = faker.sentence()
    data["user"] = random.choice(username)
    return json.dumps(data)

# Main method
if __name__ == "__main__":
    for i in range(200):
        profile = faker.simple_profile()
        username.append(profile["username"])
    while True:
        publish(publisher, topic_path, generate_tweep())
        time.sleep(0.5)