# EVALUACIÓN UNIDAD III PROGRAMACIÓN WEB
# NERY  ESPINOZA  P.

from flask import Flask, render_template, request

app = Flask(__name__)

# Definición de página de inicio
@app.route('/')
def index():
    return render_template('index.html')

# Desarrollo Ejercicio 1
@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    msg = None
    estado = None
    promedio = 0
    mostrarResultado = False
    if request.method == 'POST':
        try:
            # Notas las guarde en listas
            notas = [
                float(request.form['nota1']),
                float(request.form['nota2']),
                float(request.form['nota3'])
            ]
            asistencia = float(request.form['asistencia'])

            if all(10 <= nota <= 70 for nota in notas):
                promedio = round(sum(notas) / len(notas), 2)
                if promedio >= 40 and asistencia >= 75:
                    estado = "APROBADO"
                else:
                    estado = "REPROBADO"
                mostrarResultado = True
            else:
                msg = "Las notas deben estar en el rango de 10 a 70."
        except ValueError as e:
            msg = f"Sólo puedes ingresar valores numéricos para las notas y la asistencia. Error: {e}"
    return render_template('ejercicio1.html', estado=estado, promedio=promedio, mostrarResultado=mostrarResultado, msg=msg)

# Desarrollo Ejercicio 2
@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    nombreLargo = None
    longitudLargo = None
    if request.method == 'POST':
        nombres = [
            request.form['nombre1'],
            request.form['nombre2'],
            request.form['nombre3']
        ]
        nombreLargo = max(nombres, key=len)
        longitudLargo = len(nombreLargo)
    return render_template('ejercicio2.html', nombre=nombreLargo, longitud=longitudLargo)

if __name__ == '__main__':
    app.run(debug=True, port=5001)