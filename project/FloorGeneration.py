from random import randint
from FirstLevelVrgi import *

def roommon():
    n = []
    for i in range(1, randint(1, 2) + 1):
        n.append(Monstors1[randint(0, 5)])
    return n

def roomchil():
    return randint(5, 20)

def roomgold():
    pass

def roomlvl1():
    print('Вы подымаетесь выше и вот развилка...')
    var1 = view[randint(0, 3)]
    var2 = view[randint(0, 3)]
    print('Куда вы пройдете дальше?', '=========================', f'1 - комната {var1}', f'2 - комната {var2}', sep='\n')


view = ['монстров', 'отдыха', 'сокровищь', 'ловушка']

roommon()