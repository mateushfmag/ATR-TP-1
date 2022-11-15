from random import random

import constantes
import time


class Motor:
    def __init__(self, id):
        self.id = id

    velocidade = 0
    vel_desejada = 0
    dT = 1


    def define_velocidade_desejada(self):
        self.vel_desejada = int(input(f"Escolha a velocidade pro motor {self.id}: "))


    def torque_motor_fn(self, i):
        return constantes.Km*constantes.Ia

    def tensao_fn(self, i):
        return constantes.V

    def velocidade_fn(self):
        if self.velocidade > self.vel_desejada:
            self.velocidade -= random()
        elif self.velocidade < self.vel_desejada:
            self.velocidade += random()
    def liga_desliga(self, id, liga):
        if liga:
            constantes.mutex.acquire()
            print(f'LIGA ID: {id} \n MOTORES ATIVOS: {constantes.MOTORES_ATIVOS}\n\n')
            id_posterior = id+1
            id_anterior = id-1
            pode_ativar = id_anterior not in constantes.MOTORES_ATIVOS and id_posterior not in constantes.MOTORES_ATIVOS
            if pode_ativar and id not in constantes.MOTORES_ATIVOS:
                print(f'motor {id} ligado')
                self.define_velocidade_desejada()
                constantes.MOTORES_ATIVOS.append(id)
            elif not pode_ativar:
                print(f'motor {id} nao pode ser ativo')
            constantes.mutex.release()
            return pode_ativar
        elif id in constantes.MOTORES_ATIVOS:
            constantes.mutex.acquire()
            print(f'DESLIGA ID: {id} \n MOTORES ATIVOS: {constantes.MOTORES_ATIVOS}\n\n')
            if(id in constantes.MOTORES_ATIVOS):
                constantes.MOTORES_ATIVOS.remove(id)
                print(f'motor {id} desligado')
            constantes.mutex.release()
        return False

    def logica(self, id):
        """
        Função responsável pela lógica executada pelo motor.
        """
        # while True:
        for i in range(3):
            constantes.semaforo.acquire()
            periodo = time.time() + constantes.PERIODO_MOTOR
            while self.liga_desliga(id, True):
                if(time.time() > periodo):
                    periodo = time.time() + constantes.PERIODO_MOTOR
                    self.velocidade_fn()
                    print(f'velocidade motor {id}: {self.velocidade}\n')
                time.sleep(1)
            self.liga_desliga(id,False)
            constantes.semaforo.release()
