from app.models import Role

import unittest


class BlogModelTest(unittest.TestCase):
    def setUp(self):
        

         self.new_role = Role(name = "user")

    def test_init(self):
        self.assertEqual(self.new_role.name,"user") 