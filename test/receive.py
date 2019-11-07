#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pika

# Establish connection with RabbitMQ server
credentials = pika.PlainCredentials('guest', 'guest')
connection = pika.BlockingConnection(pika.ConnectionParameters('docker6', 5672, 'MQcluster_vhost', credentials))

channel = connection.channel()

# Function called for incomming messages
def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)

# Set up subscription on the queue
channel.basic_consume(queue='MQcluster_queue_direct', on_message_callback=callback, auto_ack=True)
channel.basic_consume(queue='MQcluster_queue_fanout1', on_message_callback=callback, auto_ack=True)
channel.basic_consume(queue='MQcluster_queue_fanout2', on_message_callback=callback, auto_ack=True)
channel.basic_consume(queue='MQcluster_queue_header', on_message_callback=callback, auto_ack=True)
channel.basic_consume(queue='MQcluster_queue_topic_first', on_message_callback=callback, auto_ack=True)
channel.basic_consume(queue='MQcluster_queue_topic_firstandsecond', on_message_callback=callback, auto_ack=True)
channel.basic_consume(queue='MQcluster_queue_topic_second', on_message_callback=callback, auto_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
