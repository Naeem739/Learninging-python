class Phone:
    
    #consturctor 
    def __init__(self,own,price,brand):
        self.owner = own
        self.price = price
        self.brand = brand 
        self.cart = []


    def add_to_cart(self,item):
        self.cart.append(item)


myPhone = Phone("Naeem",26000,"Samsung")
myPhone.add_to_cart("Samsung M11")
myPhone.add_to_cart("Samsung S23 Ultra Plus")
rphon= Phone("RIfat",2400,"realmi")
rphon.add_to_cart("realmi C55")

print(myPhone.brand,myPhone.owner)
print(myPhone.cart)
print(rphon.cart)





        