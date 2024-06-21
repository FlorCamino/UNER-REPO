import json
import os

class CustomerManager:
    def __init__(self, filename='clientes.json'):
        self.filename = filename
        self.load_data()

    def load_data(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r', encoding='utf-8') as file:
                self.data = json.load(file)
        else:
            self.data = {"customers": [], "last_id": 0}

    def save_data(self):
        with open(self.filename, 'w', encoding='utf-8') as file:
            json.dump(self.data, file, indent=4)

    def get_next_id(self):
        self.data['last_id'] += 1
        self.save_data()
        return self.data['last_id']

    def store_customer(self, params):
        customer_id = self.get_next_id()
        params["id_cliente"] = customer_id
        self.data['customers'].append(params)
        self.save_data()
        return customer_id

    def update_customer(self, customer_id, updated_params):
        for customer in self.data['customers']:
            if customer['id_cliente'] == customer_id:
                customer.update(updated_params)
                self.save_data()
                return True
        return False

    def delete_customer(self, customer_id):
        for i, customer in enumerate(self.data['customers']):
            if customer['id_cliente'] == customer_id:
                del self.data['customers'][i]
                self.save_data()
                return True
        return False
