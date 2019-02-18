from flask import Blueprint, jsonify
from flask_restful import Api, reqparse, fields, Resource

from beers.app.blueprints.api.models.beer_model import Beer as BeerModel
from beers.app.blueprints.api.models.ingredients_model import BeerIngredients as IngredientsModel


from beers.app.blueprints.api.utils import beers_serializer, ingredients_serializer

bp = Blueprint('rest_api', __name__, url_prefix='/api/v1')
api = Api(bp)


beers_parser = reqparse.RequestParser()
beers_parser.add_argument('beer_name', type=str)
beers_parser.add_argument('description', type=str)
beers_parser.add_argument('harmonization', type=str)
beers_parser.add_argument('color', type=str)
beers_parser.add_argument('alcohol', type=str)
beers_parser.add_argument('temperature', type=str)
beers_parser.add_argument('beer_image', type=str)


resource_fields = {
    'id': fields.Integer,
    'beer_name': fields.String,
    'description': fields.String,
    'harmonization': fields.String,
    'color': fields.String,
    'alcohol': fields.String,
    'temperature': fields.String,
    'beer_image': fields.String,
}


class ListBeers(Resource):

    def __init__(self):
        pass

    @staticmethod
    def get():
        query = BeerModel.get_all()
        serialized = beers_serializer(query)
        serialized[0]['ingredients'] = ['test', 'test']
        return jsonify(serialized)


ingredients_parser = reqparse.RequestParser()
ingredients_parser.add_argument('name', type=str)
ingredients_parser.add_argument('ingredients', type=dict)

resource_fields_ingredients = {
    'id': fields.Integer,
    'name': fields.String,
    'beer_id': fields.Integer,
}


class BeerIngredients(Resource):

    def __init__(self):
        self.ingredients_args = ingredients_parser.parse_args()

    @staticmethod
    def get():
        query = IngredientsModel.get_all()
        serialized = ingredients_serializer(query)
        return jsonify(serialized)


def init_app(app):
    api.add_resource(ListBeers, '/beers', endpoint='list_beers')
    api.add_resource(BeerIngredients, '/beers/ingredients', endpoint='ingredients')
    app.register_blueprint(bp)
