
def call():
    print("calling somone i dont know")

class Phone: 
    price = 12300
    color = "blue"
    brand = "samsung"
    features = ['camera','speaker','Hammer','Call','YouTube']
    def call(self):
        print("calling one person")
    def send_sms(self,phone,person):
        print(f'send sms to {person} from this {phone}')


myphone = Phone()
print(myphone.features)
myphone.call()
myphone.send_sms("01623094662","Rifat")

