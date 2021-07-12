# dictionary comprehension

# creating a new dict from a list
# new_dict = {new_key:new_value for item in list if condition}

# creating a new dict from a dict
# new_dict = {new_key:new_value for (key,value) in dict.items() if condition}

import random

names = ["Alex", "Beth", "Angela", "Dave", "Eleanor", "Freddie"]

# creating a dictionary from a list
student_scores = {name: random.randint(0, 100) for name in names}
print(f"student scores: {student_scores}")

# creating a new dictionary from a dictionary
passed_students = {
    name: score for (name, score) in student_scores.items() if score >= 50
}
print(f"passed students: {passed_students}")

# exercise 1:
# create a dict with each word and its number of letters for the sentence
sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
new_dict = {word: len(word) for word in sentence.split()}
print(new_dict)

# exercise 2:
# convert a dict of temp in Celsius to a dict with temp in fahrenheit

weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}

weather_f = {day: (temp_c * 9/5) + 32 for (day, temp_c) in weather_c.items()}
print(weather_f)
