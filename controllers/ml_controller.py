from fastapi import APIRouter, HTTPException, status
from models import Prediction_Input,Prediction_Output
# Importamos las librerias necesarias
import sys
import numpy as np
from tensorflow import keras
import pickle

def load_scaler(scaler_filename):
    with open(scaler_filename, 'rb') as scaler_file:
        scaler = pickle.load(scaler_file)
    return scaler 

MODEL_PATH = "model.h5"
model = keras.models.load_model(MODEL_PATH)


# Cargar el objeto scaler
TOKENIZER_PATH = 'scaler.pkl'
scaler = load_scaler(TOKENIZER_PATH)

router = APIRouter()
preds = []

@router.get("/ml")
def get_pred():
    return preds

@router.post("/ml",status_code=status.HTTP_201_CREATED, response_model = Prediction_Output)
def predict(pred_input: Prediction_Input):
    print(pred_input)
    input_values = pred_input.input.split(",")  # Dividir la cadena en una lista de cadenas
    input_values = [value.strip() for value in input_values]  # Eliminar espacios en blanco de las cadenas
    lista = []
    for var in input_values:
        var = float(var)
        lista.append(var)
    # A partir de aquí, puedes realizar cualquier operación que desees con la lista de números.
    # Asumiendo que tienes un modelo y un scaler definidos previamente:
    input_values_scaled = scaler.transform(np.array([lista]))
    print(input_values_scaled)
    prediction = model.predict(input_values_scaled)
    prediction_dict = {"input": str(pred_input), "output": str(prediction)}  # Corrección aquí
    preds.append(prediction_dict)
    return prediction_dict  