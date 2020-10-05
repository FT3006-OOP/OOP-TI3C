class Hero: #template
    pass

hero1 = Hero() #object
hero2 = Hero()
hero3 = Hero()

hero1.name ="zilong"
hero1.health = 100

hero2.name ="alucard"
hero2.health = 500

hero3.name ="miya"
hero3.health = 1000

print(hero1)
print(hero1.__dict__)
print(hero1.name)