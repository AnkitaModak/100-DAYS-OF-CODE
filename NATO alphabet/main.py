#TODO 1. Create a dictionary in this format:{"A": "Alfa", "B": "Bravo"}
import pandas
data = pandas.read_csv("nato_phonetic_alphabet.csv")
dict = {row.letter:row.code for (index,row) in data.iterrows()}
print(dict)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
word = input("enter a word:").upper()
output_list = [dict[letter] for letter in word]
print(output_list)
