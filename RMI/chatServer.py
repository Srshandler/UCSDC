import Pyro4

# Classe para o servidor de chat
@Pyro4.expose
class ChatServer(object):
    def __init__(self):
      self.messages = []
      
    def send_message(self, username, message):
      self.messages.append(f"{username}: {message}")
      print(f"{username} disse: {message}")
      
    def get_messages(self):
      return self.messages
      
# Inicialize o servidor Pyro4
daemon = Pyro4.Daemon(port=3000)

# Registre o objeto do servidor de chat
uri = daemon.register(obj_or_class=ChatServer, objectId="ChatServer")
print("URI do servidor de chat:", uri)

# Inicie o servidor
print("Aguardando conexões...")
daemon.requestLoop()