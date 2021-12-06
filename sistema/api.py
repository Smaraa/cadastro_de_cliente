from flask import Flask, request, jsonify
from flask_ngrok import run_with_ngrok

from controladores.controlador_cliente import ControladorCliente
from controladores.controlador_profissao import ControladorProfissao

app = Flask(__name__)
run_with_ngrok(app)
controladorCliente = ControladorCliente()


@app.route("/clientes")
def listar_clientes():
    todos = controladorCliente.listar_todo_cliente()
    return jsonify(todos)


#Cadastro do cliente:
@app.route("/cliente",methods=["POST"])    
def cadastrarCliente():
    try:
        dados = request.get_json()
        cpf = dados["cpf"]
        nome = dados["nome"]
        cidade = dados["cidade"]
        telefone = dados["telefone"]
        profissao = dados["profissao"]
        controladorCliente.cadastrar_cliente(cpf, nome, cidade, telefone, profissao)

        return{"status": "CREATED", "mensagem": "Cadastrado com Sucesso"}
    except:
        return {"status": "ERRO", "mensagem": "Erro ao cadastrar"}


#Deletar cliente:
@app.route("/cliente/<id>", methods=["DELETE"])
def deletarCliente(id):
    try:
        controladorCliente.excluir_cliente(id)
        return{"status": "OK", "mensagem": "Cliente deletado com Sucesso"}
    except:
        return{"status": "ERRO", "mensagem": "Erro alterando cliente"}


#Atualizar cliente:
@app.route("/cliente/<id>",methods=["PATCH"])    
def atualizarCliente(id):
    try:
        dados = request.get_json()
        cpf = dados["cpf"]
        nome = dados["nome"]
        cidade = dados["cidade"]
        telefone = dados["telefone"]
        profissao = dados["profissao"]
        controladorCliente.atualizar_alterar_cliente(id, cpf, nome, cidade, telefone, profissao)

        return{"status": "OK", "mensagem": "Cliente alterado com Sucesso"}
    except:
        return {"status": "ERRO", "mensagem": "Erro ao cadastrar"}
    

#Obter dados cliente:
@app.route("/cliente/<id>", methods=["GET"])
def getClientByNome(id):
    try:
        cliente = controladorCliente.obter_dado_cliente(id)
        return jsonify(cliente)
    except:
        return {"status": "ERRO", "mensagem": "Erro ao obter dados do cliente"}


controladorProfissao = ControladorProfissao()


#Cadastro profissão:
@app.route("/profissao", methods=["POST"])
def cadastrarProfissao():
    try:
        dados = request.get_json()
        profissao = dados["profissao"]
        controladorProfissao.cadastrar_profissao(profissao)
        return{"status": "OK", "mensagem": "Profissão cadastrada com Sucesso"}
    except:
        return {"status": "ERRO", "mensagem": "Erro ao cadastrar profissão"}

#Excluir Profissão:
@app.route("/profissao/<id>",methods=["DELETE"])
def excluirProfissao(id):
    controladorProfissao.excluir_profissao(id)
    return{"status": "OK", "mensagem": "Profissão deletada com Sucesso"}

    
#Atualizar profissão:
@app.route("/profissao/<id>",methods=["PATCH"])
def atualizarProfissao(id):
    dados = request.get_json()
    profissao = dados["profissao"]
    controladorProfissao.atualizar_alterar_profissao(id, profissao)
    return{"status": "OK", "mensagem": "Profissão atualizada com Sucesso"}



app.run()