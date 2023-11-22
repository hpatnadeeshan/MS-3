from flask import render_template
from recipehub import app, db
from recipehub.models import Cuisine, Recipe, Tools,RecipeTool


@app.route("/")
def home():
    return render_template("index.html")
