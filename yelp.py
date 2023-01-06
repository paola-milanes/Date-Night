import requests 
from json import dump
from os import environ


api_key = "sb0-lgSojLcvo_8-ICAvMhNYWpc89Dk4cNEhfNpL6-eqdekUFZ_gs4ZkJgs8qSBNRB7FOR7mmR2Q3vQ7LgCGcf3vGs77O5lj4JgRUwsIw-aqNekJSe-HcfnNiK2kY3Yx"

url = "https://api.yelp.com/v3/businesses/search"
HEADER = {'Authorization': f'Bearer {api_key}'}



"""this will give you restaurants, parks, Museums and bars for a date"""
def find_business(term, location):

    payload = {
        "term": term,
        "location": location,
        'limit': 3,
    }
    response = requests.get(url, headers=HEADER, params=payload)
    res = response.json()


    # with open('api_res.json','w') as f:
    #     dump(businesses, f)
    # businesses = res
    return res

def search_by_id(id):
    id_url = f"https://api.yelp.com/v3/businesses/search/{id}"

    res= requests.get(id_url, headers= HEADER)
    res = res.json()

    return res
    
        