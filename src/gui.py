import customtkinter as ctk
from university_management import UniversityManagement

um = UniversityManagement()

def add_person_window(role):
    window = ctk.CTkToplevel()
    window.title(f"Ajouter un {role[:-1]}")

    label_name = ctk.CTkLabel(window, text="Nom:")
    label_name.pack(pady=5)
    entry_name = ctk.CTkEntry(window)
    entry_name.pack(pady=5)

    def submit():
        name = entry_name.get()
        if name:
            um.add_person(role, name)
            window.destroy()
        else:
            ctk.CTkMessageBox.show_info("Erreur", "Le nom ne peut pas être vide")

    submit_button = ctk.CTkButton(window, text="Ajouter", command=submit)
    submit_button.pack(pady=20)

def start_gui():
    root = ctk.CTk()
    root.title("Gestion Universitaire")

    def open_add_person_window(role):
        add_person_window(role)

    button_add_staff = ctk.CTkButton(root, text="Ajouter Personnel", command=lambda: open_add_person_window("personnel"))
    button_add_staff.pack(pady=10)

    button_add_professor = ctk.CTkButton(root, text="Ajouter Professeur", command=lambda: open_add_person_window("professeurs"))
    button_add_professor.pack(pady=10)

    button_add_student = ctk.CTkButton(root, text="Ajouter Étudiant", command=lambda: open_add_person_window("étudiants"))
    button_add_student.pack(pady=10)

    button_display_all = ctk.CTkButton(root, text="Afficher Tout", command=um.display_all)
    button_display_all.pack(pady=10)

    root.mainloop()
