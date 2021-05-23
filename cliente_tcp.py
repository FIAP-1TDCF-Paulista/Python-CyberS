import socket
import sys

def main():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    except socket.error as e:
        print('A CONEXÃO FALHOU!!!')
        print(f'ERRO : {e}')
        sys.exit()
    print('SOCKET CRIADO COM SUCESSO!')

    hostAlvo = input('Digite o HOST ou IP a ser conectado: ')
    portaAlvo = input('Digite a PORTA a ser conectada: ')

    try:
        s.connect((hostAlvo, int(portaAlvo)))
        print('Cliente TCP conectado com Sucesso no HOST: ' + hostAlvo + ' e na PORTA: ' + portaAlvo)
        s.shutdown(2)
    except socket.error as e:
        print('Não foi possivel conectar no HOST: ' + hostAlvo + ' - PORTA: ' + portaAlvo)
        print(f'ERRO: {e}')
        sys.exit()

if __name__ == '__main__':
    main()
