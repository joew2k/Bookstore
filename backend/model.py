
import os
from flask import  jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Integer, Column, String, create_engine

database_name = 'bookstore'
database_path = 'postgresql://{}:{}@{}/{}'.format('jose', 'Odom232#', 'localhost:5432', database_name)

# Intiate database

db = SQLAlchemy()

'''
Create a set_up function that binds application and db
'''

def set_up(app, database_path = database_path):
    app.config['SQLALCHEMY_DATABASE_URI'] = database_path
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app = app
    db.init_app(app)
    db.create_all()

'Book'
class Book(db.Model):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    author = Column(String)
    rating = Column(Integer)

    def __init__(self, id, title, author, rating):
        self.id = id
        self.title = title
        self.author = author
        self.rating = rating
    
    # Query formating
    
    # Insert
    def insert(self):
        db.session.add(self)
        db.session.commit()
    
    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return jsonify({
            'id': self.id,
            'title': self.title,
            'author': self.author,
            'rating': self.rating
        })
    

    
