import unittest
from test.conftest import client, json_of_response
from config import Config
from app import app
from models.cat_model import Cat



# class APPFunctionalTest(unittest.TestCase):
#     def setUp(self):
#         pass

#     def tearDown(self):
#         pass

def test_cat_random(client):

    """
    GIVEN a get call to '/cat/random'
    WHEN a new response is return 
    THEN check the name is a string and 'public/img' is in the url 
    """
    response = client.get('/cat/random')
    assert response.status_code == 200
    response_json = json_of_response(response)
    name = response_json["name"]
    path = response_json["path"]
    assert isinstance(name, str)
    assert isinstance( path, str)

    assert(Config.UPLOAD_PATH in response_json["path"])
    
    assert len(name)>0

# def test_cat(client):
#     response = client.get('/cat',
#                       json = {
#                         "id": 1
#                       })
#     assert response.status_code == 200
#     response_json = json_of_response(response)
#     id = response_json['id']
#     name = response_json["name"]
#     path = response_json["path"]
#     assert id == 1 
#     assert name == 'cat_1'
#     assert path == "public/image/cats/1-cat_1.jpg"

def test_cat_num(client):
    with app.app_context():
        response = client.get('/cat/3')
        assert response.status_code == 200
        response_json = json_of_response(response)
        id = response_json['id']
        name = response_json["name"]
        path = response_json["path"]
        cat = Cat.query.get(3)
        assert id == cat.id
        assert name == cat.name
        assert path == ''.join([Config.UPLOAD_PATH,str(cat.id),"_",cat.image_name])




