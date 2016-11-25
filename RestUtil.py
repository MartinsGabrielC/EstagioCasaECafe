from urllib.request import urlopen
import json
import sys

def opportunitiesCount(ID):
    url = "http://ec2-35-164-139-210.us-west-2.compute.amazonaws.com/hirers/"+ID+"/opportunities"
    html = urlopen(url).read().decode("utf-8")
    j_obj = json.loads(html)
    print(len(j_obj))
    
try:
	ID = sys.argv[1]
	opportunitiesCount(ID)
except IndexError:
	print("Error: Enviar ID como argumento")
	sys.exit()
