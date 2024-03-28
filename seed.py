import json

from app import app
from db.database import db
from models.cat_model import Cat

init_data = open('db/init_data.json')
data = json.load(init_data)


def seed_cats():
    with app.app_context():
        for cat in data["data"]:
            id = cat["id"]
            name = cat["name"]
            path = cat["path"]

            cat_instance = Cat(id = id, name = name, path = path)
            db.session.add(cat_instance)
        
        db.session.commit()

if __name__ == "__main__":
    seed_cats()
