from urllib.parse import urlparse
from io import BytesIO, open
from PIL import Image
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

def test_cat(client):
    response = client.get('/cat',
                    json = {
                        "id": 1
                    })
    assert response.status_code == 200
    response_json = json_of_response(response)
    id = response_json['id']
    name = response_json["name"]
    path = response_json["path"]
    assert id == 1
    assert name == "cat_1"
    assert path == ''.join([Config.UPLOAD_PATH,str(1),"_","cat_1.jpg"])

def test_cat_num(client):
    response = client.get('/cat/3')
    assert response.status_code == 200
    response_json = json_of_response(response)
    id = response_json['id']
    name = response_json["name"]
    path = response_json["path"]
    assert id == 3
    assert name == "cat_3"
    assert path == ''.join([Config.UPLOAD_PATH,str(3),"_","cat_3.jpg"])




def test_cat_new(client):
    """
    GIVEN a post call to '/cat' with new cat data
    WHEN a new response is returned
    THEN check that new cat is created with the same data that is given and check that response is 200 
    """
    with app.app_context():
        with open('public/image/cats/test_cat_image.jpg', 'rb') as img1:
            imgStringIO1 = BytesIO(img1.read())

        response  = client.post("/cat", content_type='multipart/form-data',data={'name':'test_item',
        'name':'mittens',
        'image': (imgStringIO1, 'mycat.jpg')})

        redirect_url = urlparse(response.location).path
        new_cat_id = redirect_url.split('/')[2]
        new_cat = Cat.query.get(new_cat_id)
        assert new_cat.name == 'mittens'
        assert response.status_code == 302 ## we use 302 code becuase Flask redirects us 
        assert redirect_url == f'/cat/{new_cat_id}'
