print(__file__)

numbers = [1, 2, 3, 4, 5, 6]
number = int(input("number"))
squares = []

for number in numbers:
    squares.append(number ** 2)
try:
    index_pos = numbers.index(number)
    print(squares[index_pos])
except ValueError:
    print('no such number in value')
