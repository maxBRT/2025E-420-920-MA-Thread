import random
import time


def long_task(task_id=None):
    # Simuler du travail en dormant pendant une durée aléatoire entre 3 et 7 secondes
    duree = random.randint(3, 7)
    time.sleep(duree)
    
    if task_id is not None:
        return f"Task #{task_id} completed successfully"
    else:
        return "Task completed successfully"
