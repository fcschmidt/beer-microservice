.PHONY: test install pep8 clean

test:
	@pytest --verbose --cov= --color=yes tests/


install:
	virtualenv -p python3.6 .venv
	source .venv/bin/activate
	pip install --upgrade pip
	pip install -r requirements.txt

migrate:
	flask db init
	flask db migrate -m "Created Beers Microservice"
	flask db upgrade

dropdb:
	dropdb beers

createdb:
	createdb beers

run:
	flask run

clean:
	rm -rf migrations
