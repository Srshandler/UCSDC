import socket
# Configuração do servidor
host = '127.0.0.1'  # Endereço IP do servidor
port = 12345  # Porta para o servidor
# Cria um objeto socket do servidor
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Liga o servidor ao end e porta especificados
server_socket.bind((host, port))
# Define o núm máximo de conexões pendentes
server_socket.listen(5)
print(f"Servidor escutando em {host}:{port}")
while True:
  # Aguarda por uma conexão
  client_socket, addr = server_socket.accept()
  print(f"Conexão recebida de {addr}")  while True:
    # Recebe a mensagem do cliente    message = client_socket.recv(1024)
    # Se a mens estiver vazia, encerra a conexão 
  if not message:      break
  print(f"Cliente diz: {message.decode()}")
# Envia uma resposta para o cliente
  response = "Mensagem recebida com sucesso!"  
  client_socket.send(response.encode())
# Fecha a conexão com o cliente 
  client_socket.close()