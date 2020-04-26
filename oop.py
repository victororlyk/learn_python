class Kettle(object):
    power_source = "electricity"

    def __init__(self, make, price):
        self.make = make
        self.price = price
        self.on = False

    def switch_on(self):
        self.on = True


kenwood = Kettle("Kenwood", 8.99)
hamilton = Kettle("Hamilton", 14.55)

print(hamilton.on)  # False
hamilton.switch_on()
print(hamilton.on)  # True

Kettle.switch_on(kenwood)
print(kenwood.on)  # True

print("*" * 80)
# we nay add attributes to instances
kenwood.power = 1.5
print(kenwood.power)  # 1.5

print(Kettle.power_source)
print(hamilton.power_source)
print(kenwood.power_source)
# electricity
# electricity
# electricity

Kettle.power_source = "atomic"

print(Kettle.power_source)
print(hamilton.power_source)
print(kenwood.power_source)
# atomic
# atomic
# atomic
