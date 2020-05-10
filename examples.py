# Create a comprehension that returns a list of all the locations that have an exit to the forest.
# The list should contain the description of each location, if it's possible to get to the forest from there.
#
# The forest is location 5 in the locations dictionary
# The exits for each location are represented by the exits dictionary.
#
# Remember that a dictionary has a .values() method, to return a list of the values.
#
# The forest can be reached from the road, and the hill; so those should be the descriptions that appear in your list.
#
# Test your program with different destinations (such as 1 for the road) to make sure it works.
#
# Once it's working, modify the program so that the comprehension returns a list of tuples.
# Each tuple consists of the location number and the description.
#
# Finally, wrap your comprehension in a for loop, and print the lists of all the locations that lead to each of the
# other locations in turn.
# In other words, use a for loop to run the comprehension for each of the keys in the locations dictionary.
import timeit

locations = {0: "You are sitting in front of a computer learning Python",
             1: "You are standing at the end of a road before a small brick building",
             2: "You are at the top of a hill",
             3: "You are inside a building, a well house for a small stream",
             4: "You are in a valley beside a stream",
             5: "You are in the forest"}

exits = {0: {"Q": 0},
         1: {"W": 2, "E": 3, "N": 5, "S": 4, "Q": 0},
         2: {"N": 5, "Q": 0},
         3: {"W": 1, "Q": 0},
         4: {"N": 1, "W": 2, "Q": 0},
         5: {"W": 2, "S": 1, "Q": 0}}

print("nested for loops")
print("-" * 10)
nested_loop = """\
for loc in sorted(locations):
    exits_to_destination_1 = []
    for xit in exits:
        if loc in exits[xit].values():
            exits_to_destination_1.append((xit, locations[xit]))
    print("location leading to {}".format(loc), end='\t')
    print(exits_to_destination_1)
"""
# for loc in sorted(locations):
#     exits_to_destination_1 = []
#     for xit in exits:
#         if loc in exits[xit].values():
#             exits_to_destination_1.append((xit, locations[xit]))
#     print("location leading to {}".format(loc), end='\t')
#     print(exits_to_destination_1)

print()

print("list comprehesion inside a for loop")
print("-" * 10)
loop_comp = """\
for loc in sorted(locations):
    exits_to_destination_2 = [(xit, locations[xit]) for xit in exits
                              if loc in exits[xit].values()]
    print("locations leading to {}".format(loc), end='\t')
    print(exits_to_destination_2)
"""
print()

print("neededc omprehension")
print("-" * 10)
nested_comp = """\
exits_to_destination_3 = [[(xit, locations[xit]) for xit in exits
                           if loc in exits[xit].values()]
                          for loc in sorted(locations)]
for index, loc in enumerate(exits_to_destination_3):
    print('locations leading to {}'.format(index), end='\t')
    print(loc)
"""

result_1 = timeit.timeit(nested_loop, globals=globals(), number=1000)
result_2 = timeit.timeit(loop_comp, globals=globals(), number=1000)
result_3 = timeit.timeit(nested_comp, globals=globals(), number=1000)
print("nested loop:\t{}".format(result_1))
print("loop comp:\t{}".format(result_2))
print("nested comp:\t{}".format(result_2))
