import unittest
from app.models import Subscriber

class SubModelTest(unittest.TestCase):

    def setUp(self):
        self.new_sub = Subscriber(username = 'ronald')

    def test_init(self):
        self.assertEqual(self.new_sub.username,'ronald') 