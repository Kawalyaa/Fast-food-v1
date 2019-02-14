import os
"""We import the OS since it is from the OS that we have set all the requrements in the venv."""


class Config(object):
    """Parent configuration class contains information that other environment will inherite."""
    DEBUG = False
    SECRET = os.getenv('SECRET')
    """This gets the SECRET key from our .env file"""
    DATABBASE_URI = os.getenv('DATABBASE_URL')
    """This gets the DATABASE_URL from the .env file"""


class DevelopmentConfig(Config):
    """Configurations for Development."""
    DEBUG = True


class TestingConfig(Config):
    """Configuration for testing with a seperate test database"""
    TESTING = True
    DATABASE_URI = 'Testing the URL for the test DB'
    DEGUG = True


class StagingConfig(Config):
    """Configurations for staging"""
    DEBUG = True


class ProductionConfig(Config):
    """Configurations for production"""
    TESTING = False
    DEBUG = False


app_config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'staging': StagingConfig,
    'production': ProductionConfig
}
