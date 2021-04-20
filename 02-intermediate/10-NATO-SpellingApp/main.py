import pandas as pd


# 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"...}

# reading csv file
alpha_file = "02-intermediate/10-NATO-SpellingApp/nato_phonetic_alphabet.csv"
df_alpha = pd.read_csv(alpha_file)

# creating nato alphabet dict
alpha_dict = {row.letter: row.code for (
    index, row) in df_alpha.iterrows()}

# 2. Create a list of the phonetic code words from a word that the user inputs.


def generate_phonetic():
    # getting a word from user
    word = input("Type a word: ").upper()
    # creating and printing the list
    try:
        spelling_list = [alpha_dict[letter] for letter in word]
    except KeyError:
        print("Error: Character not found NATO alphabet")
        generate_phonetic()
    else:
        print(spelling_list)


generate_phonetic()
