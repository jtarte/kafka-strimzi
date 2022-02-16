from encodings import utf_8
from kafka import KafkaProducer, KafkaConsumer
import json

consumer = KafkaConsumer('topic2', bootstrap_servers='development-kafka-bootstrap-cp4i.cluster-roks-on-vpc-6b01-f54dfdb602b48210069b59bca45066bc-0000.eu-de.containers.appdomain.cloud:443', ssl_cafile='/Users/jtarte/dev/kafka-strimzi/ca.crt', security_protocol="SSL",auto_offset_reset='earliest', enable_auto_commit=False)

for message in consumer:
    # message value and key are raw bytes -- decode if necessary!
    # e.g., for unicode: `message.value.decode('utf-8')`©
    print ("%s:%d:%d: value=%s" % (message.topic, message.partition,message.offset,message.value))