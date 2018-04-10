from wheels import Wheels

class Car:

    num_of_cars = 0

    def __init__(self,theChassis,theWheels,theFuel,theEngine,theTransmission,theColour,theMax):
        self.engine = theEngine
        self.wheels = theWheels
        self.chassis = theChassis
        self.transmission = theTransmission
        self.fuel = theFuel
        self.isOn = False
        self.speed = 0
        self.age = 0
        self.hodometre = 0
        self.colour = theColour
        self.maxSpeed = theMax


    def __str__(self):
        newString = ""


        newString += self.colour + " "
        newString += self.chassis + " " + str(self.hodometre) + " "
        newString += str(self.transmission)

        return newString

    def getHodometre(self):
        return self.hodometre

    def getAge(self):
        return self.age

    def getSpeed(self):
        return self.speed

    #A method to increase/decrease speed. Time is in seconds
    #Amount is the speed increase per second in km/h
    def accelerate(self,time,amount):
        i = 0

        #increase speed as time X amount
        while i < time:
            self.speed += amount
            if (self.speed >= self.maxSpeed):
                self.speed = self.maxSpeed
                break
            i += 1


newTreds = Wheels()
newTreds.changeTire(0,10)
newTreds.changeTire(1,10)
newTreds.changeTire(2,10)
newTreds.changeTire(3,10)
lancer = Car("lancer",newTreds,"LPG","2L","Auto","Burgandy",145)
print(lancer)
lancer.accelerate(10,20)
print(lancer.getSpeed())
print(lancer.wheels)
newTreds.changeTire(0,-1)
print(lancer.wheels)