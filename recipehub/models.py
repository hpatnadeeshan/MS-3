from recipehub import db

class Cuisine(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cuisine_name = db.Column(db.String(255), nullable=False, unique=True)

    def __repr__(self):
        return self.cuisine_name

class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    recipe_name = db.Column(db.String(255), nullable=False)
    ingredients = db.Column(db.Text, nullable=False)
    preparation_steps = db.Column(db.Text, nullable=False)
    image_link = db.Column(db.String(255))

    # Foreign keys
    cuisine_id = db.Column(db.Integer, db.ForeignKey('cuisine.id'), nullable=False)
    cuisine = db.relationship('Cuisine', backref=db.backref('recipes', lazy=True))

    def __repr__(self):
        return "Recipe {}: {}".format(self.id, self.recipe_name)