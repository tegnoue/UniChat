import socket

socketTCP = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socketTCP.connect(("127.0.0.1", 2023))
socketTCP.sendall(b"Mensagem.")
msg = socketTCP.recv(1024)
print(f"{msg} <- recebida")
socketTCP.close