# Guía de Instalación de Tensorflow

Esta guía te ayudará a instalar la biblioteca `Tensorflow` en tu entorno de desarrollo de Python. Asegúrate de seguir los pasos a continuación.

 [Curso scikit-learn](https://www.youtube.com/watch?v=J8VOHBkNIT0&list=PLzKF7sAvC2S9wrGq0UPqzbypOzwXagE2J)

 [Curso de TensorFlow y comprension de redes neuronales](https://www.youtube.com/watch?v=wQ8BIBpya2k&list=PLQVvvaa0QuDfhTox0AjmQ6tvTgMBZBEXN&ab_channel=sentdex)


## Pasos de Instalación

### 1. Configurar un Entorno Virtual (opcional pero recomendado)

Si no tienes un entorno virtual, puedes crear uno para mantener tus dependencias de proyectos separadas. 
Utiliza `virtualenv` o `venv`. 

Ejemplo con `venv`:

```commandline
python -m venv .venv
.venv\Scripts\activate
```

### 2. Dependencias necesarias
#### 2.1. Actualizar pip & setuptools (opcional)
````commandline
C:\rutaAlEnv\flask-data-analysis\.venv\Scripts\python.exe pip install --upgrade pip
C:\rutaAlEnv\flask-data-analysis\.venv\Scripts\python.exe pip install --upgrade setuptools
````
#### 2.2. Numpy
````commandline
C:\rutaAlEnv\flask-data-analysis\.venv\Scripts\python.exe pip install --upgrade pip
C:\rutaAlEnv\flask-data-analysis\.venv\Scripts\python.exe pip install numpy
````

### 3. Instalar numpy, tensorflow y pandas
Debes instalarlos utiliza los siguientes comandos:

```bash
pip install numpy -U --only-binary :all:
pip install tensorflow -U --only-binary :all:
pip install pandas -U --only-binary :all:
```
Los parámetros `-U --only-binary :all:` se utilizan para asegurarse de que pandas se instale
a partir de ruedas precompiladas, lo que puede ayudar a evitar problemas de compilación y acelerar el proceso de instalación.
Yo obtenía un error constante al querer instalar de forma normal los packages `'numpy'`, `'pandas'` y `'tensorflow'`

### 4. Verificar la instalación
Para asegurarte de que todo se haya instalado correctamente, verifica la versión de scikit-learn:

```bash
python -c "import pandas; print(pandas.__version__)"
python -c "import numpy; print(numpy.__version__)"
python -c "import tensorflow; print(tensorflow.__version__)"
```
Esto te imprimirá en el terminal la versión correspondiente.

hola pichon,