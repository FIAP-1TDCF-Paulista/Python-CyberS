import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print('CLIENTE CRIADO COM SUCESSO!!')

host = 'localhost'
port = 5433
menssagem = 'Olá servidor SUAVE?'

try:
    print('Cliente: ' + menssagem)
    s.sendto(menssagem.encode(), (host, 5432))

    dados, servidor = s.recvfrom(4096)
    dados = dados.decode()
    print('Cliente: ' + dados)
finally:
    print('Cliente: FECHANDO A CONEXÃO.')
    s.close()
