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

V   = 5
Ra  = 500
La  = 10
Ia  = 0.023
Km  = 5000
Tl  = 10
Jm  = 15
B   = 53
Om  = 81
Kb  = 50

# Variáveis compartilhadas
global MAX_THREADS
global NUM_MOTORES
global MOTORES_ATIVOS
global TEMPO_FUNCIONAMENTO
global semaforo
global mutex
global mutex_velocidade
global DIMINUI_VELOCIDADE

# MAX_THREADS = 12
# NUM_MOTORES = 30
# TEMPO_FUNCIONAMENTO = 60 # segundos
PERIODO_MOTOR = 1
PERIODO_CONTROLADOR = 0.2
MAX_THREADS = 12
NUM_MOTORES = 30
TEMPO_FUNCIONAMENTO = 5 # segundos
MOTORES_ATIVOS = []
semaforo = threading.Semaphore(value=MAX_THREADS)
mutex = threading.Semaphore(value=1)
mutex_velocidade = threading.Semaphore(value=1)
