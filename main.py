# Importamos las librerias necesarias
import sys
import numpy as np
from tensorflow import keras
import pickle

# Funciones (lectura de estandar escala modelo predictivo y función principal de predicion con lectura del modelo .H5 y realización de la predicción)
def load_scaler(scaler_filename):
    with open(scaler_filename, 'rb') as scaler_file:
        scaler = pickle.load(scaler_file)
    return scaler

def main():
    # Lee el comando
    if len(sys.argv) < 2:
        print("Por favor, proporciona los valores de las variables a predecir.")
        return

    # Cargar el modelo
    MODEL_PATH = "model.h5"
    model = keras.models.load_model(MODEL_PATH)
    print(model.summary())

    # Cargar el objeto scaler
    TOKENIZER_PATH = 'scaler.pkl'
    scaler = load_scaler(TOKENIZER_PATH)

    # Obtener los valores de las variables a predecir desde los argumentos de la línea de comandos
    input_values = [float(arg) for arg in sys.argv[1:]]
    input_values_scaled = scaler.transform(np.array([input_values]))

    # Realiza la predicción
    prediction = model.predict(input_values_scaled)
    print("Predicción:", prediction)

if __name__ == "__main__":
    main()
