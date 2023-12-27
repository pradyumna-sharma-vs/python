import requests
import json
response = requests.get("https://swapi.dev/api/films/")
response.raise_for_status()
data = response.json()
list1=[]
list2=[]
number = data["count"]
for i in range (0,number,1):
    list1.append(data["results"][i]['title'])
    list2.append(data["results"][i]['producer'])
    
print('movie names',list1)
print('Producers',list2)
