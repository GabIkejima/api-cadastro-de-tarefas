from flask import Flask, request
from flask_restful import Resource, Api
import json
from habilidades import Habilidades

app = Flask(__name__)
api = Api(app)

tarefas_banco = [
    {
        'id':'0',
        'responsavel':'Gabriel',
        'habilidades':'Python',
        'tarefa':'Adicionar metodos GET e POST',
        'status':'concluido'
    },
    {
        'id':'1',
        'responsavel':'Giovanna',
        'habilidades':'Java',
        'tarefa':'Testar metodo GET',
        'status':'pendente'
    },
]


#lista a tarefa por id, permite alterar o status da tarefa e deletar uma tarefa
class Tarefas(Resource):
    def get(self, id):
        try:
            response = tarefas_banco[id]
        except IndexError:
            mensagem = 'Tarefa de ID {} não encontrada'.format(id)
            response = {'status':'erro','mensagem':mensagem}
        except Exception:
            mensagem = 'Erro não indentificado, contatar o desenvolvedor da API'
            response = {'Status': 'Erro', 'Mensagem': mensagem}
        return response

    def put(self, id):
        dados = json.loads(request.data)
        tarefas_banco[id]['status'] = dados['status']
        return dados

    def delete(self, id):
        tarefas_banco.pop(id)
        mensagem = 'Tarefa de ID {} deletada com sucesso'.format(id)
        return{'Status':'Sucesso', 'Mensagem': mensagem}

#lista as tarefas e permite adicionar uma nova tarefa para a lista
class lista_tarefas(Resource):
    def get(self):
        return tarefas_banco
    def post(self):
        dados = json.loads(request.data)
        posicao = len(tarefas_banco)
        dados['id'] = posicao
        tarefas_banco.append(dados)
        return tarefas_banco[posicao]


api.add_resource(Tarefas, '/tarefas/<int:id>/')
api.add_resource(lista_tarefas, '/tarefas/')
api.add_resource(Habilidades, '/habilidades/')

if __name__ == '__main__':
    app.run(debug=True)