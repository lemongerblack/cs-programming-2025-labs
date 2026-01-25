from random import randint

def СreatingСharacteristics():
    name = input('введите имя персонажа_')
    flag = True
    print('Выберите расу', '===============', '1 - человек', '2 - эльф', '3 - дворф', sep='\n')
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
s = {'b': 1, 'a': 3}
print(s[2])