# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

import os

from flask import Flask
from .extensions import db, bcrypt, migrate, jwt
from app.routes import AuthRoute, ProductRoute
from app.routes.auth import auth_blueprint

from importlib import import_module


def register_extensions(app):
    db.init_app(app)
    migrate.init_app(app, db)
    bcrypt.init_app(app)
    jwt.init_app(app)


def configure_database(app):
    @app.before_first_request
    def initialize_database():
        try:
            db.create_all()
        except Exception as e:
            print('> Error: DBMS Exception: ' + str(e))

    @app.teardown_request
    def shutdown_session(exception=None):
        db.session.remove()


def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)
    register_extensions(app)
    configure_database(app)
    app.register_blueprint(AuthRoute("auth", "/auth").bp)
    app.register_blueprint(ProductRoute("product", "/products").bp)

    return app
