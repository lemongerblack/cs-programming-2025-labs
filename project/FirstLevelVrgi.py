from random import randint
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
        if (playeratack > self.Defense) and (self.HP - damage != 0):
            self.HP = self.HP - damage
        elif (playeratack > self.Defense) and (self.HP - damage <= 0):
            self.HP = 0
            print("Вы отдалели эту тварь!")
        else:
             print("Вы начинаете атаковать и, к сожаление промахиваетесь")

Monstors1 = [{'ИМЯ': 'багбир', 'СТАТЫ': [20, 20, 7, 13, 7]}, {'ИМЯ': 'темная-слизь', 'СТАТЫ': [10, 11, 5, 15, 4]},
             {'ИМЯ': 'нисшая-тень', 'СТАТЫ': [16, 20, 6, 20, 5]}, {'ИМЯ': 'грязевой-монстр', 'СТАТЫ': [14, 14, 10, 5, 5]},
             {'ИМЯ': 'скелет', 'СТАТЫ': [13, 15, 13, 20, 4]}, {'ИМЯ': 'нисший-демон', 'СТАТЫ': [22, 21, 8, 3, 6]}]
Monstors2 = []
Monstors3 = []