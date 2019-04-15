from beers.tests.scripts.populate_data_base import populate_beers


def test_create_new_ingredient_not_exist_beer_id(client, session):
    populate_beers(3)
    new_ingredient = {
        'ingredient_name': 'aveia',
        'beer_id': 10
    }
    response = client.post('/api/v1/ingredients', json=new_ingredient)
    assert response.status_code == 404

    expected = {
        'error': '10 does not exist.'
    }
    resp_json = response.get_json()
    assert resp_json['error'] == expected['error']


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

    expected = {
        'message': 'Ingredient added successfully!'
    }
    resp_json = response.get_json()
    assert resp_json['message'] == expected['message']


def test_delete_ingredient_not_exist(client, session):
    populate_beers(3)
    response = client.delete('/api/v1/ingredients/30')
    assert response.status_code == 404

    expected = {
        'error': '30 does not exist.'
    }
    resp_json = response.get_json()
    assert resp_json['error'] == expected['error']


def test_delete_ingredient(client, session):
    populate_beers(3)
    response = client.delete('/api/v1/ingredients/1')
    assert response.status_code == 202

    expected = {
        'message': 'Ingredient delete successfully!'
    }
    resp_json = response.get_json()
    assert resp_json['message'] == expected['message']
