from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from config import Config

from db.database import db

class Cat(db.Model):
    __tablename__ = 'cats'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name:Mapped[str] = mapped_column() 
    image_name:Mapped[str] = mapped_column()

    def __init__(self, name:str, image_name:str):
        self.name = name
        self.image_name = image_name

    def to_json(self):
        return {
            "id":self.id,
            "name":self.name,
            "path":self.get_path()
        }
    def get_path(self):
        return "".join([Config.UPLOAD_PATH,str(self.id),"_",self.image_name])