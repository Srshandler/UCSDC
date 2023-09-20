import Pyro4

# Conecta-se ao servidor RMI
# Substitua pelo URI correto do servidor
uri = "PYRO:MeuObjetoRemoto@localhost:50000"
objeto_remoto = Pyro4.Proxy(uri)

# Chama o método remoto
nome = input("Digite seu nome: ")
resposta = objeto_remoto.saudacao(nome)

print(resposta)