import socket
# Configuração do cliente UDP
host = '127.0.0.1' 
# Endereço IP do servidor
port = 12345 
# Porta do servidor
# Cria um objeto socket UDP do cliente
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
while True:  
  # Solicita que o cliente insira uma mensagem  message = input("Digite uma mensagem para o servidor (ou digite 'exit' para sair): ")    if message.lower() == 'exit':    break # Sai do loop se o cliente digitar 'exit'      # Envia a mensagem para o servidor  client_socket.sendto(message.encode(), (host, port))    # Recebe a resposta do servidor  data, addr = client_socket.recvfrom(1024)  print(f"Servidor diz: {data.decode()}")# Fecha o socket do cliente (não é necessário no UDP, mas pode ser feito)client_socket.close()