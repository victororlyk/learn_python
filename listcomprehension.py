print(__file__)
numbers = [1, 2, 3, 4, 5, 6]

number = int(input('enter a number'))

squares = [number ** 2 for number in numbers]

try:
    index_pos = numbers.index(number)
    print(squares[index_pos])
except ValueError:
    print("no  such number")
