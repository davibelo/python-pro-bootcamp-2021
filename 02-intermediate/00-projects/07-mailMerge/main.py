
PLACEHOLDER = "[name]"

# opening files with names
with open("02-intermediate/07-mailMerge/Input/Names/invited_names.txt") as names_file:
    # return all lines in the file, as a list where each line is an item in the list object
    names = names_file.readlines()

# seeing "\n" in the end of each name
print(names)

with open("02-intermediate/07-mailMerge/Input/Letters/starting_letter.txt") as letter_file:
    letter_contents = letter_file.read()
    print(letter_contents)
    for name in names:
        # striping "\n" from the name
        stripped_name = name.strip("\n")                
        # creating a new_letter replacing the PLACEHOLDER
        new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
        # writing the new_letter to a file
        with open(f"02-intermediate/07-mailMerge/Output/ReadyToSend/letter_for_{stripped_name}.txt", mode="w") as ready_letter_file:
            ready_letter_file.write(new_letter)

