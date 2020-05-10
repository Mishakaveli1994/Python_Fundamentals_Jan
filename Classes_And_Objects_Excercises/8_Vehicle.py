class Vehicle:
    def __init__(self, type, model, price, owner=None):
        self.type = type
        self.model = model
        self.price = price
        self.owner = owner

    def buy(self, money, owner):
        if self.owner != None:
            return "Car already sold"
        elif money < self.price:
            return "Sorry, not enough money"

        else:
            self.owner = owner
            return f"Successfully bought a {self.type}. Change: {money - self.price:.2f}"

    def sell(self):
        if self.owner != None:
            self.owner = None
        else:
            return "Vehicle has no owner"

    def __repr__(self):
        if self.owner != None:
            return f"{self.model} {self.type} is owned by: {self.owner}"
        else:
            return f"{self.model} {self.type} is on sale: {self.price}"


vehicle_type = "car"
model = "BMW"
price = 30000
vehicle = Vehicle(vehicle_type, model, price)
vehicle.buy(35000, "George")
vehicle.buy(15000, "Peter")
vehicle.buy(100, "Mihail")
print(vehicle)
vehicle.sell()
print(vehicle)
