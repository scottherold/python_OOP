class Product:
    def __init__(self, price, item_name, weight, brand):
        self.price = price
        self.item_name = item_name
        self.weight = weight
        self.brand = brand
        self.status = "for sale"
    def sell(self):
        self.status = "sold"
        return self.status
    def add_tax(self, tax):
        tax_price = self.price+(self.price*tax)
        print(tax_price)
        return tax_price
    def return_item(self, reason_for_return):
        if reason_for_return == "defective":
            self.status = "defective"
            self.price = 0.00
        if reason_for_return == "like_new":
            self.status = "for sale"
        if reason_for_return == "opened":
            self.status = "used"
            self.price = self.price-(self.price*0.2)
        return self
    def display_info(self):
        print(self.price, self.item_name, self.weight, self.brand, self.status)