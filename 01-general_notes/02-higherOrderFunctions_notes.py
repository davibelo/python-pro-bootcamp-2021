# Higher Order functions
# These are functions that get functions as arguments


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


def calculator(n1, n2, operation):
    # calculator is a higher order function
    """applies operation to n1, n2 numbers"""
    return operation(n1, n2)


print(calculator(2, 3, add))
print(calculator(2, 3, subtract))


# Nested functions:
# calling nested functions
def outer_function():
    print("I'm outer")

    def nested_function():
        print("I'm inner")

    nested_function()


outer_function()


# returning nested functions and calling it after
def outer_function1():

    print("I'm outer")

    def nested_function1():
        print("I'm inner")

    return nested_function1


inner_function = outer_function1()
inner_function()