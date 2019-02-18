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

    @staticmethod
    def get_all():
        return Beer.query.all()

    def __repr__(self):
        return f'beers(id={self.id}, beer_name={self.beer_name}, description={self.description},' \
            f'harmonization={self.harmonization}, color={self.color}, alcohol={self.alcohol},' \
            f'temperature={self.temperature}, beer_image={self.beer_image})'

