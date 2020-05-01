class Wing:
    def __init__(self, ratio):
        self.ratio = ratio

    def fly(self):
        if self.ratio > 1:
            print("Wee this is fun")
        elif self.ratio == 1:
            print("this is hard work")
        else:
            print(" I think  I will just walk")


class Duck(object):
    def __init__(self):
        self.wing = Wing(1.8)

    def walk(self):
        print("Waddle, waddle, waddle")

    def swin(self):
        print("swimming")

    def quack(self):
        print("quack quack")

    def fly(self):
        self.wing.fly()


class Penguin(object):
    def __init__(self):
        self.wing = Wing(.8)

    def walk(self):
        print("Waddle, waddle, waddle")

    def swin(self):
        print("swimming it is hot in the South")

    def quack(self):
        print("I am penguin")

    def fly(self):
        self.wing.fly()


if __name__ == "__main__":
    donald = Duck()
    donald.fly()  # Wee this is fun

    percy = Penguin()
    percy.fly()  # I think  I will just walkgt
