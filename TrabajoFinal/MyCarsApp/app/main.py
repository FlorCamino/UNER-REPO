import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))

sys.path.append(current_dir)

from flask import Flask
from controllers.main_controller import app as main_blueprint
from controllers.customer_controller import customer_bp as customer_blueprint
from controllers.car_controller import car_bp as car_blueprint
from controllers.print_controller import print_bp as print_blueprint
from controllers.transaction_controller import transaction_bp as transaction_blueprint

app = Flask(__name__)
app.secret_key = os.urandom(24)

app.register_blueprint(main_blueprint)
app.register_blueprint(customer_blueprint)
app.register_blueprint(car_blueprint)
app.register_blueprint(print_blueprint)
app.register_blueprint(transaction_blueprint)

if __name__ == '__main__':
    app.run(debug=True)