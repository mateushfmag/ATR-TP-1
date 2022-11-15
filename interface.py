import constantes


def logica(motores):
    while True:
        constantes.mutex.acquire()
        for motor in motores:
            if(motor.velocidade == 0 and motor.ativo == True):
                motor.velocidade = motor.define_velocidade_desejada()
        constantes.mutex.release()