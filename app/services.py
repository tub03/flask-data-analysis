
import pandas as pd
import numpy as np
import tensorflow as tf


# Función para entrenar el modelo
def train_rnn_model(data, input_shape_c1, input_shape_c2):
    x = data[:, 0]  # COLUMNA1
    y = data[:, 1]  # COLUMNA2
    x = x.reshape(x.shape[0], x.shape[1], 1)  # Reshape para que sea adecuado para la entrada de la RNN

    # Early Stopping
    early_stopping = tf.keras.callbacks.EarlyStopping(monitor='val_loss', patience=10, restore_best_weights=True)

    # Aumento de Datos (Data Augmentation)
    data_augmentation = tf.keras.Sequential([
        tf.keras.layers.experimental.preprocessing.RandomTranslation(0.2, 0.2),
        tf.keras.layers.experimental.preprocessing.RandomRotation(0.2)
    ])

    data_augmentation.compile()

    # Ajuste de Hiperparámetros
    learning_rate = 0.001
    batch_size = 32

    optimizer = tf.keras.optimizers.Adam(learning_rate=learning_rate)

    # Regularización Dropout
    model = create_rnn_model(input_shape_c1, input_shape_c2)
    model.add(tf.keras.layers.Dropout(0.2))  # Agregar capa de dropout

    # Compilar el modelo con el optimizador personalizado
    model.compile(optimizer=optimizer, loss='mean_squared_error')

    # Entrenar el modelo
    model.fit(data_augmentation(x), y, epochs=50, batch_size=batch_size, validation_split=0.2, callbacks=[early_stopping])

    # Guardar el modelo en un archivo HDF5 después del entrenamiento
    model.save("app/rnn/fase0/modelo_entrenado.h5")

    return model


# Función para crear el modelo RNN
def create_rnn_model(input_shape_c1, input_shape_c2):
    # Definicion d entradas separadas:
    inputs_c1 = tf.keras.layers.Input(shape=input_shape_c1, name='inputs_c1')
    inputs_c2 = tf.keras.layers.Input(shape=input_shape_c2, name='inputs_c2')

    # Capas LSTM separadas para cada columna
    lstm_c1 = tf.keras.layers.LSTM(32)(inputs_c1)
    lstm_c2 = tf.keras.layers.LSTM(32)(inputs_c2)

    # Concatenar las salidas de ambas columnas
    merged = tf.keras.layers.concatenate([lstm_c1, lstm_c2])

    # Capa de salida
    output = tf.keras.layers.Dense(1)(merged)

    model = tf.keras.Model(inputs=[ inputs_c1, inputs_c2 ], outputs=output)
    model.compile(optimizer='adam', loss='mean_squared_error')

    return model


# Función para realizar el preprocesamiento de los datos
def preprocess_data(df):
    # Eliminar la primera fila (encabezados)
    df = df.iloc[ 1: ]
    data = df.values
    return data


# Función para realizar un análisis inicial de los datos
def initial_analisys(df):
    input_shape_c1 = (3, 1)  # COLUMNA1 tiene 3 cifras
    input_shape_c2 = (5, 1)  # COLUMNA2 tiene 5 cifras
    data = preprocess_data(df)

    # Entrenar el modelo y obtener la historia del entrenamiento
    model = train_rnn_model(data, input_shape_c1, input_shape_c2)

    # Realizar predicciones utilizando el modelo cargado
    predictions = model.loaded_model.predict(data)

    error_message = "El archivo CSV no cumple con la nomenclatura requerida (COLUMNA1: 3 cifras, COLUMNA2: 5 cifras)."

    return predictions
