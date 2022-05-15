import requests

r = requests.get('https://ghibliapi.herokuapp.com/films')
r.json()