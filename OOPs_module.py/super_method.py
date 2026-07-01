class Car:
    def __init__(self,type):
        self.type= type

    @staticmethod
    def start():
        print("car started..")
    
    @staticmethod
    def stop():
        print("car stopped..")

class ToyotaCar(Car):
    def __init__(self,brand,type):
        super().__init__(type)
        self.brand= brand
        self.type= type
        super().start()

car1= ToyotaCar("Fortuner", "diesel")
print(car1.type)
        
