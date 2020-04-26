class Kettle(object):
    def __init__(self, make, price):
        self.make = make
        self.price = price
        self.on = False


kenwood = Kettle("Kenwood", 8.99)
print(kenwood.make)  # Kenwood
print(kenwood.price)  # 8.99

kenwood.price = 13
print(kenwood.price)  # 13

hamilton = Kettle("Hamilton", 14.55)

print(hamilton.price, hamilton.make)  # 14.55 Hamilton

print("Models:{} = {}, {}={}".format(kenwood.make, kenwood.price,
                                     hamilton.make, hamilton.price))
# Models:Kenwood = 13, Hamilton=14.55
