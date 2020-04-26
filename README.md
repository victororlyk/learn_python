scopes are made in functions, modules and classes, 
to gain access to code in modules body we may use in function 
```
def fn():
    global var
    #now we have access to var
```

another way is to use `nonlocal`

```
def outer():
    a = 0
    def inner():
        nonlocal a
        # now we have access to a which is declared

```
