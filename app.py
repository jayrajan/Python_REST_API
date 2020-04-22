#  Code written by Jerin Rajan on 15th April 2020
#  app.py - this file contains code that handles the
# entry & exit point to our application (View)

from flask import Flask
from service import ToDoService

# create an app instance
app = Flask(__name__)

# at the end point /
@app.route("/total", methods=["GET"])

def total():
    # creating an instance of class: ToDoService()
    b = ToDoService()
    # Extracting the respose from List_total service
    response = b.list_total()
    # return the reponse in the requested format
    return {"total": response}

# on running python app.py
if __name__ == '__main__':
    # run the flask app
    app.run(debug=True)
