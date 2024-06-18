
from peewee import SqliteDatabase,Model,IntegerField,CharField

#configuração do banco de dados
db = SqliteDatabase('example1.db')

#definição do modelo
class User(Model):
    nome = CharField()
    idade = IntegerField ()

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

#outra forma de fazer
from peewee import SqliteDatabase,Model,IntegerField,CharField

#configuração do banco de dados
db = SqliteDatabase('example1.db')

#definição do modelo
class User(Model):
    nome = CharField()
    idade = IntegerField ()

    class Meta:
        database = db

#criação das tabelas
db.connect()
db.create_tables([User])

#adição de um novo usuário
User.create(nome='Chris',idade =27)
User.create(nome='Felix',idade =24)
User.create(nome='I.n',idade =23)
User.create(nome='Minho',idade =26)

#função para consultar registros por nome e idade
def encontrar_usuario_por_nome_idade(nome,idade):
    query =User.select().where((User.nome == nome)& (User.idade == idade))
    return query

#consulta de usuarios
users =encontrar_usuario_por_nome_idade('Felix',24)
for user in users:
    print(f'Name:{user.nome},Idade:{user.idade}')
