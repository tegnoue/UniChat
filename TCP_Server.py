import socket
import threading
from env import address_server

active_users = {}

def identify_user(message, sock_user, address_user):
    active_users.setdefault(address_user, message)

def establish_connection(client_address, conn):
    print(f"conexao estabelecida com o cliente {client_address}")
    while True:
        msg = socketClient.recv(1024)
        print(f"mensagem recebida: {msg}")
        identify_user(msg, client_address, conn)
        socketClient.sendall(str.encode("Mensagem recebida"))
        print(f"Eis os usuarios online:\n {active_users}")

socketTCP = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

socketTCP.bind(address_server)
socketTCP.listen()

while True:
    socketClient, address = socketTCP.accept()
    threadClient = threading.Thread(target=establish_connection, args=(socketClient, address))
    threadClient.start()