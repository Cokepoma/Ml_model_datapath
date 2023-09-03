# Importamos librerias fastapi 
from fastapi import FastAPI
#Importamos el archivo routes
from routes import router

app = FastAPI()

app.include_router(router)