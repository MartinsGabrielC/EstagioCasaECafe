import requests
import json
import sys

def opportunitiesCount(ID):
    #criacao do get
    url = "http://ec2-35-164-139-210.us-west-2.compute.amazonaws.com/hirers/"+ID+"/opportunities"
    html = requests.get(url)
    #criacao de um objeto json para decodificacao
    j_obj = json.loads(html.text)
    print(len(j_obj))

try:
	ID = sys.argv[1]
	opportunitiesCount(ID)
except IndexError:
	print("Error: Enviar ID como argumento")
	sys.exit()
