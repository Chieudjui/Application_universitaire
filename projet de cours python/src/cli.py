from university_management import UniversityManagement

def cli_menu():
    um = UniversityManagement()
    while True:
        print("\n--- Menu de Gestion Universitaire ---")
        print("1. Ajouter un personnel")
        print("2. Ajouter un professeur")
        print("3. Ajouter un étudiant")
        print("4. Afficher toutes les personnes")
        print("5. Quitter")
        try:
            choice = int(input("Entrez votre choix: "))
            if choice == 1:
                um.add_person("personnel")
            elif choice == 2:
                um.add_person("professeurs")
            elif choice == 3:
                um.add_person("étudiants")
            elif choice == 4:
                um.display_all()
            elif choice == 5:
                break
            else:
                print("Choix invalide. Veuillez réessayer.")
        except ValueError:
            print("Erreur: Veuillez entrer un nombre.")
