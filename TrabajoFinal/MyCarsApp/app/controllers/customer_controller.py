from flask import Blueprint, render_template, redirect, url_for, flash, request
from models.customer_manager import CustomerManager

customer_manager = CustomerManager()
customer_bp = Blueprint('customer_bp', __name__, url_prefix='/customers')

@customer_bp.route('/customers', methods=['GET'], endpoint='customers')
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


    
@customer_bp.route('/update_customer/<int:customer_id>', methods=['GET', 'POST'])
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
        return redirect(url_for('customer_bp.customers'))
    else:
        customer = next((customer for customer in customer_manager.data['customers'] if customer['id_cliente'] == customer_id), None)
        if customer is None:
            return "Cliente no encontrado", 404
        return render_template('customer/update_customer.html', customer=customer)

@customer_bp.route('/store_customer', methods=['GET', 'POST'])
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
        return redirect(url_for('customer_bp.customers'))
    return render_template('customer/store_customer.html')

@customer_bp.route('/delete_customer/<int:customer_id>', methods=['GET', 'POST'])
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
        return redirect(url_for('customer_bp.customers'))
    else:
        customer = next((customer for customer in customer_manager.data['customers'] if customer['id_cliente'] == customer_id), None)
        if customer is None:
            flash('Cliente no encontrado.', 'danger')
            return redirect(url_for('customer_bp.customers'))
        return render_template('customer/delete_customer.html', customer=customer)

