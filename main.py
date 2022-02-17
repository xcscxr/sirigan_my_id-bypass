import requests
from base64 import b64decode

url = ""
# https://sirigan.my.id/xyz123

def bypass(url):
    client = requests.Session()
    res = client.get(url)
    url = res.url.split('=', maxsplit=1)[-1]

    while True:
        try: url = b64decode(url).decode('utf-8')
        except: break

    return url.split('url=')[-1]

print(bypass(url))
