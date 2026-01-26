from random import randint
from CharacterCreation import *
from FloorGeneration import *
from Inventory import *
# Функция для интересного вывода текста
def print(*text, sep=' ', end='\n', flush=False, delay=0.1): 
    from time import sleep 
    from builtins import print 
    string = sep.join(map(str, text)) + end 
    for char in string: 
        print(char, end='', flush=flush) 
        sleep(delay)
# Функция для печати статов
def PrCharacteristics(s):
    print("Нынешние статы:", "===============", sep="\n", end="\n", flush=True, delay=0.1)
    for i in s:
        print(i, s[i], sep=' ', end='\n', flush=True, delay=0.09)
    print(f'Максимально количество здоровья: {mxhp}', f'Максимальное количество защиты: {mxdef}')
# Функция для обозночения повышения этажа
def floor():
    lvlfloor += 1
# Функция для печати выбора действий
def praction():
    print('Выберите действие:', '==================', '1 - Атаковать', '2 - Использовать предмет',
          '3 - Оскорбить монстра', '4 - Попробовать проскочить мимо него', sep='\n', end='\n', flush=True, delay=0.1)
# Функция для проведения боя с монстрами
def fight(n):
    for i in range(1, randint(1, 2) + n):
        monstor = roommon()
        print(f'Впереди вас {monstor.Name}, пока вас необнорожили ваши действия?')
        while (monstor.HP != 0) and player['ЗДОРОВЬЕ'] > 0:
            praction()
            while True:
                varplayer = input('Введите ваш вариант_')
                if varplayer not in '1234':
                    print('Выберите один из четырех вариантов!')
                else:
                    break
            if varplayer == '1':
                kickplayer = randint(1, 20) + (player['СИЛА_АТАКИ'] // 10)
                if len(weapon) > 0:
                    damage = 5 + weapon[0]['c'] + (player['СИЛА_АТАКИ'] // 10)
                else:
                    damage = 5 + (player['СИЛА_АТАКИ'] // 10)
                print(f'Ваша значение атаки {kickplayer}, значение защиты у врага {monstor.Defense}', sep='\n', end='\n', flush=True, delay=0.1)
                monstor.TakingDamage(kickplayer, damage)
            elif varplayer == '2':
                prinvetory()
                use()
            elif varplayer == '3':
                pass

# Создание персонажа и вывод изначальных статов
player = СreatingСharacteristics()
mxhp = player['ЗДОРОВЬЕ']
mxdef = player['ЗАЩИТА']
mxatt = player['СИЛА_АТАКИ']
PrCharacteristics(player)
# Предыстория начало игры
histori = '''

Давным-давно, когда мир был спокоен, а человечество жило под солнцем, всё изменилось в один ужасный миг. Примерно три столетия назад реальность треснула: из недр земли хлынули разломы, извергающие хаос, ужас и древнюю нечисть. Проклятые твари, словки густой тьмой, окутали поверхность мира, сделав её непроглядной и смертоносной. Последним спасением для уцелевших стал побег вглубь, под каменные своды, в спасительный мрак.

Здесь, в лабиринтах пещер и величественных подземных полостях, родилось Царство Последнего Очага — оплот человечества, названный так в честь неугасимого пламени надежды, что горит в его сердцевине. Веками люди отбивали яростные атаки тварей у своих укреплённых врат. Битва длится и по сей день; каждый день добывается дорогой ценой, и никто не знает, сколько ещё хватит сил.

Вы — дитя подземелий. Для вас солнечный свет — лишь древняя легенда, а свежий ветер и пение птиц — чуждые понятия из забытых сказок. Но в вашей душе тлеет неугасимое любопытство. Оно и привело вас к роковому решению: пробиться наверх. Не для славы, а чтобы своими глазами увидеть мир, который у вас украли. Чтобы узнать, можно ли его отвоевать.

Готовы ли вы стать тем, кто не просто бросит вызов тьме, но и, возможно, зажжёт первый луч надежды на возвращение домой?

'''
print(histori, sep=' ', end='\n', flush=True, delay=0.08)
# Код игры
lvlfloor = 1
countroom = 0
end = 0
while player['ЗДОРОВЬЕ'] > 0:
    roomd = roomlvl1()
    if roomd[0] == 'монстров':
        print('Вы вошли в комнату монстров', sep='\n', end='\n', flush=True, delay=0.1)
        fight(lvlfloor)