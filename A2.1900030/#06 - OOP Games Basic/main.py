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
        print(self.name + ' attacked ' + opponent.name)
        attack_received = attackPower_opponent/self.armorNumber
        print(' attack received : ' + str(attack_received))
        self.health -= attack_received
        print(' health : ' + self.name + ' tersisa ' + str(self.health))

naruto = Hero('naruto',100,10,5)
sasuke = Hero('sasuke',100,20,10)

naruto.attack(sasuke)
print("\n")
sasuke.attack(naruto)
print("\n")
