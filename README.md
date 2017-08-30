Twitter-Python-MongoDB
===============
Gio Cádiz
* Twitter : [@Gio_Cadiz](https://twitter.com/Gio_Cadiz)
## Description
El objetivo de este script en [Python](https://es.wikipedia.org/wiki/Python), es obtener la información generada por los 
usuarios de [Twitter](https://twitter.com/),
mediante un [#Hashtag](https://es.wikipedia.org/wiki/Hashtag) especifico desde la  [API oficial de Twitter](https://apps.twitter.com/) 
y posteriormente almacenar los datos en una base de datos [NoSQL](https://es.wikipedia.org/wiki/NoSQL) 
llamada [MongoDB](https://es.wikipedia.org/wiki/MongoDB).




## Requirements
Este script requiere lo siguiente:
* Python version 2.7.13 [Download Python](https://www.python.org/downloads/)
* Api Twitter [Twitter Apps](https://apps.twitter.com/)
* Twython [Web Oficial](https://pypi.python.org/pypi/twython/2.7.0)
* Pymongo [Web Oficial](https://api.mongodb.com/python/2.7.2/installation.html)
* MongoDB [Download](https://www.mongodb.com/download-center#community), [Documentación Oficial](https://docs.mongodb.com/)
* Robo 3T [Download](https://robomongo.org/download)

## Installation
La forma más fácil de instalar la última versión de **twython** y **pymongo** es utilizando **pip** o **easy_install**:
>`pip install twython`

>`easy_install twython`

>`pip install pymongo`

>`easy_install pymongo`

Si no tenemos una cuenta de [Twitter](https://twitter.com/) hay que registrarnos, en caso de que la tengamos, 
vamos a logearnos en el [portal de desarrollo](https://apps.twitter.com/) y crearemos una nueva aplicación, 
para tener acceso a los datos de autenticación [OAuth](https://es.wikipedia.org/wiki/OAuth) a la API.
>
Una vez creada la aplicación en el portal debemos guardar los siguientes valores para la autenticación:
>`consumer_key`,
>`consumer_secret`,
>`access_token_key`,
>`access_token_secret`
>
Reemplazar los valores de autenticación en el script:

>`consumer_key = 'consumer_key here'`<br/>
>`consumer_secret = 'consumer_secret here'`<br/>
>`access_token = 'access_token here'`<br/>
>`access_token_secret = 'access_token_secret here'`
>
Reemplazar [#hashtag](https://es.wikipedia.org/wiki/Hashtag) con una "palabra" como parametro de busqueda:
```python
twitterStream.filter(track = ["#hashtag here"])
``` 
>
Para instalar **MongoDB** se recomienda seguir el [tutorial](https://docs.mongodb.com/tutorials/) de la web oficial, 
correspondiente al [sistema operativo](https://es.wikipedia.org/wiki/Sistema_operativo) de cada usuario.
>
**Robo 3T** *(anteriormente Robomongo)* nos permite conectarnos al servidor de base de datos de forma sencilla y 
es la interfaz gráfica de usuario ligera libre para los entusiastas de MongoDB.
