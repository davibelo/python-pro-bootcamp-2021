# FileNotFoundError
# with open("a_file.txt") as file:
#     file.read()

# KeyError
# a_dict = {"key": "value"}
# value = a_dict["non_existent_key"]

# IndexError
# fruit_list = ["apple", "banana", "pear"]
# fruit = fruit_list[3]

# TypeError
# text = "abc"
# print(text + 3)

# To handle errors in python use:
# try:
#   something that might cause an exception
# except <error>:
#   do this if there was an exception
# else:
#   do this if there were no exceptions
# finally:
#   do this no matter what happens


# FileNotFoundError with exception code
try:
    file = open("02-intermediate/12a-a_file.txt")
    a_dict = {"key": "value"}
    print(a_dict["key"])
except FileNotFoundError:
    file = open("02-intermediate/12a-a_file.txt", "w")
    file.write("Something")
except KeyError as error_message:
    print(f"The key {error_message} does not exists")
else:
    content = file.read()
    print(content)
finally:
    file.close()
    print("file was closed")

# raise
# raise can be used to show your own exception

# height = float(input("Height (m): "))
# weight = int(input("Weight (kg): "))

# if height > 3:
#     raise ValueError("human height > 3m")

# bmi = weight / height ** 2
# print(f"BMI:{bmi}")


# exercise 1

fruits = ["apple", "banana", "pear"]


def make_pie(index):
    try:
        fruit = fruits[index]
    except IndexError:
        print("fruit pie")
    else:
        print(fruit + " pie")


make_pie(0)
make_pie(4)

# exercise 2

facebook_posts = [
    {'Likes': 21, 'Comments': 2},
    {'Likes': 13, 'Comments': 2, 'Shares': 1},
    {'Likes': 33, 'Comments': 8, 'Shares': 3},
    {'Comments': 4, 'Shares': 2},
    {'Comments': 1, 'Shares': 1},
    {'Likes': 19, 'Comments': 3}
]

total_likes = 0

for post in facebook_posts:
    try: 
        total_likes = total_likes + post['Likes']
    except KeyError:
        pass
    
print(total_likes)


