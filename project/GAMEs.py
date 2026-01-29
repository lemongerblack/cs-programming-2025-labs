from random import randint

# Функция для интересного вывода текста
def print(*text, sep="\n", end="\n", flush=True, delay=0.005):
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
    player['ЗДОРОВЬЕ'] += 5 * lvlplayer
    player['ЗАЩИТА'] += 1 + lvlplayer
    mxhp += 5
    mxdef += 1
# Функция для печати выбора действий
def praction():
    print('Выберите действие:', '==================', '1 - Атаковать', '2 - Использовать предмет',
          '3 - Оскорбить монстра', '4 - Попробовать проскочить мимо него', '5 - Осмотреться')
# Функция для проведения боя с монстрами
def fight(lvlfloor):
    global pointr
    global lvlpr
    for _ in range(1, randint(2, 4)):
        if player['ЗДОРОВЬЕ'] <= 0:
            continue
        monstor = roommon()
        print(f'Впереди вас {monstor.Name}, пока вас не обнаружили, ваши действия?')
        v = 0
        while (monstor.HP > 0) and player['ЗДОРОВЬЕ'] > 0:
            print(f'Ваше здоровье {player['ЗДОРОВЬЕ']}, здоровье врага {monstor.HP}')
            praction()
            while True:
                varplayer = input('Введите ваш вариант_')
                if varplayer not in ['1', '2', '3', '4', '5']:
                    print('Выберите один из четырех вариантов!')
                else:
                    break
            if varplayer == '1':
                kickplayer = randint(1, 20) + (player['СИЛА_АТАКИ'] // 10) + lvlplayer
                if len(weapon) > 0:
                    damage = 6 + weapon[0]['c'] + (player['СИЛА_АТАКИ'] // 10) + v + lvlplayer
                else:
                    damage = 6 + (player['СИЛА_АТАКИ'] // 10) + v + lvlplayer
                print(f'Ваша значение атаки {kickplayer}, значение защиты у врага {monstor.Defense}')
                monstor.TakingDamage(kickplayer, damage)
            elif varplayer == '2':
                prinvetory()
                use(player, monstor)
            elif varplayer == '3':
                fc = input("Ну давай_")
                morkick = randint(1, 20) + (player['СИЛА_АТАКИ'] // 10) + (player['ВНИМАТЕЛЬНОСТЬ'] // 10) + v + lvlplayer  
                damag = 3 + lvlplayer
                monstor.TakingDamage(morkick, damag)
                print('Не важно был ли нанесен урон. Знай это было подло... ')
            elif varplayer == '4':
                attemptplayer = randint(1, 20) + (player['ЛОВКОСТЬ'] // 10) + lvlplayer
                attemmonstors = randint(1, 20) + (monstor.Agility // 10) + lvlfloor
                if attemptplayer > attemmonstors:
                    print("Вы успешно проскачили мимо него")
                    player['ЛОВКОСТЬ'] -= (2 + lvlfloor)
                    print(f'ваша ЛОВКОСТЬ была уменьшина на {2 + lvlfloor}')
                    monstor.HP = 0
                else:
                    print(f'К сожалению {monstor.Name} не пропускает вас')
                    player['ЛОВКОСТЬ'] -= 1
                    print('ваша ЛОВКОСТЬ была уменьшина на 1')
            elif varplayer == '5':
                inspection = randint(1, 20) + player['ВНИМАТЕЛЬНОСТЬ']
                if (inspection > monstor.Defense) and (v == 0):
                    v = 2 + (player['ВНИМАТЕЛЬНОСТЬ'] // 10)
                    print(f'Вы нашли слабое место соперника, теперь ваш урон по нему увеличен на {v}!')
                    player['ВНИМАТЕЛЬНОСТЬ'] -= (3 + lvlfloor)
                    print(f'Ваша Внимательность была уменьшина на {3 + lvlfloor}')
                else:
                    player['ВНИМАТЕЛЬНОСТЬ'] -= 1
                    print('Ваша Внимательность была уменьшина на 1')

            if monstor.HP > 0:
                print('Монстр атакует!')
                monstor.Attacks(player, 0)
        print('Вы одалели эту тварь!')
    else:
        print('Вы прошли комнату!')
        pointr += 6 + (lvlfloor * 2)
        lvlpr += 6 + (lvlfloor * 2)
    
# Функция для создания персонажа
def СreatingСharacteristics():
    name = input('введите имя персонажа_')
    r = {'1': 'ЧЕЛОВЕК', '2': 'ЭЛЬФ', '3': 'ДВОРФ'}
    s = {'1': [randint(20, 35), randint(20, 30), randint(10, 15), randint(20, 25), randint(10, 20), randint(152, 184), randint(60, 90)],
         '2': [randint(20, 30), randint(15, 30), randint(13, 15), randint(30, 35), randint(10, 20), randint(150, 185), randint(60, 90)],
         '3': [randint(30, 45), randint(25, 35), randint(13, 15), randint(15, 19), randint(13, 20), randint(122, 152), randint(50, 80)]}
    print('Выберите расу', '===============', '1 - человек', '2 - эльф', '3 - дворф')
    while True:
        n = input('введите ваш выбор_')
        if (n == '1') or (n == '2') or (n == '3'):
            return {'ИМЯ': name, 'РАСА': r[n],'ЗДОРОВЬЕ': s[n][0], 'СИЛА_АТАКИ': s[n][1], 'ЗАЩИТА': s[n][2],
                     'ЛОВКОСТЬ': s[n][3], 'ВНИМАТЕЛЬНОСТЬ': s[n][4], 'РОСТ': s[n][5], 'ВЕС': s[n][6]}
            break
        else:
            print("ОШИБКА: выберите число от 1 до 3, чтобы выбрать расу")
# функция для прокачки
def upppoint():
    global pointr
    print(f'Ваши очки опыта {pointr}')
    sp = ['СИЛА_АТАКИ', 'ЛОВКОСТЬ', 'ВНИМАТЕЛЬНОСТЬ']
    print('какие характеристики можно прокачать:', '1 - СИЛА_АТАКИ', '2 - ЛОВКОСТЬ', '3 - ВНИМАТЕЛЬНОСТЬ')
    while True:
        varr = input('Ваш выбор и через пробел сколько очков_').split()
        try:
            if pointr - int(varr[1]) >= 0:
                player[sp[int(varr[0]) - 1]] += int(varr[1])
                pointr -= int(varr[1])
                break
            elif pointr == 0:
                print('У вас нет очков опыта, чтобы прокачать навыки')
                break
            else:
                print('у вас столько очков нет!')
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
# функция для атаки игрока
    def Attacks(self, player, evade):
        kick = randint(1, 20)
        damager = randint(self.Damage // 2, self.Damage)
        if (evade > 0) and ((kick + (self.Attack // 10)) > evade):
            player["ЗДОРОВЬЕ"] = player["ЗДОРОВЬЕ"] - damager
            print(f"Вы получили - {damager} урона")
        elif ((kick + (self.Attack // 10)) > player["ЗАЩИТА"]):
            player["ЗДОРОВЬЕ"] = player["ЗДОРОВЬЕ"] - damager
            print(f"Вы получили - {damager} урона")
        else:
            print("Вы избежали урона! Это отличный шанс!")
# функция для атаки на монстра
    def TakingDamage(self, playeratack : int, damage : int):
        global pointr
        global lvlpr
        if (playeratack >= self.Defense) and (self.HP - damage != 0):
            self.HP = self.HP - damage
            print(f'Вы нанесли {damage} урона!')
            player['СИЛА_АТАКИ'] -= (1 + lvlfloor)
            print(f'Ваша СИЛА_АТАКИ была уменьшина на {1 + lvlfloor}')
        elif (playeratack >= self.Defense) and (self.HP - damage <= 0):
            self.HP = 0
            player['СИЛА_АТАКИ'] -= (1 + lvlfloor)
            print(f'Ваша СИЛА_АТАКИ была уменьшина на {1 + lvlfloor}')
            pointr += (lvlfloor) + 3
            lvlpr += (lvlfloor) + 3
        else:
             print("Вам к сожалению не удается нанести урон...")
             player['СИЛА_АТАКИ'] -= 1
             print(f'Ваша СИЛА_АТАКИ была уменьшина на 1')
# функции определения комнат
# функция для создания монстра в комнате
def roommon():
    n = []
    n.append(eval(f'Monstors{str(lvlfloor)}[randint(0, 5)]'))
    return mon1(n[0]['ИМЯ'], n[0]['СТАТЫ'][0], n[0]['СТАТЫ'][1], n[0]['СТАТЫ'][2], n[0]['СТАТЫ'][3], n[0]['СТАТЫ'][4])
# функция для комнаты отдыха, которая возращает число, которое восстановит здоровье игроку на то число
def roomchil():
    return randint(5, 20)
# функция для комнаты сокровищь, возращает рандомный предмет
def roomgold():
    return abcde[randint(0, 4)][randint(0, 4)]
# функция для комнаты ловушек, возращает сколько игрок получит урона
def roomtrap(lvlf):
    return randint(1, 5 * lvlf)
# функция для определения комнаты
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
            print("Введите выринт из указанных")
# ивентарь и функции для ивенторя
iventory = {'1': [], '2': [], '3': [], '4': [], '5': []}
# функция для вывода ивенторя, экиперовки и оружия
def prinvetory():
    print('ваш ивентарь')
    for i in range(1, 6):
        if iventory[str(i)] != []:
            print(f'{i} {iventory[str(i)][0]['name']}')
        else:
            print(f'{i} {iventory[str(i)]}')
    if equipment == []:
        print(f"Ваша экиперовка - {equipment}")
    else:
        print(f"Ваша экиперовка - {equipment[0]['name']}")
    if weapon == []:
        print(f"Ваше оружие - {weapon}")
    else:
        print(f"Ваше оружие - {weapon[0]['name']}")
# функция для очистки ивентаря
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
# функция подбора предметов
def iven():
    n = roomgold()
    print(f'Вы нашли {n['name']}')
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
# функция для использования лечебных предметов
def ause(var):
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
# функция для экиперования брони
def buse(var):
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
# функция для экиперования оружия
def cuse(var):
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
# функция для использования метательных расходников
def duse(var, monstor):
    monstor.HP = monstor.HP - iventory[var][0]['d']
    print(f"Вы нанесли {iventory[var][0]['d']} урона")
    iventory[var] = []
# функция для переработки драгоценностей в очки опыта
def euse(var):
    global pointr
    global lvlpr
    pointr += iventory[var][0]['e']
    lvlpr += iventory[var][0]['e']
    print(f'Ваше золото переработано в {iventory[var][0]['e']} очков')
    iventory[var] = []
# общая функция которая использует предметы из ивентаря вызывая другие функции
def use(player, monstor):
    while True:
        var = input("Выберите какой предмет вы хотите использовать_ ")
        try:
            if len(iventory[var]) > 0:
                if 'a' in iventory[var][0]:
                    ause(var)
                elif 'b' in iventory[var][0]:
                    buse(var)
                elif 'c' in iventory[var][0]:
                    cuse(var)
                elif 'd' in iventory[var][0]:
                    duse(var, monstor)
                elif 'e' in iventory[var][0]:
                    euse(var)
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

Monstors3 = [{'ИМЯ': 'высший-демон', 'СТАТЫ': [55, 44, 15, 33, 11]}, {'ИМЯ': 'высшая-тень', 'СТАТЫ': [40, 37, 13, 33, 10]},
             {'ИМЯ': 'огр', 'СТАТЫ': [31, 23, 7, 7, 7]}, {'ИМЯ': 'голем', 'СТАТЫ': [52, 44, 17, 22, 12]},
             {'ИМЯ': 'живая-броня', 'СТАТЫ': [66, 33, 19, 33, 6]}, {'ИМЯ': 'демон', 'СТАТЫ': [38, 30, 10, 11, 9]}]
# виды комнат
view = ['монстров', 'монстров', 'монстров', 'монстров', 'монстров',
        'монстров', 'монстров', 'монстров', 'монстров', 'монстров',
        'отдыха', 'сокровищь', 'сокровищь', 'ловушек', 'ловушек',
        'ловушек', '???', '???', '???', '???', '???']
# предметы
ahilsitems = [{'name': 'МалоеЗельеЛечения', 'a': 3}, {'name': 'ЗельеЛечения', 'a': 5}, {'name': 'БольшоеЗельеЛечения', 'a': 10},
              {'name': 'ЦелебныйГриб', 'a': 2}, {'name': 'БольшойЦелебныйГриб', 'a': 3}]

barmorPlus = [{'name': 'КожанныйДоспех', 'b': 2}, {'name': 'ПроклёпанныйКожаныйДоспех', 'b': 3}, {'name': 'ЧешуйчатыйДоспех', 'b': 4},
              {'name': 'Кольчуга', 'b': 5}, {'name': 'Латы', 'b': 6}]

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

Здесь, в лабиринтах пещер и величественных подземных полостях, родилось Царство Последнего Очага — оплот человечества, названный так в честь неугасимого пламени надежды, что горит в его сердцевине. Веками люди отбивали яростные атаки тварей у своих укреплённых врат. Битва длится и по сей день; каждый день добывается дорогой ценой, и никто не знает, сколько ещё хватит сил.

Вы — дитя подземелий. Для вас солнечный свет — лишь древняя легенда, а свежий ветер и пение птиц — чуждые понятия из забытых сказок. Но в вашей душе тлеет неугасимое любопытство. Оно и привело вас к роковому решению: пробиться наверх. Не для славы, а чтобы своими глазами увидеть мир, который у вас украли. Чтобы узнать, можно ли его отвоевать.

Готовы ли вы стать тем, кто не просто бросит вызов тьме, но и, возможно, зажжёт первый луч надежды на возвращение домой?

'''

continues = '''Путь наверх оказался долгим и смертельно опасным. Вы пробирались через забытые тоннели, миновали заставы, где столетиями не ступала нога человека, и сражались с тенями, что цеплялись за ваши пятки. Воздух менялся: тяжёлый, спёртый запах камня и плесени постепенно уступал место новым, незнакомым ароматам — сырости, гниению и чему-то неописуемо свежему.

И вот, когда силы были уже на пределе, вы увидели свет. Не жёлтое мерцание факелов или багровое зарево подземной магмы, а холодный, рассеянный, но живой свет. Он струился из-за груды обломков, преграждавших путь к последней расщелине. Сердце заколотилось в груди, и, забыв об усталости, вы начали растаскивать камни.

С последним усилием вы протиснулись сквозь узкий проход — и мир обрушился на вас.

Сначала воздух. Он был таким резким, таким полным, что вы закашлялись. Он обжигал лёгкие своей свободой и странными запахами — влажной земли, цветущей где-то вдали полыни, железа и вечной пыли.

Затем пространство. Вы привыкли к давящим сводам пещер и тесным улицам Последнего Очага. А здесь… Здесь не было потолка. Только бескрайний, серо-пепельный купол небес, простирающийся в бесконечность. От этого голова закружилась, и вы непроизвольно прислонились к скале, чувствуя себя букашкой на ладони гиганта.

И, наконец, мир. Тот самый, о котором слагали легенды. Но это была не прекрасная страна из сказок. Перед вами простиралась Великая Пустошь. Бесплодные земли, покрытые пеплом и остовами мёртвых деревьев, уходили к горизонту. Извилистые трещины в земле, те самые разломы, сочились тусклым багровым светом и клубами ядовитого пара. Вдали, в мареве, маячили силуэты руин — склепы того, что когда-то было городами. И повсюду, в этом безмолвии, чувствовалось присутствие. Чуждое, враждебное. Вы были не одни. Вся эта земля дышала тихой, древней угрозой.

Но в разрыве тяжёлых туч на миг пробился луч. Он коснулся вашего лица — теплое, почти невесомое прикосновение, о котором вы знали лишь по книгам. Это было Солнце. Первый луч за триста лет, упавший на лицо живого человека из подземного царства.

Страх и благоговение смешались в груди. Путь назад был забыт. Вы ступили на проклятую землю. Вы стали глазами своего народа и щитом, направленным против тьмы. Легенда закончилась. Теперь начинается ваша история.

Судьба двух миров теперь лежит на ваших плечах. Осмелитесь ли вы сделать следующий шаг?'''

# игра
print(histori)
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
        print(continues)
        break
    if lvlpr >= 30 * lvlplayer:
        playerup()
        lvlpr = 0
        PrCharacteristics(player)

    if countroom >= 6:
        floor()
        print('Вы поднялись на этаж выше!')
        pointr += 25 * (lvlfloor - 1)
        lvlpr += 25 * (lvlfloor - 1)
        end += 1
        countroom = 0

    roomd = roomlvl1()
    if roomd[0] == "???":
        roomd[0] = view[randint(0, 20)]

    if roomd[0] == "???":
        roomd[0] = view[13]

    if roomd[0] == 'монстров':
        print('Вы вошли в комнату монстров')
        fight(lvlfloor)
        if player['ЗДОРОВЬЕ'] <= 0:
            continue
        rn = randint(1, 100)
        if 65 <= rn:
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
        countroom += 1
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
else:
    print('Но к сожалению вы мертвы!')