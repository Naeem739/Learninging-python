class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __repr__(self):
        return f'Product(name={self.name}, price={self.price})'

class Shop:
    def __init__(self):
        self.products = []

    def add_product(self, name, price):
        product = Product(name, price)
        self.products.append(product)

    def buy_product(self, name):
        for product in self.products:
            if product.name == name:
                self.products.remove(product)
                return f'Congratulations! You have successfully bought {name}.'
        return f'Sorry, {name} is not available in the shop.'

    def __repr__(self):
        return '\n'.join([f'{product.name}: {product.price}' for product in self.products])

myShop = Shop()
myShop.add_product("Samsung M11", 14500)
myShop.add_product("Realme 10", 15500)

print(myShop)  # Output the list of products in the shop

# Attempt to buy a product
print(myShop.buy_product("Samsung M11"))  # Should print the congratulations message
print(myShop.buy_product("iPhone 12"))   # Should print the product not available message

print(myShop)  # Output the updated list of products in the shop after purchase
