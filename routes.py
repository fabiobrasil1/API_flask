from flask import Flask, request
from flask.wrappers import Response

from main import insertUsuario

app = Flask("youtube")

@app.route("/olamundo", methods=["GET"])
def olaMundo():
    return {"ola":"mundo"}



@app.route("/cadastra/usuario",methods=["POST"])
def cadastrarUsuario():
    
    body = request.get_json()

    if("nome" not in body):
        return {"status": 400,  "menssagem" : "O parametro nome é obrigatório"}
    
    if("email" not in body):
        return {"status": 400,  "menssagem" : "O parametro email é obrigatório"}
    
    if("senha" not in body):
        return {"status": 400,  "menssagem" : "O parametro senha é obrigatório"}
    
    usuario = insertUsuario(body["nome"], body["email"], body["senha"])

    return geraResponse(200, "usuário criado","user", usuario)


def geraResponse(status,mensagem, nome_do_conteudo=False, conteudo=False):

    response = {}
    response["status"] = status
    response["messagem"] = mensagem
    
    if(nome_do_conteudo and conteudo):
        response[nome_do_conteudo] = conteudo

    return response

app.run()