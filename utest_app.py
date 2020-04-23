#  Code written by Jerin Rajan on 22nd April 2020
# Unit Testing
# Use below command to run unittest
# python3 -m unittest utest_app.py

from app import total
from service import ToDoService
import unittest

resp = total()

class test_models(unittest.TestCase):

    # TestCase01 - verifying the output for the function total()
    def test_response_req_total(self):
        self.assertEqual(resp,{"total": '50000005000000'},
                    'Error: incorrect response from total() ')

if __name__ == 'main':
    unittest.main()
