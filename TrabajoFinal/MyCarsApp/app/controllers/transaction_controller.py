from flask import Blueprint, render_template, redirect, url_for, flash, request
from datetime import datetime
from models.transaction_manager import TransactionManager
from models.customer_manager import CustomerManager
from models.car_manager import CarManager

car_manager = CarManager()
customer_manager = CustomerManager()
transaction_manager = TransactionManager()
transaction_bp = Blueprint('transaction_bp', __name__, url_prefix='/transactions')

@transaction_bp.route('/transactions', methods=['GET'])
def transactions():
    fecha_min = request.args.get('fecha_min')
    fecha_max = request.args.get('fecha_max')
    monto_min = request.args.get('monto_min', type=float)
    monto_max = request.args.get('monto_max', type=float)
    cliente_nombre = request.args.get('cliente_nombre', '').strip().lower()
    vehiculo_marca_modelo = request.args.get('vehiculo_marca_modelo', '').strip().lower()
    tipo_transaccion = request.args.get('tipo_transaccion')

    filtered_transactions = transaction_manager.data['transactions']
        
    if tipo_transaccion:
        filtered_transactions = [t for t in filtered_transactions if t['tipo_transaccion'].lower() == tipo_transaccion.lower()]

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

    total_monto = sum(t['monto'] for t in filtered_transactions)

    clientes = sorted({f"{cust['nombre']} {cust['apellido']}" for cust in customers}, key=lambda x: x.lower())
    vehiculos = sorted({f"{car['marca']} {car['modelo']}" for car in cars}, key=lambda x: x.lower())

    return render_template('transaction/index.html', transactions=filtered_transactions, total_monto=total_monto, clientes=clientes, vehiculos=vehiculos)


@transaction_bp.route('/store_transaction', methods=['GET', 'POST'])
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


@transaction_bp.route('/update_transaction/<int:transaction_id>', methods=['GET', 'POST'])
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

@transaction_bp.route('/delete_transaction/<int:transaction_id>', methods=['GET', 'POST'])
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