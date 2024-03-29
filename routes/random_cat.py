from flask import jsonify, request, render_template
from app import app 
from models.cat_model import Cat
import random

@app.get("/cat/random")
def get_cat_random():
    cat_id = random.randrange(1,10,1)
    cat = Cat.query.get_or_404(cat_id)
    return jsonify(cat.to_json())


@app.get("/cat")
def get_cat():
    content = request.get_json()
    id = content['id']
    cat = Cat.query.get_or_404(id)
    return jsonify(cat.to_json())


@app.get("/cat/<int:id>")
def get_cat_id(id):
    cat = Cat.query.get_or_404(id)
    return jsonify(cat.to_json())

@app.post("/cat")
def post_cat_new():
    return "you can create a new cat here"


@app.get("/cat/new")
def get_new_cat():
    return render_template("new_cat.html")