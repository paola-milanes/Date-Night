import requests
from json import dump
api_key = "3604e5cc59c4f64bff82a3d5a1720b32"
payloads = {'api_key': api_key}
url = 'https://api.themoviedb.org/3/movie/now_playing'


    
def get_movies():
    res= requests.get(url, params=payloads)
    res_jason = res.json()
    return res_jason

# with open('movie_rea.json','w') as f:
#     dump(res_jason, f)

def movie_img(id):
    url = 'https://api.themoviedb.org/3/movie/315162/images'
    res= requests.get(url, params=payloads)
    res_jason = res.json()
    # print(res_jason)
    return res_jason
# movie_img(2)