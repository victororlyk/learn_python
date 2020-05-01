class Duck(object):
    def walk(self):
        print("Waddle, waddle, waddle")

    def swin(self):
        print("swimming")

    def quack(self):
        print("quack quack")


class Penguin(object):
    def walk(self):
        print("Waddle, waddle, waddle")

    def swin(self):
        print("swimming it is hot in the South")

    def quack(self):
        print("I am penguin")


def test_duck(duck):
    duck.walk()
    duck.swin()
    duck.quack()


if __name__ == "__main__":
    donald = Duck()
    test_duck(donald)

    percy = Penguin()
    test_duck(percy)
