
from peewee import SqliteDatabase,Model,IntegerField,CharField

#configuração do banco de dados
db = SqliteDatabase('example1.db')

#definição do modelo
class User(Model):
    nome = CharField()
    idade = IntegerField

    class Meta:
        database = db

#criação das tabelas
db.connect()
db.create_tables([User])

#adição de um novo usuário
#novo = user(nome='Chris',idade=27)
