from app import db

# ####################
# Cada classe é uma tabela no banco de dados
# ####################

#Casa herda todas as características de db.Model
class Casa(db.Model):

    #Propriedades de Casa
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    qtdQuartos = db.Column(db.Integer)
    qtdBanheiros = db.Column(db.Integer)
    rua = db.Column(db.String(100))

    #Construtor, recebendo os parâmetros para adicionar ao objeto
    def __init__(self, qtdQuartos, qtdBanheiros, rua):
        self.qtdQuartos = qtdQuartos
        self.qtdBanheiros = qtdBanheiros
        self.rua = rua


class Blog(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    titulo = db.Column(db.String(80))
    noticia = db.Column(db.Text())
    imagens = db.Column(db.Text())
    data = db.Column(db.Data())
    album = db.Column(db.Integer())


def __init__(self, titulo, noticia, imagens, data, album):
        self.titulo = titulo
        self.noticia = noticia
        self.imagens = imagens
        self.data = data
        self.album = album

