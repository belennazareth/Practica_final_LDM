Primero probaremos la API principal, haremos tres peticiones con curl usando parámetros:

* Comprobamos que introduciendo el "id" como parámetro de como salida la información de la película:

        curl -X GET -H "Content-Type: application/json" "https://ghibliapi.herokuapp.com/films?id=790e0028-a31c-4626-a694-86b7a8cada40"


    ![](/screenshots/peticion1.png)


* A continuación probamos con parámetros que contienen espacios como puede ser el título:

        curl -X GET -H "Content-Type: application/json" "https://ghibliapi.herokuapp.com/films?title=Whisper+of+the+Heart"


    ![](/screenshots/peticion2.png)


* Por último haremos una petición con comillas y espacios en el título:

        curl -X GET -H "Content-Type: application/json" "https://ghibliapi.herokuapp.com/films?title=Howl's+Moving+Castle"

    ![](/screenshots/peticion3.png)