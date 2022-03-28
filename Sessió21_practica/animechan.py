import requests

#prova de cridar a una api
response = requests.get('https://animechan.vercel.app/api/random')

print(response.json())