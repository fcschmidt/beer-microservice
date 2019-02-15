from flask import Blueprint
from flask_restful import Api, reqparse, Resource


bp = Blueprint('beers_api', __name__, url_prefix='/api/v1')
api = Api(bp)


beers_parser = reqparse.RequestParser()
beers_parser.add_argument('beer_name', type=str)
beers_parser.add_argument('description', type=str)
beers_parser.add_argument('harmonization', type=str)
beers_parser.add_argument('color', type=str)
beers_parser.add_argument('alcohol_content', type=str)
beers_parser.add_argument('temperature', type=str)
beers_parser.add_argument('ingredients', type=str)
beers_parser.add_argument('beer_photo', type=str)


class Beers(Resource):

    def __init__(self):
        self.args = beers_parser.parse_args()

    @staticmethod
    def get():
        return {'message': 'estou funcionando!'}


def init_app(app):
    api.add_resource(Beers, '/beers', endpoint='beers')
    app.register_blueprint(bp)
