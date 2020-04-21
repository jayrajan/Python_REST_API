#  Code written by Jerin Rajan on 15th April 2020
# service.py - converts the request into a response
from models import calculation

class ToDoService:
    def __init__(self):
        self.c = calculation()

    def list_total(self):
        response = self.c.total()
        return response
