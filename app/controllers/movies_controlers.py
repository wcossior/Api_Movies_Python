from flask import request, jsonify
from app.models import db, MyMovie

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

def get_movies():
    movies = MyMovie.query.all()
    result = []
    for movie in movies:
        movie_data = {
            'ID': movie.ID,
            'Autor': movie.Autor,
            'Descripcion': movie.Descripcion,
            'Fecha_de_Estreno': movie.Fecha_de_Estreno
        }
        result.append(movie_data)
    return jsonify(result)

def update_movie(id):
    movie = MyMovie.query.get(id)
    if not movie:
        return jsonify({'message': 'Movie not found'}), 404

    data = request.get_json()
    movie.Autor = data['Autor']
    movie.Descripcion = data['Descripcion']
    movie.Fecha_de_Estreno = data['Fecha_de_Estreno']

    db.session.commit()
    return jsonify({'message': 'Movie updated'}), 200

def delete_movie(id):
    movie = MyMovie.query.get(id)
    if not movie:
        return jsonify({'message': 'Movie not found'}), 404

    db.session.delete(movie)
    db.session.commit()
    return jsonify({'message': 'Movie deleted'}), 200
