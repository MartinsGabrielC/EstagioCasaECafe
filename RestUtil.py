from urllib.request import urlopen
import json
import pprint

url = "http://ec2-35-164-139-210.us-west-2.compute.amazonaws.com/hirers/111222/opportunities"
html = urlopen(url).read().decode("utf-8")
j_obj = json.loads(html)
