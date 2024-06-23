from flask import Flask, request, render_template, redirect, url_for, flash
from datetime import datetime
import os
from car_manager import CarManager
from customer_manager import CustomerManager
from transaction_manager import TransactionManager

app = Flask(__name__)
app.secret_key = os.urandom(24)

car_manager = CarManager()
customer_manager = CustomerManager()
transaction_manager = TransactionManager()

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/cars', methods=['GET'], endpoint='cars')
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


@app.route('/customers', methods=['GET'], endpoint='customers')
def customers():
    documento = request.args.get('documento', '').strip().lower()
    nombre = request.args.get('nombre', '').strip().lower()
    apellido = request.args.get('apellido', '').strip().lower()
    
    filtered_customers = customer_manager.data['customers']
    
    if documento:
        filtered_customers = [customer for customer in filtered_customers if documento in customer['documento'].lower()]
    if nombre:
        filtered_customers = [customer for customer in filtered_customers if nombre in customer['nombre'].lower()]
    if apellido:
        filtered_customers = [customer for customer in filtered_customers if apellido in customer['apellido'].lower()]
    return render_template('customer/index.html', customers=filtered_customers)

@app.route('/transactions', methods=['GET'], endpoint='transactions')
def transactions():
    fecha_min = request.args.get('fecha_min')
    fecha_max = request.args.get('fecha_max')
    monto_min = request.args.get('monto_min', type=float)
    monto_max = request.args.get('monto_max', type=float)
    cliente_nombre = request.args.get('cliente_nombre', '').strip().lower()
    vehiculo_marca_modelo = request.args.get('vehiculo_marca_modelo', '').strip().lower()

    filtered_transactions = transaction_manager.data['transactions']

    if fecha_min:
        try:
            fecha_min_dt = datetime.strptime(fecha_min, '%d-%m-%Y')
            filtered_transactions = [t for t in filtered_transactions if datetime.strptime(t['fecha'], '%Y-%m-%d') >= fecha_min_dt]
        except ValueError:
            pass
    if fecha_max:
        try:
            fecha_max_dt = datetime.strptime(fecha_max, '%d-%m-%Y')
            filtered_transactions = [t for t in filtered_transactions if datetime.strptime(t['fecha'], '%Y-%m-%d') <= fecha_max_dt]
        except ValueError:
            pass
    if monto_min is not None:
        filtered_transactions = [t for t in filtered_transactions if t['monto'] >= monto_min]
    if monto_max is not None:
        filtered_transactions = [t for t in filtered_transactions if t['monto'] <= monto_max]
            
    cars = car_manager.data['cars']
    customers = customer_manager.data['customers']

    for transaction in filtered_transactions:
        vehicle = next((car for car in cars if car['id_vehiculo'] == transaction['id_vehiculo']), None)
        customer = next((cust for cust in customers if cust['id_cliente'] == transaction['id_cliente']), None)
        transaction['vehiculo'] = vehicle if vehicle else {"marca": "Desconocido", "modelo": ""}
        transaction['cliente'] = customer if customer else {"nombre": "Desconocido", "apellido": ""}
        transaction['fecha_formateada'] = datetime.strptime(transaction['fecha'], '%Y-%m-%d').strftime('%d-%m-%Y')

    if cliente_nombre:
        filtered_transactions = [t for t in filtered_transactions if cliente_nombre in f"{t['cliente']['nombre'].lower()} {t['cliente']['apellido'].lower()}"]

    if vehiculo_marca_modelo:
        filtered_transactions = [t for t in filtered_transactions if vehiculo_marca_modelo in f"{t['vehiculo']['marca'].lower()} {t['vehiculo']['modelo'].lower()}"]

    return render_template('transaction/index.html', transactions=filtered_transactions)

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
        return redirect(url_for('cars'))
    return render_template('car/store_car.html')

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
        return redirect(url_for('cars'))
    else:
        car = next((car for car in car_manager.data['cars'] if car['id_vehiculo'] == car_id), None)
        if car is None:
            return "Vehículo no encontrado!", 404
        return render_template('car/update_car.html', car=car)

@app.route('/delete_car/<int:car_id>', methods=['GET', 'POST'])
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
        return redirect(url_for('cars'))
    else:
        car = next((car for car in car_manager.data['cars'] if car['id_vehiculo'] == car_id), None)
        if car is None:
            flash('Vehículo no encontrado.', 'danger')
            return redirect(url_for('cars'))
        return render_template('car/delete_car.html', car=car)

    
@app.route('/update_customer/<int:customer_id>', methods=['GET', 'POST'])
def update_customer(customer_id):
    if request.method == 'POST':
        updated_params = {
            "nombre": request.form['nombre'],
            "apellido": request.form['apellido'],
            "documento": request.form['documento'],
            "direccion": request.form['direccion'],
            "telefono": request.form['telefono'],
            "correo_electronico": request.form['correo_electronico']
        }
        update_success = customer_manager.update_customer(customer_id, updated_params)
        return redirect(url_for('customers'))
    else:
        customer = next((customer for customer in customer_manager.data['customers'] if customer['id_cliente'] == customer_id), None)
        if customer is None:
            return "Cliente no encontrado", 404
        return render_template('customer/update_customer.html', customer=customer)

