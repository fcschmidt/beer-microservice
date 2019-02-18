from beers.app.blueprints.api.schemas import BeerSchema, BeerIngredientsSchema


beers_schema = BeerSchema(strict=True)


def beers_serializer(content):
    serialized = beers_schema.dump(content, many=True).data
    return serialized


ingredients_schema = BeerIngredientsSchema(strict=True)


def ingredients_serializer(content):
    serialized = ingredients_schema.dump(content, many=True).data
    return serialized
