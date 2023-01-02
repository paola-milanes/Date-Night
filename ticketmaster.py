import requests
api_key = ""
HEADER = {'apikey': api_key,}
url = 'https://app.ticketmaster.com/discovery/v2/events'
# res = requests.get(url, params=payload)
# ticket_m = res.json()
# print(res)


def find_event(City, startDateTime ):
    payload = {
        "city" : City,
        "startDateTime" : startDateTime
    }
    res = requests.get(url, header = HEADER, params=payload)
    res_json = res.json()
    return res_json
