# create a new list from a another list
numbers = [1, 2, 3]
new_list = []
for n in numbers:
    add_1 = n+1
    new_list.append(add_1)
print("a)", new_list)

# List comprehension offers a shorter syntax when
# you want to create a new list based on the values
# of an existing list.
new_list_2 = [n+1 for n in numbers]
print("b)", new_list_2)

# it can also be used with strings
name = "Angela"
letter_list = [letter for letter in name]
print("c)", letter_list)

# it can be used with other sequences
range_list = [n*2 for n in range(1, 5)]
print("d)", range_list)

# conditional list comprehension
names = ["Alex", "Beth", "Angela", "Dave", "Eleanor", "Freddie"]
short_names = [name for name in names if len(name) < 5]
print("e)", short_names)

long_names = [name.upper() for name in names if len(name) > 5]
print("f)", long_names) 

numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
odd_numbers = [n for n in numbers if n % 2 != 0]
print("g)", odd_numbers)
