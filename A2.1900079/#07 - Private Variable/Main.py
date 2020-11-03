class Hero:

        # class variabel
        jumlah = 0
        __privatejumlah = 0

        def __init__(self,name,health):
            self.name = name
            self.health = health

            # variable instance private
            self.__private = "private"
            # variabel instance protected
            self.__protected = "protected"



lina = Hero("lina",100)

print(lina.__dict__)
print(Hero.__dict__)
print(Hero.__privateJumlah)