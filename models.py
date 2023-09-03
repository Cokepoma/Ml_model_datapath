from pydantic import BaseModel

class Prediction_Input(BaseModel):
    input : str

class Prediction_Output(BaseModel):
    input : str
    output : str