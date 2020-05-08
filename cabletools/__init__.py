from flask import Flask
from flask_cors import CORS
from cabletools.config import Config


app = Flask(__name__)
CORS(app)
app.config.from_object(Config)
from cabletools import routes
