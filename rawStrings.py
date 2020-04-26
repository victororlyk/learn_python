a_string = "this is \na string split\t\t and tabbed"
print(a_string)
# this is
# a string split		 and tabbed

raw_string = r"this is \na string split\t\t and tabbed"
print(raw_string)
# this is \na string split\t\t and tabbed

b_string = "this is" + chr(10) + "a string split" + chr(9) + chr(9) + "and " \
                                                                      "tabbed"
print(b_string)
# this is
# a string split		and tabbed

backslash_string = "this is backslash \followed by some text"
print(backslash_string)
# this is backslash ollowed by some text

backslash_string = "this is backslash \\followed by some text"
print(backslash_string)
# this is backslash \followed by some text

error_string = r"this string ends with \\"
print(error_string)
# this string ends with \\
