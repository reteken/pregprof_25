import json
import requests
import sqlite3



lt = []
t = 0
#lt_full = []
#while len(lt) != 16:
#    pars = requests.get('https://olimp.miet.ru/ppo_it/api')
#    info = pars.json()
#    if info not in lt:
#        lt.append(info['message']['data'])
pars = requests.get('https://olimp.miet.ru/ppo_it/api/coords')
info = pars.json()
basa1 = info['message']['sender']
basa2 = info['message']['listener']

lt = [[1, 0] * 128] * 256

def find(kolvo, now0, now1, price_full, minrast):
    price = 0
    minpoint = [0, 0]
    for o in range(now0, now0 + 64):
        for p in range(now1, now1 + 64):
            if lt[o][p] == 1:
                rast = ((now0 - o) ** 2 + (now1 - p) ** 2) ** 0.5
                print(rast)
                if rast <= 32:
                    rast_to_station = ((basa2[1] - o) ** 2 + (basa2[0] - p) ** 2) ** 0.5
                    if rast_to_station <= minrast:
                        minrast = rast_to_station
                        minpoint = [o, p]
                        price = info['message']['price'][0]
                elif rast <= 64:
                    rast_to_station = ((basa2[1] - o) ** 2 + (basa2[0] - p) ** 2) ** 0.5
                    if rast_to_station <= minrast:
                        minrast = rast_to_station
                        minpoint = [o, p]
                        price = info['message']['price'][1]
                kolvo += 1
                price_full += price
                if minrast <= 32 or minrast <= 64:
                    return kolvo, price_full
                find(kolvo, minpoint[0], minpoint[1], price_full, minrast)


print(find(0, int(basa1[0]), int(basa1[1]), 0, ((basa2[0] - basa1[0]) ** 2 + (basa2[1] - basa1[1]) ** 2) ** 0.5))

