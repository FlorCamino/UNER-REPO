import json
import os

class CarManager:
    def __init__(self, filename='vehiculos.json'):
        self.filename = filename
        self.load_data()

    def load_data(self):
        try:
            if os.path.exists(self.filename):
                with open(self.filename, 'r', encoding='utf-8') as file:
                    self.data = json.load(file)
            else:
                self.data = {"cars": [], "last_id": 0}
        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f"Error loading data from {self.filename}: {e}")
            self.data = {"cars": [], "last_id": 0}

    def save_data(self):
        try:
            with open(self.filename, 'w', encoding='utf-8') as file:
                json.dump(self.data, file, indent=4)
        except (IOError, OSError) as e:
            print(f"Error saving data to {self.filename}: {e}")

    def get_next_id(self):
        self.data['last_id'] += 1
        self.save_data()
        return self.data['last_id']

    def store_car(self, params):
        try:
            car_id = self.get_next_id()
            params["id_vehiculo"] = car_id
            self.data['cars'].append(params)
            self.save_data()
            return car_id
        except Exception as e:
            print(f"Error storing car: {e}")
            return None

    def update_car(self, car_id, updated_params):
        try:
            for car in self.data['cars']:
                if car['id_vehiculo'] == car_id:
                    car.update(updated_params)
                    self.save_data()
                    return True
            return False
        except Exception as e:
            print(f"Error updating car with ID {car_id}: {e}")
            return False

    def delete_car(self, car_id):
        try:
            for i, car in enumerate(self.data['cars']):
                if car['id_vehiculo'] == car_id:
                    del self.data['cars'][i]
                    self.save_data()
                    return True
            return False
        except Exception as e:
            print(f"Error deleting car with ID {car_id}: {e}")
            return False
