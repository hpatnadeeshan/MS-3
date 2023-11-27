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

    tools = db.session.query(Tools).join(RecipeTool).filter(RecipeTool.recipe_id == recipe_id).all()

    return render_template('recipe.html', recipe=recipe, tools=tools)



@app.route('/add_recipe', methods=['GET', 'POST'])
def add_recipe():
       # If the request method is GET, render the add_recipe.html template
    cuisines = list(Cuisine.query.order_by(Cuisine.cuisine_name).all())
    tools = list(Tools.query.order_by(Tools.tool_name).all())

    return render_template('add_recipe.html', cuisines=cuisines, tools=tools)