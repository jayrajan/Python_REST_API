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
                             'incorrect instance of class')
# TestCase02 - Testing if the dimension of the list is assigned
    def test_size_dimension(self):
        size_dimension = 10000001
        self.assertEqual(item.size,size_dimension,
                        'incorrect size dimension detected')

# TestCase03 - Testing the total calculation method response
    def test_total_response(self):
        c = item.total()
        self.assertEqual(c,'50000005000000','error')

# TestCase04 - Testing the sum calculation capability


if __name__ == 'main':
    unittest.main()
