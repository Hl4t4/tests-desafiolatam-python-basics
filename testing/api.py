import json
import requests
app_id = "3410023e"
app_key = "6f82faaee87b2b823916b58f72f648b6"
word = "hello"
url = f"https://od-api.oxforddictionaries.com/api/v2/entries/en/{word}"
r = requests.get(url, headers = {"app_id": app_id, "app_key": app_key})
print(r)
r = json.loads(r.text)
print(r)