import json
import os

class CarManager:
    def __init__(self, filename='vehiculos.json'):
        self.filename = filename
        self.load_data()

    def load_data(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                self.data = json.load(file)
        else:
            self.data = {"cars": [], "last_id": 0}

    def save_data(self):
        with open(self.filename, 'w') as file:
            json.dump(self.data, file, indent=4)

    def get_next_id(self):
        self.data['last_id'] += 1
        self.save_data()
        return self.data['last_id']

    def store_car(self, params):
        car_id = self.get_next_id()
        params["id_vehiculo"] = car_id
        self.data['cars'].append(params)
        self.save_data()
        return car_id

    def update_car(self, car_id, updated_params):
        for car in self.data['cars']:
            if car['id_vehiculo'] == car_id:
                car.update(updated_params)
                self.save_data()
                return True
        return False

    def delete_car(self, car_id):
        for i, car in enumerate(self.data['cars']):
            if car['id_vehiculo'] == car_id:
                del self.data['cars'][i]
                self.save_data()
                return True
        return False
