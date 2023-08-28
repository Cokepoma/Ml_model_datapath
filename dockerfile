#Utilizamos la imagen base
FROM python:3.9

# Creamos la carpeta APP
WORKDIR /app

# Copiamos el archivo Requirements.txt
COPY requirements.txt .

# Ejecutamso las instalaciones de librerias necesarias
RUN pip install --no-cache-dir -r requirements.txt

# Copiamos los archivos necesarios a la carpeta de la imagen
COPY model.h5 .
COPY scaler.pkl .
COPY main.py .

# Le decimos que cuando arranque ejecute el archivo main.py
ENTRYPOINT [ "python", "main.py" ]
