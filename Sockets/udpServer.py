import socket
# Configuração do servidor UDP
host = '127.0.0.1' # Endereço IP do servidor
port = 12345 # Porta para o servidor

# Cria um objeto socket UDP do servidor
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# Liga o servidor ao endereço e porta especificados
server_socket.bind((host, port))
print(f"Servidor UDP escutando em {host}:{port}")

while True:
  # Recebe a mensagem do cliente
  data, addr = server_socket.recvfrom(1024)
  print(f"Cliente {addr[0]}:{addr[1]} diz: {data.decode()}")
  # Envia uma resposta para o cliente
response = "Mensagem recebida com sucesso!"
server_socket.sendto(response.encode(), addr)