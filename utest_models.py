#  Code written by Jerin Rajan on 22nd April 2020
# Unit Testing
# Use below command to run unittest
# python -m unittest utest

from models import calculation
import unittest

# Initialisation
item = calculation()

class test_models(unittest.TestCase):

# TestCase01 - Testing if correct instance of the class is called
    def test_instance_of_calculation(self):
        self.assertIsInstance(item, calculation,
                             'Error: incorrect instance of class')
# TestCase02 - Testing if the dimension of the list is assigned
    def test_size_dimension(self):
        size_dimension = 10000001
        self.assertEqual(item.size,size_dimension,
                        'Error: incorrect size dimension detected')

# TestCase03 - Testing the sum calculation capability
    def test_total_response(self):

        # Test input list [0,1,2,3]
        item.numbers_to_add = list(range(4))
        # Calling an instance of total function
        d = item.total()
        # Expected sum of elements in list = '6'
        self.assertEqual(d,'6',
                        'Error: incorrect response from total() function ')

# TestCase04 - Testing the sum calculation in returning a string
#               for a test input list
    def test_total_string(self):
        # Test input list [0,1,2,3,4]
        item.numbers_to_add = list(range(5))
        e = item.total()
        # Expected results is a string of '10'
        self.assertNotEqual(e,10,
                          'Error: function giving a non-string response')

if __name__ == 'main':
    unittest.main()
