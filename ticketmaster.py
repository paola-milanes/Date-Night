import requests
url = 'https://app.ticketmaster.com/discovery/v2/events'
# res = requests.get(url, params=payload)
# ticket_m = res.json()
# print(res)


def find_event(City, startDateTime):
    payload = {
        'apikey':"nbWkAQsjj5SuyrsYanz2r5u2n60ajrWC",
        "city" : City,
    }
    res = requests.get(url, params=payload)
    res_json = res.json()
    events = res_json['_embedded']['events']
    print(events[0])
    return events
find_event("san jose", "moday")