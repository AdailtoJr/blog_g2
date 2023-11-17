from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)


@app.route('/')
def index():
    with conectar_bd() as connection:
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM posts ORDER BY data DESC')
        posts = cursor.fetchall()
    
    return render_template('index.html', posts=posts)


# Configuração do banco de dados
DATABASE = 'banco_de_dados.db'

def conectar_bd():
    return sqlite3.connect(DATABASE)

# Rotas
@app.route('/')
def index():
    # Lógica para buscar os posts do banco de dados e passar para o template
    return render_template('index.html', posts=posts)


def criar_tabela():
    with conectar_bd() as connection:
        cursor = connection.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS posts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                data TEXT NOT NULL,
                titulo TEXT NOT NULL,
                conteudo TEXT NOT NULL
            )
        ''')
        connection.commit()

# Chame esta função para criar a tabela quando o aplicativo for executado
criar_tabela()


if __name__ == '__main__':
    app.run(debug=True)


