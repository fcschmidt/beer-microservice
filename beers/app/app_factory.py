from beers.settings import app_config
from flask import Flask


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(app_config[config_name])

    # Initialize Extensions
    register_extensions(app)

    # Initialize Blueprints
    register_blueprints(app)

    return app


def register_blueprints(app):
    """Register Blueprints"""
    from beers.app.blueprints.api.beers import resource as beer_api
    from beers.app.blueprints.api.list_beers import resource as list_beers_api

    beer_api.init_app(app)
    list_beers_api.init_app(app)
    return app


def register_extensions(app):
    """Register extensions."""
    from beers.app.ext.db import db
    from beers.app.ext.migrate import migrate

    db.init_app(app)
    migrate.init_app(app, db)
    return app
