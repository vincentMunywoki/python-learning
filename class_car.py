# a car has model, color, size, fuel type
# fuel capacity

class Car:
    # define the init method
    def __init__(self,model,color,fuel_capacity):
        self.model = model
        self.color = color
        self.fuel_capacity = fuel_capacity
    
    def sayHello(self):
        print("Hello world")
        
    def sayColor(self):
        print("My color is", self.color)
    
    def spendFuel(self, fuelAmount):
        self.fuel_capacity -= fuelAmount
    
new_car = Car("BMW","blue",20000)
print(new_car.model)
print(new_car.color)
print(new_car.fuel_capacity)
new_car.spendFuel(1000)
print(new_car.fuel_capacity)

# new_car.sayHello()
# new_car.sayColor()
# new_car.spendFuel(1000)
