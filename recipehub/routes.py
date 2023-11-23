from flask import render_template
from recipehub import app, db
from recipehub.models import Cuisine, Recipe, Tools,RecipeTool
import random



@app.route("/")
def home():
    recipes = Recipe.query.all()
    # print(recipes[1])
    random_recipes = random.sample(recipes, 4)
    return render_template('index.html', recipes=random_recipes,is_index=True)


# Define the route for displaying a recipe
@app.route('/recipe/<int:recipe_id>')
def view_recipe(recipe_id):
    recipe = Recipe.query.get(recipe_id)

    return render_template('recipe.html', recipe=recipe)