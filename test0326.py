import json
from urllib.request import urlopen
url = 'https://www.thecocktaildb.com/api/json/v1/1/search.php?strDrink=margarita'
response = urlopen(url)
source = response.read().decode('utf-8')

print(source[:500])

parsed = json.loads(source)
posts = []
for d in parsed:
    posts.append(d['idDrink'])

text = ''.join(posts)
[print(text)]
