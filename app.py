from flask import Flask, render_template, request, redirect #pip install flask
from flask_sqlalchemy import SQLAlchemy # pip install flask-sqlalchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///musicas.sqlite3'
db = SQLAlchemy(app)

class Filme(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome_filme = db.Column(db.String(150), nullable=False)
    link_image = db.Column(db.String(300), nullable=False)

    def __init__(self, nome_filme, link_image):
        self.nome_filme = nome_filme
        self.link_image = link_image

@app.route('/')
def index():
    filmes = Filme.query.all()
    return render_template('index.html', filmes=filmes)


