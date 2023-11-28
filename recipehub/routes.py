from flask import render_template, request, redirect, url_for
from recipehub import app, db
from recipehub.models import Cuisine, Recipe, Tools, RecipeTool
import random


@app.route("/")
def home():
    recipes = Recipe.query.all()
    # print(recipes[1])
    random_recipes = random.sample(recipes, 4)
    return render_template('index.html', recipes=random_recipes, is_index=True)


# Define the route for displaying a recipe
@app.route('/recipe/<int:recipe_id>')
def view_recipe(recipe_id):
    recipe = Recipe.query.get(recipe_id)

    tools = db.session.query(Tools).join(RecipeTool).filter(
        RecipeTool.recipe_id == recipe_id).all()

    return render_template('recipe.html', recipe=recipe, tools=tools)




new_recipes_data = [
    {
        'recipe_name': 'Sushi Rolls',
        'cuisine_id': 3,  # Japanese Cuisine
        'ingredients': 'Sushi rice, nori, fish (e.g., tuna, salmon), vegetables',
        'preparation_steps': 'Prepare sushi rice, place ingredients on nori, roll, and slice.',
        'image_link': 'https://as2.ftcdn.net/v2/jpg/06/21/61/79/1000_F_621617987_aep8cjHB9RdXrQkk32lvGiQErIzB6Eq2.jpg',
        'tools': [6, 2, 7, 12],  # Measuring Cups, Cutting Board, Measuring Spoons, Peeler
    },
    {
        'recipe_name': 'Chicken Fajitas',
        'cuisine_id': 4,  # Mexican Cuisine
        'ingredients': 'Chicken, bell peppers, onions, fajita seasoning, tortillas',
        'preparation_steps': 'Slice chicken and vegetables, sauté with fajita seasoning, serve in tortillas.',
        'image_link': 'https://as2.ftcdn.net/v2/jpg/00/89/81/29/1000_F_89812966_tFKNZ1u84JDlEY4wXQ186q31VQKaMBO6.jpg',
        'tools': [1, 2, 3, 8, 9, 14],  # Knife, Cutting Board, Spatula, Pots, Pans, Colander
    },
    {
        'recipe_name': 'Greek Salad',
        'cuisine_id': 9,  # Greek Cuisine
        'ingredients': 'Cucumbers, tomatoes, olives, feta cheese, red onion, olive oil',
        'preparation_steps': 'Chop vegetables, mix with olives and feta, drizzle with olive oil.',
        'image_link': 'https://as2.ftcdn.net/v2/jpg/06/01/41/97/1000_F_601419791_uc5aDyufhkA7K1dmIup0fbhQUykvvwad.jpg',
        'tools': [1, 2, 14, 20],  # Knife, Cutting Board, Colander, Mortar and Pestle
    },
    {
        'recipe_name': 'Pad Thai',
        'cuisine_id': 8,  # Thai Cuisine
        'ingredients': 'Rice noodles, shrimp, tofu, peanuts, bean sprouts, tamarind sauce',
        'preparation_steps': 'Soak noodles, stir-fry ingredients, add tamarind sauce, garnish with peanuts.',
        'image_link': 'https://as2.ftcdn.net/v2/jpg/05/82/28/31/1000_F_582283184_ujIxEouBpzMJtVec3z2dDqcbkU28vDco.jpg',
        'tools': [6, 2, 3, 4, 7, 20],  # Measuring Cups, Cutting Board, Spatula, Mixing Bowl, Measuring Spoons, Mortar and Pestle
    },
    {
        'recipe_name': 'Caprese Salad',
        'cuisine_id': 1,  # Italian Cuisine
        'ingredients': 'Tomatoes, fresh mozzarella, basil, balsamic glaze',
        'preparation_steps': 'Slice tomatoes and mozzarella, layer with basil, drizzle with balsamic glaze.',
        'image_link': 'https://as2.ftcdn.net/v2/jpg/02/22/33/85/1000_F_222338561_iOLR0dPFgfYhLp6NgQOOmQhyvxa2BSDk.jpg',
        'tools': [1, 2, 14, 21],  # Knife, Cutting Board, Colander, Pastry Brush
    },
    {
        'recipe_name': 'Chicken Teriyaki',
        'cuisine_id': 3,  # Japanese Cuisine
        'ingredients': 'Chicken thighs, soy sauce, sake, mirin, sugar, garlic, ginger',
        'preparation_steps': 'Marinate chicken, grill or pan-fry until cooked, glaze with teriyaki sauce.',
        'image_link': 'https://as1.ftcdn.net/v2/jpg/04/63/13/68/1000_F_463136844_iYuuMOmTHM974F9TsHNhc5TeAGZUrorv.jpg',
        'tools': [1, 2, 9, 13, 4],  # Knife, Cutting Board, Grill or Pan, Tongs, Mixing Bowl
    },
    {
        'recipe_name': 'Guacamole',
        'cuisine_id': 4,  # Mexican Cuisine
        'ingredients': 'Avocado, tomato, onion, lime, cilantro, salt',
        'preparation_steps': 'Mash avocados, add chopped tomatoes, onions, cilantro, lime juice, and salt.',
        'image_link': 'https://as1.ftcdn.net/v2/jpg/00/99/07/42/1000_F_99074252_aCglAEpkfqyR8Jrn1Z1teDnuvn0pYKBz.jpg',
        'tools': [1, 2, 4, 25, 20],  # Knife, Cutting Board, Mixing Bowl, Citrus Juicer, Mortar and Pestle
    },
]













@app.route('/add_recipe', methods=['GET', 'POST'])
def add_recipe():
    # If the request method is GET, render the add_recipe.html template
    cuisines = list(Cuisine.query.order_by(Cuisine.cuisine_name).all())
    tools = list(Tools.query.order_by(Tools.tool_name).all())

    for recipe_data in new_recipes_data:
    # Add the recipe
        new_recipe = Recipe(
            recipe_name=recipe_data['recipe_name'],
            cuisine_id=recipe_data['cuisine_id'],
            ingredients=recipe_data['ingredients'],
            preparation_steps=recipe_data['preparation_steps'],
            image_link=recipe_data['image_link']
        )

        db.session.add(new_recipe)
        db.session.commit()

        # Retrieve the ID of the newly added recipe
        new_recipe_id = new_recipe.id

        # Add tools for the new recipe
        for tool_id in recipe_data['tools']:
            recipe_tool = RecipeTool(recipe_id=new_recipe_id, tool_id=tool_id)
            db.session.add(recipe_tool)

        db.session.commit()





    if request.method == 'POST':

       # Create a new recipe
        new_recipe = Recipe(
            recipe_name=request.form.get('recipe_name'),
            cuisine_id=request.form.get('cuisine_name'),
            ingredients=request.form.get('ingredients'),
            preparation_steps=request.form.get('preparation_steps'),
            image_link=request.form.get('image_link')
        )

        db.session.add(new_recipe)
        db.session.commit()

        selected_tools = request.form.getlist('required_tools[]')
        print(selected_tools)
        print(new_recipe.id)
        for tool_id in selected_tools:
            recipe_tool = RecipeTool(
                recipe_id=new_recipe.id, tool_id=int(tool_id))
            db.session.add(recipe_tool)

        db.session.commit()

        return redirect(url_for("add_recipe"))

    return render_template('add_recipe.html', cuisines=cuisines, tools=tools)


@app.route('/explore_recipes')
def explore_recipes():
    
    recipes = Recipe.query.all()

    return render_template('recipe_explore.html', recipes=recipes)