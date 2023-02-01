import requests
import json


for i in range(6):
  url = f'http://rickandmortyapi.com/api/character/{i+1}'
  r = requests.get(url)
  j = r.json()
  name = j['name']
  status = j['status']
  print(f'El personaje {name} esta {status}')
  

