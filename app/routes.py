from flask import request, jsonify
from app.models import db, MyMovie
from app.controllers import movies_controlers

def register_routes(app):
    
    @app.route('/')
    def home():
        return "Api de peliculas"
    

    @app.route('/movies', methods=['POST'])
    def create_movie():
        return movies_controlers.create_movie()
    

    @app.route('/movies', methods=['GET'])
    def get_movies():
       return movies_controlers.get_movies()


    @app.route('/movies/<int:id>', methods=['PUT'])
    def update_movie(id):
       return movies_controlers.update_movie(id)


    @app.route('/movies/<int:id>', methods=['DELETE'])
    def delete_movie(id):
       return movies_controlers.delete_movie(id)