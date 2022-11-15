import constantes
import time

dT = 1

def torque_motor_fn(i):
    return constantes.Km*constantes.Ia

def tensao_fn(i):
    return constantes.V

def velocidade_fn(i):
    termo_1 = constantes.La*( torque_motor_fn(i+1) - torque_motor_fn(i) )/dT
    termo_2 = constantes.Km*tensao_fn(i)
    termo_3 = constantes.Km*constantes.Kb
    termo_4 = constantes.Ra*torque_motor_fn(i)
    velocidade = (termo_2 - termo_1 - termo_4)/termo_3

    if constantes.DIMINUI_VELOCIDADE:
        velocidade /= 2

    return velocidade

def liga_desliga(id, liga):
    if liga:
        print(f'LIGA ID: {id} \n MOTORES ATIVOS: {constantes.MOTORES_ATIVOS}\n\n')
        id_posterior = id+1
        id_anterior = id-1
        constantes.mutex.acquire()
        pode_ativar = id_anterior not in constantes.MOTORES_ATIVOS and id_posterior not in constantes.MOTORES_ATIVOS
        if pode_ativar and id not in constantes.MOTORES_ATIVOS:
            print(f'motor {id} ligado')
            constantes.MOTORES_ATIVOS.append(id)
        elif not pode_ativar:
            print(f'motor {id} nao pode ser ativo')
        constantes.mutex.release()
        return pode_ativar
    else:
        constantes.mutex.acquire()
        print(f'DESLIGA ID: {id} \n MOTORES ATIVOS: {constantes.MOTORES_ATIVOS}\n\n')
        if(id in constantes.MOTORES_ATIVOS):
            constantes.MOTORES_ATIVOS.remove(id)
            print(f'motor {id} desligado')
        constantes.mutex.release()
        return False

def logica(id):
    """
    Função responsável pela lógica executada pelo motor.
    """
    # while True:
    for i in range(3):
        constantes.semaforo.acquire()
        print(f'Tenta ligar motor {id}')
        periodo = time.time() + constantes.PERIODO_MOTOR
        while liga_desliga(id, True):
            if(time.time() > periodo):
                periodo = time.time() + constantes.PERIODO_MOTOR
                print(f'velocidade motor {id}: {velocidade_fn(i)}\n')
            time.sleep(1)
        liga_desliga(id,False)
        constantes.semaforo.release()