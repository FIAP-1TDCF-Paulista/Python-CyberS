import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print('SOCkET criado com sucesso!!!')

host = 'localhost'
port = 5432

s.bind((host, port))
menssagem = '\nServidor: OLÁ CLIENTE'

while 1:
    dados, end = s.recvfrom(4096)

    if dados:
        print('Servidor envidando msg...')
        s.sendto(dados + menssagem.encode(), end)
