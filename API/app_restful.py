from flask import Flask, request
from flask_restful import Resource, Api
import json
from habilidades import lista_habilidades, habilidades

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


#lista a tarefa por id, permite alterar ou deletar uma tarefa
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
        try:
            dados = json.loads(request.data)
            tarefas_banco[id] = dados
            return tarefas_banco[id]
        except IndexError:
            mensagem = 'Tarefa de ID {} não existe'.format(id)
            return {'Status':'Erro', 'Mensagem': mensagem}

        except Exception:
            mensagem = 'Erro não indentificado, contatar o desenvolvedor da API'
            return {'Status': 'Erro', 'Mensagem': mensagem}

    def delete(self, id):
        try:
            tarefas_banco.pop(id)
            mensagem = 'Tarefa {} excluída com sucesso!'.format(id)
            response = {'Status':'Sucesso', 'Mensagem':mensagem}
        except IndexError:
            mensagem = 'Tarefa de ID {} não existe'.format(id)
            response = {'Status':'Erro', 'Mensagem': mensagem}
        return response

#lista e permite adicionar uma nova tarefa para a lista
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
api.add_resource(lista_habilidades, '/habilidades/')
api.add_resource(habilidades, '/habilidades/<int:id>/')


if __name__ == '__main__':
    app.run(debug=True)