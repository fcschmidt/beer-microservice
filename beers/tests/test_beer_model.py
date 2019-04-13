from beers.tests.scripts.populate_data_base import populate_beers
from beers.app.blueprints.api.models.beer_model import Beer
from beers.tests.scripts.data import beers_data
from beers.app.blueprints.api.utils import beers_serializer


def test_create_beer(session):
    populate_beers(2)
    get_beer = Beer.get_beer_id(1)
    assert get_beer.id == 1
    assert get_beer.beer_name == beers_data[0]['beer_name']


def test_delete_beer(session):
    populate_beers(2)
    query_beer = Beer.get_beer_id(1)
    query_beer.delete()
    assert query_beer is not None
    assert query_beer.id == 1
    assert query_beer.beer_name == beers_data[0]['beer_name']


def test_update_beer(session):
    populate_beers(2)
    new_data = beers_data[1]
    query_beer = Beer.get_beer_id(1)
    Beer.update(query_beer, new_data)
    get_beer = Beer.get_beer_id(1)
    assert get_beer.id == 1
    assert get_beer.beer_name == beers_data[1]['beer_name']


def test_list_all_beers_empty(session):
    get_all_beers = Beer.get_beers()
    assert len(get_all_beers) == 0


def test_list_all_beers(session):
    populate_beers(2)
    get_all_beers = Beer.get_beers()
    serialized = beers_serializer(get_all_beers, True)
    assert len(serialized) > 0
    assert serialized[0]['beer_name'] == beers_data[0]['beer_name']


def test_filter_beer_by_name(session):
    populate_beers(2)
    beer_name = beers_data[0]['beer_name']
    query_filter_name = Beer.filter_beer_name(beer_name)
    serialized = beers_serializer(query_filter_name, True)
    assert serialized[0]['id'] == 1
    assert serialized[0]['beer_name'] == beers_data[0]['beer_name']


def test_filter_beer_by_color(session):
    populate_beers(2)
    beer_color = beers_data[0]['color']
    query_filter_color = Beer.filter_beer_color(beer_color)
    serialized = beers_serializer(query_filter_color, True)
    assert serialized[0]['color'] == beers_data[0]['color']
    assert serialized[0]['beer_name'] == beers_data[0]['beer_name']


def test_filter_beer_by_alcohol(session):
    populate_beers(2)
    beer_alcohol = beers_data[0]['alcohol']
    query_filter_alcohol = Beer.filter_beer_alcohol(beer_alcohol)
    serialized = beers_serializer(query_filter_alcohol, True)
    assert serialized[0]['alcohol'] == beers_data[0]['alcohol']
    assert serialized[0]['beer_name'] == beers_data[0]['beer_name']


def test_filter_beer_by_temperature(session):
    populate_beers(2)
    beer_temperature = beers_data[0]['temperature']
    query_filter_temperature = Beer.filter_beer_temperature(beer_temperature)
    serialized = beers_serializer(query_filter_temperature, True)
    assert serialized[0]['temperature'] == beers_data[0]['temperature']
    assert serialized[0]['beer_name'] == beers_data[0]['beer_name']
