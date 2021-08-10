from flask import Flask, render_template, request, redirect, flash, session
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://ayoxqpey:7piSTuDTaP8hNx8XREMJUrHu7Pigfcyi@kesavan.db.elephantsql.com/ayoxqpey'
db = SQLAlchemy(app)
app.secret_key = 'nineflix'

class Filme(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(150), nullable=False)
    cartaz = db.Column(db.String(500), nullable=False)
    # categoria = db.Column(db.String(150), nullable=False)

    def __init__(self, nome, cartaz): #passar categoria como parametro
        self.nome = nome
        self.cartaz = cartaz
        # self.categoria = categoria

@app.route('/')
def index():
    session['user_logado'] = None
    return render_template('index.html')

@app.route('/adm')
def adm():
    if 'user_logado' not in session or session['user_logado'] == None:
        flash('Faça o login antes de acessar essa rota!')
        return redirect('/login')
    filmes = Filme.query.all()
    return render_template('adm.html', filmes=filmes, filme='')

@app.route('/new', methods=['GET', 'POST'])
def new():
    if request.method == 'POST':
        filme = Filme(
            request.form['nome'],
            request.form['cartaz']
            # request.form['categoria']
            )
        db.session.add(filme)
        db.session.commit()
        flash('Filme adicionado com sucesso!')
        return redirect('/adm')
    flash('Você não tem autorização para acessar essa rota!')
    return redirect('/login')

@app.route('/delete/<id>')
def delete(id):
    if 'user_logado' not in session or session['user_logado'] == None:
        flash('Faça o login antes de acessar essa rota!')
        return redirect('/login')

    filme = Filme.query.get(id)
    db.session.delete(filme) #para apagar a tabela no browse do elephant digitar: drop table 'filme'
    db.session.commit()
    flash('Filme apagado com sucesso!')
    return redirect('/adm')

@app.route('/edit/<id>', methods=['GET', 'POST'])
def edit(id):
    if 'user_logado' not in session or session['user_logado'] == None:
        flash('Faça o login antes de acessar essa rota!')
        return redirect('/login')

    filme = Filme.query.get(id)
    filmes = Filme.query.all()
    if request.method == 'POST':
        filme.nome = request.form['nome']
        filme.cartaz = request.form['cartaz']
        # filme.categoria = request.form['categoria']
        db.session.commit()
        return redirect('/adm')
    return render_template('adm.html', filme=filme, filmes=filmes)

@app.route('/catalogo')
def catalogo():
    filmes = Filme.query.all()
    return render_template('catalogo.html', filmes=filmes)

@app.route('/<id>')
def filme_por_id(id):
    filmeDel = Filme.query.get(id)
    return render_template('adm.html', filmeDel=filmeDel, filme='')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/auth', methods=['GET', 'POST'])
def auth():
    if request.form['senha'] == 'adm123':
        session['user_logado'] = 'logado'
        flash('Login feito com sucesso!')
        return redirect('/adm')
    else:
        flash('Erro no login, tente novamente!')
        return redirect('/login')

############## descomentar quando zerar a tabela e criar com coluna categoria
# @app.route('/filter', methods=['GET', 'POST'])
# def filter():
#     filmes = Filme.query.filter_by(categoria=request.form['search']).all()
#     return render_template('catalogo.html', filmes=filmes)
############## descomentar quando zerar a tabela e criar com coluna categoria


############## testando com coluna nome
@app.route('/filter', methods=['GET', 'POST'])
def filter():
    filmes = Filme.query.filter_by(nome=request.form['search']).all()
    return render_template('catalogo.html', filmes=filmes) 
############## testando com coluna nome 

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
