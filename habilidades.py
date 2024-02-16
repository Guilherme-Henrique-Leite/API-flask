from flask_restful import Resource
from flask import Flask, request
import json

lista_habilidades = ['Python', 'Java', 'PHP', 'Flask']

class Habilidades(Resource):
    def get(self):
        return lista_habilidades
    def post(self):
        return lista_habilidades.append('Javascript')

class ManipulaHabilidades(Resource):
    def put(self, id):
        dados = json.loads(request.data)
        lista_habilidades[id] = dados
        return lista_habilidades
    def delete(self, id):
        lista_habilidades.pop(id)
        return {'status':'sucesso', 'mensagem': 'Habilidade excluída'}