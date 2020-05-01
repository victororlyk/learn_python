import random


class Enemy:  # basically it is the same as Enemy(object) python give us
    # shorthand to this means it inherits only from object no other parent

    def __init__(self, name='Enemy', hit_points=0, lives=1):
        self.name = name
        self.hit_points = hit_points
        self.lives = lives
        self.alive = True

    def take_damage(self, damage):
        remaining_point = self.hit_points - damage
        if remaining_point >= 0:
            self.hit_points = remaining_point
            print('I took {} points and have {} left'.format(damage,
                                                             self.hit_points))
        else:
            self.lives -= 1
            if self.lives > 0:
                print("{0.name} lost a life".format(self))
            else:
                self.alive = False
                print("{0.name} is dead".format(self))

    def __str__(self):
        return "Name: {0.name}, Lives:{0.lives}, Hit points: {0.hit_points}".format(
            self)


class Troll(Enemy):  # Troll extends enemy class
    def __init__(self, name):
        super().__init__(name=name, lives=1, hit_points=23)

    def grunt(self):
        print("me {0.name}, {0.name}".format(self))


class Vampyre(Enemy):
    def __init__(self, name):
        super().__init__(name=name, lives=3, hit_points=12)

    def dodge(self):
        if random.randint(1, 3) == 3:
            print("**** {0.name} dodges ****".format(self))
            return True
        else:
            return False

    def take_damage(self, damage):
        if not self.dodge():
            super().take_damage(damage=damage)


class VampyreKing(Vampyre):
    def __init__(self, name):
        super().__init__(name=name)
        self.hit_points = 140

    def take_damage(self, damage):
        damage = damage // 4
        super().take_damage(damage=damage)
