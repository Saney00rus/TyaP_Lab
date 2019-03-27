import os
f = open('Products.txt', 'r')

global prod
prod = []

for line in f:
    line = line.strip()
    line = line.split(';')
    prod.append([line[0], line[1], line[2], line[3]])

max = int(len(prod))

#Задание №1
def Z1():
    path = input('Введите путь к папке: ')
    files = next(os.walk(path))
    print('Количество файлов в папке: ', len(files))

    print('__________________________________________________________\n'
          '1 - Повторить программу\n'
          '0 - Выход в меню\n'
          '__________________________________________________________\n')
    cont = input('Выберете команды: ')
    if cont == "1":
        Z1()
    elif cont == "0":
        start()

#Задание №2
def Z2():
    print('Сортировка по:\n',
              '1 - Убыванию\n',
              '2 - Возрастанию')
    a = input('Выберете команду: ')
    if a == '1':
        print('                Таблица:')
        prod.sort(key=lambda line: int(line[2]), reverse=True)
        for i in range(0, len(prod)):
            print(prod[i])
    elif a == '2':
        print('                Таблица:')
        prod.sort(key=lambda line: int(line[2]))
        for i in range(0, len(prod)):
            print(prod[i])
    else:
        print('Неверная команда!')
        Z2()

    print('__________________________________________________________\n'
          '1 - Повторить программу\n'
          '0 - Выход в меню\n'
          '__________________________________________________________\n')
    cont = input('Выберете команды: ')
    if cont == "1":
        Z2()
    elif cont == "0":
        start()
    return prod

#Задание №3
def Z3():
    id = []
    print('                Таблица:')
    for i in range(0, len(prod)):
        print(prod[i])
    print('0 - Остановка ввода ID')

    work = True
    while work:
        ID = input('Введите ID товара: ')
        if ID.isdigit():
            ID = int(ID)
            if ID == 0:
                work = False
            elif ID <= max:
                id.append(ID)
            else:
                print('Такого ID не существует! Максимальный ID:', max)
                work = True
        else:
            print('Неверный символ! Повторите попытку.')
            work = True

    chan = int(input('Введите значение, на которое нужно уменьшить кол-во: '))
    for i in range(0, len(prod)):
        for j in range(0, len(id)):
            if int(prod[i][0]) == int(id[j]):
                prod[i][3] = int(prod[i][3]) - chan

    print('Изменения сохранены!\n'
          '         Новая таблица: ')
    for i in range(0, len(prod)):
        print(prod[i])

    print('__________________________________________________________\n'
          '1 - Повторить программу\n'
          '0 - Выход в меню\n'
          '__________________________________________________________\n')
    cont = input('Выберете команды: ')
    if cont == "1":
        Z3()
    elif cont == "0":
        start()
    return prod

#Задание №4
def Z4():
    print('                 Как сохранить результат?\n'
          '__________________________________________________________\n'
          '1 - Сохранить в данном документе\n'
          '2 - Сохранить в новом документе\n'
          '__________________________________________________________\n')
    a = input('Выберете команду: ')

    if a == '1':
        file = open('Products.txt', 'r+')
        for i in range(0, len(prod)):
            for j in range(0, len(prod[i])):
                if 0 <= j <= 2:
                    file.write(str(prod[i][j]) + ";")
                else:
                    file.write(str(prod[i][j]))
            file.write('\n')
        print('Файл Products.txt успешно сохранен!')
        file.close()

    if a == '2':
        name = input('Введите название файла: ')
        new = open(name, 'w')
        for i in range(0, len(prod)):
            for j in range(0, len(prod[i])):
                if 0 <= j <= 2:
                    new.write(str(prod[i][j]) + ";")
                else:
                    new.write(str(prod[i][j]))
            new.write('\n')
        print('Файл ', name, ' успешно сохранен!')
        new.close()

    print('__________________________________________________________\n'
          '1 - Повторить программу\n'
          '0 - Выход в меню\n'
          '__________________________________________________________\n')
    cont = input('Выберете команды: ')
    if cont == "1":
        Z4()
    elif cont == "0":
        start()

#Меню
def start():
    print('________________________МЕНЮ______________________________\n'
          '1 - Задание №1 - Открыть файл\n'
          '2 - Задание №2 - Сортировка по цене\n'
          '3 - Задание №3 - Уменьшение количества\n'
          '4 - Задание №4 - Сохранить изменения\n'
          '0 - Выход из программы\n'
          '__________________________________________________________\n')
    a = input('Выберете команду: ')

    if a == "1":
        Z1()
    elif a == "2":
        Z2()
    elif a == "3":
        Z3()
    elif a == "4":
        Z4()
    elif a == "0":
        print('                     До свидания!')
        exit()
    else:
        print('Неверная команда!')
        start()

start()

f.close()