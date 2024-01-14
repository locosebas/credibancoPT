from flask import Flask
from datetime import datetime
import pytz

# Crear la aplicación Flask
app = Flask(__name__)

# Definir una ruta para la página principal
@app.route('/')
def initialPage():
    colombia_tz = pytz.timezone('America/Bogota')
    hora_colombia = datetime.now(colombia_tz)
    
    # Formato HTML mejorado con CSS
    html_response = """
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Bienvenido</title>
    </head>
    <body>
        <h1>Hola, bienvenido</h1>
        <p>Hoy es {}</p>
        <p>La hora en Colombia es: {}</p>
    </body>
    </html>
    """.format(hora_colombia.strftime('%A, %d %B %Y'), hora_colombia.strftime('%H:%M:%S'))
    
    return html_response

# Punto de entrada para la aplicación
if __name__ == '__main__':
    app.run(debug=True)
