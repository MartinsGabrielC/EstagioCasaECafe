# encoding: utf-8
import requests
import datetime
import sys

def postOpportunitie():
    #Url a ser enviado os dados
    url = "http://ec2-35-164-139-210.us-west-2.compute.amazonaws.com/opportunities"
    #ciacao do dicionario que recebera todos os dados a serem enviados
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
    data['id']=int(str(data['hirer']['id'])+input("id ")) #id e composto do id do contratante e do id da vaga definida
    data['title']=input("title ")
    data['description']=input("description ")
    data['created_at']=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") #data de criacao e definida automaticamente a partir do horario atual do host do script
    data['is_contact_available']=True if(input("is_contact_available(y/n) ").lower()=="y") else False  #caso a entrada seja 'y' ou 'Y' envia True, qualquer outra coisa retorna False
    data['is_active']=True if(input("is_active?(y/n) ").lower()=="y") else False #caso a entrada seja 'y' ou 'Y' envia True, qualquer outra coisa retorna False

    data['location']={} #inicializacao do dicionario vazio para receber os dados de localizacao
    data['location']['neighborhood']=input("neighborhood ")
    data['location']['address']=input("address ")
    data['location']['address_type']=input("address_type ")
    data['location']['latitude']=float(input("latitude ") or 0) #para caso de entrada vazia o valor default sera o '0'
    data['location']['longitude']=float(input("longitude ") or 0) #para caso de entrada vazia o valor default sera o '0'
    data['location']['city_id']=input("city_id ")
    data['location']['city']=input("city ")
    data['location']['zipcode']=input("zipcode ")
    data['location']['state']=input("state ")

    data['frequency']=input("frequency ")
    data['is_automatic']=True if(input("is_automatic(y/n) ").lower()=="y") else False #caso a entrada seja 'y' ou 'Y' envia True, qualquer outra coisa retorna False
    data['score']=int(input("score ") or 0) #para caso de entrada vazia o valor default sera o '0'

    data['category']={}
    data['category']['id']=int(input("category id ") or 0) #para caso de entrada vazia o valor default sera o '0'
    data['category']['name']=input("category name ")

    data['salary_requirements']=int(input("salary_requirements ") or 0) #para caso de entrada vazia o valor default sera o '0'
    data['characteristics']=[]
    data['starts']=input("starts ")
    data['amout_candidates']=int(input("amout_candidates ") or 0) #para caso de entrada vazia o valor default sera o '0'
    data['amount_visualizations']=int(input("amount_visualizations ") or 0) #para caso de entrada vazia o valor default sera o '0'
    data['feedback']=input("feedback ")
    data['salary_research']=input("salary_research ")
    data['relevancy']=input("relevancy ")

    #envio dos dados para o servidor
    try:
        html = requests.post(url,json=data)
    except :
        print("Erro: Servidor não pode ser acessado")
        sys.exit()
    #caso o envio nao tenha retornado erros
    if(html.ok):
        print("Vaga Adicionada")
    #em caso de erro imprime o codigo do erro e o texto referente a este erro
    else:
        print("Erro Status:" +html.status_code)
        print(html.json()['errors'])

postOpportunitie()
