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


class Tools(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tool_name = db.Column(db.String(255), nullable=False)
    brand_name = db.Column(db.String(255))
    
    def __repr__(self):
        return "Tool {}: {} (Brand: {})".format(self.id, self.tool_name, self.brand_name)

class RecipeTool(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    # Foreign keys
    recipe_id = db.Column(db.Integer, db.ForeignKey('recipe.id'), nullable=False)
    tool_id = db.Column(db.Integer, db.ForeignKey('tool.id'), nullable=False)

    # Relationships
    recipe = db.relationship('Recipe', backref=db.backref('recipe_tools', lazy=True))
    tool = db.relationship('Tool', backref=db.backref('recipe_tools', lazy=True))

    def __repr__(self):
        return "RecipeTool {}: Recipe {}, Tool {}".format(self.id, self.recipe_id, self.tool_id)