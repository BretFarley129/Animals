class Animal(object):
    def __init__(self, name):
        self.name = name
        self.health = 40

    def walk(self):
        print "WakaWakaWaka"
        self.health -= 1
        return self
    
    def run(self):
        print "WANANANA"
        self.health -= 5
        return self

    def displayHealth(self):
        print "Health: {}\n".format(str(self.health))

class Dog(Animal):
    def __init__(self, name):
        super(Dog, self).__init__(name)
        self.health = 150
    
    def pet(self):
        print "WHOS A GOOD BOY\n"
        self.health +=5

class Dragon(Animal):
    def __init__(self, name):
        super(Dragon, self).__init__(name)
        self.health = 170
    
    def fly(self):
        print "flapflapflap\n"
        self.health -= 10

    def displayHealth(self):
        super(Dragon,self).displayHealth()
        print self.health
        print "i am a dragon.\n"

frog = Animal("kermit")
frog.displayHealth()
frog.walk()
frog.run()
frog.displayHealth()

spike = Dog("spike")
spike.displayHealth()
spike.walk()
spike.displayHealth()
spike.pet()
spike.displayHealth()

trogdor = Dragon("Trogdor")
trogdor.displayHealth()
trogdor.walk()
trogdor.displayHealth()
trogdor.fly()
trogdor.displayHealth()

#These do not work
#frog.fly()
#frog.pet()
#spike.fly()
