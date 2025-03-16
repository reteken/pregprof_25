import requests
import sqlite3



lt = []
t = 0
while len(lt) != 16:
    pars = requests.get('https://olimp.miet.ru/ppo_it/api')
    info = pars.json()
    if info not in lt:
        lt.append(info)
    else:
        t += 1


for i in lt:
    print(i)
print(len(lt))
print(t)
a = json.dumps(lt)
with open('data.jsonl', 'w') as f:
    f.write(a)
