# https://www.exchangerate-api.com/docs/standard-requests
# pip install requests
import requests

response = requests.get("https://v6.exchangerate-api.com/v6/9632e464476958fc4b144d60/latest/PLN")

if response.ok:
    data = response.json()
    print(type(data))
    time_last_update_utc = data["time_last_update_utc"]
    time_next_update_utc = data["time_next_update_utc"]
    base_code = data["base_code"]
    conversion_rates = data["conversion_rates"]

    print(time_last_update_utc)
    print(time_next_update_utc)
    print(base_code)
    print(conversion_rates)

for key in conversion_rates:
    print("Base rate: {}, value: {}".format(key, conversion_rates[key]))


for values in data.values():
    rateList = []
    rateList.append(values)

print(rateList)