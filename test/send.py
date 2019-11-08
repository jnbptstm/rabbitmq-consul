#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pika

# Establish connection with RabbitMQ server
credentials = pika.PlainCredentials('guest', 'guest')
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost', port=5672, virtual_host='MQcluster_vhost', credentials=credentials))

# Create channel over TCP connection
channel = connection.channel()
properties=pika.BasicProperties(delivery_mode=2)

# Publish the message through the channel.
channel.basic_publish(exchange='MQcluster_exchange_direct',
                        routing_key='MQcluster_routing_key_direct',
                        body='Hello Direct!',
                        properties=properties)
print(" [x] Sent 'Hello Direct!'")

channel.basic_publish(exchange='MQcluster_exchange_fanout',
                        routing_key='',
                        body='Hello Fanout!',
                        properties=properties)
print(" [x] Sent 'Hello Fanout!'")

channel.basic_publish(exchange='MQcluster_exchange_topic',
                        routing_key='MQcluster_queue_topic.second',
                        body='Hello Topic!',
                        properties=properties)
print(" [x] Sent 'Hello Topic!'")

headers={"arg1":"val1", "arg2":"val2"}
properties=pika.BasicProperties(delivery_mode=2, headers=headers)
channel.basic_publish(exchange='MQcluster_exchange_headers',
                        routing_key='',
                        body='Hello Headers!',
                        properties=properties)
print(" [x] Sent 'Hello Headers!'")

connection.close()
