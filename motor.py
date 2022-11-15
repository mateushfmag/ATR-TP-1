from random import random

import constantes
import time


class Motor:
    def __init__(self, id):
        self.id = id
        self.kill = False
        self.velocidade = 0
        self.vel_desejada = 0
        self.dT = 1


    def define_velocidade_desejada(self):
        self.vel_desejada = int(input(f"Escolha a velocidade pro motor {self.id}: "))


    def torque_motor_fn(self, i):
        return constantes.Km*constantes.Ia

    def tensao_fn(self, i):
        return constantes.V

    def velocidade_fn(self):
        if self.velocidade > self.vel_desejada:
            self.velocidade -= random()*10
        elif self.velocidade < self.vel_desejada:
            self.velocidade += random()*10
    def liga_desliga(self, liga):
        if liga:
            constantes.mutex.acquire()
            print(f'LIGA ID: {self.id} \n MOTORES ATIVOS: {constantes.MOTORES_ATIVOS}\n\n')
            id_posterior = self.id+1
            id_anterior = self.id-1
            pode_ativar = id_anterior not in constantes.MOTORES_ATIVOS and id_posterior not in constantes.MOTORES_ATIVOS
            if pode_ativar and self.id not in constantes.MOTORES_ATIVOS:
                print(f'motor {self.id} ligado')
                self.define_velocidade_desejada()
                constantes.MOTORES_ATIVOS.append(self.id)
            elif not pode_ativar:
                print(f'motor {self.id} nao pode ser ativo')
            constantes.mutex.release()
            return pode_ativar
        elif self.id in constantes.MOTORES_ATIVOS:
            constantes.mutex.acquire()
            print(f'DESLIGA ID: {self.id} \n MOTORES ATIVOS: {constantes.MOTORES_ATIVOS}\n\n')
            if(self.id in constantes.MOTORES_ATIVOS):
                constantes.MOTORES_ATIVOS.remove(self.id)
                print(f'motor {self.id} desligado')
            constantes.mutex.release()
        return False

    def logica(self):
        """
        Função responsável pela lógica executada pelo motor.
        """
        while self.kill == False:
            constantes.semaforo.acquire()
            periodo = time.time() + constantes.PERIODO_MOTOR
            while self.liga_desliga(True) and self.kill == False:
                if(time.time() > periodo):
                    periodo = time.time() + constantes.PERIODO_MOTOR
                    self.velocidade_fn()
                    print(f'velocidade motor {self.id}: {self.velocidade}\n')
                time.sleep(1)
            self.liga_desliga(False)
            constantes.semaforo.release()
