from flask import Flask
from cabletools.config import Config


app = Flask(__name__)
app.config.from_object(Config)

from cabletools import routes
