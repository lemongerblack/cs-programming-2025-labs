from Game import *
from Items import *

iventory = {'1': [], '2': [], '3': [], '4': [], '5': []}
equipment = []
weapon = []

def prinvetory():
    print(f"Ваш ивентарь - {iventory}", f"Ваша экиперовка - {equipment}", f"Ваше оружие - {weapon}", sep='\n', end='\n', flush=True, delay=0.1)

def use():
    while True:
        var = input("Выберите какой предмет вы хотите использовать_ ")
        try:
            if len(iventory[var]) > 0:
                if 'a' in iventory[var][0]:
                    if iventory[var][0]['a'] + player['ЗДОРОВЬЕ'] <= mxhp:
                        player['ЗДОРОВЬЕ'] = player['ЗДОРОВЬЕ'] + iventory[var][0]['a']
                        iventory[var] = []
                        prinvetory()
                    else:
                        player['ЗДОРОВЬЕ'] = mxhp
                        iventory[var] = []
                        prinvetory()
                elif 'b' in iventory[var][0]:
                    if len[equipment] == 0:
                        equipment.append(iventory[var][0])
                        player['ЗАЩИТА'] = player['ЗАЩИТА'] + iventory[var][0]['b']
                        iventory[var] = []
                        prinvetory()
                    else:
                        print(f"Вы хотите поменять {equipment[0]} на {iventory[var][0]}", "1 - Да", "2 - нет", sep="\n", end="\n", flush=True, delay=0.1)
                        while True:
                            playerotv = input("Введите ваш вариант")
                            if playerotv == '1':
                                equipment = [iventory[var][0]]
                                player['ЗАЩИТА'] = mxdef + iventory[var][0]['b']
                                iventory[var] = []
                                prinvetory()
                                break
                            elif playerotv == '2':
                                break
                            else:
                                print("Выберите возможный вариант 1 или 2")
                elif 'c' in iventory[var][0]:
                    if len[weapon] == 0:
                        weapon.append(iventory[var][0])
                        player['СИЛА_АТАКИ'] = player['СИЛА_АТАКИ'] + iventory[var][0]['c'][0]
                        iventory[var] = []
                        prinvetory()
                    else:
                        print(f"Вы хотите поменять {weapon[0]} на {iventory[var][0]}", "1 - Да", "2 - нет", sep="\n", end="\n", flush=True, delay=0.1)
                        while True:
                            playerotv = input("Введите ваш вариант")
                            if playerotv == '1':
                                weapon = [iventory[var][0]]
                                player['СИЛА_АТАКИ'] = mxatt + iventory[var][0]['c'][0]
                                iventory[var] = []
                                prinvetory()
                                break
                            elif playerotv == '2':
                                break
                            else:
                                print("Выберите возможный вариант 1 или 2")
                elif 'd' in iventory[var][0]:
                    pass
        except:
            pass 