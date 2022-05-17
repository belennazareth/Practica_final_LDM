import requests
import json
import os

url_base="https://ghibliapi.herokuapp.com/films"

## Petición para la película Ponyo usando como parámetro el título y dando como salida el título seguido de la descripción 

title={'title':'Ponyo'}
r =requests.get(url_base, params=title)
if r.status_code == 200:
    doc=r.json()
    for elem in doc:
        print(elem["title"]+ " : " +elem["description"])


## Petición para mostrar las películas usando como parámetro el nombre de uno de los productores

producer={'producer':'Toshio Suzuki'}

r = requests.get(url_base, params=producer)
if r.status_code == 200:
    doc=r.json()
    print()
    print(elem["producer"])
    for elem in doc:
        print(" : " +elem["description"])

## Petición que muestra la información de las películas usando de parámetro director

#director={'director':'Hayao Miyazaki'}
#
#r= requests.get("https://ghibliapi.herokuapp.com/films", params=director)
#r.status_code
#r.text
#