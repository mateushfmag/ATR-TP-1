import threading
import motor
import constantes
import controlador
import logger
import server
from multiprocessing import Process


if __name__ == '__main__':
    # Disparando as Threads
    try:
        f = open("logger.txt", "w")
        f.close()

        motores = []
        for id in range(constantes.NUM_MOTORES):
            motores.append(motor.Motor(id))
            motor_thread = threading.Thread(target=motores[id].logica, args=[])
            motor_thread.start()

        controle_thread = threading.Thread(target=controlador.logica, args=[motores])
        controle_thread.start()

        logger_thread = threading.Thread(target=logger.logica, args=[motores])
        logger_thread.start()

        proc_scada = Process(target=server.synoptic_process)
        proc_scada.start()
        server.server()

    finally:
        logger_thread.join()
        controle_thread.join()
