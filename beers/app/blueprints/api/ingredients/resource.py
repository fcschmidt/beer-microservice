from flask import Blueprint
from flask_restful import Api, reqparse, fields, Resource


bp = Blueprint('ingredients_api', __name__, url_prefix='/api/v1')
api = Api(bp)

ingredients_parser = reqparse.RequestParser()
ingredients_parser.add_argument('ingredient_name', type=str)

resource_fields_ingredients = {
    'id': fields.Integer,
    'ingredient_name': fields.String,
    'beer_id': fields.Integer,
}


class Ingredients(Resource):
    pass


def init_app(app):
    api.resource(Ingredients, '/ingredients', endpoint='ingredients')
    app.register_blueprint(bp)
