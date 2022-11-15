import constantes
from datetime import datetime
import time

def logica(motores):
    periodo = time.time() + constantes.PERIODO_LOGGER
    while True:
        if (time.time() > periodo):
            periodo = time.time() + constantes.PERIODO_LOGGER
            f = open("logger.txt", "a")
            for motor in motores:
                f.write(f"[{datetime.now()}] velocidade motor {motor.id}: {motor.velocidade}\n")
            f.close()
