from flask_marshmallow import Marshmallow
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow import fields
from sqlalchemy import true


from app.model import Autor, Book

ma = Marshmallow()

def configure(app):
    ma.init_app(app)
    

class AutorSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Autor
        load_instance = true
        
        id_autor = fields.Integer()
        name = fields.Str()
        
class BookSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Book
        load_instance = true
        include_relationships = True
        include_fk = True
        
        id_book = fields.Integer()
        livro = fields.Str()
        autor_id = fields.Integer()
        autor = fields.Nested(AutorSchema)
