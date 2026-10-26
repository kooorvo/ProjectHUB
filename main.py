import customtkinter as ctk
from ctk_date_picker import CTkDatePicker

tasksList = []

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("ProjectHUB")
        self.geometry("1300x700")
        ctk.set_appearance_mode("dark")

        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # -- Sidebar --
        self.sidebar_frame = ctk.CTkFrame(self, width=200, corner_radius=10)
        self.sidebar_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(2, weight=1)

        self.wnTitle = ctk.CTkLabel(self.sidebar_frame, text="ProjectHUB", font=ctk.CTkFont(size=24, weight="bold"))
        self.wnTitle.grid(row=0, column=0, padx=20, pady=(20, 10))
        self.toDoBtn = ctk.CTkButton(self.sidebar_frame, text="To do list", command=self.afficher_toDo, width=190, height=50, font=ctk.CTkFont(size=14, weight="bold"))
        self.toDoBtn.grid(row=1, column=0, padx=20, pady=10)

        # -- Main frame --

        self.main_frame = ctk.CTkFrame(self, corner_radius=10)
        self.main_frame.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")

        self.afficher_toDo()

    def nettoyer_main_frame(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()

    def afficher_toDo(self):
        self.nettoyer_main_frame()

        self.titre = ctk.CTkLabel(self.main_frame, text="To do list", font=ctk.CTkFont(size=28, weight="bold"))
        self.titre.pack(pady=20)

        self.add_toDo_Btn = ctk.CTkButton(self.main_frame, text="Ajouter une tâche", width=300, height=70, command= self.afficher_ajouter_toDo, font=ctk.CTkFont(size=14, weight="bold"))
        self.add_toDo_Btn.pack(pady=10)
        self.show_toDo_Btn = ctk.CTkButton(self.main_frame, text="Afficher les tâches", width=300, height=70, command= self.afficher_liste, font=ctk.CTkFont(size=14, weight="bold"))
        self.show_toDo_Btn.pack(pady=10)

    def afficher_ajouter_toDo(self):
        self.nettoyer_main_frame()

        self.titreAddTD = ctk.CTkLabel(self.main_frame, text="Ajouter une tâche", font=ctk.CTkFont(size=28, weight="bold"))
        self.titreAddTD.pack(pady=20)
        self.task_name = ctk.CTkEntry(self.main_frame, placeholder_text="Nom de la tâche :", width=300, height=70, font=ctk.CTkFont(size=14, weight="bold"))
        self.task_name.pack(pady=10)
        self.priority = ctk.CTkComboBox(self.main_frame, values=["Priorité haute", "Priorité moyenne", "Priorité basse"], width=300, height=70, font=ctk.CTkFont(size=14, weight="bold"))
        self.priority.pack(pady=10)
        self.status = ctk.CTkComboBox(self.main_frame, values=["Pas commencée", "En cours", "Finie"], width=300, height=70, font=ctk.CTkFont(size=14, weight="bold"))
        self.status.pack(pady=10)
        self.datePicker = CTkDatePicker(self.main_frame, width=300, height=70)
        self.datePicker.set_allow_manual_input(False)
        self.datePicker.set_date_format("%d-%m-%Y")
        self.datePicker.pack(pady=10)
        self.confirmBtn = ctk.CTkButton(self.main_frame, text="Ajouter", font=ctk.CTkFont(size=28, weight="bold"), width=300, height=70, command=self.add_toDo)
        self.confirmBtn.pack(pady=10)

    def afficher_liste(self):
        self.nettoyer_main_frame()

        self.titreShowTD = ctk.CTkLabel(self.main_frame, text="Tâches en cours", font=ctk.CTkFont(size=28, weight="bold"))
        self.titreShowTD.pack(pady=20)
        self.menu_déroulant = ctk.CTkScrollableFrame(self.main_frame, width=750, height=500, label_text="Liste des tâches")
        self.menu_déroulant.pack(pady=10)

        for task in tasksList:
            self.btnTD = ctk.CTkButton(self.menu_déroulant, text=f"{task["nom"]} (avant le {task["échéance"]})\n{task["priorité"]}, {task["statut"]}", width=700, height=70, font=ctk.CTkFont(size=18))
            self.btnTD.pack(pady=10)

    # -- Logique --

    def add_toDo(self):
        taskName = self.task_name.get()
        prio = self.priority.get()
        stat = self.status.get()
        date = self.datePicker.get_date()

        tasksList.append({"nom":taskName, "priorité": prio, "statut": stat, "échéance":date})

        print(tasksList)

app = App()
app.mainloop()