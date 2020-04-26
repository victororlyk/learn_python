def spam1():
    def spam2():
        def spam3():
            z = " even"
            z += y
            print("in spam 3", locals())
            return z

        y = " more " + x  # y must exist before calling spam3
        y += spam3()
        print("in spam 2", locals())
        return y

    x = "spam"  # x must exist before calling spam2
    x += spam2()
    print("in spam 1", locals())
    return x


print(spam1())
# in spam 3 {'z': ' even more spam', 'y': ' more spam'}
# in spam 2 {'spam3': <function spam1.<locals>.spam2.<locals>.spam3 at 0x102ad4620>, 'y': ' more spam even more spam', 'x': 'spam'}
# in spam 1 {'spam2': <function spam1.<locals>.spam2 at 0x1028d9598>, 'x': 'spam more spam even more spam'}
# spam more spam even more spam
