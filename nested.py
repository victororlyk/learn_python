burgers = ['beef', 'chicken', 'spicy bean']
toppings = ['cheese', 'egg', 'beans', 'spam']

# for meals in [(burger, topping) for burger in burgers for topping in toppings]:
#  print(meals)
# (burger, topping)  here is an expression


# for burger in burgers:
#     for topping in toppings:
#         print((burger, topping))


# for meals in [[(burger, topping) for burger in burgers] for topping in
#               toppings]:
#     print(meals)
# # [('beef', 'cheese'), ('chicken', 'cheese'), ('spicy bean', 'cheese')]
# # [('beef', 'egg'), ('chicken', 'egg'), ('spicy bean', 'egg')]
# # [('beef', 'beans'), ('chicken', 'beans'), ('spicy bean', 'beans')]
# # [('beef', 'spam'), ('chicken', 'spam'), ('spicy bean', 'spam')]

# for nested_meals in [[(burger, topping) for topping in toppings] for burger
#                      in burgers]:
#     print(nested_meals)

# for i in range(1, 11):
#     for j in range(1, 11):
#         print(i, i * j)

# for value in [(x, x * y) for x in range(1, 11) for y in range(1, 11)]:
#     x, y = value
#     print(x, y)
    # print(value)
for x, y in ((x, x * y) for x in range(1, 11) for y in range(1, 11)):
    print(x, y)
