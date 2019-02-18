from flask import Blueprint, jsonify
from flask_restful import Api, reqparse, fields, Resource

from beers.app.blueprints.api.models.beer_model import Beer as BeerModel
from beers.app.blueprints.api.models.ingredients_model import BeerIngredients as IngredientsModel

from beers.app.blueprints.api.utils import beers_serializer

from beers.app.blueprints.api.responses import resp_not_items

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
        query_beers = BeerModel.get_all()

        if not query_beers:
            return resp_not_items()
        serialized = beers_serializer(query_beers)

        count = 0
        ingredients_list = []

        for beer in query_beers:
            quer_filter = IngredientsModel.filter_beer_id(beer.id)

            if quer_filter:
                for f in quer_filter:
                    ingredients_list.append(f.name)
                serialized[count]['ingredients'] = ingredients_list
                count += 1
                ingredients_list = []
        return jsonify(serialized)


def init_app(app):
    api.add_resource(ListBeers, '/beers', endpoint='list_beers')
    app.register_blueprint(bp)
