# student_dict = {
#     "student": ["Angela", "James", "Lily"],
#     "score": [56, 76, 98]
# }

#Looping through dictionaries:
# for (key, value) in student_dict.items():
    #Access key and value
    # pass


# student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    # pass
# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

import pandas

#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
read = pandas.read_csv("nato_phonetic_alphabet.csv")
phone_dic = {row.letter:row.code for (index,row) in read.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
def word(n):
 item = list(n.upper())
 phon_item = []
 for m in item:
  if m in phone_dic:
   k = phone_dic.get(m)
   phon_item.append(k)
 return phon_item

words = input("Enter a word: ")
print(word(words))
