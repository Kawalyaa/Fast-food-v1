"""Creating App"""

# import os
# """we import os to get the exported environment variables listed in the .env"""
from flask import Flask
from my_config.config import app_config
"""importing configurations from .config file in the instance folder"""


from app.version1.views import food_app as v1
"""Importing Blueprint from the views file"""


def creat_app(config_name):
    """Creating app using configurations in the dictionary from config file"""

    app = Flask(__name__, instance_relative_config=True)

    app.register_blueprint(v1, url_prefix='/api/v1')

    app.config.from_object(app_config['development'])
    """This will load the default configuration"""

    # app.config.from_pyfile('config.py')
    # """This will load the configuration from the config file"""
    return app
