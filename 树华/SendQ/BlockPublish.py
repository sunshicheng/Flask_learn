#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pika
from pika.spec import BasicProperties
import json
import time


class BlockPublish(object):
    EXCHANGENAME = 'blockpublishdemo'
    EXCHANGETYPE = 'direct'
    QUEUENAME = 'blockpublishdemoqueue'
    ROUTINGKEY = 'blockpublishroutingkey'

    def __init__(self, amqp_url):
        super().__init__()
        self._url = amqp_url
        self._connection = None
        self._channel = None
        self.suspend = False
        self.suspends = []
        self.create_connection()
        self.bind_queue()

    def create_connection(self):
        try:
            # amqp: // username: password @ host:port / < virtual_host > [?query - string]
            self._connection = pika.BlockingConnection(pika.URLParameters(self._url))
            self._channel = self._connection.channel()
        except BaseException as e:
            print(e)
    def connection_on_blocked(self,connection,method):
        if isinstance(method,pika.spec.Connection.Blocked):
            self.suspend = True

    def add_connection_block(self):
        self._connection.add_on_connection_blocked_callback(self.connection_on_blocked)

    def connection_on_unblocked(self,connection,method):
        if isinstance(method,pika.spec.Connection.Unblocked):
            self.suspend = False
    def add_connection_unblock(self):
        self._connection.add_on_connection_unblocked_callback(self.connection_on_unblocked)

    def bind_queue(self):
        if self._channel:
            try:
                self._channel.exchange_declare(exchange=self.EXCHANGENAME, exchange_type=self.EXCHANGETYPE,
                                               durable=True)
                self._channel.queue_declare(queue=self.QUEUENAME, durable=True)
                self._channel.queue_bind(exchange=self.EXCHANGENAME, queue=self.QUEUENAME, routing_key=self.ROUTINGKEY)
                self._channel.confirm_delivery()
            except BaseException as e:
                print(e)
        else:
            print("does not exist channel")

    def publish_message(self, **kwargs):
        if self._channel:
            try:
                pro = BasicProperties(content_type='application/json', delivery_mode=2)

                self._channel.basic_publish(exchange=self.EXCHANGENAME, routing_key=self.ROUTINGKEY,
                                            body=json.dumps(kwargs), properties=pro)
                print("message has sent --> {0} --> {1}".format(kwargs, time.time()))
            except BaseException as e:
                print(e)
        else:
            print("does not exist channel")


if __name__ == '__main__':
    pub = BlockPublish(amqp_url='amqp://guest:guest@localhost:5672/%2F?connection_attempts=3&heartbeat=3600')
    counter = 0
    while True:
        time.sleep(1)
        if not pub.suspend:
            pub.publish_message(message=counter)
            counter += 1
        else:
            pub.suspends.append(counter)
