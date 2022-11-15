from time import time
import constantes


def logica(motores):
    periodo = time() + constantes.PERIODO_CONTROLADOR
    while True:
        if (time() > periodo):
            periodo = time() + constantes.PERIODO_CONTROLADOR
            for motor in motores:
                motor.velocidade /= 2
