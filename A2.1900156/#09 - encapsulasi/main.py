class Hero:

    def __init__(self,name,health,attackPower):
        self.__name = name
        self.__health = health
        self.__attPower = attackPower

    # getter
    def getName(self):
        return self.__name

    def getHealth(self):
        return self.__health

    # setter

    def diserang(self,serangPower):
        self.__health -= serangPower

    def setAttPower(self,nilaibaru):
        self.__attPower = nilaibaru

# permulaan dari game
earthspirit = Hero("Earth Spirit",50, 5)

# game running

print(earthspirit.getName())
print(earthspirit.getHealth())
earthspirit.diserang(5)
print(earthspirit.getHealth())