from flask import request, jsonify
from app.models import db, MyMovie

def register_routes(app):
    
    @app.route('/')
    def holamundo():
        return "Hello, World!"
    

    @app.route('/movies', methods=['POST'])
    def create_movie():
        data = request.get_json()
        new_movie = MyMovie(
            Autor=data['Autor'],
            Descripcion=data['Descripcion'],
            Fecha_de_Estreno=data['Fecha_de_Estreno']
        )
        db.session.add(new_movie)
        db.session.commit()
        return jsonify({'message': 'New movie created!'}), 201
    

    