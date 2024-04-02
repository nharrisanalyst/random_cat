import json

from app import app
from db.database import db
from models.cat_model import Cat

init_data = open('db/init_data.json')
data = json.load(init_data)


def seed_cats():
    with app.app_context():
        for cat in data["data"]:
            name = cat["name"]
            image_name = cat["image_name"]

            cat_instance = Cat(name = name, image_name = image_name)
            db.session.add(cat_instance)
        
        db.session.commit()

if __name__ == "__main__":
    seed_cats()
