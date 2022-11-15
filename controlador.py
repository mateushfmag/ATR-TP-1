from time import time
import constantes


def logica():
    periodo = time() + constantes.PERIODO_CONTROLADOR
    while True:
        constantes.DIMINUI_VELOCIDADE = False
        if (time() > periodo):
            periodo = time() + constantes.PERIODO_CONTROLADOR
            constantes.DIMINUI_VELOCIDADE = True
            