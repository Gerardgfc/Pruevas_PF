from fastapi import FastAPI,Query
from fastapi.responses import HTMLResponse
import funcion_api as fa

import importlib
importlib.reload(fa)

app = FastAPI(debug=True)

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


@app.get(path="/Zona",
         description= """ <front color='blue'>
                        INSTRUCCIONES<br>
                        1. Haga click en "Try it out".<br>
                        2. Ingrese el año en el box abajo.<br>
                        3. Scrollear a "Responses" para ver los juegos más recomendados para el año dado.
                        </font>
                    """,
            tags=["Consultas Frecuentes"])
def Zona(state: str = Query(...,
                            description="Estado a obtener los lugares",
                            example='PA'),
         city: str = Query(...,
                           description="Ciudad a obtener los lugares",
                           example='Newtown')):
    return fa.Zona(state, city) 