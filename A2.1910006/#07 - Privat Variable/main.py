class Hero:

    # class variabel
    jumlah = 0
    __privatejumlah = 0

    def __init__(self,name,health):
        self.name = name 
        self.health = health

        # variabel instance private
        self.__private = "private"
        #variabel instance protected
        self._protected = "protected"



Metmet = Hero("Metmet",100)

print(Metmet.__dict__)
print(Hero.__dict__)
print(Hero.__privatejumlah)