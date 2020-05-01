class Player(object):
    def __init__(self, name):
        self.name = name
        self._lives = 3
        self._level = 1
        self.score = 0

    def _get_lives(self):
        return self._lives

    def _set_lives(self, lives):
        if lives >= 0:
            self._lives = lives
        else:
            print("can't be negative")
            self._lives = 0

    lives = property(_get_lives, _set_lives)  # setter and getter

    def _get_level(self):
        return self._level

    def _set_level(self, level):
        if level > 0:
            delta = level - self._level
            self._level = level
            self.score += (delta * 1000)
        elif self._level > 0:
            print("level can't be less then 0")

    level = property(_get_level, _set_level)

    def __str__(self):
        return "Name: {0.name}, Lives: {0.lives}, Level: {0.level}, Score: {0.score}".format(
            self)
