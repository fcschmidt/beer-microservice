from flask_migrate import Migrate
from beers.app.ext.db import db

migrate = Migrate()


def init_app(app):
    migrate.init_app(app, db)
