class Enemy:  # basically it is the same as Enemy(object) python give us
    # shorthand to this means it inherits only from object no other parent

    def __init__(self, name='Enemy', hit_points=0, lives=1):
        self.name = name
        self.hit_points = hit_points
        self.lives = lives

    def take_damage(self, damage):
        remaining_point = self.hit_points - damage
        if remaining_point >= 0:
            self.hit_points = remaining_point
            print('I took {} points and have {} left'.format(damage,
                                                             self.hit_points))
        else:
            self.lives -= 1

    def __str__(self):
        return "Name: {0.name}, Lives:{0.lives}, Hit points: {0.hit_points}".format(
            self)


class Troll(Enemy):  # Troll extends enemy class
    pass
