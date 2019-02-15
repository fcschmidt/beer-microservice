from beers.app.ext.db import db


class Beers(db.Model):
    """Beers Model"""
    __tablename__ = 'beers'

    id = db.Column(db.Integer, primary_key=True)
    beer_name = db.Column(db.String, nullable=False, unique=True)
    description = db.Column(db.Text, nullable=False)
    harmonization = db.Column(db.Text, nullable=False)
    color = db.Column(db.String(40), nullable=False)
    alcohol = db.Column(db.String(40), nullable=False)
    temperature = db.Column(db.String(40), nullable=False)
    ingredients = db.Column(db.String(40), nullable=False)
    beer_photo = db.Column(db.String(40), nullable=False)


class BeersQueries(Beers):

    def __init__(self):
        self.model = Beers()

    def create(self):
        db.session.add(self)
        db.session.commit()

    def update(self, data):
        self.beer_name = data['beer_name']
        self.description = data['description']
        self.harmonization = data['harmonization']
        self.color = data['color']
        self.alcohol = data['alcohol_content']
        self.temperature = data['temperature']
        self.ingredients = data['ingredients']
        self.beer_photo = data['beer_photo']
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit(self)
