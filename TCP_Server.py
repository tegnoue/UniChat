import socket
import threading
from env import address_server

active_users = {}

def identify_user(message, address_user):
    active_users.setdefault(address_user, message)

def chat_user(message, sender, receiver):
    msg = " ".join(message)
    chat_msg = f"mensagem de {sender}: {msg}"
    receiver.sendall(str.encode(chat_msg))

def establish_connection(client_address, conn):
    print(f"conexao estabelecida com o cliente {client_address}")
    while True:
        msg = client_address.recv(1024)
        print(f"mensagem recebida: {msg}")
        identify_user(msg, client_address)
        client_address.sendall(str.encode("Mensagem recebida"))
        if(msg[0:4] == "/chat"):
            message_chat = msg.split(" ")
            chat_user(msg[2:], client_address, msg[1])
        #print(f"Eis os usuarios online:\n {active_users}")

socketTCP = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

socketTCP.bind(address_server)
socketTCP.listen()

while True:
    socketClient, address = socketTCP.accept()
    threadClient = threading.Thread(target=establish_connection, args=(socketClient, address))
    threadClient.start()