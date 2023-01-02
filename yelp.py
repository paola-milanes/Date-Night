import requests

api_key = "x"
url = "https://api.yelp.com/v3/businesses/search"
HEADER = {'Authorization': f'Bearer {api_key} '}

"""this will give you restaurants, parks, Museums and bars for a date"""
def find_buisness(term, location):

    payload = {
        "term": term,
        "location": location,
        'limit': 20,
    }
    res = requests.get(url, headers=HEADER, params=payload)
    res_jsn = res.json()

    return res_jsn