import threading
import motor
import constantes


def logica_controle():
    for i in range(1):
        print('OLA EU SOU O CONTROLADOR')


if __name__ == '__main__':
    # Disparando as Threads
    for id in range(constantes.NUM_MOTORES):
        motor_thread = threading.Thread(target=motor.logica, args=[id])
        motor_thread.start()
    controle_thread = threading.Thread(target=logica_controle)
    controle_thread.start()
