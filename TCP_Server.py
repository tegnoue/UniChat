import socket
import threading

def establish_connection(clientAddress, conn):
    print(f"conexao estabelecida com o cliente {clientAddress}")
    while True:
        msg = socketClient.recv(1024)
        print(f"mensagem recebida: {msg}")
        socketClient.sendall(str.encode("Mensagem recebida"))

socketTCP = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

socketTCP.bind(("127.0.0.1", 2026))
socketTCP.listen()

while True:
    socketClient, address = socketTCP.accept()
    threadClient = threading.Thread(target=establish_connection, args=(socketClient, address))
    threadClient.start()