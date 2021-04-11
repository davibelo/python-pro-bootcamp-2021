with open("02-intermediate/06b-file1.txt") as file1:
    file1_contents = file1.readlines()

numbers_1 = [int(n.strip("\n")) for n in file1_contents]
print(numbers_1)

with open("02-intermediate/06b-file2.txt") as file1:
    file2_contents = file1.readlines()

numbers_2 = [int(n) for n in file2_contents]
print(numbers_2)

# create a list called result which contains the numbers
# that are common in both files.
numbers_3 = [n for n in numbers_1 if n in numbers_2]
print(numbers_3)
