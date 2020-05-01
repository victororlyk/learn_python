from player import Player

tim = Player("Tim")
tim.level = 2
print(tim)
tim.level += 6
print(tim)
tim.level -= 2
print(tim)
# Name: Tim, Lives: 3, Level: 2, Score: 1000
# Name: Tim, Lives: 3, Level: 8, Score: 7000
# Name: Tim, Lives: 3, Level: 6, Score: 5000
