from beers.tests.scripts.populate_data_base import populate_beers


def test_create_new_ingredient_not_exist_beer_id(client, session):
    populate_beers(3)
    new_ingredient = {
        'ingredient_name': 'aveia',
        'beer_id': 10
    }
    response = client.post('/api/v1/ingredients', json=new_ingredient)
    assert response.status_code == 404


def test_create_new_ingredient_already_exists(client, session):
    populate_beers(3)
    new_ingredient = {
        'ingredient_name': 'cevada',
        'beer_id': 1
    }
    response = client.post('/api/v1/ingredients', json=new_ingredient)
    assert response.status_code == 400

    expected = {
        'error': 'An ingredient with this name already exists.'
    }
    resp_json = response.get_json()
    assert resp_json['error'] == expected['error']


def test_create_new_ingredient(client, session):
    populate_beers(3)
    new_ingredient = {
        'ingredient_name': 'mirtilo',
        'beer_id': 1
    }
    response = client.post('/api/v1/ingredients', json=new_ingredient)
    assert response.status_code == 201
