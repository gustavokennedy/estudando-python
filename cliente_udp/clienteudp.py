import socket
import time

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print('Cliente Socket criado com sucesso!')
print('-'*60)

host = 'localhost'
porta = 5433
mensagem = 'Olá servidor, esse é um teste. OK?'

try:
    print('Cliente: ' + mensagem)
    print('-' * 60)
    # Empacota mensagem e envia ao host na porta
    s.sendto(mensagem.encode(), (host, 5432))

    # Cria dados e servidor para receber resposta do servidor
    dados, servidor = s.recvfrom(4096)
    # Desempactar dados
    dados = dados.decode()
    print('Cliente: ' + dados)
finally:
    print('Cliente: fechando a conexão.')
    # Fecha conexão
    s.close()