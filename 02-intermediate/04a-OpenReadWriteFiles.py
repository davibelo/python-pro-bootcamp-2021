import os

# getting path
script_dir = os.path.dirname(__file__)
rel_path = "04b-example.txt"
abs_file_path = os.path.join(script_dir, rel_path)

# # open a file
# file = open(abs_file_path)

# # reading a file
# contents = file.read()
# print(contents)

# # close to free computer resources
# file.close()

# better way (no need to close file!)
with open(abs_file_path) as file:
    contents = file.read()
    print(contents)

# writting:
# mode w = write (erases previous contents, create file if it doesn't exists)
# mode a = append (adds content)

with open(abs_file_path, mode="a") as file:
    file.write("\nmy text!!!")

