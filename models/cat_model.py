from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from db.database import db

class Cat(db.Model):
    __tablename__ = 'cats'

    id: Mapped[int] = mapped_column(primary_key=True)
    name:Mapped[str] = mapped_column(unique=True) 
    path:Mapped[str] = mapped_column(unique=True)

    def __init__(self, id, name:str, path:str):
        self.id = id
        self.name = name
        self.path = path

    def to_json(self):
        return {
            "id":self.id,
            "name":self.name,
            "path":self.path
        }