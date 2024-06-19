from database import load_data, save_data

class UniversityManagement:
    def __init__(self):
        self.data = load_data()

    def add_person(self, role, name=None):
        if name is None:
            name = input(f"Entrez le nom du {role}: ")
        self.data[role].append(name)
        save_data(self.data)
        print(f"{role.capitalize()} ajouté avec succès!")

    def display_all(self):
        for role, persons in self.data.items():
            print(f"\n{role.capitalize()}:")
            for person in persons:
                print(person)
