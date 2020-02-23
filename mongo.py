from pymongo import MongoClient
import datetime
import pprint

# URI = MongoClient('mongodb://[usuario]:[senha]@[host]/[database]')

client = MongoClient('mongodb://superuser:kickflip@localhost/admin') # Logar no MongoBD
db = client.test_database # Selecionar/Criar BD
collection = db.posts # Coleções do BD selecionado

# Insert com uma querya
# post = {
#     "author": "Mike",
#     "text": "My first blog post!",
#     "tags": ["mongodb", "python", "pymongo"],
#     "date": datetime.datetime.utcnow()
# }

posts = db.posts
# post_id = posts.insert_one(post).inserted_id

# Insert com multiplas querys
# new_posts = [
#     {
#         "author": "Mike",
#         "text": "Another post!",
#         "tags": ["bulk", "insert"],
#         "date": datetime.datetime(2009, 11, 12, 11, 14)
#     },
#     {
#         "author": "Elliot",
#         "title": "MongoDB is fun",
#         "text": "and pretty easy too!",
#         "date": datetime.datetime(2009, 11, 10, 10, 45)
#     }
# ]

# result = posts.insert_many(new_posts)
# print(result.inserted_ids)

# Pesquisar no DB
# pprint.pprint(posts.find_one({"author": "Mike"})) # Pesquisa por uma chave especifica
# pprint.pprtin(posts.find_one({"_id": post_id})) # Pesquisa por ObjectId
# pprint.pprint(posts.find_one()) # Pesquisa sem query, mostra o ultimo item adicionado

# Pesquisar em multiplos documentos (tabelas) -> SELECT * FROM
# for post in posts.find():
#     pprint.pprint(post)

# Contar queries no DB
# print(posts.count_documents({})) # Contar todas as queries do DB
# print(posts.count_documents({"author": "Mike"})) # Contar todos os documentos que satisfazem os requisitos

