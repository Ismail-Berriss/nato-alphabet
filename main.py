import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
alphabets = {row.letter: row.code for (index, row) in data.iterrows()}

user_input = input("Enter a word: ").upper()
phonetic_code = [alphabets[letter] for letter in user_input]
print(phonetic_code)
