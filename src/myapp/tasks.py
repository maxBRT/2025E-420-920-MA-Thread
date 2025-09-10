import random
import time
import threading


def sleep_long_task(duree):
    time.sleep(duree)


def long_task(task_id=None):
    # Simuler du travail en dormant pendant une durée aléatoire entre 3 et 7 secondes
    duree = random.randint(3, 7)
    t = threading.Thread(target=sleep_long_task, args=duree)
    t.start()
    if task_id is not None:
        return f"Task #{task_id} completed successfully"
    else:
        return "Task completed successfully"
