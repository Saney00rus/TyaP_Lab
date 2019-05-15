import socket


def det(mat):
    print('Получена матрица:', mat)
    return (mat[0] * (mat[4] * mat[8] - mat[5] * mat[7]) -
            mat[1] * (mat[3] * mat[8] - mat[5] * mat[6]) +
            mat[2] * (mat[3] * mat[7] - mat[6] * mat[4]))


print('\033[94m', 'Сервер запущен!', '\033[0m')

sock = socket.socket()
sock.bind(('', 9090))
sock.listen()
conn, add = sock.accept()

print('Пользователь с IP-адресом:', add, 'подключен!')

work = True
while work:
    mat = conn.recv(1024).decode()
    if mat == 'n':
        work = False
        print('Пользователь с IP-адресом:', add, 'завершил работу программы!')
        sock.close()
    else:
        mat = mat.strip().split(' ')
        mat = [int(x) for x in mat]
        answer = det(mat)
        conn.send(str(answer).encode())