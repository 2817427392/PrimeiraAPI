from flask import Flask,request

from main import insertUsuario

app = Flask("Youtube")

@app.route("/olamundo",methods=["GET"])
def olaMundo():
    return {"ola":"mundo"}

@app.route("/cadastra/usuario",methods=["POST"])
def cadastrarUsuario():
    body=request.get_json()

    if("nome" not in body):
        return gerarResponse(400,"O parâmetro nome é obrigatório")
    if("email" not in body):
        return gerarResponse(400,"O parâmetro email é obrigatório")
    if("senha" not in body):
        return gerarResponse(400,"O parâmetro senha é obrigatório")
        
    usuario = insertUsuario(body["nome"], body["email"],body["senha"])

    return gerarResponse(200,"Usuário criado", "user",usuario )

def gerarResponse(status,mensagem,nome_do_conteudo=False,conteudo=False):
    response = {}
    response["status"] = status
    response["mensagem"]=mensagem

    if (nome_do_conteudo and conteudo):
        response [nome_do_conteudo] = conteudo
    return response

