class Hero: #template
    pass

hero1 = Hero() #object
hero2 = Hero()
hero3 = Hero()

hero1.name = "nandi"
hero1.health = 1000

hero2.name = "juned"
hero2.health = 2000

hero3.name = "boy"
hero3.health = 3000

print(hero1)
print(hero1.__dict__)
print(hero1.name)