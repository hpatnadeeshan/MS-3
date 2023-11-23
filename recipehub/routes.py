from flask import render_template
from recipehub import app, db
from recipehub.models import Cuisine, Recipe, Tools,RecipeTool
import random



@app.route("/")
def home():
    recipes = Recipe.query.all()
    # print(recipes[1])
    random_recipes = random.sample(recipes, 4)
    return render_template('index.html', recipes=random_recipes)
