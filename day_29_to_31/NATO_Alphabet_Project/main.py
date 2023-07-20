import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
# Create a dictionary in this format:
nato_dict = {row.letter: row.code for (index, row) in data.iterrows()}


def generate_phonetic():
    # Create a list of the phonetic code words from a word that the user inputs.
    word = input("Enter a word: ").upper()
    try:
        output_list = [nato_dict[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic()
    else:
        print(output_list)


generate_phonetic()
