class Hero:

        def __init__(self, name, health, attackpower):
            self.__name = name
            self.__health = health
            self.__attpower = attackpower

        # getter
        def getName(self):
            return self.__name

        def getHealth(self):
            return self.__health

        # setter
        def diserang(self,serangPower):
            self.__health -=serangPower

        def settAttPower(self,nilaibaru):
            self.__attPower = nilaibaru

# awal dari game
earthshaker = Hero("earthshaker",50,5)

# game berjalan
print(earthshaker.getName())
print(earthshaker.getHealth())
earthshaker.diserang(5)
print(earthshaker.getHealth())