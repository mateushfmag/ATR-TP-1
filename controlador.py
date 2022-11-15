from time import time, sleep
import constantes


def logica(motores):
    periodo = time() + constantes.PERIODO_CONTROLADOR
    while True:
        if (time() > periodo):
            periodo = time() + constantes.PERIODO_CONTROLADOR
            for motor in motores:
                motor.vel_desejada /= 2
            sleep(60)
            for motor in motores:
                if motor.id in constantes.MOTORES_ATIVOS:
                    motor.liga_desliga(False)

