def add(*args):
    total = 0
    for arg in args:
        if not isinstance(arg, int):
            raise TypeError(f"Enter numbers only --> '{arg}' is not a number")
        total += arg
    return total

print(add(1,2,3,'t',4,5,6,7))