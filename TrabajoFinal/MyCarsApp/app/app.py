from flask import Flask, request, render_template, redirect, url_for
from car_manager import CarManager
from customer_manager import CustomerManager
from transaction_manager import TransactionManager

app = Flask(__name__)

car_manager = CarManager()
customer_manager = CustomerManager()
transaction_manager = TransactionManager()

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/logout')
def logout():
    return render_template('logout.html')

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
    tipo_transaccion = request.args.get('tipo_transaccion')
    fecha_min = request.args.get('fecha_min')
    fecha_max = request.args.get('fecha_max')
    monto_min = request.args.get('monto_min', type=float)
    monto_max = request.args.get('monto_max', type=float)

    filtered_transactions = transaction_manager.data['transactions']

    if tipo_transaccion:
        filtered_transactions = [t for t in filtered_transactions if tipo_transaccion.lower() in t['tipo_transaccion'].lower()]
    if fecha_min:
        filtered_transactions = [t for t in filtered_transactions if t['fecha'] >= fecha_min]
    if fecha_max:
        filtered_transactions = [t for t in filtered_transactions if t['fecha'] <= fecha_max]
    if monto_min is not None:
        filtered_transactions = [t for t in filtered_transactions if t['monto'] >= monto_min]
    if monto_max is not None:
        filtered_transactions = [t for t in filtered_transactions if t['monto'] <= monto_max]

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
            return "Car not found", 404
        return render_template('car/update_car.html', car=car)

@app.route('/delete_car/<int:car_id>', methods=['GET', 'POST'])
def delete_car(car_id):
    if request.method == 'POST':
        delete_success = car_manager.delete_car(car_id)
        return redirect(url_for('cars'))
    else:
        car = next((car for car in car_manager.data['cars'] if car['id_vehiculo'] == car_id), None)
        if car is None:
            return "Car not found", 404
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
        customer_id = customer_manager.store_customer(params)
        return redirect(url_for('customers'))
    return render_template('customer/store_customer.html')

@app.route('/delete_customer/<int:customer_id>', methods=['GET', 'POST'])
def delete_customer(customer_id):
    if request.method == 'POST':
        delete_success = customer_manager.delete_customer(customer_id)
        return redirect(url_for('customers'))
    else:
        customer = next((customer for customer in customer_manager.data['customers'] if customer['id_cliente'] == customer_id), None)
        if customer is None:
            return "Cliente no encontrado", 404
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
        transaction_id = transaction_manager.store_transaction(params)
        return redirect(url_for('transactions'))
    return render_template('transaction/store_transaction.html')

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
        return render_template('transaction/update_transaction.html', transaction=transaction)

@app.route('/delete_transaction/<int:transaction_id>', methods=['GET', 'POST'])
def delete_transaction(transaction_id):
    if request.method == 'POST':
        delete_success = transaction_manager.delete_transaction(transaction_id)
        return redirect(url_for('transactions'))
    else:
        transaction = next((t for t in transaction_manager.data['transactions'] if t['id_transaccion'] == transaction_id), None)
        if transaction is None:
            return "Transacción no encontrada", 404
        return render_template('transaction/delete_transaction.html', transaction=transaction)

if __name__ == '__main__':
    app.run(debug=True)
