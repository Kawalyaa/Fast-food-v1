"""Creating App"""

import os
"""we import os to get the exported environment variables listed in the .env"""
from flask import Flask
from instance.config import app_config
"""importing configurations from .config file in the instance folder"""


def creat_app(config_name):
    """Creating app using configurations in the dictionary from config file"""

    app = Flask(__name__, instance_relarive_config=True)

    app.config.from_object(app_config['config_name'])
    """This will load the default configuration"""

    app.config.from_pyfile('config.py')
    """This will load the configuration from the config file"""
    return app
