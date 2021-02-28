from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///biblioteca.db'
db = SQLAlchemy(app)


class biblioteca(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(100), nullable=False)
    senha = db.Column(db.String(300), nullable=False)

    def _repr_(self, nome, senha):
        self.nome = nome
        self.senha = senha


db.create_all()


@app.route('/')
def inicial():
    resultadofinal = "<h1>Tabela do Banco de Dados</h1><br><ul>"
    for table in db.metadata.tables.items():
        resultadofinal += "<li>%s</li>" % str(table)
    resultadofinal += "</ul>"
    return resultadofinal


@app.route('/inclusao')
def inclusao():
    nomepessoa = biblioteca(nome='João', senha='010203')
    nome2 = biblioteca(nome='Camila', senha='101112')
    nome3 = biblioteca(nome='Pedro', senha='232425')
    db.session.add(nomepessoa)
    db.session.add(nome2)
    db.session.add(nome3)
    db.session.commit()
    resultadofinal = "Usuários adicionados."
    return resultadofinal


@app.route('/leitura/<int:id>')
def leitura(id):
    nome = biblioteca.query.get(id)
    resultadofinal = "<h2>Usuário encontrado:</h2>"
    resultadofinal += "<p> id=" + str(nome.id) + "</p>"
    resultadofinal += "<p> Nome=" + nome.nome + "</p>"
    resultadofinal += "<p> Senha=" + nome.senha + "</p>"
    return resultadofinal


@app.route('/leituratotal')
def leituratotal():
    nome = biblioteca.query.order_by(biblioteca.nome).all()
    resultadofinal = '<h1>Todos os usuários cadastrados:</h1><br><ul>'
    for nome in nome:
        resultadofinal += '<p>'
        resultadofinal += 'Id=' + str(nome.id)
        resultadofinal += ' Nome=' + nome.nome
        resultadofinal += ' Senha=' + nome.senha
        resultadofinal += '</p>'
    return resultadofinal


@app.route('/deletar/<int:id>')
def deletar(id):
    resultadofinal = "<h1>Excluir:</h1><br><ul>"
    nome = biblioteca.query.get(id)
    db.session.delete(nome)
    db.session.commit()
    resultadofinal += str(nome.nome) + ' excluído(a) com sucesso!'
    return resultadofinal


@app.route('/alteraçao/<int:id>')
def alteraçao(id):
    resultadofinal = "<h1>Atualização:</h1><br><ul>"
    nome = biblioteca.query.get(id)
    nome.nome = "Jade"
    db.session.commit()
    resultadofinal += 'Alteração feita para Jade <br>'
    return resultadofinal


if __name__ == '__main__':
    app.run()