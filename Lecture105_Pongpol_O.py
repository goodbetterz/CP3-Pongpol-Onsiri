# class หลัก
class Vehicle:
    licenseCode = ""
    serialCode = ""
    def turnOnAirConditioner(self):
        print("Turn on Air")

class Car(Vehicle): # class ลูก
    def sayHello(self):
        print("Hello World")

class PickUp(Vehicle):
    pass

class Van(Vehicle):
    pass

class EstateCar(Vehicle):
    pass

car1 = Car()
car1.turnOnAirConditioner()
car1.sayHello()

pickup1 = PickUp()
pickup1.turnOnAirConditioner()

van1 = Van()
van1.turnOnAirConditioner()

estatecar1 = EstateCar()
estatecar1.turnOnAirConditioner()