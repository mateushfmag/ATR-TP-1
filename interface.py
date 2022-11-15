import constantes


def logica(motores):
    while True:
        constantes.mutex.acquire()
        for motor in motores:
            if(motor.ativo and motor.sem_velocidade_definida):
                motor.define_velocidade_desejada()
                motor.sem_velocidade_definida = False
        constantes.mutex.release()