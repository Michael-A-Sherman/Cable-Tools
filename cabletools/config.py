import os
import json

with open("cabletools/config.json") as config_file:
    config = json.load(config_file)


class Config:
    SECRET_KEY = config.get("SECRET_KEY")
    SERVER_NAME = config.get("SERVER_NAME")

