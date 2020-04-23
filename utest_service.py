#  Code written by Jerin Rajan on 22nd April 2020
# Unit Testing
# Use below command to run unittest
# python3 -m unittest utest_service.py

from service import ToDoService
import unittest

# Initialisation
inst = ToDoService()

class test_models(unittest.TestCase):

    def test_instance_ToDoService(self):
        # TestCase01 - Testing if correct instance of the class is called
            def test_instance_of_calculation(self):
                self.assertIsInstance(inst, ToDoService,
                                     'Error: incorrect instance of class')

if __name__ == 'main':
    unittest.main()
