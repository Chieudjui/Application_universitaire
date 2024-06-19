import sys
from cli import cli_menu
from gui import start_gui

def main():
    print("Choisissez le mode d'interface:")
    print("1. Interface en ligne de commande")
    print("2. Interface graphique (GUI)")

    try:
        choice = int(input("Entrez votre choix (1 ou 2): "))
        if choice == 1:
            cli_menu()
        elif choice == 2:
            start_gui()
        else:
            print("Choix invalide. Veuillez entrer 1 ou 2.")
    except ValueError:
        print("Erreur: Veuillez entrer un nombre.")

if __name__ == "__main__":
    main()
