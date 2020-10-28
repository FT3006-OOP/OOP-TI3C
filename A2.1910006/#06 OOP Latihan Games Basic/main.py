class Hero:

    def __init__(self,name,health,attackPower,armorNumber):
        self.name = name
        self.health = health
        self.attackPower = attackPower
        self.armorNumber = armorNumber

    def attack(self, opponent):
        print(self.name + ' attack ' + opponent.name )
        opponent.attacked(self, self.attackPower)

    def attacked(self, opponent, attackPower_opponent):
        print(self.name + ' attack ' + opponent.name )
        attack_received = attackPower_opponent/self.armorNumber
        print(' attack received : ' + str(attack_received))
        self.health -=attack_received
        print(' health : ' + ' tersisa ' + ' str(self.health')

Hachi = Hero('Hachi',100,10,5)
Metmet = Hero('Metmet',100,10,10)

Hachi.attack(Metmet)
print("\n")
Metmet.attack(Hachi)
print("\n")