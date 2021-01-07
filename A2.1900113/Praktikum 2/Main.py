class Hero :
    pass


hero1 = Hero()
hero2 = Hero()
hero3 = Hero();

hero1.name  = "sniper"
hero1.health = 100

hero2.name = "sven"
hero2.health = 200

hero3.name = "dzikri"
hero3.health = 999

print(hero1)
print(hero1.__dict__)
print(hero1.name)

print(hero2)
print(hero2.__dict__)
print(hero2.name)

print(hero3)
print(hero3.__dict__)
print(hero3.name)