class Bike:
    def __init__(self, price, max_speed):
        self.price = price
        self.max_speed = max_speed
        self.miles = 0
    def displayInfo(self):
        print(self.price, self.max_speed, self.miles)
    def ride(self):
        print("Riding")
        self.miles += 10
        return self
    def reverse(self):
        if self.miles >= 5:
            print("Reversing")
            self.miles -= 5
        else:
            print("The bike has 0 miles!")
        return self

new_bike1 = Bike(200,"25mph")
new_bike2 = Bike(150,"15mph")
new_bike3 = Bike(300,"30mph")
    
new_bike1.ride().ride().ride().displayInfo()
new_bike2.ride().ride().reverse().reverse().displayInfo()
new_bike3.reverse().reverse().reverse().displayInfo()

# I added an if statement to prevent the bike from having less than 0 miles.
# The only methods that need to return self are ride and reverse.