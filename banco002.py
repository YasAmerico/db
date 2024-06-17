
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
novo = user(nome='Chris',idade=27)

#novo = User(nome='jake' idade =22)
#novo = save()

#consulta de usuarios
users = User.select()
for user in user:
    print(user.nome,user.idade)

userChris = User.get(nome="Chris")
print(userChris.nome,userChris.idade)
