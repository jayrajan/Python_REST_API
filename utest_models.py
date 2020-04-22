#  Code written by Jerin Rajan on 22nd April 2020
# Unit Testing
# Use below command to run unittest
# python -m unittest utest

from models import calculation
import unittest

# Initialisation
item = calculation()

class test_models(unittest.TestCase):

    def test_size_dimension(self):
        size_dimension = 10000001
        self.assertEqual(item.size,size_dimension,
                        'incorrect consumer key detected')

    def test_size_of_list(self):
        pass


if __name__ == 'main':
    unittest.main()
