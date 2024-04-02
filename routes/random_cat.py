from flask import jsonify, request, render_template, redirect
from PIL import Image
from app import app 
from db.database import db
from models.cat_model import Cat
from routes.form.cat_form import CatFormName,CatFormImage
import random

import os 

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

@app.get("/cat/new")
def get_new_cat():
    return render_template("new_cat.html")

@app.post("/cat")
def post_cat_new():
    form = CatFormName(request.form)
    file = CatFormImage(request.files)
    img = Image.open(file.image.data)
    img_name = request.files['image'].filename
    UPLOAD_PATH = 'public/image/cats'
    path = "".join([UPLOAD_PATH,img_name])
    cat = Cat(name = str(form.name), path = path)
    db.session.add(cat)
    db.session.commit()
    img_save_path ="".join([UPLOAD_PATH,str(cat.id),"_",img_name])
    img.save(os.path.join(img_save_path))
    
    return redirect(f'/cats/{cat.id}')