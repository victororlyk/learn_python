import timeit
from statistics import mean, stdev


def fact(n):
    result = 1
    if n > 1:
        for f in range(2, n + 1):
            result *= f
        return result


fact_test = """\
def fact(n):
    result = 1
    if n > 1:
        for f in range(2, n + 1):
            result *= f
        return result
y = fact(5)
"""


def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)


factorial_test = """\
def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)
y = factorial(5)
"""

# rest1 = timeit.timeit(fact_test, number=1000)
# rest2 = timeit.timeit(factorial_test, number=1000)
#
# print(rest1,'\n', rest2)

if __name__ == '__main__':
    list1 = timeit.repeat("x=fact(130)", setup='from __main__ import fact',
                        number=1000)
    list2 = timeit.repeat("x=factorial(130)",
                          setup='from __main__ import factorial', number=1000)

    print(mean(list1), stdev(list1))
    print(mean(list2), stdev(list2))


