from beers.app.blueprints.api.schemas import BeerSchema, BeerIngredientsSchema
from beers.app.blueprints.api.models.ingredients_model import BeerIngredients as IngredientsModel

beers_schema = BeerSchema(strict=True)


def beers_serializer(content, state):
    serialized = beers_schema.dump(content, many=state).data
    return serialized


ingredients_schema = BeerIngredientsSchema(strict=True)


def ingredients_serializer(content, state):
    serialized = ingredients_schema.dump(content, many=state).data
    return serialized


def serializer(query):
    serialized = beers_serializer(query, True)
    serialized = add_ingredients(query, serialized)
    return serialized


def add_ingredients(query, serialized):
    count = 0
    ingredients_list = []
    for beer in query:
        quer_filter = IngredientsModel.filter_beer_id(beer.id)
        if quer_filter:
            for f in quer_filter:
                ingredients_list.append(f.ingredient_name)
            serialized[count]['ingredients'] = ingredients_list
            count += 1
            ingredients_list = []
    return serialized


def parser_beers(serialized, name):
    beers = []
    for beer in serialized:
        if name in beer['ingredients']:
            beers.append(beer)
    return beers


