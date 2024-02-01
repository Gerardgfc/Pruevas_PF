from fastapi import FastAPI,Query
from fastapi.responses import HTMLResponse
import api_func as fa

import importlib
importlib.reload(fa)

#Se inicializa la APP
app = FastAPI(debug=True)

#Funciones
@app.get(path="/",
         response_class=HTMLResponse,
         tags=["Inicio"])

def home():
    '''
    Página de inicio que muestra una presentación.

    Returns:
    HTMLResponse: Respuesta HTML que muestra la presentación.
    '''
    return fa.presentacion()

@app.get(path="/top_hoteles_por_ubicacion",
         description= """ <front color='blue'>
                        INSTRUCCIONES<br>
                        1. Haga click en "Try it out".<br>
                        2. Ingrese el género en el box abajo.<br>
                        3. Scrollear a "Responses" para ver el año con más horas jugadas para un género específico teniendo en cuenta los géneros disponibles.
                        </font>
                    """,
         tags=["Consultas Frecuentes"])

def top_hoteles_por_ubicacion(estado: str = Query(None, description="Ingresar estado y ciudad para obtener el top 5 de mejores hoteles según su calificación", example="CA"), 
                                    ciudad: str = Query(None, example="Nashville")):
    return fa.top_hoteles_por_ubicacion(estado, ciudad)


@app.get(path="/locales_cercanos_uvi",
         description= """ <front color='blue'>
                        INSTRUCCIONES<br>
                        1. Haga click en "Try it out".<br>
                        2. Ingrese el género en el box abajo.<br>
                        3. Scrollear a "Responses" para ver el año con más horas jugadas para un género específico teniendo en cuenta los géneros disponibles.
                        </font>
                    """,
         tags=["Consultas Frecuentes"])

def ordenar_por_cercania(local: str = Query(None, description="Ingresar un hotel y para ver los locales mas cercanos", example="Ghost City Tours Nashville")):
    return fa.ordenar_por_cercania(local)
    

@app.get(path="/locales_cercanos_rev",
         description= """ <front color='blue'>
                        INSTRUCCIONES<br>
                        1. Haga click en "Try it out".<br>
                        2. Ingrese el género en el box abajo.<br>
                        3. Scrollear a "Responses" para ver el año con más horas jugadas para un género específico teniendo en cuenta los géneros disponibles.
                        </font>
                    """,
         tags=["Consultas Frecuentes"])

def ordenar_por_bussines_stars(local: str = Query(None, description="Ingresar un hotel y para ver los locales mas cercanos", example="Ghost City Tours Nashville")):
    return fa.ordenar_por_bussines_stars(local)
