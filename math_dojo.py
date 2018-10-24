class MathDojo:
    def __init__(self):
        self.total = 0
    def add(self, x, *y):
        y_total = sum(y)
        self.total += x + y_total
        return self
    def subtract(self, x, *y):
        y_total = sum(y)
        self.total -= x + y_total
        return self
    def result(self):
        print(self.total)
    
md = MathDojo
md().add(2).add(2,5,1).subtract(3,2).result()