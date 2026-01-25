from random import randint
class mon1:
    def __init__(self, HP, Attack, Defense, Agility, Damage):
        self.HP = HP
        self.Attack = Attack
        self.Defense = Defense
        self.Agility = Agility
        self.Damage = Damage

    def Attacks(self, player, evade):
        kick = randint(1, 20)
        damager = randint(1, self.Damage)
        if ((kick + (self.Attack // 10)) > player["ЗАЩИТА"]) or ((kick + (self.Attack // 10)) > evade):
            player["ЗДОРОВЬЕ"] = player["ЗДОРОВЬЕ"] - damager
            print(f"Вы получили - {damager} урона")
        else:
            print("Вы избежали урона! Это отличный шанс!")
    
    def TakingDamage(self, playeratack, damage):
        if (playeratack > self.Defense) and (self.HP - damage != 0):
            self.HP = self.HP - damage
        elif self.HP - damage <= 0:
            self.HP = 0
            print("Вы отдалели эту тварь!")
        else:
             print("Вы начинаете отаковать и, к сожаление промахиваетесь")

def mong():
    return Monstors1[randint(0, 5)]

Monstors1 = {'багбир': [20, 20, 7, 13, 7], 'темная-слизь': [10, 11, 5, 15, 4], 'нисшая-тень': [16, 20, 6, 20, 5],
              'грязевой-монстр': [14, 14, 10, 5, 5], 'скелет': [13, 15, 13, 20, 4], 'нисший-демон': [22, 21, 8, 3, 6]}
Monstors2 = {}
Monstors3 = {}