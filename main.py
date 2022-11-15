import threading
import motor
import constantes
import controlador
import logger
import server
from multiprocessing import Process
import atexit

threads = []

if __name__ == '__main__':
    # Disparando as Threads
    f = open("logger.txt", "w")
    f.close()
    motores = []
    for id in range(constantes.NUM_MOTORES):
        motores.append(motor.Motor(id))
        motor_thread = threading.Thread(target=motores[id].logica, args=[])
        motor_thread.daemon = True
        motor_thread.start()
        threads.append(motor_thread)

    controle_thread = threading.Thread(target=controlador.logica, args=[motores])
    controle_thread.daemon = True
    controle_thread.start()
    threads.append(controle_thread)

    logger_thread = threading.Thread(target=logger.logica, args=[motores])
    logger_thread.daemon = True
    logger_thread.start()
    threads.append(logger_thread)

    # proc_scada = Process(target=server.synoptic_process)
    # proc_scada.start()
    # server.server()


def exit_handler():
    for thread in threads:
        thread.join()

atexit.register(exit_handler)
