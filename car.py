class Car:
    def __init__(self, price, speed, fuel, mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        def tax(self):
            tax = 0.012
            if self.price > 10000:
                tax = 0.015
            return tax
        self.tax = tax(self)
    def displayInfo(self):
        print(self.price, self.speed, self.fuel, self.mileage, self.tax)
        

new_car1 = Car(2000, "35mph", "Full", "15mpg")
new_car2 = Car(2000, "5mph", "Not Full", "105mpg")
new_car3 = Car(2000, "15mph", "Kind of Full", "95mpg")
new_car4 = Car(2000, "25mph", "Full", "25mpg")
new_car5 = Car(2000, "45mph", "Empty", "25mpg")
new_car6 = Car(2000000, "35mph", "Empty", "15mpg")

new_car1.displayInfo()
new_car2.displayInfo()
new_car3.displayInfo()
new_car4.displayInfo()
new_car5.displayInfo()
new_car6.displayInfo()

