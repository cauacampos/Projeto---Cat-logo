from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://ayoxqpey:7piSTuDTaP8hNx8XREMJUrHu7Pigfcyi@kesavan.db.elephantsql.com/ayoxqpey3'
db = SQLAlchemy(app)

class Filme(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(150), nullable=False)
    cartaz = db.Column(db.String(500), nullable=False)

    def __init__(self, nome, cartaz):
        self.nome = nome
        self.cartaz = cartaz

@app.route('/')
def index():
    filmes = Filme.query.all()
    return render_template('catalogo.html', filmes=filmes)

@app.route('/adm')
def adm():
    filmes = Filme.query.all()
    return render_template('adm.html', filmes=filmes)

# @app.route('/<id>')
# def filme_pelo_id(id):
#     filme = Filme.query.get(id)
#     return render_template('catalogo.html', filme=filme)

# @app.route('/new', methods=['GET', 'POST'])
# def new():
#     if request.method == 'POST':
#         filme = Filme(
#             request.form['nome'],
#             request.form['cartaz']
#             )
#         db.session.add(filme)
#         db.session.commit()
#         return redirect('/#catalogo')
#     return render_template('new.html')

# @app.route('/edit/<id>', methods=['GET', 'POST'])
# def edit(id):
#     filme = Filme.query.get(id)
#     if request.method == 'POST':
#         filme.nome = request.form['nome']
#         filme.cartaz = request.form['cartaz']
#         db.session.commit()
#         return redirect('/#catalogo')
#     return render_template('edit.html', filme=filme)

# @app.route('/delete/<id>')
# def delete(id):
#     filme = Filme.query.get(id)
#     db.session.delete(filme)
#     db.session.commit()
#     return redirect('/#catalogo')

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
