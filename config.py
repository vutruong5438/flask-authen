# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

import os, random, string


class Config(object):
    basedir = os.path.abspath(os.path.dirname(__file__))

    # Set up the App SECRET_KEY
    SECRET_KEY = os.getenv('SECRET_KEY', "you-will-never-know")
    if not SECRET_KEY:
        SECRET_KEY = ''.join(random.choice(string.ascii_lowercase) for i in range(32))

    # Set up JWT config
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY', "you-will-never-know")
    JWT_REFRESH_TOKEN_EXPIRES = os.getenv('JWT_REFRESH_TOKEN_EXPIRES', 60 * 60)

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    DB_ENGINE = os.getenv('DB_ENGINE', "postgresql")
    DB_USERNAME = os.getenv('DB_USERNAME', "odoo")
    DB_PASS = os.getenv('DB_PASS', "odoo")
    DB_HOST = os.getenv('DB_HOST', "localhost")
    DB_PORT = os.getenv('DB_PORT', 5432)
    DB_NAME = os.getenv('DB_NAME', "flask_authen")

    USE_SQLITE = False

    # try to set up a Relational DBMS
    if DB_ENGINE and DB_NAME and DB_USERNAME:
        try:
            # Relational DBMS: PSQL, MySql
            SQLALCHEMY_DATABASE_URI = '{}://{}:{}@{}:{}/{}'.format(
                DB_ENGINE,
                DB_USERNAME,
                DB_PASS,
                DB_HOST,
                DB_PORT,
                DB_NAME
            )
            USE_SQLITE = False
        except Exception as e:
            print('> Error: DBMS Exception: ' + str(e))


class DevelopmentConfig(Config):
    """Statement for enabling the development environment"""
    # Define the database - we are working with
    DEBUG = True


class ProductionConfig(Config):
    DEBUG = False


# Load all possible configurations
config_dict = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
}
