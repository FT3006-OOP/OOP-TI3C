class Hero:

    # class variabel
    jumlah = 0
    __privateJumlah = 0

    def __init__(self,name,health):
        self.name = name
        self.health = health

        # variabel instance private
        self.__private = "private"
        # variabel instance protected
        self._protected = "protected"


berseker = Hero("berseker",100)

print(berseker.__dict__)
print(berseker.__dict__)
print(Hero.__privateJumlah)
