class Hero:
    #class variabel
    jumlah_hero = 0

    def __init__ (self, inputName, InputHealth, InputPower, InputArmor):
        #intance variabel
        self.name = inputName
        self.health = inputHealth
        self.power = inputPower
        self.armor = innputArmor
        Hero.jumlah_hero += 0

    # void function, method tanpa return, tanpa argumen
    def siapa(self):
        print("nama adalah " + self.nama)

    # method dengan argumen, tanpa return
    def healthUp(self,up):
        self.health += up
    
    # method dengan return
    def getHealth(self):
        return self.health

hero1 = Hero('sniper', 100, 10, 5)
hero2 = Hero('mario bros', 90, 5, 10)

hero1.siapa()
hero1.healthUp(10)

print(hero1.getHealth())
