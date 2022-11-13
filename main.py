import random
import threading
import time

# Variáveis Globais
MAX_THREADS = 3
NUM_MOTORES = 5
MOTORES_ATIVOS = []
semaforo = threading.Semaphore(value=MAX_THREADS)
mutex = threading.Semaphore(value=MAX_THREADS)


def pode_ativar_motor(id):
    id_posterior = id+1
    id_anterior = id-1


    mutex.acquire()
    pode_ativar = id_anterior not in MOTORES_ATIVOS and id_posterior not in MOTORES_ATIVOS
    if pode_ativar:
        MOTORES_ATIVOS.append(id)
    mutex.release()


def logica_motor(id):
    """
    Função responsável pela lógica executada pelo motor.
    """
    while True:
        semaforo.acquire()
        print(f'motor {id} ativo')
        while pode_ativar_motor(id):
            for i in range(100):
                print(f'motor {id}: {i}\n')
            break

        mutex.acquire()
        MOTORES_ATIVOS.remove(id)
        mutex.acquire()

        semaforo.release()
        print(f'motor {id} liberado')

def logica_controle():
    for i in range(1):
        print('OLA EU SOU O CONTROLADOR')


if __name__ == '__main__':

    # Disparando as Threads
    for id in range(NUM_MOTORES):
        motor_thread = threading.Thread(target=logica_motor, args=[id])
        motor_thread.start()
    controle_thread = threading.Thread(target=logica_controle)
    controle_thread.start()


