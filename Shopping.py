class shopping:

    def __init__(self,name):
        self.name = name
        self.cart = []
    
    def add_to_cart(self,item,price,quantity):
        product={
              'item': item,
               'price':price,
               'quantity' : quantity
        }
        self.cart.append(product)
    def checkout(self,amount):
        total = 0
        for item in self.cart:
            total += item['price'] * item['quantity']
        print(f'total Price = {total}')
        if total>amount:
            print("Insufficient Balance")
        else: 
            print("Successfuly Checkout")


Naeem = shopping("Naeem")
Naeem.add_to_cart("Rubik's Cube",100,14)
Naeem.checkout(1200)

