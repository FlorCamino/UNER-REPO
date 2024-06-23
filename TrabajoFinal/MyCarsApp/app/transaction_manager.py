import json
import os

class TransactionManager:
    def __init__(self, filename='transacciones.json'):
        self.filename = filename
        self.load_data()

    def load_data(self):
        if os.path.exists(self.filename):
            try:
                with open(self.filename, 'r', encoding='utf-8') as file:
                    self.data = json.load(file)
            except (IOError, json.JSONDecodeError):
                self.data = {"transactions": [], "last_id": 0}
        else:
            self.data = {"transactions": [], "last_id": 0}

    def save_data(self):
        try:
            with open(self.filename, 'w', encoding='utf-8') as file:
                json.dump(self.data, file, indent=4)
        except IOError as e:
            print(f"Error saving data: {e}")

    def get_next_id(self):
        self.data['last_id'] += 1
        return self.data['last_id']

    def store_transaction(self, params):
        # Verifica si la transacción ya existe
        existing_transaction = next((t for t in self.data['transactions'] if t.get('id_transaccion') == params.get('id_transaccion')), None)
        if existing_transaction:
            print(f"Transaction with ID {params.get('id_transaccion')} already exists.")
            return None
        
        transaction_id = self.get_next_id()
        params["id_transaccion"] = transaction_id
        self.data['transactions'].append(params)
        self.save_data()
        return transaction_id

    def update_transaction(self, transaction_id, updated_params):
        for transaction in self.data['transactions']:
            if transaction.get('id_transaccion') == transaction_id:
                transaction.update(updated_params)
                self.save_data()
                return True
        return False

    def delete_transaction(self, transaction_id):
        for i, transaction in enumerate(self.data['transactions']):
            if transaction.get('id_transaccion') == transaction_id:
                del self.data['transactions'][i]
                self.save_data()
                return True
        return False

    def find_transaction_by_id(self, transaction_id):
        for transaction in self.data['transactions']:
            if transaction.get('id_transaccion') == transaction_id:
                return transaction
        return None
