# Beers Catalog


Nesse serviço, encontra-se o acesso aos recursos do catalogo de cervejas.

**Principais tecnologias utilizadas:**

Solução desenvolvida em [python](https://www.python.org/) versão 3.6.8.

- [Flask](http://flask.pocoo.org/): Micro Framework Web.
- [PostgreSQL](https://github.com/fcschmidt/backend-challenge/blob/master): Banco de Dados Relacional de alta performance de código aberto.
- [Pycharm Professional](https://www.jetbrains.com/pycharm/): IDE de desenvolvimento Python.
- [Ubuntu](http://releases.ubuntu.com/16.04/): versão Ubuntu 16.04.5 LTS.
- [DBeaver](https://dbeaver.io/download/): Para visualização da Base de Dados. Cliente SQL e ferramenta de administração de banco de dados.
- [Postman](https://www.getpostman.com/): ferramenta para testar serviços RESTful (WEB APIs), por meio do envio de requisições HTTP.


## Preparando o Ambiente

**Iniciando o download do projeto:**

`$ git clone git@github.com:fcschmidt/beers-microservice.git`

Criando um arquivo `.env`.

**Adicionando as variáveis de ambiente:**

```text
export FLASK_APP=manage.py
export FLASK_ENV=development
DEBUG=True
DATABASE_URL='dialect+driver://username:password@host:port/database'
```

Sobre a configuração do SQLAlchemy [https://docs.sqlalchemy.org/en/latest/core/engines.html#database-urls](https://docs.sqlalchemy.org/en/latest/core/engines.html#database-urls).

Por default, se nenhum caminho for inserido no `DATABASE_URL`, ele irá criar uma base de dados usando SQLite no caminho `sqlite:////var/tmp/scheduling_dev.sqlite`.

**Criando um ambiente de desenvolvimento isolado com [virtualenv](https://virtualenv.pypa.io/en/latest/) ou [pipenv](https://virtualenv.pypa.io/en/latest/):**

`$ virtualenv -p python3.6 .venv.`

**Ativando o ambiente:**

`$ source .venv/bin/activate`.

**Instalando as dependências do sistema:**

`$ pip install -r requirements.txt`.

## Gerando Migrações

```text
flask db init
flask db migrate -m "Created Meeting Room"
flask db upgrade
```

## Executando a aplicação


## RestAPI


### Beers API

Cria, atualiza e deleta cervejas do catalogo.

|Método|URI|Código de Status|Resposta|
|-------|-------|-------|-------|
|POST|`http://localhost:5000/api/v1/beers`|201|Cerveja criada com sucesso.|
|PUT|`http://localhost:5000/api/v1/beers/<int:beer_id>`|200|Cerveja atualizada com sucesso.|
|DELETE|`http://localhost:5000/api/v1/beers/<int:beer_id>`|202|Cerveja deletada com sucesso.|

### Beers List API

Lista todas as cervejas do catalogo.

|Método|URI|Código de Status|Resposta|
|-------|-------|-------|-------|


## License
[MIT](https://opensource.org/licenses/MIT) © Fábio Schmidt