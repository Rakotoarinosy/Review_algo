import socket
import time

HOST_IP = "127.0.0.1"
HOST_PORT = 32000
MAX_DATA_SIZE = 1024

s = socket.socket()


print(f"Connexion au serveur {HOST_IP}, port {HOST_PORT}")
while True:
    try:
        s.connect((HOST_IP,HOST_PORT))
    except ConnectionRefusedError:
        print("ERREUR : impossible de se connecter au serveur. Reconnexion...")
        time.sleep(4)
    else:
        print("Connecté au Serveur")
        break

while True:        
    data_recu = s.recv(MAX_DATA_SIZE)
    if not data_recu:
        break
    print(data_recu.decode())
    texte_envoye = input("Vous: ")
    s.sendall(texte_envoye.encode())
        
    
s.close()