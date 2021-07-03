import time

# Python decorator function
# can be used to give aditional functionalitty to a function
# trigger something before or after, call that function more times...



def delay_decorator(function):
    def wrapper_function():
        time.sleep(2)
        function()
        function()
        print("...")

    return wrapper_function


@delay_decorator
def say_hello():
    print("Hello")


@delay_decorator
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
    return wrapped_function()

@speed_calc_decorator
def fast_function():
    for i in range(10000000):
        i * i


@speed_calc_decorator
def slow_function():
    for i in range(100000000):
        i * i
