string = 'Лимузин, Литий, Лувр, Лицемерие, Лайк'
string = string.split(', ')
for a in range(0, len(string)-1):
    if string[a][0] == 'Л' and string[a][1] == 'и':
        print(string[a])