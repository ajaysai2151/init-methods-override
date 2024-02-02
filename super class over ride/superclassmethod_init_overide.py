class Product:
    def __init__(self,name,price,deal_price,ratings):
        self.name = name 
        self.price = price
        self.deal_price = deal_price
        self.ratings = ratings
        self.you_Save = price - deal_price
    def display_product_details(self):
        print("product : {}".format(self.name))
        print("price : {}".format(self.price))
        print("deal_price : {}".format(self.deal_price))
        print("ratings : {}".format(self.ratings))
        print("you_Save : {}".format(self.you_Save))
    def get_deal_price(self):
        return self.deal_price
         
class Electronic_Items(Product):
    def __init__(self,name,price,deal_price,ratings,set_warranty):
        super().__init__(name,price,deal_price,ratings)
        self.warranty = set_warranty
    #def set_warranty(self,warranty):
        #self.warranty = warranty
    def  display_product_details(self):
        super().display_product_details()
        print("warranty : {}".format(self.warranty))
       
        
class GroceryItem(Product):
    def __init__(self,name,price,deal_price,ratings,set_expiry_date):
        super().__init__(name,price,deal_price,ratings)
        self.expiry_date = set_expiry_date
    #def set_expiry_date(self,expiry_date):
        #self.expiry_date = expiry_date
    def  display_product_details(self):
        super().display_product_details()
        print("expiry_date : {}".format(self.expiry_date))
       
class Order:
    def __init__(self,delivery_address,delivery_speed):
        self.items_in_cart = []
        self.delivery_address = delivery_address
        self.delivery_speed = delivery_speed
    def add_items(self,product,quantity):
        #list kabbati append chystunamu (tuple laga append chystunamu )
        self.items_in_cart.append((product,quantity)) 
    def display_order_details(self):
        #order details display chydaniki.cart lo items add chysamu 
        #cart list kabbati iterate avachu
        #each item tuple kabbati unpack chyachu
        for product,quantity in self.items_in_cart:
            #print(product)
            #print(quantity)
            #product class instance ni estunamu product ki value
            #andukey product.display_product_detailsani call chygalgutunam
            #product Electronic_Item or GroceryItem ina indachu
            #enduku antey both Electronic_Items & GroceryItem istnaces ah display_product_details method  ni call chygalgutai
            product.display_product_details()
            print("quantity : {}".format(quantity)) 
            print("-----------------------")
    def get_total_bill(self):
        total_bill = 0 
        for product,quantity in self.items_in_cart:
            #get_deal_price() aneydi product class method
            #super class methods ni sublass nundi access chyachu
            price = product.get_deal_price()
            total_bill += price * quantity
        print("total_price : {}".format(total_bill))
        return total_bill
        

#laptop ani oka product create chysamu
#product class nundi latop aney instance create chysamu
laptop = Electronic_Items("laptop",35000,30000,4.2,24)
#laptop.set_warranty("24-months")
#laptop.display_electronic_item_details()
#milk ani oka product create chysamu
#product class nundi milk aney instance create chysamu
milk = GroceryItem("milk",35,30,4,"7-days")
#milk.set_expiry_date("7-days")
#milk.display_grocery_details()


#order create chyalli 
my_order = Order("hyderabad","normal")
#product ki manam manam product class tho create chysina instance estamu
my_order.add_items(laptop,1)
my_order.add_items(milk,5)
my_order.display_order_details()
my_order.get_total_bill()






