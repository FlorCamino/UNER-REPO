from flask import Flask, request, render_template, redirect, url_for
from car_manager import CarManager

app = Flask(__name__, template_folder='templates/car')
# Crear una instancia de CarManager
car_manager = CarManager()

@app.route('/')
def index():
    return render_template('index.html', cars=car_manager.data['cars'])

@app.route('/store_car', methods=['GET', 'POST'])
def store_car():
    if request.method == 'POST':
        params = {
            "patente": request.form['patente'],
            "marca": request.form['marca'],
            "modelo": request.form['modelo'],
            "tipo": request.form['tipo'],
            "anio": int(request.form['anio']),
            "kilometraje": int(request.form['kilometraje']),
            "precio_compra": int(request.form['precio_compra']),
            "precio_venta": int(request.form['precio_venta']),
            "estado": request.form['estado']
        }
        car_id = car_manager.store_car(params)
        return redirect(url_for('index'))
    return render_template('store_car.html')

@app.route('/update_car/<int:car_id>', methods=['GET', 'POST'])
def update_car(car_id):
    if request.method == 'POST':
        updated_params = {
            "patente": request.form['patente'],
            "marca": request.form['marca'],
            "modelo": request.form['modelo'],
            "tipo": request.form['tipo'],
            "anio": int(request.form['anio']),
            "kilometraje": int(request.form['kilometraje']),
            "precio_compra": int(request.form['precio_compra']),
            "precio_venta": int(request.form['precio_venta']),
            "estado": request.form['estado']
        }
        update_success = car_manager.update_car(car_id, updated_params)
        return redirect(url_for('index'))
    else:
        # Obtener los datos del coche para rellenar el formulario
        car = next((car for car in car_manager.data['cars'] if car['id_vehiculo'] == car_id), None)
        if car is None:
            return "Car not found", 404
        return render_template('update_car.html', car=car)

@app.route('/delete_car/<int:car_id>', methods=['GET', 'POST'])
def delete_car(car_id):
    if request.method == 'POST':
        delete_success = car_manager.delete_car(car_id)
        return redirect(url_for('index'))
    else:
        car = next((car for car in car_manager.data['cars'] if car['id_vehiculo'] == car_id), None)
        if car is None:
            return "Car not found", 404
        return render_template('delete_car.html', car=car)

if __name__ == '__main__':
    app.run(debug=True)
