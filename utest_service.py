#  Code written by Jerin Rajan on 22nd April 2020
# Unit Testing
# Use below command to run unittest
# python3 -m unittest utest_service.py

# IMPORTANT - Refer README.md file before running the script. It contains
# instructions on how to run the script

from service import ToDoService
from models import calculation
import unittest

# Initialisation
inst = ToDoService()
inst1 = ToDoService().__init__()
a = ToDoService().list_total()

class test_models(unittest.TestCase):
            # TestCase01 - Testing if correct instance of the class is called
    def test_instance_of_Todoservice(self):
        self.assertIsInstance(inst, ToDoService,
                            'Error: incorrect instance of class ToDoService')
            # TestCase02 - Testing for response from function list_total()
    def test_instance_of_list_total(self):
        self.assertEqual(a,'50000005000000',
                        'Error: incorrect response from list_total() function ')


if __name__ == 'main':
    unittest.main()
