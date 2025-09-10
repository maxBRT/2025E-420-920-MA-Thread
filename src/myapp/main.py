import tkinter as tk
import concurrent.futures
from myapp.app import MyApp


def main() -> None:
    # Créer la fenêtre principale
    root = tk.Tk()

    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as exec:
        # Créer l'application
        app = MyApp(root, exec)

        # Lancer la boucle principale
        app.start()

