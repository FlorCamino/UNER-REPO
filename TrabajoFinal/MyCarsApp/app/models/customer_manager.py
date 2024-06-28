import json
import os

class CustomerManager:
    def __init__(self, filename='clientes.json'):
        self.filename = filename
        self.load_data()

    def load_data(self):
        try:
            if os.path.exists(self.filename):
                with open(self.filename, 'r', encoding='utf-8') as file:
                    self.data = json.load(file)
            else:
                self.data = {"customers": [], "last_id": 0}
        except (FileNotFoundError, json.JSONDecodeError) as e:
            self.data = {"customers": [], "last_id": 0}
            raise Exception(f"Error loading data from {self.filename}: {e}")

    def save_data(self):
        try:
            with open(self.filename, 'w', encoding='utf-8') as file:
                json.dump(self.data, file, indent=4)
        except (IOError, OSError) as e:
            raise Exception(f"Error saving data to {self.filename}: {e}")

    def get_next_id(self):
        self.data['last_id'] += 1
        self.save_data()
        return self.data['last_id']

    def store_customer(self, params):
        try:
            customer_id = self.get_next_id()
            params["id_cliente"] = customer_id
            self.data['customers'].append(params)
            self.save_data()
            return customer_id
        except Exception as e:
            raise Exception(f"Error storing customer: {e}")

    def update_customer(self, customer_id, updated_params):
        try:
            for customer in self.data['customers']:
                if customer['id_cliente'] == customer_id:
                    customer.update(updated_params)
                    self.save_data()
                    return True
            return False
        except Exception as e:
            raise Exception(f"Error updating customer with ID {customer_id}: {e}")

    def delete_customer(self, customer_id):
        try:
            for i, customer in enumerate(self.data['customers']):
                if customer['id_cliente'] == customer_id:
                    del self.data['customers'][i]
                    self.save_data()
                    return True
            return False
        except Exception as e:
            raise Exception(f"Error deleting customer with ID {customer_id}: {e}")
