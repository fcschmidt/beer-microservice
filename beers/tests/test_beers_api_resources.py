

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
