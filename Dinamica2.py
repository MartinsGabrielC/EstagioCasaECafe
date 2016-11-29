# encoding: utf-8
import requests
import datetime

def postOpportunitie():
    url = "http://ec2-35-164-139-210.us-west-2.compute.amazonaws.com/opportunities"
    data = {}
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
    data['id']=int(str(data['hirer']['id'])+input("id "))
    data['title']=input("title ")
    data['description']=input("description ")
    data['created_at']=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    data['is_contact_available']=True if(input("is_contact_available(y/n) ")=="y") else False
    data['is_active']=True if(input("is_active?(y/n) ")=="y") else False
    data['location']={}
    data['location']['neighborhood']=input("neighborhood ")
    data['location']['address']=input("address ")
    data['location']['address_type']=input("address_type ")
    data['location']['latitude']=float(input("latitude "))
    data['location']['longitude']=float(input("longitude "))
    data['location']['city_id']=input("city_id ")
    data['location']['city']=input("city ")
    data['location']['zipcode']=input("zipcode ")
    data['location']['state']=input("state ")
    data['frequency']=input("frequency ")
    data['is_automatic']=True if(input("is_automatic(y/n) ")=="y") else False
    data['score']=int(input("score "))
    data['category']={}
    data['category']['id']=int(input("category id "))
    data['category']['name']=input("category name ")
    data['salary_requirements']=int(input("salary_requirements "))
    data['characteristics']=[]
    data['starts']=input("starts ")
    data['amout_candidates']=int(input("amout_candidates "))
    data['amount_visualizations']=int(input("amount_visualizations "))
    data['feedback']=input("feedback ")
    data['salary_research']=input("salary_research ")
    data['relevancy']=input("relevancy ")

    html = requests.post(url,json=data)
    if(html.ok):
        print("Vaga Adicionada")
    else:
        print("Erro Status:" +html.status_code)
        print(html.json()['errors'])

postOpportunitie()
