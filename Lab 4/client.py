import socket


print('_______________________________________________\n',
      'К какому серверу вы хотите подключиться?\n',
      '1 - Этот компьютер\n',
      '2 - Ввести самостоятельно\n',
      '_______________________________________________')
serv = input('Введите команду: ')
if serv == '1':
    IP = 'localhost'
elif serv == '2':
    IP = input('Введите IP сервера: ')

sock = socket.socket()
sock.connect((IP, 9090))

print('\033[94m', 'Вы подключены к серверу!', '\033[0m')

work = True
while work:
    def end():
        cont = input('Повторить?(y/n)')
        if cont == 'n':
            print('До свидания!')
            sock.send(cont.encode())
            work = False
        elif cont == 'y':
            work = True
        else:
            print('Неизвестная команда!')
            end()
        return work


    mat = input('Введите элементы матрицы 3x3 через пробел: ')
    sock.send(mat.encode())
    print('det A = ', sock.recv(1024).decode())
    work = end()



