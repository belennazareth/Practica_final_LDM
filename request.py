import requests

## Petición para la película Ponyo usando como parámetro el título

title={'title':'Ponyo'}
r =requests.get("https://ghibliapi.herokuapp.com/films", params=title)
r.status_code
r.text


## Petición para mostrar las películas usando como parámetro el nombre de uno de los productores

producer={'producer':'Toshio Suzuki'}

r = requests.get("https://ghibliapi.herokuapp.com/films", params=producer)
r.status_code
r.text

## Petición que muestra la información de las películas usando de parámetro