@app.route('/store_customer', methods=['GET', 'POST'])
def store_customer():
    if request.method == 'POST':
        params = {
            "nombre": request.form['nombre'],
            "apellido": request.form['apellido'],
            "documento": request.form['documento'],
            "direccion": request.form['direccion'],
            "telefono": request.form['telefono'],
            "correo_electronico": request.form['correo_electronico']
        }
        try:
            customer_id = customer_manager.store_customer(params)
            flash('Cliente guardado exitosamente!', 'success')
        except Exception as e:
            flash(str(e), 'danger')
        return redirect(url_for('customers'))
    return render_template('customer/store_customer.html')

@app.route('/delete_customer/<int:customer_id>', methods=['GET', 'POST'])
def delete_customer(customer_id):
    if request.method == 'POST':
        try:
            delete_success = customer_manager.delete_customer(customer_id)
            if delete_success:
                flash('Cliente eliminado exitosamente.', 'success')
            else:
                flash('No se encontró el cliente a eliminar.', 'danger')
        except Exception as e:
            flash(f'Error al eliminar el cliente: {str(e)}', 'danger')
        return redirect(url_for('customers'))
    else:
        customer = next((customer for customer in customer_manager.data['customers'] if customer['id_cliente'] == customer_id), None)
        if customer is None:
            flash('Cliente no encontrado.', 'danger')
            return redirect(url_for('customers'))
        return render_template('customer/delete_customer.html', customer=customer)



@app.route('/store_transaction', methods=['GET', 'POST'])
def store_transaction():
    if request.method == 'POST':
        params = {
            "id_vehiculo": int(request.form['id_vehiculo']),
            "id_cliente": int(request.form['id_cliente']),
            "tipo_transaccion": request.form['tipo_transaccion'],
            "fecha": request.form['fecha'],
            "monto": float(request.form['monto']),
            "observaciones": request.form['observaciones']
        }
        try:
            transaction_id = transaction_manager.store_transaction(params)
            if transaction_id:
                if params['tipo_transaccion'].lower() == 'venta':
                    vehicle = next((car for car in car_manager.data['cars'] if car['id_vehiculo'] == params['id_vehiculo']), None)
                    if vehicle:
                        vehicle['estado'] = 'Reservado'
                        car_manager.save_data()
                flash('Transacción guardada exitosamente!', 'success')
            else:
                flash('La transacción ya existe!', 'danger')
        except Exception as e:
            flash(str(e), 'danger')
        return redirect(url_for('transactions'))
    
    available_cars = [car for car in car_manager.data['cars'] if car['estado'].lower() == 'disponible']
    clientes = customer_manager.data['customers']
    return render_template('transaction/store_transaction.html', vehiculos=available_cars, clientes=clientes)


@app.route('/update_transaction/<int:transaction_id>', methods=['GET', 'POST'])
def update_transaction(transaction_id):
    if request.method == 'POST':
        updated_params = {
            "id_vehiculo": int(request.form['id_vehiculo']),
            "id_cliente": int(request.form['id_cliente']),
            "tipo_transaccion": request.form['tipo_transaccion'],
            "fecha": request.form['fecha'],
            "monto": float(request.form['monto']),
            "observaciones": request.form['observaciones']
        }
        update_success = transaction_manager.update_transaction(transaction_id, updated_params)
        return redirect(url_for('transactions'))
    else:
        transaction = next((t for t in transaction_manager.data['transactions'] if t['id_transaccion'] == transaction_id), None)
        if transaction is None:
            return "Transacción no encontrada", 404
        vehiculos = car_manager.data['cars']
        clientes = customer_manager.data['customers']
        return render_template('transaction/update_transaction.html', transaction=transaction, vehiculos=vehiculos, clientes=clientes)

@app.route('/delete_transaction/<int:transaction_id>', methods=['GET', 'POST'])
def delete_transaction(transaction_id):
    if request.method == 'POST':
        transaction = transaction_manager.find_transaction_by_id(transaction_id)
        if transaction is None:
            return "Transacción no encontrada", 404
        delete_success = transaction_manager.delete_transaction(transaction_id)
        if delete_success:
            flash('Transaccción eliminada exitosamente!', 'success')
        else:
            flash('Error al eliminar la transacción', 'danger')
        return redirect(url_for('transactions'))
    else:
        transaction = transaction_manager.find_transaction_by_id(transaction_id)
        if transaction is None:
            return "Transacción no encontrada", 404
        return render_template('transaction/delete_transaction.html', transaction=transaction)

if __name__ == '__main__':
    app.run(debug=True)
