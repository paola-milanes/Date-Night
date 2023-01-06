import requests
api_key = "ftjzgz6yamk4m7q687mb66fh"
HEADER = {'apikey': api_key,}
url = 'http://api.rottentomatoes.com/api/public/v1.0'

res= requests.get(url, params = HEADER)
res_jason = res.json()
print(res_jason)
