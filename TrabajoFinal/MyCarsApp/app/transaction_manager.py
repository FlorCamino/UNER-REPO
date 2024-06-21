import json
import os

class TransactionManager:
    def __init__(self, filename='transacciones.json'):
        self.filename = filename
        self.load_data()

    def load_data(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r', encoding='utf-8') as file:
                self.data = json.load(file)
        else:
            self.data = {"transactions": [], "last_id": 0}

    def save_data(self):
        with open(self.filename, 'w', encoding='utf-8') as file:
            json.dump(self.data, file, indent=4)

    def get_next_id(self):
        self.data['last_id'] += 1
        self.save_data()
        return self.data['last_id']

    def store_transaction(self, params):
        transaction_id = self.get_next_id()
        params["id_transaction"] = transaction_id
        self.data['transactions'].append(params)
        self.save_data()
        return transaction_id

    def update_transaction(self, transaction_id, updated_params):
        for transaction in self.data['transactions']:
            if transaction['id_transaccion'] == transaction_id:
                transaction.update(updated_params)
                self.save_data()
                return True
        return False

    def delete_transaction(self, transaction_id):
        for i, transaction in enumerate(self.data['transactions']):
            if transaction['id_transaccion'] == transaction_id:
                del self.data['transactions'][i]
                self.save_data()
                return True
        return False
