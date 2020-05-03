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
    def __init__(self):
        # here we add a reference to aviate method so here we can really
        # call this property like real method
        self.fly = self.aviate

    def walk(self):
        print("Waddle, waddle, I waddle too")

    def swim(self):
        print("Come on in, but it's a bit chilly this far South")

    def quack(self):
        print("Are you 'avin' a larf? I'm a penguin")

    def aviate(self):
        print("I won the lottery")


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
        else:
            raise TypeError(
                "Can add only flying animals, are you sure it is not {}".format(
                    str(type(duck).__name__)))

    def migrate(self):
        problem = None
        for duck in self.flock:
            try:
                duck.fly()
                raise AttributeError("testing exception handle in migarate")
                # TODO remove this before release
            except AttributeError as e:
                print("one duck donw")
                problem = e
        if problem:
            raise problem


if __name__ == '__main__':
    donald = Duck()
    donald.fly()
