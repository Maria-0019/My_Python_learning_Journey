class Car:
    @staticmethod
    def start():
        print("car started..")

    
    @staticmethod
    def stop():
        print("car stopped..")

class ToyotaCar(Car):
    def __init__(self,brand,type):
        self.brand= brand
        self.type= type

car1= ToyotaCar("Fortuner", "diesel")
print(car1.brand)
print(car1.type)

print(car1.start())
print(car1.stop())
