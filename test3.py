# 120

import requests
btc = requests.get("https://api.bithumb.com/public/ticker/").json()['data']

print("{}:{}".format(key, btc[key]))
