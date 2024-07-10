class Vehical:
    def __init__(self,name,price,color):
        self.name = name 
        self.price = price
        self.color = color 
    def move(self):
        pass

class Bus(Vehical):
    def __init__(self, name, price, color,seat):
        self.seat = seat 
        super().__init__(name, price, color)


class ACBus(Bus):
    def __init__(self, name, price, color, seat,temp):
        self.temparature = temp 
        super().__init__(name, price, color, seat)

   
    def __repr__(self) -> str:
        print(f"Name = {self.name} seat = {self.seat}, temp = {self.temparature}")
        return super().__repr__()

dola = ACBus("Dola-101",1200000,"White",46,25)

print(dola)
