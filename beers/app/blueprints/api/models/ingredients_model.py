from beers.app.ext.db import db


class BeerIngredients(db.Model):
    """Beer Ingredients Model"""
    __tablename__ = 'ingredients'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    beer_id = db.Column(db.Integer, db.ForeignKey('beers.id'), nullable=False)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @staticmethod
    def update(ingredient, data):
        ingredient.name = data['name']
        ingredient.beer_id = data['beer_id']
        db.session.commit()

    @staticmethod
    def get_ingredients():
        return BeerIngredients.query.all()

    @staticmethod
    def get_ingredient_id(_id):
        return BeerIngredients.query.get(_id)

    @staticmethod
    def filter_beer_id(beer_id):
        return BeerIngredients.query.filter(BeerIngredients.beer_id == beer_id).all()

    def __repr__(self):
        return f'ingredients(id={self.id}, name={self.name}, beer_id={self.beer_id})'
