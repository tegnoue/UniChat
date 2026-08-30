import socket

socketTCP = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

socketTCP.bind(("127.0.0.1", 2023))
socketTCP.listen()

socketCliente, endereco = socketTCP.accept()

msg = socketCliente.recv(1024)
print(f"mensagem recebida: {msg}")

socketCliente.sendall(str.encode("Mensagem recebida!"))
socketCliente.close()