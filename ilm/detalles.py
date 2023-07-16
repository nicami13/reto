import time

def pantalla_carga():
    for _ in range(2):
        for _ in range(3):
            print("Volviendo al menu principal", end="")
            time.sleep(0.5)
            print("...", end="\r")
            time.sleep(0.5)
        print("Volviendo al menu principal   ", end="\r")
        