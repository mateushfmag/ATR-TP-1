import constantes

def liga_desliga(id, liga):
    if liga:
        print(f'LIGA ID: {id} \n MOTORES ATIVOS: {constantes.MOTORES_ATIVOS}\n\n')
        id_posterior = id+1
        id_anterior = id-1
        constantes.mutex.acquire()
        pode_ativar = id_anterior not in constantes.MOTORES_ATIVOS and id_posterior not in constantes.MOTORES_ATIVOS
        if pode_ativar:
            print(f'motor {id} ligado')
            constantes.MOTORES_ATIVOS.append(id)
        else:
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
        while liga_desliga(id, True):
            for i in range(100):
                print(f'motor {id}: {i}\n')
            break
        liga_desliga(id,False)
        constantes.semaforo.release()