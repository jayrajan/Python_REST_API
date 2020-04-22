#  Code written by Jerin Rajan on 15th April 2020
# service.py - converts the request into a response (Controller)

from models import calculation

# defines all the supported services for user requests
class ToDoService:
    def __init__(self):
        # creating an instance of class calculation
        self.c = calculation()
    # including the calculation.total service
    def list_total(self):
        # calling the total function
        response = self.c.total()
        # returning the output calculated response
        return response
