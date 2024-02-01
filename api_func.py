import pandas as pd
import numpy as np
from math import radians, sin, cos, sqrt, atan2

hoteles = pd.read_csv('hoteles_unicos.csv')
categorias = pd.read_csv('categorias_unicas.csv')

def presentacion():
    '''
    Genera una página de presentación HTML para la API Steam de consultas de videojuegos.
    
    Returns:
    str: Código HTML que muestra la página de presentación.
    '''
    return '''
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Betta API</title>
        <style>
            body {
                font-family: 'Arial', sans-serif;
                background-image: url('https://www.canva.com/design/DAF6rs8MY2s/D_7gB7CeBAAxfx7leOATkA/view?utm_content=DAF6rs8MY2s&utm_campaign=designshare&utm_medium=link&utm_source=editor');
                background-attachment: fixed;
                background-color: #f0f0f0;
                color: #333;
                margin: 0;
                padding: 0;
            }

            header {
                background-color: #333;
                color: white;
                padding: 18.5px;
                text-align: center;
            }

            main {
                max-width: 800px;
                margin: 20px auto;
                padding: 20px;
                background-color: rgba(255, 255, 255, 0.8);
                box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            }

            a {
                color: #007bff;
                text-decoration: none;
            }

            a:hover {
                text-decoration: underline;
            }

            footer {
                text-align: center;
                margin-top: 20px;
                padding: 10px;
                background-color: #333;
                color: white;
            }
        </style>
    </head>
    <body>
        <header>
            <h1>Betta Proyecto Final Henrry</h1>
        </header>
        
        <main>

        </main>
        <br>
        <br>
        <br>
        <br>
        <footer>
            <p>&copy; 2023</p>
        </footer>
    </body>
    </html>
    '''
    
def top_hoteles_por_ubicacion(estado:str, ciudad:str):

    estado = estado.upper()
    ciudad = ciudad.capitalize()
    
    hoteles_ubicacion = hoteles[(hoteles['state'] == estado) & (hoteles['city'] == ciudad)]
    if hoteles_ubicacion.empty:
        return {"No se encontraron hoteles en la ubicación proporcionada."}
    else:
        top_hoteles = hoteles_ubicacion.nlargest(5, 'bussines_stars')
        top_hoteles = top_hoteles[['name', 'bussines_stars']]
        return {f'El top de hoteles para tu ubicación es':top_hoteles.to_dict(orient='records')}



def distancia_haversine(lat1, lon1, lat2, lon2):
    # Convertir grados a radianes
    lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])

    # Radio de la Tierra en kilómetros
    radio_tierra = 6371.0

    # Diferencia de latitud y longitud
    dlat = lat2 - lat1
    dlon = lon2 - lon1

    # Calcular la distancia utilizando la fórmula haversine
    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    distancia = radio_tierra * c

    return distancia

# Función para ordenar el DataFrame categorias en función de la cercanía al local indicado
def ordenar_por_cercania(local:str):
    #global hoteles, categorias
    global hoteles, categorias

    # Obtiene las coordenadas del local indicado
    latitud_local, longitud_local, ciudad_local, estado_local = hoteles[hoteles['name'] == local][['latitude', 'longitude','city','state']].values[0]

    # Filtrar las filas que tienen la misma ciudad y estado que el local
    categorias = categorias[(categorias['city'] == ciudad_local) & (categorias['state'] == estado_local)]

    # Calculamos la distancia entre las coordenadas del local y cada negocio en categorias
    categorias['distancia'] = categorias.apply(lambda row: distancia_haversine(latitud_local, longitud_local, row['latitude'], row['longitude']), axis=1)

    # Ordena categorias por la distancia calculada
    categorias_ordenado = categorias.sort_values(by='distancia')
    categorias_ordenado = categorias_ordenado[['name','categories', 'distancia', 'city', 'state']]
    
    return {f'Los locales mas cercanos son':categorias_ordenado.to_dict(orient='records')}

# Función para ordenar el DataFrame categorias por 'bussines_stars' de mayor a menor, conservando la distancia
def ordenar_por_bussines_stars(local):
    global hoteles, categorias
    # Obtenemos las coordenadas del local indicado
    
    latitud_local, longitud_local, ciudad_local, estado_local = hoteles[hoteles['name'] == local][['latitude', 'longitude','city','state']].values[0]
    #latitud_local, longitud_local = hoteles[hoteles['name'] == local][['latitude', 'longitude']].values[0]
    
    # Calculamos la distancia entre las coordenadas del local y cada negocio en categorias
    categorias['distancia'] = categorias.apply(lambda row: distancia_haversine(latitud_local, longitud_local, row['latitude'], row['longitude']), axis=1)

    # Filtrar las filas que tienen la misma ciudad y estado que el local
    #categorias = categorias[(categorias['city'] == ciudad_local) & (categorias['state'] == estado_local)]

    # Ordenamos categorias por 'bussines_stars' de mayor a menor
    categorias_ordenado = categorias.sort_values(by='bussines_stars', ascending=False)

    categorias_ordenado = categorias_ordenado[['name', 'bussines_stars','categories', 'distancia', 'city', 'state']]
    return {f'El top de hoteles para tu ubicación es':categorias_ordenado.to_dict(orient='records')}
