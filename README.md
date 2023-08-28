# Proyecto ML Datapath

## Pasos
### Primer paso
#### Creación del entorno virtual a través de la terminal.
![Creación de entorno Virtual](imgs/creacion_venv.png)

#### Activación del entorno
![Activación entorno](imgs/activacion_venv.png)

### Creación del modelo de predicción
Importamos las librerías
![imagen importación](imgs/importacion.png)

### Lectura Data
Lectura archivo .CSV 
![lectura csv](imgs/lectura_csv.png)

Datos descargados desde kaggle 
[Kaggle](https://www.kaggle.com/datasets/brsdincer/pulsar-classification-for-class-prediction?datasetId=1250649&sortBy=voteCount)




### Predicción nuevos datos
Probamos a la predicción de los datos de index 0 en el dataframe df puedes verlo en el Modelo.ipynb
```bash
python main.py 140.5625 55.68378214 -0.234571412 -0.699648398 3.199832776 19.11042633 7.975531794 74.24222492
```
![resultado](imgs/resultado.png)

Probamos a la predicción de los datos de index 1 en la variable 
```python
valores_positivos = df[df.Class == 1].reset_index(drop=True)
```

```bash
python main.py 99.3671875 41.57220208 1.547196967 4.154106043 27.55518395 61.71901588 2.20880796 3.662680136
```
![prediccion_positiva](imgs/prediccion_positiva.png)


### Creación de imagen

``` bash
docker build -t ml_datapath .
```
![Alt text](imgs/imagen_datapath.png)



### Docker Run predicción

![Prediccion](imgs/prediccion_docker.png)