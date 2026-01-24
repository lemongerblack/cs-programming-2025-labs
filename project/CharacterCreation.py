from random import randint
def СreatingСharacteristics():
    name = input('введите имя персонажа_')
    print('Выберите расу', '===============', '1 - человек', '2 - эльф', '3 - дворф', sep='\n')
    while True:
        n = input('введите ваш выбор_')
        if n == '1':
            HP = randint(20, 35)
            Attack = randint(20, 30)
            Defense = randint(10, 15)
            Agility = randint(20, 25)
            Attentiveness = randint(10, 20)
            Height = randint(152, 184)
            Weight = Height - 90
            return {'name': name, 'r': 'ЧЕЛОВЕК','hp': HP, 'at': Attack, 'def': Defense, 'agl': Agility, 'att': Attentiveness, 'hei': Height, 'wei': Weight}
            break
        elif n == '2':
            HP = randint(20, 30)
            Attack = randint(15, 30)
            Defense = randint(13, 15)
            Agility = randint(30, 35)
            Attentiveness = randint(10, 20)
            Height = randint(150, 185)
            Weight = Height - 100
            return {'name': name, 'r': 'ЭЛЬФ','hp': HP, 'at': Attack, 'def': Defense, 'agl': Agility, 'att': Attentiveness, 'hei': Height, 'wei': Weight}
            break
        elif n == '3':
            HP = randint(30, 45)
            Attack = randint(25, 35)
            Defense = randint(13, 15)
            Agility = randint(15, 19)
            Attentiveness = randint(13, 20)
            Height = randint(122, 152)
            Weight = Height - 75
            return {'name': name, 'r': 'ДВОРФ','hp': HP, 'at': Attack, 'def': Defense, 'agl': Agility, 'att': Attentiveness, 'hei': Height, 'wei': Weight}
            break
        else:
            print("ОШИБКА: выберите число от 1 до 3, чтобы выбрать расу")
print(СreatingСharacteristics())