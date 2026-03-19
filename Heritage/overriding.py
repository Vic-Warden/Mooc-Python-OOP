# Parent Class
class Drink:
    def __init__(self, price):
        self.price = price

    def drink(self):
        print("Drinking something generic")

# Child Class
class Coffee(Drink):
    
    # Class dictionary
    prices = {"simple": 1, "serré": 1, "allongé": 1.5}

    def __init__(self, coffee_type):
        self.coffee_type = coffee_type
        
        # Use parent's __init__ to set the price
        super().__init__(price=self.prices.get(coffee_type, 1))

    # Overriding the parent's method
    def drink(self):
        print("Drinking a nice coffee!")

# Instantiate a coffee
my_coffee = Coffee("allongé")

print(my_coffee.price) 
my_coffee.drink()     