# Code written by Jerin Rajan on 15th April 2020
# models.py - handles everything that involves a Database.
class calculation:
    size = 10000001
    numbers_to_add = []

    def __init__(self):
        self.numbers_to_add = list(range(self.size))

    def total(self):
        response = str(sum(self.numbers_to_add))
        return response
