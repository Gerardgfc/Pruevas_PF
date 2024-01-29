import pandas as pd



df = pd.read_csv('hoteleria_turismo.csv')

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
        <title>Explora la API de Steam</title>
        <style>
            body {
                font-family: 'Arial', sans-serif;
                background-image: url('https://i.blogs.es/400138/steam-boicot-reddit/1366_2000.png');
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
            <h1>Explora la API de Steam</h1>
        </header>
        
        <main>
            <h2>¡Explora la API de Steam para obtener información sobre videojuegos! Realiza diversas consultas directamente desde la plataforma.</h2>
            
            <h3><strong>Cómo empezar:</strong></h3>
            <ul>
                <li>Agrega <span style="background-color: lightgray;">/docs</span> al final de la URL actual para explorar e interactuar con la API.</li>
                <li>O simplemente hacé <a href="https://proyecto-integrador-1.onrender.com/docs" target="_blank">click acá</a> para acceder a la documentación.</li>
            </ul>

            <p>Si deseas conocer más sobre el proyecto, puedes visitar mi perfil en <a href="https://www.linkedin.com/in/gerard-carrizo-508b16133/" target="_blank">LinkedIn</a>.</p>

            <p>El desarrollo completo está disponible en <a href="https://github.com/Gerardgfc/Gerardgfc-Proyecto_Integrador_1" target="_blank">GitHub</a>.</p>
        </main>
        <br>
        <br>
        <br>
        <br>
        <footer>
            <p>&copy; 2023 Gerardo Carrizo</p>
        </footer>
    </body>
    </html>
    '''


def Zona (state,city:str):
    """ Eligiendo una ciudad devuelve los nombres, de los locales en ese lugar

    Args:
        city: _description_

    Returns:
        _description_
    """
    df['city'] = df['city'].astype(str)
    df['state'] = df['state'].astype(str)
    filtro = df[(df['city'] == city) & (df['state'] == state)]
    lugares = filtro[['name','category']]

    estado = filtro['state'].iloc[0]
    
    lugares_dict = lugares.to_dict(orient='records')

        
    return {"En la ciudad": city ,"del estado de": estado , "Tiene estos lugares": lugares_dict}   
