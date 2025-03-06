from datetime import datetime

# Airflow imports 
from airflow import DAG
from airflow.operators.python import PythonOperator

import uuid
import time
import requests
import json
import  logging

# kafka imports
from kafka import KafkaProducer



default_args = {
    "owner":"airscholar",
    "start_date": datetime(2025,3,5,1)
    }

def get_data():
    response = requests.get("https://randomuser.me/api/")
    data = response.json()
    
    response_1 = data["results"][0]
    # print(json.dumps(response_1),indent=4)
    
    return response_1

def format_data(response1):
    data_cleaned = {}
    
    location = response1['location']
    data_cleaned['id'] = uuid.uuid4()
    data_cleaned['first_name'] = response1['name']['first']
    data_cleaned['last_name'] = response1['name']['last']
    data_cleaned['gender'] = response1['gender']
    data_cleaned['address'] = f"{str(location['street']['number'])} {location['street']['name']}, " \
                              f"{location['city']}, {location['state']}, {location['country']}"
    data_cleaned['post_code'] = location['postcode']
    data_cleaned['email'] = response1['email']
    data_cleaned['username'] = response1['login']['username']
    data_cleaned['dob'] = response1['dob']['date']
    data_cleaned['registered_date'] = response1['registered']['date']
    data_cleaned['phone'] = response1['phone']
    data_cleaned['picture'] = response1['picture']['medium']

    return data_cleaned

    
def stream_data():
    

    current_time = time.time()
    producer =  KafkaProducer(
        
        bootstrap_servers = ["broker:29092"],
        max_block_ms = 5000
    )
    
    while True:
        if time.time() > current_time + 60:
            break
        try:
            res = get_data()
            res = format_data(res)
            producer.send("users_created", json.dumps(res).encode("utf-8"))
        
        except Exception as e:
            logging.error(f"Error is:  {e}")  



    # print(json.dumps(res,indent=4))

with DAG("user_automation",
        default_args=default_args,
        schedule="*/15 * * * *",
        catchup = False
) as dag:
    streaming_task = PythonOperator(
        task_id = "stream_data_from_api",
        python_callable = stream_data
    )
    
    