import socket as s
host = input('website:')
print(f'IP Address of {host} is {s.gethostbyname(host)}')

