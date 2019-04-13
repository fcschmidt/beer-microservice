from beers.tests.scripts.populate_data_base import populate_beers


def test_create_new_beer(client, session):
    new_beer = {
        'beer_name': 'Skoll',
        'description': 'A Cerveja Adriática 600ml foi criada pelo alemão Henrique Thielen, um visionário cervejeiro do início do século XX, ela teve seu nome em homenagem a cervejaria que traduz toda uma era de tradição passada de pai para filho. Hoje, conhecida como a irmã mais velha da Original, ela é uma cerveja pedida certa para a mesa de bar. Reconhecidamente uma cerveja puro malte de alta qualidade, fácil de beber e com aromas especiais que dão um toque equilibrado!.',
        'harmonization': 'Ela é leve e refrescante, por isso harmoniza muito bem com pratos leves! Assim, um sabor não vai sobrepor o outro!',
        'color': 'clara',
        'alcohol': '3',
        'temperature': '4',
        'ingredients': [
            {'names': ['cevada', 'lupulo', 'malte', 'trigo']}
        ]
    }
    response = client.post('/api/v1/beers', json=new_beer)
    assert response.status_code == 201

    resp_json = response.get_json()
    expected = {
        'message': 'Beer create successfully!'
    }
    assert resp_json['message'] == expected['message']


def test_update_beer_not_exist(client, session):
    populate_beers(2)
    update_beer = {
        'beer_name': 'Skoll',
        'description': 'A Cerveja Adriática 600ml foi criada pelo alemão Henrique Thielen, um visionário cervejeiro do início do século XX, ela teve seu nome em homenagem a cervejaria que traduz toda uma era de tradição passada de pai para filho. Hoje, conhecida como a irmã mais velha da Original, ela é uma cerveja pedida certa para a mesa de bar. Reconhecidamente uma cerveja puro malte de alta qualidade, fácil de beber e com aromas especiais que dão um toque equilibrado!.',
        'harmonization': 'Ela é leve e refrescante, por isso harmoniza muito bem com pratos leves! Assim, um sabor não vai sobrepor o outro!',
        'color': 'clara',
        'alcohol': '3',
        'temperature': '4',
        'ingredients': [
            {'names': ['cevada', 'lupulo', 'malte', 'trigo']}
        ]
    }
    response = client.put('/api/v1/beers/4', json=update_beer)
    assert response.status_code == 404

    expected = {
        'error': '4 does not exist.'
    }
    resp_json = response.get_json()
    assert resp_json['error'] == expected['error']


def test_update_beer(client, session):
    populate_beers(3)
    update_beer = {
        'beer_name': 'Skoll',
        'description': 'A Cerveja Adriática 600ml foi criada pelo alemão Henrique Thielen, um visionário cervejeiro do início do século XX, ela teve seu nome em homenagem a cervejaria que traduz toda uma era de tradição passada de pai para filho. Hoje, conhecida como a irmã mais velha da Original, ela é uma cerveja pedida certa para a mesa de bar. Reconhecidamente uma cerveja puro malte de alta qualidade, fácil de beber e com aromas especiais que dão um toque equilibrado!.',
        'harmonization': 'Ela é leve e refrescante, por isso harmoniza muito bem com pratos leves! Assim, um sabor não vai sobrepor o outro!',
        'color': 'clara',
        'alcohol': '3',
        'temperature': '4',
        'ingredients': [
            {'names': ['lupulo', 'malte', 'trigo']}
        ]
    }
    response = client.put('/api/v1/beers/2', json=update_beer)
    assert response.status_code == 200

    expected = {
        'message': 'Beer update successfully!'
    }
    resp_json = response.get_json()
    assert resp_json['message'] == expected['message']


def test_delete_beer_not_exist(client, session):
    populate_beers(3)
    response = client.delete('/api/v1/beers/10')
    assert response.status_code == 404

    expected = {
        'error': '10 does not exist.'
    }
    resp_json = response.get_json()
    assert resp_json['error'] == expected['error']


def test_delete_beer(client, session):
    populate_beers(3)
    response = client.delete('/api/v1/beers/1')
    assert response.status_code == 202

    expected = {
        'message': 'Beer delete successfully!'
    }
    resp_json = response.get_json()
    assert resp_json['message'] == expected['message']
