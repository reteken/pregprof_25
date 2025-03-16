import requests

response = requests.get("https://olimp.miet.ru/ppo_it/api/coords")

response_json = response.json()

print(response_json)
