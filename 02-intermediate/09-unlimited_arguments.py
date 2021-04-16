# unlimited position arguments
def add(*args):
    # args are store as a tuple
    print(type(args))
    
    # args can be accessed with index
    print(args[0])

    # args can be used in a for loop
    sum = 0
    for n in args:
        sum += n
    return sum


num1 = add(1, 2, 3)
print(num1)

# many keyword arguments
def calculate(n, **kwargs):
    # kwards are stored as dictionaries
    print(type(kwargs))
    print(kwargs)
    
    # kwargs can be used inside a for looṕ
    for key, value in kwargs.items():
        print(key, value)

    # example of use of kwargs
    n += kwargs["add"]
    n *= kwargs["multiply"]
    return n

num2 = calculate(10, add=3, multiply=4)
print(num2)




