from flask import request
from flask_restful import Resource
import json

habilidades_banco = [
    {'Habilidade':'Python',
      'Id':'0'
    },
    {'Habilidade':'Java',
     'Id':'1'
    },
]

#lista a habilidade por id, permite alterar ou deletar uma habilidade
class habilidades(Resource):
    def get(self, id):
        try:
            response = habilidades_banco[id]

        except IndexError:
            mensagem = 'Habilidade de id {} não existe'.format(id)
            response = {'Status':'Erro', 'Mensagem':mensagem}

        except Exception:
            mensagem = 'Erro não indentificado, contatar o desenvolvedor da API'
            response = {'Status': 'Erro', 'Mensagem': mensagem}
        return response

    def put(self, id):
        try:
            dados = json.loads(request.data)
            habilidades_banco[id] = dados
            return habilidades_banco[id]

        except IndexError:
            mensagem = 'Habilidade de id {} não existe'.format(id)
            return {'Status':'Erro', 'Mensagem':mensagem}

        except Exception:
            mensagem = 'Erro não indentificado, contatar o desenvolvedor da API'
            return {'Status':'Erro', 'Mensagem':mensagem}

    def delete(self, id):
        try:
            habilidades_banco.pop(id)
            mensagem = 'Habilidade {} excluída com sucesso!'.format(id)
            response = {'Status':'Sucesso', 'Mensagem':mensagem}
        except IndexError:
            mensagem = 'Habilidade de id {} não existe'.format(id)
            response = {'Status':'Erro', 'Mensagem':mensagem}
        return response

#lista e permite adicionar uma nova habilidade para a lista
class lista_habilidades(Resource):
    def get(self):
        return habilidades_banco

    def post(self):
        dados = json.loads(request.data)
        posicao = len(habilidades_banco)
        dados['id']=posicao
        habilidades_banco.append(dados)
        return habilidades_banco[posicao]



