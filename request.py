import requests

## Petición para la película Ponyo usando como parámetro el título

r =requests.get("https://ghibliapi.herokuapp.com/films?title=Ponyo")
r.status_code
r.text


