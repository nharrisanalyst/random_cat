from flask import Flask
from flask_migrate import Migrate
from config import Config

from models.cat_model import Cat
from db.database import db





def create_app():
    app = Flask(__name__)
    app.config.from_mapping(
        SECRET_KEY = "My_Secret_Key"
    )  
    
    app.config.from_object(Config)
    # Database related part
    db.init_app(app)
    
    migrate = Migrate(app, db)

    return app


app = create_app()


@app.get("/")
def get_hello():
    return "<h1> Hello World</h1>"

## import routes 
import routes.random_cat
