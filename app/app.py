from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/calificaciones', methods=['GET', 'POST'])
def calificaciones():
    resultado = None
    if request.method == 'POST':
        nota1 = float(request.form['nota1'])
        nota2 = float(request.form['nota2'])
        nota3 = float(request.form['nota3'])
        asistencia = float(request.form['asistencia'])

        # Calcular el promedio de las notas
        promedio = (nota1 + nota2 + nota3) / 3
        # Determinar si el estudiante está aprobado o reprobado
        estado = "Aprobado" if promedio >= 40 and asistencia >= 75 else "Reprobado"

        resultado = f'El promedio de las notas es: {promedio:.2f}. Estado: {estado}'
    return render_template('calificaciones.html', resultado=resultado)

@app.route('/formulario', methods=['GET', 'POST'])
def formulario():
    resultado = None
    if request.method == 'POST':
        nombre1 = request.form['nombre1']
        nombre2 = request.form['nombre2']
        nombre3 = request.form['nombre3']
        nombres = [nombre1, nombre2, nombre3]

        # Encontrar el nombre con más caracteres
        nombre_mas_largo = max(nombres, key=len)
        # Obtener la cantidad de caracteres del nombre más largo
        caracteres_mas_largo = len(nombre_mas_largo)

        resultado = f'El nombre con más caracteres es: {nombre_mas_largo}, con {caracteres_mas_largo} caracteres.'
    return render_template('formulario.html', resultado=resultado)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
