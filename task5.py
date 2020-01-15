class Soldier():
    def __init__(self, name):
        self.name = name

class Guns():
    def __init__(self, model):
        self.model = model
        self.bullets = 30

    def fire(self):
        for i in range(self.bullets, -1, -1):
            print(i)
            self.bullets -= 1
        print("empty need reload")

    def reload(self):
        self.bullets = 30
        print("Перезарядил")

    def again(self):
        self.fire()
        self.reload()
        self.fire()

class Act_of_shooting(Soldier, Guns):
    def __init__(self, name, model):
        Soldier.__init__(self, name)
        Guns.__init__(self, model)


Warrior = Act_of_shooting("Ryan", "AK47")
Warrior.again()