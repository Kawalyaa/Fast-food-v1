"""app initializer """
import os
"""We import this to get all that we had defined in the .env file"""
from app import create_app
"""We import app from __init__ file contained in our app subdirectory"""
config_name = os.getenv('FLASK_ENV')
"""Get the app settinng defined in the .env file"""

app = create_app(config_name)
"""Defining configuration to be used"""
if __name__ == '__main__':
    app.run()
