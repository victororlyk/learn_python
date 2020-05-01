from player import Player
from enemy import Troll, Vampyre, VampyreKing

tim = Player("Tim")

first_troll = Troll("Big troll")
print("some troll {}".format(first_troll))
first_troll.take_damage(18)
print(first_troll)
brother_troll = Troll("Urg")
print(brother_troll)
brother_troll.take_damage(4)
brother_troll.grunt()


vamp = Vampyre("vlad")
print(vamp)
vamp.take_damage(3)
print(vamp)

print("*"*40)
print(first_troll)

while vamp.alive:
        vamp.take_damage(1)
        print(vamp)

drakula = VampyreKing("vlad")
print(drakula)

drakula.take_damage(22)
print(drakula)
