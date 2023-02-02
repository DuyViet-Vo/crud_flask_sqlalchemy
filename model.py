from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
db = SQLAlchemy()

class students(db.Model):
    __tablename__ = 'students'
    
    id = db.Column(db.Integer, primary_key=True , autoincrement=True)
    name = db.Column(db.String())
    date_birth = db.Column(db.DateTime)
    address = db.Column(db.String())
    phone = db.Column(db.String())
    
    def __init__(self,name,date_birth,address,phone):
        self.name = name
        self.date_birth = date_birth
        self.address = address
        self.phone = phone
        
    def __repr__(self):
        return f'{self.name} {self.date_birth} {self.address} {self.phone}'