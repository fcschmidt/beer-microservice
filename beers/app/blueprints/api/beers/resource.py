from flask import Blueprint
from flask_restful import Api, reqparse, fields, Resource

from beers.app.blueprints.api.models.beer_model import Beer as BeerModel
from beers.app.blueprints.api.models.ingredients_model import BeerIngredients as IngredientsModel

bp = Blueprint('beers_api', __name__, url_prefix='/api/v1')
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

ingredients_parser = reqparse.RequestParser()
ingredients_parser.add_argument('name', type=str)
ingredients_parser.add_argument('ingredients', type=dict)

resource_fields_ingredients = {
    'id': fields.Integer,
    'name': fields.String,
    'beer_id': fields.Integer,
}


class Beers(Resource):

    def __init__(self):
        self.beer_args = beers_parser.parse_args()
        self.ingredients_args = ingredients_parser.parse_args()

    def post(self):
        beer_name = self.beer_args['beer_name']
        description = self.beer_args['description']
        harmonization = self.beer_args['harmonization']
        color = self.beer_args['color']
        alcohol = self.beer_args['alcohol']
        temperature = self.beer_args['temperature']
        beer_image = self.beer_args['beer_image']
        beer_ingredients = self.ingredients_args['ingredients']

        beers = BeerModel(
            beer_name=beer_name.lower(),
            description=description,
            harmonization=harmonization,
            color=color,
            alcohol=alcohol,
            temperature=temperature,
            beer_image=beer_image
        )
        beers.save()

        beer_id = beers.id
        for i in beer_ingredients['names']:
            ingredients = IngredientsModel(
                name=i,
                beer_id=beer_id
            )
            ingredients.save()
        return {'message': 'Beer create successfully!'}

    def put(self):
        pass

    def delete(self):
        pass


def init_app(app):
    api.add_resource(Beers, '/beers', endpoint='beers')
    app.register_blueprint(bp)
