from random import randint

# Функция для интересного вывода текста
def print(*text, sep="\n", end="\n", flush=True, delay=0.05):
    from time import sleep 
    from builtins import print 
    string = sep.join(map(str, text)) + end 
    for char in string: 
        print(char, end='', flush=flush) 
        sleep(delay)
# Функция для печати статов
def PrCharacteristics(s):
    print("Нынешние статы:", "===============", f'уровень персонажа: {lvlplayer}', f'количество очков: {pointr}')
    for i in s:
        print(i, s[i], sep=' ', end='\n', flush=True, delay=0.005)
    print(f'Максимально количество здоровья: {mxhp}', f'Максимальное количество защиты: {mxdef}')
# Функция для обозночения повышения этажа
def floor():
    global lvlfloor
    lvlfloor += 1
# функция для повышения уровня персонажа
def playerup():
    global lvlplayer
    lvlplayer += 1
    player['ЗДОРОВЬЕ'] += 5
    player['ЗАЩИТА'] += 1
    mxhp += 5
    mxdef += 1
# Функция для печати выбора действий
def praction():
    print('Выберите действие:', '==================', '1 - Атаковать', '2 - Использовать предмет',
          '3 - Оскорбить монстра', '4 - Попробовать проскочить мимо него')
# Функция для проведения боя с монстрами
def fight(lvlfloor):
    global pointr
    global lvlpr
    for i in range(1, randint(1, 2) + lvlfloor):
        monstor = roommon()
        print(f'Впереди вас {monstor.Name}, пока вас не обнаружили, ваши действия?')
        while (monstor.HP > 0) and player['ЗДОРОВЬЕ'] > 0:
            print(f'Ваше здоровье {player['ЗДОРОВЬЕ']}, здоровье врага {monstor.HP}')
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
                print(f'Ваша значение атаки {kickplayer}, значение защиты у врага {monstor.Defense}')
                monstor.TakingDamage(kickplayer, damage)
            elif varplayer == '2':
                prinvetory()
                use(player, monstor)
            elif varplayer == '3':
                fc = input("Ну давай_")
                morkick = randint(1, 20) + (player['СИЛА_АТАКИ'] // 10)
                damag = 3
                monstor.TakingDamage(morkick, damag)
                print('Не важно был ли нанесен урон. Знай это было подло... ')
            else:
                attemptplayer = randint(1, 20) + (player['ЛОВКОСТЬ'] // 10)
                attemmonstors = randint(1, 20) + (monstor.Agility // 10)
                if attemptplayer > attemmonstors:
                    print("Вы успешно проскачили мимо него")
                    monstor.HP = 0
            if monstor.HP > 0:
                print('Монстр атакует!')
                monstor.Attacks(player, 0)
    else:
        print('Вы прошли комнату!')
        pointr += 5
        lvlpr += 5
    
# Функция для создания персонажа
def СreatingСharacteristics():
    name = input('введите имя персонажа_')
    flag = True
    print('Выберите расу', '===============', '1 - человек', '2 - эльф', '3 - дворф')
    while flag:
        n = input('введите ваш выбор_')
        if n == '1':
            HP = randint(20, 35)
            Attack = randint(20, 30)
            Defense = randint(10, 15)
            Agility = randint(20, 25)
            Attentiveness = randint(10, 20)
            Height = randint(152, 184)
            Weight = Height - 90
            return {'ИМЯ': name, 'РАСА': 'ЧЕЛОВЕК','ЗДОРОВЬЕ': HP, 'СИЛА_АТАКИ': Attack, 'ЗАЩИТА': Defense,
                     'ЛОВКОСТЬ': Agility, 'ВНИМАТЕЛЬНОСТЬ': Attentiveness, 'РОСТ': Height, 'ВЕС': Weight}
            break
        elif n == '2':
            HP = randint(20, 30)
            Attack = randint(15, 30)
            Defense = randint(13, 15)
            Agility = randint(30, 35)
            Attentiveness = randint(10, 20)
            Height = randint(150, 185)
            Weight = Height - 100
            return {'ИМЯ': name, 'РАСА': 'ЭЛЬФ','ЗДОРОВЬЕ': HP, 'СИЛА_АТАКИ': Attack, 'ЗАЩИТА': Defense,
                     'ЛОВКОСТЬ': Agility, 'ВНИМАТЕЛЬНОСТЬ': Attentiveness, 'РОСТ': Height, 'ВЕС': Weight}
            break
        elif n == '3':
            HP = randint(30, 45)
            Attack = randint(25, 35)
            Defense = randint(13, 15)
            Agility = randint(15, 19)
            Attentiveness = randint(13, 20)
            Height = randint(122, 152)
            Weight = Height - 75
            return {'ИМЯ': name, 'РАСА': 'ДВОРФ','ЗДОРОВЬЕ': HP, 'СИЛА_АТАКИ': Attack, 'ЗАЩИТА': Defense,
                     'ЛОВКОСТЬ': Agility, 'ВНИМАТЕЛЬНОСТЬ': Attentiveness, 'РОСТ': Height, 'ВЕС': Weight}
            break
        else:
            print("ОШИБКА: выберите число от 1 до 3, чтобы выбрать расу")
# функция для прокачки
def upppoint():
    global pointr
    sp = ['СИЛА_АТАКИ', 'ЛОВКОСТЬ', 'ВНИМАТЕЛЬНОСТЬ']
    print('Прокачка персонажа, чтобы прокочаться напишите название характеристики и сколько потратите очков:', 'пример_ЗДОРОВЬЕ 10')
    print('какие характеристики можно прокачать:', '1 - СИЛА_АТАКИ', '2 - ЛОВКОСТЬ', '3 - ВНИМАТЕЛЬНОСТЬ')
    while True:
        varr = input('введите как в примере_').split()
        try:
            if (int(varr[1]) <= pointr) and (varr[0] in sp):
                player[varr[0]] += int(varr[1])
                pointr -= int(varr[1])
                break
        except:
            print('Некорректный ввод')
# класс монстров
class mon1:
    def __init__(self, Name, HP, Attack, Defense, Agility, Damage):
        self.Name = Name
        self.HP = HP
        self.Attack = Attack
        self.Defense = Defense
        self.Agility = Agility
        self.Damage = Damage

    def Attacks(self, player, evade):
        kick = randint(1, 20)
        damager = randint(1, self.Damage)
        if (evade > 0) and ((kick + (self.Attack // 10)) > evade):
            player["ЗДОРОВЬЕ"] = player["ЗДОРОВЬЕ"] - damager
            print(f"Вы получили - {damager} урона")
        elif ((kick + (self.Attack // 10)) > player["ЗАЩИТА"]):
            player["ЗДОРОВЬЕ"] = player["ЗДОРОВЬЕ"] - damager
            print(f"Вы получили - {damager} урона")
        else:
            print("Вы избежали урона! Это отличный шанс!")
    
    def TakingDamage(self, playeratack : int, damage : int):
        global pointr
        global lvlpr
        if (playeratack > self.Defense) and (self.HP - damage != 0):
            self.HP = self.HP - damage
            print(f'Вы нанесли {damage} урона!')
        elif (playeratack > self.Defense) and (self.HP - damage <= 0):
            self.HP = 0
            print("Вы отдалели эту тварь!")
            pointr += (3 * lvlfloor)
            lvlpr += (3 * lvlfloor)
        else:
             print("Вы начинаете атаковать и, к сожаление промахиваетесь")
# функции определения комнат
def roommon():
    n = []
    n.append(eval(f'Monstors{str(lvlfloor)}[randint(0, 5)]'))
    return mon1(n[0]['ИМЯ'], n[0]['СТАТЫ'][0], n[0]['СТАТЫ'][1], n[0]['СТАТЫ'][2], n[0]['СТАТЫ'][3], n[0]['СТАТЫ'][4])

def roomchil():
    return randint(5, 20)

def roomgold():
    return abcde[randint(0, 4)][randint(0, 4)]

def roomtrap(lvlf):
    return randint(1, 5 * lvlf)

def roomnoname(lvlf):
    randomvar = randint(0, 4)
    return [view[randomvar], viewcod[randomvar]]

def roomlvl1():
    print('Вы подымаетесь выше и вот развилка...')
    var1 = randint(0, 20)
    var2 = randint(0, 20)
    print('Куда вы пройдете дальше?', '=========================', f'1 - комната {view[var1]}', f'2 - комната {view[var2]}')
    while True:
        varplayer = input("Ваш выбор_")
        if varplayer == '1':
            return [view[var1], 0]
            break
        elif varplayer == '2':
            return [view[var2], 0]
            break
        else:
            varplayer = input("Введите выринт из указанных")
# функции для ивенторя
def prinvetory():
    print(f"Ваш ивентарь - {iventory}", f"Ваша экиперовка - {equipment}", f"Ваше оружие - {weapon}")

def popinvetory():
    prinvetory()
    while True:
        varplayer = input('Какой предмет вы хотите выкинуть(1,2,3,4,5)?')
        if varplayer not in iventory:
            print('Введите корректное число от 1 до 5')
        else:
            iventory[varplayer] = []
            break
    prinvetory

def iven():
    n = roomgold()
    print(f'Вы нашли {n}')
    for i in range(1, 6):
        if iventory[str(i)] == []:
            iventory[str(i)] = [n]
            break
    else:
        print('Место в ивентаре не достаточно...', 'Будишь менять предметы?', '1 - да', '2 - нет')
        while True:
            varplayer = input('Введите ваш ответ')
            if varplayer == '1':
                prinvetory()
                print('Какой предмет меняете?', '=====================', '1 - 1', '2 - 2', '3 - 3', '4 - 4', '5 - 5')
                while True:
                    varp = input('Выберите какой предмет хотите поменять_')
                    if varp in iventory:
                        break
                    else:
                        print('Ведите ваш выбор от 1 до 5')
                iventory[varp] = n
                break
            else:
                break

def ause():
    if iventory[var][0]['a'] + player['ЗДОРОВЬЕ'] <= mxhp:
        player['ЗДОРОВЬЕ'] = player['ЗДОРОВЬЕ'] + iventory[var][0]['a']
        print(f"Вы восстановили {iventory[var][0]['a']} здоровья")
        iventory[var] = []
        prinvetory()
    else:
        player['ЗДОРОВЬЕ'] = mxhp
        print(f"Вы восстановили {iventory[var][0]['a'] - mxhp} здоровья")
        iventory[var] = []
        prinvetory()

def buse():
    global equipment
    if equipment == []:
        equipment = [iventory[var][0]]
        player['ЗАЩИТА'] = player['ЗАЩИТА'] + iventory[var][0]['b']
        print(f"Вы экиперовали {iventory[var][0]['name']}, ваша защита равна {player['ЗАЩИТА']}")
        iventory[var] = []
        prinvetory()
    else:
        print(f"Вы хотите поменять {equipment[0]} на {iventory[var][0]}", "1 - Да", "2 - нет")
        while True:
            playerotv = input("Введите ваш вариант")
            if playerotv == '1':
                equipment = [iventory[var][0]]
                player['ЗАЩИТА'] = mxdef + iventory[var][0]['b']
                print(f"Вы экиперовали {iventory[var][0]['name']}, ваша защита равна {player['ЗАЩИТА']}")
                iventory[var] = []
                prinvetory()
                break
            elif playerotv == '2':
                break
            else:
                print("Выберите возможный вариант 1 или 2")

def cuse():
    global weapon
    if weapon == []:
        weapon = [iventory[var][0]]
        player['СИЛА_АТАКИ'] = player['СИЛА_АТАКИ'] + iventory[var][0]['c']
        print(f"Теперь ваше оружие {iventory[var][0]['name']}, ваша сила атаки {player['СИЛА_АТАКИ']}")
        iventory[var] = []
        prinvetory()
    else:
        print(f"Вы хотите поменять {weapon[0]} на {iventory[var][0]}", "1 - Да", "2 - нет")
        while True:
            playerotv = input("Введите ваш вариант")
            if playerotv == '1':
                weapon = [iventory[var][0]]
                player['СИЛА_АТАКИ'] = mxatt + iventory[var][0]['c'][0]
                print(f"Теперь ваше оружие {iventory[var][0]['name']}, ваша сила атаки {player['СИЛА_АТАКИ']}")
                iventory[var] = []
                prinvetory()
                break
            elif playerotv == '2':
                break
            else:
                print("Выберите возможный вариант 1 или 2")

def euse():
    global pointr
    global lvlpr
    pointr += iventory[var][0]['e']
    lvlpr += iventory[var][0]['e']
    iventory[var] = []

def use(player, monstor):
    while True:
        var = input("Выберите какой предмет вы хотите использовать_ ")
        try:
            if len(iventory[var]) > 0:
                if 'a' in iventory[var][0]:
                    ause()
                elif 'b' in iventory[var][0]:
                    buse()
                elif 'c' in iventory[var][0]:
                    cuse()
                elif 'd' in iventory[var][0]:
                    monstor.HP = monstor.HP - iventory[var][0]['d']
                    print(f"Вы нанесли {iventory[var][0]['d']} урона")
                    iventory[var] = []
                elif 'e' in iventory[var][0]:
                    euse()
            else:
                print('Эта ячейка ивенторя пуста!')
                break
        except:
            print('Введите вариант 1,2,3,4,5')
# Данные игры
# монстры
Monstors1 = [{'ИМЯ': 'багбир', 'СТАТЫ': [20, 20, 9, 13, 7]}, {'ИМЯ': 'темная-слизь', 'СТАТЫ': [10, 11, 5, 15, 4]},
             {'ИМЯ': 'нисшая-тень', 'СТАТЫ': [16, 20, 6, 20, 5]}, {'ИМЯ': 'грязевой-монстр', 'СТАТЫ': [14, 14, 10, 5, 5]},
             {'ИМЯ': 'скелет', 'СТАТЫ': [13, 15, 13, 20, 4]}, {'ИМЯ': 'нисший-демон', 'СТАТЫ': [22, 21, 8, 3, 6]}]
Monstors2 = [{'ИМЯ': 'демон', 'СТАТЫ': [38, 30, 10, 11, 9]}, {'ИМЯ': 'упырь', 'СТАТЫ': [26, 20, 12, 15, 7]},
             {'ИМЯ': 'живой-мертвец', 'СТАТЫ': [16, 21, 9, 7, 5]}, {'ИМЯ': 'огр', 'СТАТЫ': [31, 23, 7, 7, 7]},
             {'ИМЯ': 'тень', 'СТАТЫ': [35, 31, 6, 27, 8]}, {'ИМЯ': 'грязевой-голем', 'СТАТЫ': [22, 22, 13, 5, 5]}]
Monstors3 = [{'ИМЯ': '', 'СТАТЫ': []}, {'ИМЯ': '', 'СТАТЫ': []},
             {'ИМЯ': '', 'СТАТЫ': []}, {'ИМЯ': '', 'СТАТЫ': []},
             {'ИМЯ': '', 'СТАТЫ': []}, {'ИМЯ': '', 'СТАТЫ': []}]
# виды комнат
view = ['монстров', 'монстров', 'монстров', 'монстров', 'монстров',
        'монстров', 'монстров', 'монстров', 'монстров', 'монстров',
        'отдыха', 'сокровищь', 'сокровищь', 'ловушек', 'ловушек',
        'ловушек', '???', '???', '???', '???', '???']
viewcod = ['roommon()', 'roomchil()', 'roomgold()', 'roomtrap(lvlfloor)', 'roomnoname()']
# ивентарь
iventory = {'1': [], '2': [], '3': [], '4': [], '5': []}
# предметы
ahilsitems = [{'name': 'МалоеЗельеЛечения', 'a': 3}, {'name': 'ЗельеЛечения', 'a': 5}, {'name': 'БольшоеЗельеЛечения', 'a': 10},
              {'name': 'ЦелебныйГриб', 'a': 1}, {'name': 'БольшойЦелебныйГриб', 'a': 2}]
barmorPlus = [{'name': 'КожанныйДоспех', 'b': 1}, {'name': 'ПроклёпанныйКожаныйДоспех', 'b': 2}, {'name': 'ЧешуйчатыйДоспех', 'b': 3},
              {'name': 'Кольчуга', 'b': 4}, {'name': 'Латы', 'b': 5}]
cweapon = [{'name': 'БоевойПосох', 'c': 2}, {'name': 'Кинжал', 'c': 4}, {'name': 'РучнойТопор', 'c': 4},
           {'name': 'БоевойТопор', 'c': 8}, {'name': 'ДлинныйМеч', 'c': 6}]
dkick = [{'name': 'ДротикСАвтоНаводкой', 'd': 5}, {'name': 'ДАЭТОКАМЕНЬ!', 'd': 3}, {'name': 'ЖелезнаяТряпка', 'd': 4},
         {'name': 'МешочекСПеском', 'd': 3}, {'name': "Кунай", 'd': 7}]
egold = [{'name': 'МаленькийМещочекЗолота', 'e': 5}, {'name': 'МешочекЗолота', 'e': 15}, {'name': 'БольшойМешочекЗолота', 'e': 30},
         {'name': 'СундучокСДрагоценастями', 'e': 45}, {'name': 'СлитокЗолота!', 'e': 70}]
abcde = [ahilsitems, barmorPlus, cweapon, dkick, egold]
# создание персонажа
player = СreatingСharacteristics()
mxhp = player['ЗДОРОВЬЕ']
mxdef = player['ЗАЩИТА']
mxatt = player['СИЛА_АТАКИ']
# сюжет
histori = '''Давным-давно, когда мир был спокоен, а человечество жило под солнцем, всё изменилось в один ужасный миг. Примерно три столетия назад реальность треснула: из недр земли хлынули разломы, извергающие хаос, ужас и древнюю нечисть. Проклятые твари, словки густой тьмой, окутали поверхность мира, сделав её непроглядной и смертоносной. Последним спасением для уцелевших стал побег вглубь, под каменные своды, в спасительный мрак.
#
#Здесь, в лабиринтах пещер и величественных подземных полостях, родилось Царство Последнего Очага — оплот человечества, названный так в честь неугасимого пламени надежды, что горит в его сердцевине. Веками люди отбивали яростные атаки тварей у своих укреплённых врат. Битва длится и по сей день; каждый день добывается дорогой ценой, и никто не знает, сколько ещё хватит сил.
#
#Вы — дитя подземелий. Для вас солнечный свет — лишь древняя легенда, а свежий ветер и пение птиц — чуждые понятия из забытых сказок. Но в вашей душе тлеет неугасимое любопытство. Оно и привело вас к роковому решению: пробиться наверх. Не для славы, а чтобы своими глазами увидеть мир, который у вас украли. Чтобы узнать, можно ли его отвоевать.
#
#Готовы ли вы стать тем, кто не просто бросит вызов тьме, но и, возможно, зажжёт первый луч надежды на возвращение домой?
#
#'''
print(histori)
# игра
equipment = []
weapon = []
lvlfloor = 1
countroom = 0
end = 0
lvlplayer = 1
lvlpr = 0
pointr = 0
PrCharacteristics(player)
while player['ЗДОРОВЬЕ'] > 0:
    print(f'пройдено {countroom}')
    if end == 4:
        print("Конец(:")
        break
    if lvlpr == 100:
        playerup()
        lvlpr = 0
        PrCharacteristics(player)

    if countroom >= 9:
        floor()
        end += 1
        countroom = 0

    roomd = roomlvl1()
    if roomd[0] == "???":
        roomd[0] = view[randint(0, 20)]

    if roomd[0] == 'монстров':
        print('Вы вошли в комнату монстров')
        fight(lvlfloor)
        if player['ЗДОРОВЬЕ'] <= 0:
            continue
        rn = randint(1, 100)
        if 75 <= rn:
            iven()
        PrCharacteristics(player)
        countroom += 1
    elif roomd[0] == 'отдыха':
        print('Вы вошли в комнату отдыха')
        xl = roomchil()
        if player['ЗДОРОВЬЕ'] + xl > mxhp:
            player['ЗДОРОВЬЕ'] = mxhp
        else:
            player['ЗДОРОВЬЕ'] += xl
        PrCharacteristics(player)
        countroom += 1
    elif roomd[0] == 'сокровищь':
        print('Вы вошли в комнату сокровищь')
        iven()
        prinvetory()
        PrCharacteristics(player)
    elif roomd[0] == 'ловушек':
        damages = roomtrap(lvlfloor)
        print('Вы вошли в комнату ловушек')
        print(f'Вы потеряли {damages} здоровья')
        player['ЗДОРОВЬЕ'] -= damages
        if player['ЗДОРОВЬЕ'] <= 0:
            continue
        PrCharacteristics(player)
        countroom += 1
    
    while True:
        print('Что будите делать дальше?', '1 - посмотреть ивентарь', '2 - очистить ивентарь', '3 - прокачать навыки', '4 - пойти дальше')
        var = input('Введите ваш выбор_')
        if var == '1':
            prinvetory()
        elif var == '2':
            popinvetory()
        elif var == '3':
            upppoint()
        elif var == '4':
            break
        else:
            print('Введите корректно свой выбор!')