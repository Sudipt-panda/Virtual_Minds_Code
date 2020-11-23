from kafka import KafkaProducer
from time import sleep
import pandas as pd
import json


data = pd.read_csv('C:/Users/Sudipt Panda/Downloads/mysql.csv', sep = '\t', index_col = False)
mydict = [item for item in data.T.to_dict().values()]

producer = KafkaProducer(bootstrap_servers=['localhost:9092'],api_version=(0,10,1))
producer.send

c=0
for x in mydict:
    producer.send('virtual_minds', json.dumps(x).encode('utf-8'))
    #sleep(1)
    print('message sent',c)
    c=c+1

