import socket
import sys
import threading

mutex_ref = threading.Semaphore(value=1)
f = open("historiador.txt", "w")

def server():
  global connectionOnServer
  global h_ref
  PORT=8000
  SERVER = socket.gethostbyname(socket.gethostname())
  ADDR = (SERVER, PORT)

  server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  server.bind(ADDR)
  server.listen()

  while True:
    conn, addr = server.accept()
    response = conn.recv(1024)
    if(conn):
      connectionOnServer = conn
    while (response and connectionOnServer != None) :
      if(response.decode('ascii') == 'q'):
        print('SISTEMA DESATIVADO')
        sys.exit()
      else:
        mutex_ref.acquire()
        h_ref = float(response.decode('ascii'))
        mutex_ref.release()
      response = conn.recv(1024)

def thread_read_ref(s):
  pass

def synoptic_process():
  HOST = socket.gethostbyname(socket.gethostname())
  PORT = 8000
  with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    f.write("h(t), Qin(t), Qout(t)")
    f.write('\n')
    s.connect((HOST, PORT))
    th_read = threading.Thread(target=thread_read_ref, args=(s,))
    th_read.start()
    while(True):
      data = s.recv(1024)
      if(f.closed):
        break
      if(data):
        f.write(data.decode('ascii'))
        f.write('\n')
