from random import randint
from FirstLevelVrgi import *

def roommon():
    n = []
    for i in range(1, randint(1, 2) + 1):
        n.append(Monstors1[randint(0, 5)])
    print(n)
    return mon1(n['ИМЯ'], n['СТАТЫ'][0], n['СТАТЫ'][1], n['СТАТЫ'][2], n['СТАТЫ'][3], n['СТАТЫ'][4])

def roomchil():
    return randint(5, 20)

def roomgold():
    pass

def roomtrap():
    pass

def roomnoname():
    pass


def roomlvl1():
    print('Вы подымаетесь выше и вот развилка...')
    var1 = randint(0, 4)
    var2 = randint(0, 4)
    print('Куда вы пройдете дальше?', '=========================', f'1 - комната {view[var1]}', f'2 - комната {view[var2]}', sep='\n')
    while True:
        varplayer = input("Ваш выбор_")
        if varplayer == '1':
            return [var1, eval(var1)]
            break
        elif varplayer == '2':
            return [var2, eval(var2)]
            break
        else:
            varplayer = input("Введите выринт из указанных")

view = ['монстров', 'отдыха', 'сокровищь', 'ловушек', '???']
viewcod = ['roommon()', 'roomchil()', 'roomgold()', 'roomtrap()', 'roomnoname()']

print(roommon())