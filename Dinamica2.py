# encoding: utf-8
import requests
import datetime
import sys

#inputToInt
#input: String prompt
#output: Integer data
#Pede por uma entrada de dado:
#   caso essa entrada seja vazia retorna 0
#   senão tenta fazer a conversão da entrada para inteiro
#       caso consigo fazer a conversão retorna o valor
#       senão imprime mensagem de erro e pede uma nova entrada
def inputToInt(prompt):
    while True:
        data = input(prompt)
        if(not data):
            return 0
        else:
            try:
                return int(data)
            except ValueError:
                print("Esperado um valor inteiro")
                continue

#inputToFloat
#input: String prompt
#output: Float data
#Pede por uma entrada de dado:
#   caso essa entrada seja vazia retorna 0
#   senão tenta fazer a conversão da entrada para real
#       caso consigo fazer a conversão retorna o valor
#       senão imprime mensagem de erro e pede uma nova entrada
def inputToFloat(prompt):
    while True:
        data = input(prompt)
        if(not data):
            return 0.0
        else:
            try:
                return float(data)
            except ValueError:
                print("Esperado um valor real")
                continue

#inputToBool
#input: String prompt
#output: Bool data
#Pede por uma entrada de dado:
#   caso essa entrada seja 'y' ou 'Y' retorna verdadeiro
#   caso essa entrada seja vazia, 'n' ou 'N' retorna falso
#   senão imprime mensagem de erro e pede uma nova entrada
def inputToBool(prompt):
    while True:
        data = input(prompt).lower()
        if data == 'y':
            return True
        elif data == 'n' or not data:
            return False
        else:
            print("Esperado y ou n")
            continue

def postOpportunitie():
    #Url a ser enviado os dados
    url = "http://ec2-35-164-223-211.us-west-2.compute.amazonaws.com/opportunities"
    #ciacao do dicionario que recebera todos os dados a serem enviados
    #dados são colocados na formatação de json
    data = {}
    #dados do contratante sao definidos fixo
    data['hirer']= {
        "id":201294,
        "name":"Gabriel Martins de Castro",
        "account_type":"pf",
        "cnpj":None,
        "company_contact_name":None,
        "phone":"(11) 2440-2307",
        "email":"martins.gabriel.c@gmail.com",
        "mobile_phone":"(21) 93234-8378",
        "is_plan_active":True
    }
    #inicio da leitura dos dados que serao enviados
    oppID = inputToInt("id ")
    data['id']=int(str(data['hirer']['id']) + str(abs(oppID))) #id e composto do id do contratante e do id da vaga definida
    data['title']=input("title ")
    data['description']=input("description ")
    data['created_at']=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") #data de criacao e definida automaticamente
    data['is_contact_available']=inputToBool("is_contact_available(y/n) ")
    data['is_active']=inputToBool("is_active?(y/n) ")

    data['location']={} #inicializacao do dicionario vazio para receber os dados de localizacao
    data['location']['neighborhood']=input("neighborhood ")
    data['location']['address']=input("address ")
    data['location']['address_type']=input("address_type ")
    data['location']['latitude']=inputToFloat("latitude ")
    data['location']['longitude']=inputToFloat("longitude ")
    data['location']['city_id']=input("city_id ")
    data['location']['city']=input("city ")
    data['location']['zipcode']=input("zipcode ")
    data['location']['state']=input("state ")

    data['frequency']=input("frequency ")
    data['is_automatic']=inputToBool("is_automatic(y/n) ")
    data['score']=inputToInt("score ")

    data['category']={}
    data['category']['id']=inputToInt("category id ")
    data['category']['name']=input("category name ")

    data['salary_requirements']=inputToInt("salary_requirements ")
    data['characteristics']=[]
    data['starts']=input("starts ")
    data['amout_candidates']=inputToInt("amout_candidates ")
    data['amount_visualizations']=inputToInt("amount_visualizations ")
    data['feedback']=input("feedback ")
    data['salary_research']=input("salary_research ")
    data['relevancy']=input("relevancy ")

    try:
        #tentativa de enviar os dados para o servidor
        html = requests.post(url,json=data)
    except :
        #caso o servidor não esteja acessível
        print("\nErro: Servidor não pode ser acessado")
        sys.exit()

    if(html.ok):
        #caso o envio nao tenha retornado erros
        print("\nVaga Adicionada")
    else:
        #em caso de erro imprime o codigo do erro e o texto referente a este erro
        print("\nErro Status:" +html.status_code)
        print(html.json()['errors'])

postOpportunitie()
