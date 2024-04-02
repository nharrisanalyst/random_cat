import os
 
from wtforms import Form, FileField, StringField, validators

class CatFormName(Form):
    name = StringField("name")
    

class CatFormImage(Form):
    image = FileField('image')


def upload_img(image):
    UPLOAD_PATH = '/public/image/cats'