import socket

socketTCP = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socketTCP.connect(("127.0.0.1", 2026))

while True:

    txt_message = input("Digite a sua mensagem:\n")
    bytes_message = (txt_message).encode("ascii")
    socketTCP.sendall(bytes_message)
    msg = socketTCP.recv(1024)
    print(f"{msg} <- recebida")