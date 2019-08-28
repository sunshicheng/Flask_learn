"""
Author: ssc
Datetime: 2019/8/28 下午6:38
File : test_user_model.py

"""
import unittest
from app.models import User


class UserModelTestCase(unittest.TestCase):

    def test_password_setter(self):
        user = User(password='ssc')
        self.assertTrue(user.password_hash is not None)

    def test_no_password_getter(self):
        user = User(password='ssc')
        with self.assertRaises(AttributeError):
            user.password

    def test_password_verification(self):
        user = User(password='ssc')
        self.assertTrue(user.verify_password('ssc'))
        self.assertFalse(user.verify_password('fnn'))

    def test_password_salts_are_random(self):
        user = User(password='ssc')
        user1 = User(password='ssc')
        self.assertTrue(user.password_hash != user1.password_hash)
