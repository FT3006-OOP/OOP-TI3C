class Hero: #template
    pass


hero1 = Hero() # object / instance (instansiate)
hero2 = Hero()
hero3 = Hero();

hero1.name = "heri"
hero1.health = 2000

hero2.name = "dante"
hero2.health = 2000

hero3.name = "vergil"
hero3.health = 1000

print(hero1)
print(hero1.__dict__)
print(hero1.name)