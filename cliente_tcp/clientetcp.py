import socket
import sys
import time

def main():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    except socket.error as e:
        print("A conexão falhou!")
        print("Erro: {}".format(e))
        sys.exit()

    print("Socket criado com sucesso")
    print("#"*60)

    Host = input("Digite o Host/Ip a ser conectado: ")
    Porta = input("Digite a porta para conexão: ")
    print("-" * 60)
    print("Tentando conectar...")
    time.sleep(2)
    try:
        s.connect((Host, int(Porta)))
        print("Cliente TCP conectado com sucesso no host")
        print("#" * 60)
        s.shutdown(2)
    except socket.error as e:
        print("A conexão TCP falhou! Não foi possível conectar no host " + Host + " e na porta " + Porta)
        print("Erro: {}".format(e))
        print("#" * 60)
        sys.exit()

if __name__ == "__main__":
    main()