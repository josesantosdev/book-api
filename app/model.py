from flask_sqlalchemy import SQLAlchemy 
from sqlalchemy import BigInteger, ForeignKey, String
from sqlalchemy.orm import relationship


db = SQLAlchemy()

def configure(app):
    db.init_app(app)
    app.db = db
    

class Autor(db.Model):
    __tablename__ = 'Autor'    
    id_autor = db.Column(BigInteger, primary_key=True)
    name = db.Column(String(255))

class Book(db.Model):
    __tablename__ = 'Book'
    id_book = db.Column(BigInteger, primary_key=True)
    livro = db.Column(String(255))
    autor_id = db.Column(BigInteger, ForeignKey('Autor.id_autor'), nullable=False)
    autor = relationship('Autor')
