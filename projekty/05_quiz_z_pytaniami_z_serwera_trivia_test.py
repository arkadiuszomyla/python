# https://the-trivia-api.com/license/
# https://the-trivia-api.com/docs/

import requests

headers = {
    'Content-Type':'application/json'
}
response = requests.get("https://the-trivia-api.com/api/questions?limit=20&categories=science,history", headers=headers)

my_dict = {}

while response.ok:
    data = response.json()
    #print(type(data))  #list
    i = 1

    for d in data:
        #print(type(d))   #dict
        d["numer"] = i
        for values in d.values():
            if values == 6:
                print(d.get("question"))
        # print(d)
        i += 1
    break







