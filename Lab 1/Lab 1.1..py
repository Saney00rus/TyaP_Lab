a = int(input('a= '))
b = int(input('b= '))
c = int(input('c= '))
d = int(input('d= '))
k = int(input('k= '))
if a != 0 and b !=0:
  rez = abs(((((a**2)-(b**3)-(c**3)*(a**2))*(b-c+c*(k-d/(b**3)))-((k/b)-(k/a))*c)**2)-20000)
  print('Ответ: ', rez)
else:
  print('Нельзя делить на 0!')
