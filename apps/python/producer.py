from kafka import KafkaProducer
import json

producer = KafkaProducer(bootstrap_servers='development-kafka-bootstrap-cp4i.cluster-roks-on-vpc-6b01-f54dfdb602b48210069b59bca45066bc-0000.eu-de.containers.appdomain.cloud:443', ssl_cafile='/Users/jtarte/dev/kafka-strimzi/ca.crt', security_protocol="SSL")
for i in range(100):
    message = {'value': i}
    producer.send('topic2', json.dumps(message).encode('utf_8'))
producer.flush()

