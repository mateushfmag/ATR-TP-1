import threading
import motor
import constantes
import controlador


if __name__ == '__main__':
    # Disparando as Threads
    for id in range(constantes.NUM_MOTORES):
        motor_thread = threading.Thread(target=motor.logica, args=[id])
        motor_thread.start()
    controle_thread = threading.Thread(target=controlador.logica)
    controle_thread.start()
