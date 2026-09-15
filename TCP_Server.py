import socket
import threading
from env import address_server

active_users = {}

def identify_user(message, address_user):
    active_users.setdefault(address_user, message)

def chat_user(message, sender, receiver):
    msg = " ".join(message)
    chat_msg = f"mensagem de {sender}: {msg}"
    rcv_address = active_users[receiver]
    rcv_address.sendall(str.encode(chat_msg))

def sign_up_user(conn, user):
    active_users.setdefault(user, conn)

def establish_connection(conn, client_address):
    print(f"conexao estabelecida com o cliente {conn}")
    while True:
        msg_rcv = conn.recv(1024)
        msg = msg_rcv.decode().split(" ")
        conn.sendall(str.encode("Mensagem recebida"))
        if(msg[0] == "/chat"):
            message_chat = msg[2:]
            receiver = msg[1]
            chat_user(message_chat, conn, receiver)
        elif(msg[0] == "USER"):
            user = msg[1]
            sign_up_user(conn, user)
        # print(f"Eis os usuarios online:\n {active_users}")

socketTCP = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

socketTCP.bind(address_server)
socketTCP.listen()

while True:
    socketClient, address = socketTCP.accept()
    threadClient = threading.Thread(target=establish_connection, args=(socketClient, address))
    threadClient.start()