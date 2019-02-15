from beers.app.blueprints.api.schemas import Beers


beers_schema = Beers(strict=True)


def beers_serializer(content):
    serialized = beers_schema.dump(content, many=True).data
    return serialized
