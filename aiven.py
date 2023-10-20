'''
Your task is to create a Kafka service into Aiven and write a piece 
of code that produces valid JSON data to a topic in that service.

The key should be a valid JSON string containing a random id, e.g. UUID, 
and the message payload should be a valid JSON object. The payload should be 
a mock "event" from an interesting use case, e.g. IoT sensor, stock tickets, 
or financial transactions. The event should include a timestamp represented
by a string with the date in ISO 8601 format.

The producer's data should be readable from the Aiven web console from the 
Kafka service view > Topics => Topic => Fetch Messages (Format: json)

'''

from datetime import date
from kafka import KafkaProducer
import uuid
import json
import time
import random

loopLength = 10

#init Kafka connection 

producer = KafkaProducer(
 bootstrap_servers='kafka-dirk-dirk-aiven.a.aivencloud.com:13138',
 security_protocol="SSL",
 ssl_cafile="./ca.pem",
 ssl_certfile="./service.cert",
 ssl_keyfile="./service.key",
 value_serializer=lambda v: json.dumps(v).encode('ascii')
)

# create uuid 

for loop in range(0, loopLength):

   uniqueIdentifier = uuid.uuid4()
   sensorDataX = random()
   sensorDataY = random()
   payloadDate = date.today()
   
   producer.send(
    'dirk',
    value=
       {
        "key": str(uniqueIdentifier),
        "sensorDataX": sensorDataX,
        "sensorDataY": sensorDataY,
        "timestamp": str(payloadDate)
        }
   )
   producer.flush()

   time.sleep(10) 
