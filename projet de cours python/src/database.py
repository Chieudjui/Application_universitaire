import json

DATABASE_FILE = 'database.json'

def load_data():
    try:
        with open(DATABASE_FILE, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {"personnel": [], "professeurs": [], "étudiants": []}

def save_data(data):
    with open(DATABASE_FILE, 'w') as file:
        json.dump(data, file, indent=4)
