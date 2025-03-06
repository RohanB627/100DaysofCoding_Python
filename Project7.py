import random

Stages = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', 
'''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', 
'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', 
'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', 
'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', 
'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', 
'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']


word_list = ["aardvark", "baboon", "camel"]

lives = 6
chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
for letter in range(0, len(chosen_word)):
    placeholder += "_ "
print(placeholder)

Turn = False
display_fin = []
i=0


while not Turn:
    guess = input("Guess a letter: ").lower()
    display = ""
    if guess not in chosen_word:
        i+=1
        lives -=1
    print(Stages[i])
        


    for letter in chosen_word:
        if letter == guess:
            display+= letter
            display_fin.append(guess)
        elif letter in display_fin:
            display += letter
        else:
            display += "_"

        
    print(display)
    print(f"Your current life is {lives}")
    
    if "_" not in display:
        Turn = True
        print("You win!")
    elif lives == 0 or lives <= 0:
        Turn = True
        print("You Lose")

        








    
