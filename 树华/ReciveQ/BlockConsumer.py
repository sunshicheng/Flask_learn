#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pika
import functools
import time


class BlockConsumer(object):
    EXCHANGENAME = 'blockpublishdemo'
    EXCHANGETYPE = 'direct'
    QUEUENAME = 'blockpublishdemoqueue'
    ROUTINGKEY = 'blockpublishroutingkey'

    def __init__(self, amqpurl):
        super().__init__()
        self._url = amqpurl
        self._connection = None
        self._channel = None
        self.create_connection()
        self.bind()

    def create_connection(self):
        try:
            self._connection = pika.BlockingConnection(pika.URLParameters(self._url))
            self._channel = self._connection.channel()
        except BaseException as e:
            print(e)

    def bind(self):
        if self._channel:
            try:
                self._channel.exchange_declare(exchange=self.EXCHANGENAME, exchange_type=self.EXCHANGETYPE,
                                               durable=True)
                self._channel.queue_declare(queue=self.QUEUENAME, durable=True)
                self._channel.queue_bind(exchange=self.EXCHANGENAME, queue=self.QUEUENAME, routing_key=self.ROUTINGKEY)
            except BaseException as e:
                print(e)
        else:
            print("does not exist channel")

    def add_message_callback(self, callback):
        if self._channel:
            try:
                fcallback = functools.partial(callback, instance=self)
                self._channel.basic_consume(queue=self.QUEUENAME, auto_ack=False, on_message_callback=fcallback)
                self._channel.start_consuming()
            except BaseException as e:
                print(e)
        else:
            print("does not exist channel")


if __name__ == '__main__':
    def message_callback(chan, method_frame, _header_frame, body, instance):
        print("receive message -->{1} --> {0}".format(time.time(),body))
        time.sleep(3)
        print("consumer done --> {0}".format(time.time()))
        chan.basic_ack(delivery_tag=method_frame.delivery_tag)

    consumer = BlockConsumer(amqpurl='amqp://guest:guest@localhost:5672/%2F?connection_attempts=3&heartbeat=3600')
    consumer.add_message_callback(message_callback)
