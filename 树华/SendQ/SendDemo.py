#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pika
from pika.spec import BasicProperties
import json

import time

def create_connection():
    try:
         connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
         channel = connection.channel()
         channel.exchange_declare('xindi', durable=True)
         channel.queue_declare(queue='wellque',durable=True)
         channel.queue_bind(queue='wellque',exchange='xindi',routing_key='wellcrash')
         channel.confirm_delivery()
         return channel
    except BaseException as e:
        print(e)

def publish_message(channel):
    try:
        if channel:
            msg = {'crashid':45}
            pro = BasicProperties(content_type='application/json',delivery_mode=2)
            channel.basic_publish(exchange='xindi',routing_key='wellcrash',body=json.dumps(msg),properties=pro)
            print("message sent ---> {0}".format(time.time()))
    except BaseException as e:
        print(e)
# connection = pika.BlockingConnection(
#     pika.ConnectionParameters(host='localhost'))
# channel = connection.channel()
# channel.exchange_declare('lshbackup',durable=True,exchange_type='fanout')
# exchange = channel.exchange_declare('lsh',durable=True,arguments={'alternate-exchange':'lshbackup'})
# print(exchange.method.__class__)
# channel.queue_declare(queue='hellobackup',durable=True)
# channel.queue_declare(queue='hello',durable=True)
# channel.queue_bind(queue='hello',exchange='lsh',routing_key='xindi')
# channel.queue_bind(queue='hellobackup',exchange='lshbackup')
# channel.basic_publish(exchange='lsh', routing_key='xindi', body='Hello World!')
# print(" [x] Sent 'Hello World!'")
# connection.close()

if __name__ == '__main__':
    channel = create_connection()
    while True:
        time.sleep(1)
        publish_message(channel)
