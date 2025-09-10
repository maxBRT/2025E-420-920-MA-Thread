import tkinter as tk

from myapp.app import MyApp

def main() -> None:
    # Créer la fenêtre principale
    root = tk.Tk()
    
    # Créer l'application
    app = MyApp(root)
    
    # Lancer la boucle principale
    app.start()