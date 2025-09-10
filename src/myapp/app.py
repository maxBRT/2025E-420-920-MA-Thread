import tkinter as tk
from tkinter import scrolledtext
import time
from myapp.tasks import long_task

class MyApp:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("Pratique Threading")
        self.root.geometry("600x300")
        
        # Compteur de tâches
        self.task_counter = 0
        
        # Variable pour le toggle switch
        self.toggle_var = tk.BooleanVar()
        
        # Créer l'interface
        self.setup_ui()
        
    def setup_ui(self):
        # Conteneur principal
        frame = tk.Frame(self.root)
        frame.pack(expand=True, fill='both', padx=20, pady=20)
        
        # Bouton de démarrage
        self.start_button = tk.Button(
            frame, 
            text="Lancer une tâche longue", 
            command=self.start_long_task
        )
        self.start_button.pack(pady=10)
        
        # Toggle switch pour démontrer le gel de l'interface
        self.toggle_check = tk.Checkbutton(
            frame,
            text="Essayez de me cliquer pendant l'exécution !",
            variable=self.toggle_var,
            command=self.on_toggle
        )
        self.toggle_check.pack(pady=10)
        
        # Zone de texte pour afficher les résultats
        result_label = tk.Label(frame, text="Résultats des tâches :")
        result_label.pack(anchor="w", pady=(10, 5))
        
        self.result_text = scrolledtext.ScrolledText(
            frame, 
            height=8, 
            width=50,
            state="disabled"
        )
        self.result_text.pack(expand=True, fill='both', pady=5)

    def start(self):
        """Démarre la boucle principale de l'application"""
        self.root.mainloop()

    def log_message(self, message):
        """Ajoute un message avec timestamp dans la zone de texte"""
        timestamp = time.strftime("%H:%M:%S")
        full_message = f"[{timestamp}] {message}\n"
        
        self.result_text.config(state="normal")
        self.result_text.insert(tk.END, full_message)
        self.result_text.see(tk.END)  # Scroll vers la fin
        self.result_text.config(state="disabled")
        
    def on_toggle(self):
        """Méthode appelée quand le toggle est activé/désactivé"""
        state = "ACTIVÉ" if self.toggle_var.get() else "DÉSACTIVÉ"
        self.log_message(f"Bouton bascule : {state}")
        
    def start_long_task(self):
        """Démarre une tâche longue qui bloque le GUI"""
        # Désactiver le bouton immédiatement
        self.start_button.config(state=tk.DISABLED)

        # Mettre à jour le compteur
        self.task_counter += 1
        task_id = self.task_counter
        
        # Logger le début de la tâche
        self.log_message(f"Début de la tâche #{task_id}")
        
        # Exécuter la tâche longue
        result = long_task(task_id=task_id)
        self.log_message(f"Résultat : {result}")
        
        # Réactiver le bouton
        self.start_button.config(state=tk.NORMAL)



