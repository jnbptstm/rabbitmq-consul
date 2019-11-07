#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pika

# Establish connection with RabbitMQ server
credentials = pika.PlainCredentials('guest', 'guest')
connection = pika.BlockingConnection(pika.ConnectionParameters('docker6', 5672, 'MQcluster_vhost', credentials))

# Create channel over TCP connection
channel = connection.channel()

# Publish the message through the channel.
channel.basic_publish(exchange='MQcluster_exchange_direct',
                        routing_key='MQcluster_routing_key_direct',
                        body='Hello Direct!')
print(" [x] Sent 'Hello Direct!'")

channel.basic_publish(exchange='MQcluster_exchange_fanout',
                        routing_key='',
                        body='Hello Fanout!')
print(" [x] Sent 'Hello Fanout!'")

channel.basic_publish(exchange='MQcluster_exchange_topic',
                        routing_key='MQcluster_queue_topic.second',
                        body='Hello Topic!')
print(" [x] Sent 'Hello Topic!'")

connection.close()