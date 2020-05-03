class Wing:

    def __init__(self, ratio):
        self.ratio = ratio

    def fly(self):
        if self.ratio > 1:
            print("Weee, this is fun")
        elif self.ratio == 1:
            print("This is hard work, but I'm flying")
        else:
            print("I think I'll just walk")


class Duck:

    def __init__(self):
        self._wing = Wing(1.8)

    def walk(self):
        print("Waddle, waddle, waddle")

    def swim(self):
        print("Come on in, the water's lovely")

    def quack(self):
        print("Quack quack")

    def fly(self):
        self._wing.fly()


class Penguin:

    def walk(self):
        print("Waddle, waddle, I waddle too")

    def swim(self):
        print("Come on in, but it's a bit chilly this far South")

    def quack(self):
        print("Are you 'avin' a larf? I'm a penguin")


class Mallard(Duck):
    pass


class Flock:
    def __init__(self):
        self.flock = []

    def add_duck(self, duck: Duck) -> None:
        print(type(duck), isinstance(duck, Duck))
        fly_method = getattr(duck, "fly", None)
        if callable(fly_method):
            self.flock.append(duck)

    def migrate(self):
        problem = None
        for duck in self.flock:
            try:
                duck.fly()
            except AttributeError as e:
                print("one duck donw")
                problem = e
        if problem:
            raise problem


if __name__ == '__main__':
    donald = Duck()
    donald.fly()
