from random import randint
from Items import *
from FirstLevelVrgi import *

def roommon():
    n = []
    n.append(Monstors1[randint(0, 5)])
    print(n)
    return mon1(n[0]['ИМЯ'], n[0]['СТАТЫ'][0], n[0]['СТАТЫ'][1], n[0]['СТАТЫ'][2], n[0]['СТАТЫ'][3], n[0]['СТАТЫ'][4])

def roomchil():
    return randint(5, 20)

def roomgold():
    return abcde[randint(0, 4)][randint(0, 4)]

def roomtrap(lvlf):
    var = randint(1, 2)
    if var == 1:
        return [view[0], viewcod[0]]
    else:
        return randint(1, 5 * lvlf)

def roomnoname(lvlf):
    randomvar = randint(0, 4)
    return [view[randomvar], viewcod[randomvar]]

def roomlvl1():
    print('Вы подымаетесь выше и вот развилка...')
    var1 = randint(0, 4)
    var2 = randint(0, 4)
    print('Куда вы пройдете дальше?', '=========================', f'1 - комната {view[var1]}', f'2 - комната {view[var2]}', sep='\n')
    while True:
        varplayer = input("Ваш выбор_")
        if varplayer == '1':
            return [view[var1], viewcod[var1]]
            break
        elif varplayer == '2':
            return [view[var2], viewcod[var2]]
            break
        else:
            varplayer = input("Введите выринт из указанных")

view = ['монстров', 'отдыха', 'сокровищь', 'ловушек', '???']
viewcod = ['roommon()', 'roomchil()', 'roomgold()', 'roomtrap(lvlfloor)', 'roomnoname()']