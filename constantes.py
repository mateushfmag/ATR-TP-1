import threading

# Parametros do problema
global V  # Tensao de armadura (entrada)
global Ra # Resistencia do circuito de armadura
global La # Indutancia de armadura
global Ia # Corrente de armadura
global Km # Constante de torque Tmotor
global Tl # Torque de carga (perturbacao)
global Jm # Momento de inercia do motor
global B  # Atrito viscoso do motor
global Om # Velocidade de rotacao do motor (saida)
global Kb # Constante eletrica

V   = 1
Ra  = 1
La  = 1
Ia  = 1
Km  = 1
Tl  = 1
Jm  = 1
B   = 1
Om  = 1
Kb  = 1

# Variáveis compartilhadas
global MAX_THREADS
global NUM_MOTORES
global MOTORES_ATIVOS
global semaforo
global mutex

# MAX_THREADS = 12
# NUM_MOTORES = 30
MAX_THREADS = 3
NUM_MOTORES = 5
MOTORES_ATIVOS = []
semaforo = threading.Semaphore(value=MAX_THREADS)
mutex = threading.Semaphore(value=1)