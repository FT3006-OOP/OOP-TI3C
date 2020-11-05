class Hero:

    # class variable 
    jumlah = 0
    __privateJumlah = 0

    def __init__(self,name,health):
        self.name = name
        self.health = health

        # variable intance private
        self.__private = "private"
        # variable intance protected
        self.__protected = "protected"

Agung = Hero("Agung", 100)

print(Agung.__dict__)
print(Hero.__dict__)
print(Hero.__privateJumlah)
