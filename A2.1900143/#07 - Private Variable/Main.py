class Hero:

    # class Variabel
    jumlah = 0
    __privateJumlah = 0

    def __init__(self,name,health):
        self.name = name
        self.health = health

        # Variabel Instance Private
        self.__private = "private"
        # Variabel Instance Protected
        self._protected = "protected"


lina = Hero("lina",100)

print(lina.__dict__)
print(Hero.__dict__)
print(Hero.__privateJumlah)