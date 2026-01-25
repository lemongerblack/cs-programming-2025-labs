from random import randint
from FirstLevelVrgi import *

def roommon():
    n = []
    for i in range(1, randint(1, 2) + 1):
        n.append(Monstors1[randint(0,5)])
    print(n)
    return n

def roomlvl1():
    print('Вы подымаетесь выше и вот развилка...')


    print('Куда вы пройдете дальше?', '====================', '1 - ', '2 -', sep='\n')

view = ['монстров', 'отдыха', 'сокровищь', 'ловушка']

roommon()