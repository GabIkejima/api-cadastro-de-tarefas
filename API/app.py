from flask import Flask, request, jsonify
import json

app = Flask(__name__)

tarefas = [
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


#lista as tarefas e permite adicionar uma nova tarefa para a lista
@app.route('/tarefas/', methods=['POST', 'GET'])
def lista_tarefas():
    if request.method == 'GET':
        return jsonify(tarefas)

    elif request.method == 'POST':
        dados = json.loads(request.data)
        posicao = len(tarefas)
        dados['id'] = posicao #cria um ID para a tarefa e atribuí a mesma
        tarefas.append(dados)
        return jsonify(tarefas[posicao])

if __name__ == '__main__':
    app.run(debug=True)