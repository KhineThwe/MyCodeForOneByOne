#https://punkapi.com/
import json
import requests
from random import randint
# url = "https://api.punkapi.com/v2/beers/random"

# r =requests.get(url)
# data = json.loads(r.text)
# print(data[0]['name'],data[0]['tagline'])
# food_choice = input("Please enter your choice: ")#for last one
# url = f'https://api.punkapi.com/v2/beers?food=pie'
food_choice = input("Please enter your choice: ")#for last one
url = f'https://api.punkapi.com/v2/beers?food={food_choice}'
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
value = randint(0,len(beer_list))
try_this = beer_list[value]

try_name = try_this['name']
try_tagline = try_this['tagline']
try_abv  = try_this['abv']
print(f'You should try{try_name}, {try_tagline}, {try_abv}%')
