from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class MyMovie(db.Model):
    __tablename__ = 'my_movies'

    ID = db.Column(db.Integer, primary_key=True)
    Autor = db.Column(db.String(100), nullable=False)
    Descripcion = db.Column(db.Text, nullable=False)
    Fecha_de_Estreno = db.Column(db.Date, nullable=False)

    def __init__(self, Autor, Descripcion, Fecha_de_Estreno):
        self.Autor = Autor
        self.Descripcion = Descripcion
        self.Fecha_de_Estreno = Fecha_de_Estreno
