"""
1. Primero importamos la Flask clase. Una instancia de esta clase será nuestra aplicación WSGI.

2. A continuación creamos una instancia de esta clase. El primer argumento es el nombre del módulo o paquete de la aplicación.
 __name__es un atajo conveniente para esto que es apropiado para la mayoría de los casos. Esto es necesario para que Flask
 sepa dónde buscar recursos como plantillas y archivos estáticos. Al instanciar el objeto Flask dentro de la variable app
 Podremos usar la anotacion @app.route(PATH, methods= ['GET'/'POST'/'PUT'/'PATCH']

5. Validación necesaria para que a la hora de instanciar la aplicacion se levante y ejecute la funcion run() de Flask

"""
import base64
import pandas as pd
import re
from io import BytesIO, StringIO
from flask import render_template, request
from app.services import initial_analisys
from werkzeug.datastructures.file_storage import FileStorage
import matplotlib.pyplot as plt
from flask import Flask  # 1

app = Flask(__name__)  # 2


@app.route('/', methods=[ 'GET' ])
def index():
    return render_template('index.html')

@app.route('/d-patron', methods=[ 'GET', 'POST' ])
def adivina_patron():
    predictions = None
    plot_url = None
    error_message = None

    if request.method == 'POST':
        uploaded_file: FileStorage = request.files[ 'archivo' ]  # Nombre del 'name' de HTML del formulario
        if uploaded_file.filename != '':
            # Leer el archivo CSV directamente desde el objeto uploaded_file
            csv_data = StringIO(uploaded_file.read().decode('utf-8'))
            df = pd.read_csv(csv_data)
            # Validar la nomenclatura del DataFrame
            # Llamar a initial_analisys para obtener la historia del entrenamiento y el gráfico
            predictions = initial_analisys(df)
            # Generar y mostrar el gráfico (código anterior)
            plot_url = config_show_graphic(predictions, plot_url)
    return render_template('d-patron.html', predictions=predictions, plot_url=plot_url, error_message=error_message)


def config_show_graphic(prediction, plot_url):
    # Generar y guardar el gráfico
    plt.figure(figsize=(10, 6))
    plt.plot(prediction.history[ 'loss' ], label='Perdida en Entrenamiento')
    plt.plot(prediction.history[ 'val_loss' ], label='Perdida en Validacion')
    plt.xlabel('Epocas')
    plt.ylabel('Perdida')
    plt.title('Mejora de la perdida durante el entrenamiento')
    plt.legend()
    # Guardar el gráfico en un objeto BytesIO
    img_buf = BytesIO()
    plt.savefig(img_buf, format='png')
    img_buf.seek(0)
    # Codificar el gráfico en base64
    plot_url = base64.b64encode(img_buf.read()).decode()
    return plot_url


def config_show_graphic_predictions(data_summary, predictions, plot_url):
    # Generar y guardar el gráfico
    plt.figure(figsize=(10, 6))
    plt.plot(data_summary[ 'COLUMNA1' ], label='COLUMNA1')
    plt.plot(data_summary[ 'COLUMNA2' ], label='COLUMNA2')
    plt.xlabel('Muestras')
    plt.ylabel('Valores')
    plt.title('Gráfico de Datos y Predicciones')
    plt.legend()

    # Agregar las predicciones a la gráfica
    plt.plot(predictions, label='Predicciones')

    # Guardar el gráfico en un objeto BytesIO
    img_buf = BytesIO()
    plt.savefig(img_buf, format='png')
    img_buf.seek(0)

    # Codificar el gráfico en base64
    plot_url = base64.b64encode(img_buf.read()).decode()

    return plot_url


@app.route('/pagina2')
def pagina2():
    # Lógica para la segunda página
    return "Esta es la página 2"


if __name__ == '__main__': # 5
    app.run()
