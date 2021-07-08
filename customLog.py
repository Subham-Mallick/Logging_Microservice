import pika
import sys
import json

def produceLog(log):
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    channel.exchange_declare(
        exchange='direct_logs', 
        exchange_type='direct')
    
    severity = log['logLevel']
    message = json.dumps(log)

    channel.basic_publish(
        exchange='direct_logs', 
        routing_key=severity, 
        body=message)
    print(" [x] Sent %r:%r" % (severity, message))
    connection.close()