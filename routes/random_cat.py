from flask import jsonify, request
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

@app.post('/cat')
def make_cat():
    return "lets make a cat"