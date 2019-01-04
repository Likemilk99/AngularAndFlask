from app import db
from ..common.Serializer import Serializer

class Hero(db.Model, Serializer):
  id = db.Column(db.Integer, primary_key = True)
  name = db.Column("name", db.String(80), unique = True)
  
  def __init__(self, name):
    self.name = name
    
  def serialize(self):
    return Serializer.serialize(self)