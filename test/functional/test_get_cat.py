from test.conftest import client, json_of_response


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

    assert("public/image" in response_json["path"])
    
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
    assert name == 'cat_1'
    assert path == "public/image/cats/cat_1"

def test_cat_num(client):
    response = client.get('/cat/3')
    assert response.status_code == 200
    response_json = json_of_response(response)
    id = response_json['id']
    name = response_json["name"]
    path = response_json["path"]
    assert id == 3 
    assert name == 'cat_3'
    assert path == "public/image/cats/cat_3"




