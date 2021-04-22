import os

# getting path automatically
main_dir = os.path.dirname(__file__)
rel_path = "04a-example.txt"
abs_path = os.path.join(main_dir, rel_path)

# # open a file
# file = open(abs_file_path)

# # reading a file
# contents = file.read()
# print(contents)

# # close to free computer resources
# file.close()

# better way (no need to close file!)
with open(abs_path) as file:
    contents = file.read()
    print(contents)

# writting:
# mode w = write (erases previous contents, create file if it doesn't exists)
# mode a = append (adds content)

with open(abs_path, mode="a") as file:
    file.write("\nmy text!!!")

# using the path manually
with open("02-intermediate/04a-example.txt", mode="a") as file:
    file.write("\nmy text!!!")

# you can also use relative paths
# file in same directory: "./<file>" or simply: "<file>"
# file in parent directory: "../<file"

# Paths Windows vs Linux
# Linux uses forward slash: /home/project
# Windows uses backslash: \user\documents
# Python doesn't care, uses forward slash always !
