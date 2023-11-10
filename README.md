# FLASK APPLICATION

## Aplicación web
**Desarrollada con las siguientes tecnologías** 

| Framework             | [Flask 3.0](https://flask.palletsprojects.com/en/3.0.x/installation/) |
|-----------------------|-----------------------------------------------------------------------|
| Programming Language  | Python 3.9                                                            |
| IDE                   | PyCharm                                                               |
| Managament Packages   | pip 23.3.1                                                            |



## Librerias
- Las librerias pueden ser importadas directamente en el entorno virtual a nivel de proyecto(dentro de la carpeta del proyecto)
1. Crear una carpeta .venv para nuestro entorno virtual
`py -3 -m venv .venv`
2. Activar el entorno
`venv\Scripts\activate`
3. Ahora se nos activará el entorno lo que añadirá el prefijo (.venv) en tu consola
4. Ahora podemos realizar el comando de pip para instalar las dependencias impuestas en el archivo 'requirements.txt'
`pip install -r requirements.txt`

5. Ahora podemos instalar las librerias o dependencias que queramos en nuestro entorno virtual activado.

Como por ejemplo:

 `pip install Flask`

Si añades alguna nueva librería o paquete, debes volver a ejecutar el comando que genera el archivo 'requirements.txt'

`pip freeze > requirements.txt`

¿Cuando estás añadiendo una libreria o paquete?
- Cuando ejecutas el comando `pip install XXXX`
	- Normalmente instalas un paquete/libreria cuando sabes que lo necesitas


# Ejecución
Esta aplicación se ejecuta yendo al archivo 'main.py' y pulsando en el botón de ejecución en el 'if'