# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

import os

from flask import Flask
from .extensions import db, bcrypt, migrate
from app.routes import AuthenRoute

from importlib import import_module


def register_extensions(app):
    db.init_app(app)
    migrate.init_app(app, db)
    bcrypt.init_app(app)


def configure_database(app):
    @app.before_first_request
    def initialize_database():
        try:
            db.create_all()
        except Exception as e:

            print('> Error: DBMS Exception: ' + str(e))

            # fallback to SQLite
            basedir = os.path.abspath(os.path.dirname(__file__))
            app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir,
                                                                                                          'db.sqlite3')

            print('> Fallback to SQLite ')
            db.create_all()

    @app.teardown_request
    def shutdown_session(exception=None):
        db.session.remove()


def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)
    register_extensions(app)
    configure_database(app)
    app.register_blueprint(AuthenRoute("auth", __name__))

    return app
