from flask import Blueprint, render_template, redirect, url_for, flash, request
from datetime import datetime
from models.transaction_manager import TransactionManager
from models.customer_manager import CustomerManager
from models.car_manager import CarManager

car_manager = CarManager()
customer_manager = CustomerManager()
transaction_manager = TransactionManager()
print_bp = Blueprint('print_bp', __name__, url_prefix='/transactions')

@print_bp.route('/print_transaction/<int:transaction_id>', methods=['GET'])
def print_transaction(transaction_id):
    transaction = transaction_manager.find_transaction_by_id(transaction_id)
    if not transaction:
        flash('Transacción no encontrada.', 'error')
        return redirect(url_for('transaction_bp.transactions'))
    
    vehicle = next((car for car in car_manager.data['cars'] if car['id_vehiculo'] == transaction['id_vehiculo']), None)
    customer = next((cust for cust in customer_manager.data['customers'] if cust['id_cliente'] == transaction['id_cliente']), None)
    transaction['vehiculo'] = vehicle if vehicle else {"marca": "Desconocido", "modelo": ""}
    transaction['cliente'] = customer if customer else {"nombre": "Desconocido", "apellido": ""}
    transaction['fecha_formateada'] = datetime.strptime(transaction['fecha'], '%Y-%m-%d').strftime('%d-%m-%Y')

    return render_template('transaction/ticket_transaction.html', transaction=transaction)

@print_bp.route('/print_all_transactions', methods=['GET'])
def print_all_transactions():
    fecha_min = request.args.get('fecha_min')
    fecha_max = request.args.get('fecha_max')
    monto_min = request.args.get('monto_min', type=float)
    monto_max = request.args.get('monto_max', type=float)
    cliente_nombre = request.args.get('cliente_nombre', '').strip().lower()
    vehiculo_marca_modelo = request.args.get('vehiculo_marca_modelo', '').strip().lower()
    tipo_transaccion = request.args.get('tipo_transaccion', '')

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
    if tipo_transaccion:
        filtered_transactions = [t for t in filtered_transactions if t['tipo_transaccion'].lower() == tipo_transaccion.lower()]
    if cliente_nombre:
        filtered_transactions = [t for t in filtered_transactions if cliente_nombre in f"{t['cliente']['nombre'].lower()} {t['cliente']['apellido'].lower()}"]
    if vehiculo_marca_modelo:
        filtered_transactions = [t for t in filtered_transactions if vehiculo_marca_modelo in f"{t['vehiculo']['marca'].lower()} {t['vehiculo']['modelo'].lower()}"]

    cars = car_manager.data['cars']
    customers = customer_manager.data['customers']

    for transaction in filtered_transactions:
        vehicle = next((car for car in cars if car['id_vehiculo'] == transaction['id_vehiculo']), None)
        customer = next((cust for cust in customers if cust['id_cliente'] == transaction['id_cliente']), None)
        transaction['vehiculo'] = vehicle if vehicle else {"marca": "Desconocido", "modelo": "", "tipo": ""}
        transaction['cliente'] = customer if customer else {"nombre": "Desconocido", "apellido": "", "documento": "", "direccion": "", "telefono": "", "correo": ""}
        transaction['fecha_formateada'] = datetime.strptime(transaction['fecha'], '%Y-%m-%d').strftime('%d-%m-%Y')

    grouped_transactions = {}
    total_ventas = 0
    total_compras = 0

    for transaction in filtered_transactions:
        cliente_id = transaction['cliente']['id_cliente']
        if cliente_id not in grouped_transactions:
            grouped_transactions[cliente_id] = {
                'cliente': transaction['cliente'],
                'transacciones': []
            }
        grouped_transactions[cliente_id]['transacciones'].append(transaction)

        if transaction['tipo_transaccion'].lower() == 'venta':
            total_ventas += transaction['monto']
        elif transaction['tipo_transaccion'].lower() == 'compra':
            total_compras += transaction['monto']

    return render_template('transaction/print_transactions.html', grouped_transactions=grouped_transactions, total_ventas=total_ventas, total_compras=total_compras)
