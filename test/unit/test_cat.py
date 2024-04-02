from flask import Flask
import unittest
from db.database import db
from test.test_config import TestConfig
from config import Config

from models.cat_model import Cat



class DBTests(unittest.TestCase):

    def setUp(self):
        self.app = Flask(__name__)
        self.app.config.from_object(TestConfig)
        db.init_app(self.app)
        with self.app.app_context():
            db.create_all()


    def tearDown(self):
        with self.app.app_context():
            db.session.remove()
            db.drop_all()

    def test_cat(self):
        with self.app.app_context():
            """
            GIVEN a Cat model
            WHEN a new Cat is created
            THEN check the name, image path
            """
            cat = Cat("mittens",  "mittens.jpg")
            db.session.add(cat)
            assert cat in db.session
            assert cat.name == "mittens"
            assert cat.get_path() == ''.join([Config.UPLOAD_PATH,str(cat.id),'_',cat.image_name])