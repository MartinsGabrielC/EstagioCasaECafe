# encoding utf-8
import requests
import json
import sys

def opportunitiesCount(ID):
    #criacao do get
    url = "http://ec2-35-164-139-210.us-west-2.compute.amazonaws.com/hirers/"+ID+"/opportunities"
    try:
        html = requests.get(url)
    except:
        print("Erro: Servidor não pode ser acessado")
        sys.exit()
    #criacao de um objeto json para decodificacao
    j_obj = json.loads(html.text)
    print(len(j_obj))

try:
    #id enviado como argumento do script
	ID = sys.argv[1]
    #chamada da funcao com o id recebido
	opportunitiesCount(ID)
#caso nao haja id como argumento
except IndexError:
	print("Erro: Enviar ID como argumento")
	sys.exit()
