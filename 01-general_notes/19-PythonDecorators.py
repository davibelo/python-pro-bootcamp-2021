import time

# Python decorator function
# can be used to give additional functionality to a function
# trigger something before or after, call that function more times...


def delay_decorator(function):

    def wrapper_function():
        time.sleep(5)
        function()
        function()
        print("...")

    return wrapper_function


@delay_decorator
def say_hello():
    print("Hello")


def say_greeting():
    print("How are you?")


def say_bye():
    print("Bye")


say_hello()
delay_decorator(say_greeting())
say_bye()

# ---- exercise ---- #
# Print out the speed it takes to run the given functions
# You will need to complete the speed_calc_decorator() function.
import time


def speed_calc_decorator(function):

    def wrapped_function():
        start_time = time.time()
        function()
        end_time = time.time()
        print(f"{function.__name__}, run speed: {end_time - start_time}")

    return wrapped_function


@speed_calc_decorator
def fast_function():
    for i in range(1000):
        i * i


@speed_calc_decorator
def slow_function():
    for i in range(100000000):
        i * i


fast_function()
slow_function()

## ---- Advanced Python Decorator Functions ----#


class User:

    def __init__(self, name):
        self.name = name
        self.is_logged_in = False


def is_authenticated_decorator(function):

    def wrapper(*args, **kwargs):
        if args[0].is_logged_in == True:
            function(args[0])

    return wrapper


@is_authenticated_decorator
def create_blog_post(user):
    print(f"This is {user.name}'s new blog post.")


new_user = User("angela")
new_user.is_logged_in = True
create_blog_post(new_user)


# ---- Advanced decorators exercise ---- #
def logging_decorator(fn):

    def wrapper(*args, **kwargs):
        print(f"You called {fn.__name__}{args}")
        result = fn(args[0], args[1], args[2])
        print(f"It returned: {result}")

    return wrapper


@logging_decorator
def a_function(a, b, c):
    return a * b * c


a_function(1, 2, 3)
