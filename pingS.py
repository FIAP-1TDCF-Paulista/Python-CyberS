import os

print('-=' * 30)
ip_ou_host = input('Digite o IP ou HOST a ser verificado: ')
print('-=' * 30)

os.system(f'ping -n 6 {ip_ou_host}')
