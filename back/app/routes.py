from flask import request, jsonify, make_response
from app import app, db
from sqlalchemy.exc import IntegrityError
from datetime import datetime

#Importa os modelos que vamos usar
from app.models.modelos import Casa, Blog

#CRUD
# Create -> Cria recurso -> POST
# Read -> Ler os recursos -> GET
# Update -> Atualiza um recurso -> PUT
# Delete -> Apaga um recurso -> DELETE

# Read
#Rota que lista todas as casas existes
@app.route("/blog", methods=['GET'])
def get_blog():
    blog = Blog.query.all()
    lista_blog = []
    for produto in blog:
        lista_blog.append({
            'id': blog.id,
            'titulo': blog.titulo,
            'noticia': blog.noticia,
            'imagens': blog.imagens,
            'album': blog.album,
            })

    return jsonify(lista_blog)

#Create
# Cria uma casa no banco de dados
@app.route("/blog", methods=['POST'])
def create_blog():
    dados = request.json
    titulo = dados.titulo
    noticia = dados.noticia
    imagens = dados.imagens
    album = dados.album
    blog = Blog(titulo, noticia, imagens, album)
    db.session.add(blog)
    db.session.commit()
    return jsonify({'status': 201, 'message': 'Casa criada com sucesso'}), 201




# Excluir uma categoria
@app.route('/blog/<int:blog_id>', methods=['DELETE'])
def delete_blog(blog_id):
    blog = Blog.query.get(blog_id)
    if blog is None:
        return jsonify({'error': 'Blog não encontrada'}), 404
    db.session.delete(blog)
    db.session.commit()
    return jsonify({'message': 'Blog excluída com sucesso'})


# Atualizar uma venda
@app.route('/blog/<int:blog_id>', methods=['PUT'])
def update_blog(blog_id):
    blog = Blog.query.get(blog_id)
    if blog is None:
        return jsonify({'error': 'Blog não encontrada'}), 404
    data = request.json
    blog.nome = data['nome']
    blog.descricao = data['descricao']
    blog.tipo = data['tipo']
    db.session.commit()
    return jsonify({'message': 'Blog atualizada com sucesso'})
