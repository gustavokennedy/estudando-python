import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print('Socket criado com sucesso')
print('-'*60)

host = 'localhost'
porta = 5432

# Ligação entre cliente/servidor
s.bind((host, porta))
mensagem = 'Servidor: Olá cliente, mensagem recebida!'

while 1:
    dados, end = s.recvfrom(4096)

    if dados:
        print('Servidor enviando mensagem...')
        s.sendto(dados + (mensagem.encode()), end)