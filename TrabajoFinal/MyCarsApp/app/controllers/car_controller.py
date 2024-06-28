from flask import Blueprint, render_template, redirect, url_for, flash, request
from models.car_manager import CarManager

car_manager = CarManager()
car_bp = Blueprint('car_bp', __name__, url_prefix='/cars')

@car_bp.route('/cars', methods=['GET'], endpoint='cars')
def cars():
    patente = request.args.get('patente')
    marca = request.args.get('marca')
    modelo = request.args.get('modelo')
    precio_compra_min = request.args.get('precio_compra_min', type=int)
    precio_compra_max = request.args.get('precio_compra_max', type=int)
    precio_venta_min = request.args.get('precio_venta_min', type=int)
    precio_venta_max = request.args.get('precio_venta_max', type=int)

    filtered_cars = car_manager.data['cars']

    if patente:
        filtered_cars = [car for car in filtered_cars if patente.lower() in car['patente'].lower()]
    if marca:
        filtered_cars = [car for car in filtered_cars if marca.lower() in car['marca'].lower()]
    if modelo:
        filtered_cars = [car for car in filtered_cars if modelo.lower() in car['modelo'].lower()]
    if precio_compra_min is not None:
        filtered_cars = [car for car in filtered_cars if car['precio_compra'] >= precio_compra_min]
    if precio_compra_max is not None:
        filtered_cars = [car for car in filtered_cars if car['precio_compra'] <= precio_compra_max]
    if precio_venta_min is not None:
        filtered_cars = [car for car in filtered_cars if car['precio_venta'] >= precio_venta_min]
    if precio_venta_max is not None:
        filtered_cars = [car for car in filtered_cars if car['precio_venta'] <= precio_venta_max]
    return render_template('car/index.html', cars=filtered_cars)

@car_bp.route('/store_car', methods=['GET', 'POST'])
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
        return redirect(url_for('car_bp.cars'))
    return render_template('car/store_car.html')

@car_bp.route('/update_car/<int:car_id>', methods=['GET', 'POST'])
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
        return redirect(url_for('car_bp.cars'))
    else:
        car = next((car for car in car_manager.data['cars'] if car['id_vehiculo'] == car_id), None)
        if car is None:
            return "Vehículo no encontrado!", 404
        return render_template('car/update_car.html', car=car)

@car_bp.route('/delete_car/<int:car_id>', methods=['GET', 'POST'])
def delete_car(car_id):
    if request.method == 'POST':
        try:
            delete_success = car_manager.delete_car(car_id)
            if delete_success:
                flash('Vehículo eliminado exitosamente.', 'success')
            else:
                flash('No se encontró el vehículo a eliminar.', 'danger')
        except Exception as e:
            flash(f'Error al eliminar el vehículo: {str(e)}', 'danger')
        return redirect(url_for('car_bp.cars'))
    else:
        car = next((car for car in car_manager.data['cars'] if car['id_vehiculo'] == car_id), None)
        if car is None:
            flash('Vehículo no encontrado.', 'danger')
            return redirect(url_for('car_bp.cars'))
        return render_template('car/delete_car.html', car=car)
