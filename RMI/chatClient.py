import Pyro4

# Classe para o cliente de chat
class ChatClient(object):
  def __init__(self, server_uri):
    self.server = Pyro4.Proxy(server_uri)
    self.username = input("Digite seu nome de usuário: ")
    
  def send_message(self, message):
    self.server.send_message(self.username, message)
    
  def receive_messages(self):
    messages = self.server.get_messages()
    for message in messages:
      print(message)
      
# Conecte-se ao servidor de chat
server_uri = "PYRO:ChatServer@localhost:3000"
client = ChatClient(server_uri)

# Loop para enviar e receber mensagens
while True:
  message = input("Digite sua mensagem (ou 'sair' para sair): ")
  if message.lower() == "sair":
    break
  client.send_message(message)
  client.receive_messages()
  