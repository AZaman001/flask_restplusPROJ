"""
Main file to run the app.
"""
from flask import Flask
from apis.apiv1 import api

app = Flask(__name__)
api.init_app(app)
app.run(debug=True)