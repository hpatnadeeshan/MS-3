from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import check_password_hash, generate_password_hash
from flask import render_template, request, redirect, url_for,flash
from recipehub import app, db,login_manager
from recipehub.models import Cuisine, Recipe, Tools, RecipeTool, User
import random

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/login', methods=['GET', 'POST'])
def login():
    print("login: " + str(current_user.is_authenticated))
    errors = []
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password, password):
            # Successful login logic
            flash('Login successful!', 'success')
            return redirect(url_for('home'))
        else:
            errors.append('Invalid username or password. Please try again.')

    return render_template('login.html', errors=errors)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    errors = []
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        confirm_password = request.form['confirm_password']

        if password != confirm_password:
            errors.append('Passwords do not match. Please try again.')

        # Check if the username is already taken
        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            errors.append('Username is already taken. Please choose a different one.')

        if not errors:
            hashed_password = generate_password_hash(password)
            new_user = User(username=username, password=hashed_password)
            db.session.add(new_user)
            db.session.commit()

            # flash('Sign Up successful! Please login.', 'success')
            return redirect(url_for('login'))

    return render_template('signup.html', errors=errors)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Logout successful!', 'success')
    print("logout"+str(current_user.is_authenticated))
    return redirect(url_for('home'))

@app.route("/")
# @login_required
def home():   
    # hashed_password = generate_password_hash('12345678')
    # admin_user = User(username='admin', password=hashed_password, is_admin=True)
    # db.session.add(admin_user)
    # db.session.commit()

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


@app.route('/add_recipe', methods=['GET', 'POST'])
@login_required
def add_recipe():
    cuisines = list(Cuisine.query.order_by(Cuisine.cuisine_name).all())
    tools = list(Tools.query.order_by(Tools.tool_name).all())

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


@app.route('/edit_recipe/<int:recipe_id>', methods=['GET', 'POST'])
@login_required
def edit_recipe(recipe_id):
    # Retrieve the recipe to be edited
    recipe = Recipe.query.get(recipe_id)

    if request.method == 'POST':
        # Update the recipe details based on the form submission
        recipe.recipe_name = request.form['recipe_name']
        recipe.cuisine_id = request.form['cuisine_name']
        recipe.ingredients = request.form['ingredients']
        recipe.preparation_steps = request.form['preparation_steps']
        recipe.image_link = request.form['image_link']

        # Update the recipe in the database
        db.session.commit()

        # Redirect to the view recipe page after editing
        return redirect(url_for('view_recipe', recipe_id=recipe.id))

    
    tools = Tools.query.order_by(Tools.tool_name).all()

    # Retrieve associated tools for the selected recipe
    associated_tools = [recipe_tool.tool_id for recipe_tool in RecipeTool.query.filter_by(recipe_id=recipe_id).all()]
    # associated_tools = RecipeTool.query.filter_by(recipe_id=recipe_id).all()
    cuisines = list(Cuisine.query.order_by(Cuisine.cuisine_name).all())

    return render_template('edit_recipe.html', recipe=recipe, cuisines=cuisines, tools=tools, associated_tools=associated_tools)


@app.route('/explore_recipes')
def explore_recipes():

    recipes = Recipe.query.all()
    cuisines = Cuisine.query.all()

    # Filter recipes based on user selection
    selected_cuisine_id = request.args.get('cuisine')
    # print(f"Cuisine ID: {selected_cuisine}")
    # print(recipes)
    print(cuisines)
    selected_cuisine = None
    if selected_cuisine_id:
        selected_cuisine = Cuisine.query.get(selected_cuisine_id)
        recipes = Recipe.query.filter_by(cuisine_id=selected_cuisine_id).all()

    # Search recipes based on user input
    search_query = request.args.get('search')
    if search_query:
        # Adjust the following line to match your search logic in the database
        recipes = Recipe.query.filter(
            Recipe.recipe_name.ilike(f'%{search_query}%')).all()

    return render_template('recipe_explore.html', recipes=recipes, cuisines=cuisines, selected_cuisine=selected_cuisine)


    
@app.route('/delete_recipe/<int:recipe_id>', methods=['POST'])
@login_required
def delete_recipe(recipe_id):
    # Retrieve the recipe to be deleted
    recipe = Recipe.query.get(recipe_id)

    # Check if the recipe exists
    if recipe:
        # Delete the recipe from the database
        db.session.delete(recipe)
        db.session.commit()

    # Redirect to the recipe explore page or any other appropriate page
    return redirect(url_for('explore_recipes'))

@app.route('/manage_data')
@login_required
def manage_data():
    cuisines = list(Cuisine.query.order_by(Cuisine.cuisine_name).all())
    tools = list(Tools.query.order_by(Tools.tool_name).all())
    return render_template('manage_data.html', cuisines=cuisines, tools=tools)

@app.route('/add_cuisine', methods=['GET', 'POST'])
@login_required
def add_cuisine():
    if request.method == 'POST':
        cuisine_name = request.form['cuisine_name']
        new_cuisine = Cuisine(cuisine_name=cuisine_name)
        db.session.add(new_cuisine)
        db.session.commit()
        return redirect(url_for('manage_data'))

    # return render_template('manage_data.html')

@app.route('/add_tool', methods=['GET', 'POST'])
@login_required
def add_tool():
    if request.method == 'POST':
        tool_name = request.form['tool_name']
        brand_name = request.form['brand_name']
        new_tool = Tools(tool_name=tool_name, brand_name=brand_name)
        db.session.add(new_tool)
        db.session.commit()
        return redirect(url_for('manage_data'))
    # return render_template('manage_data.html')


@app.route('/edit_cuisine/<int:cuisine_id>', methods=['GET', 'POST'])
@login_required
def edit_cuisine(cuisine_id):
    cuisine = Cuisine.query.get_or_404(cuisine_id)

    if request.method == 'POST':
        cuisine.cuisine_name = request.form['cuisine_name']
        db.session.commit()
        return redirect(url_for('manage_data'))

    # return render_template('edit_cuisine.html', cuisine=cuisine)

@app.route('/edit_tool/<int:tool_id>', methods=['GET', 'POST'])
@login_required
def edit_tool(tool_id):
    tool = Tools.query.get_or_404(tool_id)

    if request.method == 'POST':
        tool.tool_name = request.form['tool_name']
        tool.brand_name = request.form['brand_name']
        db.session.commit()
        return redirect(url_for('manage_data'))

    # return render_template('edit_tool.html', tool=tool)

@app.route('/delete_cuisine/<int:cuisine_id>', methods=['POST'])
@login_required
def delete_cuisine(cuisine_id):
    cuisine = Cuisine.query.get_or_404(cuisine_id)
    db.session.delete(cuisine)
    db.session.commit()
    return redirect(url_for('manage_data'))

@app.route('/delete_tool/<int:tool_id>', methods=['POST'])
@login_required
def delete_tool(tool_id):
    tool = Tools.query.get_or_404(tool_id)
    db.session.delete(tool)
    db.session.commit()
    return redirect(url_for('manage_data'))
