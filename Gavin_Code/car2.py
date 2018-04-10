from wheels2 import Wheels

class Car:

    def __init__(self,theChassis,theEngine,theWheels,theColour,theSeats,theDoors,theTransmission,theFuel,theMax):
        self.engine = theEngine
        self.wheels = theWheels
        self.colour = theColour
        self.chassis = theChassis
        self.seats = theSeats
        self.door = theDoors
        self.fuel = theFuel
        self.plate = ""
        self.transmission = theTransmission
        self.speed = 0
        self.odometre = 0
        self.age = 0
        self.maxSpeed = theMax

    def getSpeed(self):
        return self.speed

    def getMaxSpeed(self):
        return self.maxSpeed

    def __str__(self):

        return self.chassis + " " + str(self.odometre)


    #increase the speed of car by time X amount km/h
    #time is in seconds, thus an integer
    #amount is in km/h
    def accelerate(self,time,amount):
        i = 0

        while i < time:
            self.speed += amount
            if self.getSpeed() > self.getMaxSpeed():
                self.speed = self.getMaxSpeed()
                break
            i += 1

def main():
    tyres = Wheels()
    tyres.changeTyre(0, "10")
    tyres.changeTyre(1, "10")
    tyres.changeTyre(2, "10")
    tyres.changeTyre(3, "6")

    gavinCar = Car("lancer","2L",tyres,"Burgandy","5","4","Auto","Petrol",145)
    gavinCar.odometre = "204000"
    print(gavinCar)
    gavinCar.accelerate(10,5)

    print(gavinCar.wheels)

    print(gavinCar.speed)

    gavinCar.accelerate(10,-5)

    print(gavinCar.speed)

if __name__ == "__main__":
    main()
