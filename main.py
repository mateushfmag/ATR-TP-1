import threading
import motor
import constantes
import controlador


if __name__ == '__main__':
    # Disparando as Threads
    motores = []
    for id in range(constantes.NUM_MOTORES):
        motores.append(motor.Motor(id))
        motor_thread = threading.Thread(target=motores[id].logica, args=[id])
        motor_thread.start()

    controle_thread = threading.Thread(target=controlador.logica, args=[motores])
    controle_thread.start()

    logger_thread = threading.Thread(target=logger.logica, args=[motores])
    logger_thread.start()
