n = int(input('Длина списка: '))
lst = []
count = 0
for i in range(0, n):
    lst.append(int(input('Введите элемент ' + str(i+1) + ' : ')))
print('Ваша строка: ', lst)
lst = [x for x in lst if x % 2 != 0]
lst.append(int(input('Введите первый новый элемент: ')))
lst.append(int(input('Введите второй новый элемент: ')))
print('Новая строка: ', lst)
