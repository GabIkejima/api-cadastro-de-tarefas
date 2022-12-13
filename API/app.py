from flask import Flask, request, jsonify
import json

app = Flask(__name__)

tarefas_banco = [
    {
        'id':'0',
        'responsavel':'Gabriel',
        'tarefa':'Adicionar metodos GET e POST',
        'status':'concluido'
    },
    {
        'id':'1',
        'responsavel':'Giovanna',
        'tarefa':'Testar metodo GET',
        'status':'pendente'
    },
]

#lista a tarefa por id, permite alterar o status da tarefa e deletar uma tarefa
@app.route('/tarefas/<int:id>/', methods=['DELETE','PUT','GET'])
def tarefas(id):
    if request.method == 'GET':
        try:
            response = tarefas_banco[id]

        except IndexError:
            mensagem = 'Tarefa de ID {} não encontrada'.format(id)
            response = {'Status':'Erro', 'Mensagem':mensagem}

        except Exception:
            mensagem = 'Erro não indentificado, contatar o desenvolvedor da API'
            response = {'Status':'Erro', 'Mensagem':mensagem}

        return jsonify(response)

    if request.method == 'DELETE':
        tarefas_banco.pop(id)
        return jsonify({'Status':'Sucesso', 'Mensagem':'Tarefa deletada!'})

    elif request.method == 'PUT':
        dados = json.loads(request.data)
        tarefas_banco[id]['status'] = dados['status']
        return jsonify(dados)


#lista as tarefas e permite adicionar uma nova tarefa para a lista
@app.route('/tarefas/', methods=['POST', 'GET'])
def lista_tarefas():
    if request.method == 'GET':
        return jsonify(tarefas_banco)

    elif request.method == 'POST':
        dados = json.loads(request.data)
        posicao = len(tarefas_banco)
        dados['id'] = posicao #cria um ID para a tarefa e atribuí a mesma
        tarefas_banco.append(dados)
        return jsonify(tarefas_banco[posicao])

if __name__ == '__main__':
    app.run(debug=True)