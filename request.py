import requests

## Petición para la película Ponyo usando como parámetro el título


title={'title':'Ponyo'}
r =requests.get("https://ghibliapi.herokuapp.com/films", params=title)
r.status_code
r.text


