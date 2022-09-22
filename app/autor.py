from flask import Blueprint, current_app, jsonify, request
from .model import Autor
from .serealize import AutorSchema
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy import engine

bp_autor = Blueprint('autors', __name__)
ash = AutorSchema()
autor_schema = AutorSchema()
autors_schema = AutorSchema(many=True)


@bp_autor.route('/mostrar', methods=['GET'])
def show():
    autors = Autor.query.all()
    return jsonify(autors_schema.dump(autors)), 200

@bp_autor.route('/mostrar/<id>', methods=['GET'])
def show_unique(id):
    ash = AutorSchema()
    autor = Autor.query.filter_by(id_autor=id).first_or_404()
    autors_dump = ash.dump(autor)
    return jsonify(autors_dump), 200

    
@bp_autor.route('/cadastrar', methods=['POST'])
def create():
    data = request.get_json()
    sess = scoped_session(sessionmaker(bind=engine))
    autor = ash.load(data, session=sess)
    autors = ash.dump(autor)
    current_app.db.session.add(autor)
    current_app.db.session.commit()
    return jsonify(autors), 201
    
    
@bp_autor.route('/editar/<id>', methods=['PUT'])
def edit(id):
   query = Autor.query.filter(Autor.id_autor == id)
   query.update(request.json)
   current_app.db.session.commit()
   autors = ash.dump(query.first())
   return jsonify(autors), 200

@bp_autor.route('/deletar/<id>', methods=['DELETE'])
def delete(id):
    Autor.query.filter(Autor.id_autor == id).delete()
    current_app.db.session.commit()
    return jsonify('Deletado'), 200
