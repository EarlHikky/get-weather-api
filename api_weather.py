import requests

places = ["san francisco", "london", "svo", "череповец"]
payload = {"n": "", "T": "", "q": "", "M": "", "lang": "ru"}
url_template = 'http://wttr.in/{}'

for place in places:
    url = url_template.format(place)
    response = requests.get(url, params=payload)
    response.raise_for_status()
    print(response.text)
