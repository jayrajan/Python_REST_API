# Code written by Jerin Rajan on 15th April 2020
# models.py - handles data and business logic (Model)

# IMPORTANT - Refer README.md file before running the script. It contains
# instructions on how to run the script

class calculation:
    # Int which specifies the range size
    size = 10000001
    # initialising the list of numbers to perform the sum operation
    numbers_to_add = []

    def __init__(self):
        # generating the list of numbers based on the input int size
        self.numbers_to_add = list(range(self.size))
# The function which performs the sum operation
    def total(self):
        # performing the sum operation
        response = str(sum(self.numbers_to_add))
        # outputting the response
        return response
