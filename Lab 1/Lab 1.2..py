import random
rnd = random.randint(0,10)
print(rnd)
a = False
while a == False:
    chislo = int(input('Введите число: '))
    if rnd == chislo:
        print('Поздравляем! Вы Выиграли!')
        a = True
    else:
        if chislo < rnd:
            print('Ваше число меньше!')
        else:
            print('Ваше число больше!')