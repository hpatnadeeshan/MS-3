from recipehub import db
from flask_login import UserMixin
from datetime import datetime


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
    cuisine_id = db.Column(
        db.Integer, db.ForeignKey('cuisine.id'), nullable=False)
    cuisine = db.relationship(
        'Cuisine', backref=db.backref('recipes', lazy=True))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User', backref=db.backref('recipes', lazy=True))

    recipe_tool = db.relationship(
        'RecipeTool', backref='recipe',
        lazy=True, cascade='all, delete-orphan')

    def __repr__(self):
        return "Recipe {}: {}".format(self.id, self.recipe_name)


class Tools(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tool_name = db.Column(db.String(255), nullable=False)
    brand_name = db.Column(db.String(255))

    recipe_tool2 = db.relationship(
        'RecipeTool', backref='tools', lazy=True, cascade='all, delete-orphan')

    def __repr__(self):
        return "Tool {}: {} (Brand: {})".format(
            self.id, self.tool_name, self.brand_name)


class RecipeTool(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    # Foreign keys
    recipe_id = db.Column(
        db.Integer, db.ForeignKey('recipe.id'), nullable=False)
    tool_id = db.Column(db.Integer, db.ForeignKey('tools.id'), nullable=False)

    def __repr__(self):
        return "RecipeTool {}: Recipe {}, Tool {}".format(
            self.id, self.recipe_id, self.tool_id)


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    is_admin = db.Column(db.Boolean, nullable=False, default=False)

    def is_authenticated(self):
        return True  # Assuming all users are authenticated

    def is_active(self):
        return True  # Assuming all users are active

    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.id)

    def __repr__(self):
        return "id {}: username {}, password {}, is_admin {}".format(
            self.id, self.username, self.password, self.is_admin
        )


class ContactSubmission(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    message = db.Column(db.Text, nullable=False)
    submitted_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return (
            f"ContactSubmission(id={self.id}, "
            f"name={self.name}, email={self.email}, "
            f"submitted_at={self.submitted_at})"
        )
