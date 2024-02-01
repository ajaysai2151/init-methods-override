class Cart:
    def __init__(self):
        self.items = {}
        self.item_price = {"book":10,"laptop":30000}
    def add_items(self,item_name,quantity):
        self.items[item_name] = quantity
    def get_items(self):
        print(self.items)
    def get_total_bill(self):
        total = 0 
        for item,price in self.items.items():
            total += self.item_price[item] * price
        print(total)


cart_obj = Cart()
cart_obj.add_items("book",5)
cart_obj.add_items("laptop",1)
cart_obj.get_items()
cart_obj.get_total_bill()
print(type(cart_obj))
