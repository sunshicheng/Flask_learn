#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pika
import time


def create_connection():
    try:
        connection = pika.BlockingConnection(
            pika.ConnectionParameters(host='localhost'))
        channel = connection.channel()
        channel.queue_declare(queue='wellque', durable=True)
        return channel
    except BaseException as e:
        print(e)


def callback(ch, method, properties, body):
    print("call back received -->{0}".format(time.time()))
    time.sleep(3)
    print("consume done ---> {0}".format(time.time()))
    print(" [x] Received %r" % body)
    ch.basic_ack(delivery_tag=method.delivery_tag,multiple=False)

def start_consume(channel):
    if channel:
        try:
            channel.basic_consume(
            queue='wellque', on_message_callback=callback, auto_ack=False)

            print(' [*] Waiting for messages. To exit press CTRL+C')
            channel.start_consuming()
        except BaseException as e:
            print(e)


if __name__ == '__main__':
    channel = create_connection()
    start_consume(channel)