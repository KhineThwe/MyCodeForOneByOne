#https://punkapi.com/
import json
import requests

# url = "https://api.punkapi.com/v2/beers/random"

# r =requests.get(url)
# data = json.loads(r.text)
# print(data[0]['name'],data[0]['tagline'])

url = 'https://api.punkapi.com/v2/beers?food=burger'
r =requests.get(url)
data = json.loads(r.text)

beer_list = []
for beer in data:
    name = beer['name']
    tagline = beer['tagline']
    abv = beer['abv']
    # print(name,tagline,abv)
    beer_items ={
        'name' : name,
        'tagline': tagline,
        'abv' : abv
    }
    beer_list.append(beer_items)
print(beer_list)
