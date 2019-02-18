from beers.app.ext.db import db


class Beer(db.Model):
    """Beers Model"""
    __tablename__ = 'beers'

    id = db.Column(db.Integer, primary_key=True)
    beer_name = db.Column(db.String, nullable=False, unique=False)
    description = db.Column(db.Text, nullable=False)
    harmonization = db.Column(db.Text, nullable=False)
    color = db.Column(db.String(40), nullable=False)
    alcohol = db.Column(db.String(40), nullable=False)
    temperature = db.Column(db.String(40), nullable=False)
    beer_image = db.Column(db.String)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @staticmethod
    def update(beer, data):
        beer.beer_name = data['beer_name']
        beer.description = data['description']
        beer.harmonization = data['harmonization']
        beer.color = data['color']
        beer.alcohol = data['alcohol']
        beer.temperature = data['temperature']
        beer.beer_image = data['beer_image']
        db.session.commit()

    @staticmethod
    def get_beers():
        return Beer.query.all()

    @staticmethod
    def get_beer_id(beer_id):
        return Beer.query.get(beer_id)

    def __repr__(self):
        return f'beers(id={self.id}, beer_name={self.beer_name}, description={self.description},' \
            f'harmonization={self.harmonization}, color={self.color}, alcohol={self.alcohol},' \
            f'temperature={self.temperature}, beer_image={self.beer_image})'

