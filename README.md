# Python_REST_API
The project is an implementation of the creation of a REST endpoint that is
capable of the following:
Generating a list of numbers for a given range: [0 - 1000000]
returns the total sum of the list of numbers

## PREREQUISITIE:
1. The program is scripted in Python3. Have the correct version of
   python installed.
2. The program is using flask framework to help create the endpoint. Install
   flask.
   Follow instructions - https://flask.palletsprojects.com/en/1.1.x/installation/#dependencies
3. The program is using the following libraries:
   * Flask
4. Please have the following files in the same directory:
   * app.py
   * service.py
   * models.py
   * utest_app.py
   * utest_models.py
   * utest_service.py
5. Web browser like Google Chrome

## INSTRUCTIONS:
   1. Please run script from a Terminal. Type python3 app.py
   2. Open your web browser and use link - http://localhost:5000/total
   3. The response of the endpoint will be presented on screen in the format:
      {
        "total": "50000005000000"
      }

## RUNNING THE TESTS:

Run the Unit Test by typing in the command: python3 -m unittest utest_models.py
Run the Unit Test by typing in the command: python3 -m unittest utest_service.py
Run the Unit Test by typing in the command: python3 -m unittest utest_app.py

## SOFTWARE ENGINEERING DOCUMENTATION:
Please refer to file Software_Design_Process to study the software lifecycle
process that was followed to engineer the 'total' endpoint
using the MVC framework

## Author
* Jerin Philips Rajan
