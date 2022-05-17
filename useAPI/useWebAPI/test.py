import requests

url = "https://www.baidu.com/"
res = requests.get(url)
print(type(res))
