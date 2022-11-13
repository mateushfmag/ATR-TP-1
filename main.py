import random
import threading
import time

# Variáveis Globais
# MAX_THREADS = 12
# NUM_MOTORES = 30
MAX_THREADS = 3
NUM_MOTORES = 5
MOTORES_ATIVOS = []
semaforo = threading.Semaphore(value=MAX_THREADS)
mutex = threading.Semaphore(value=1)



def liga_desliga_motor(id, liga):
    if liga:
        print(f'LIGA ID: {id} \n MOTORES ATIVOS: {MOTORES_ATIVOS}\n\n')
        id_posterior = id+1
        id_anterior = id-1
        mutex.acquire()
        pode_ativar = id_anterior not in MOTORES_ATIVOS and id_posterior not in MOTORES_ATIVOS
        if pode_ativar:
            print(f'motor {id} ligado')
            MOTORES_ATIVOS.append(id)
        else:
            print(f'motor {id} nao pode ser ativo')
        mutex.release()
        return pode_ativar
    else:
        mutex.acquire()
        print(f'DESLIGA ID: {id} \n MOTORES ATIVOS: {MOTORES_ATIVOS}\n\n')
        if(id in MOTORES_ATIVOS):
            MOTORES_ATIVOS.remove(id)
            print(f'motor {id} desligado')
        mutex.release()
        return False

def logica_motor(id):
    """
    Função responsável pela lógica executada pelo motor.
    """
    # while True:
    for i in range(3):
        semaforo.acquire()
        print(f'Tenta ligar motor {id}')
        while liga_desliga_motor(id, True):
            for i in range(100):
                print(f'motor {id}: {i}\n')
            break
        liga_desliga_motor(id,False)
        semaforo.release()

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
