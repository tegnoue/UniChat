import socket

# envia mensagens
def send_messages(user):
    while True:
        txt_message = input("Escreva sua mensagem:\n")
        bytes_message = (txt_message).encode("ascii")
        socketTCP.sendall(bytes_message)
        msg = socketTCP.recv(1024)
        print(f"{msg} <- recebida")

#ve usuarios online
def see_online_users():
    socketTCP.sendall(b"SALL")

#se apresenta ao servidor
def login(txt_username):
    req = f"USER {txt_username}".encode("ascii")
    socketTCP.sendall(req)

#encerra conexão
def quit():
    socketTCP.sendall(b"QUIT")


socketTCP = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socketTCP.connect(("127.0.0.1", 2026))

while True:
    txt_command = input("O que deseja fazer?:\n")

    commands = txt_command.split(" ")

    if(commands[0] == "/login"):
        if(len(commands) == 2):
            login(commands[1])
        else:
            print("insira o usuário corretamente")
    elif(commands[0] == "/quit"):
        quit()
    elif(commands[0] == "/online"):
        see_online_users()
    elif(commands[0] == "/chat"):
        if(len(commands) == 2):
            send_messages(commands[1])
        else:
            print("insira o usuário corretamente")
    else:
        print("Erro no comando")