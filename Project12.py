import random
logo = r"""
 ______                                                   __      __                        __    __                          __                           
 /      \                                                 /  |    /  |                      /  \  /  |                        /  |                          
/$$$$$$  | __    __   ______    _______   _______        _$$ |_   $$ |____    ______        $$  \ $$ | __    __  _____  ____  $$ |____    ______    ______  
$$ | _$$/ /  |  /  | /      \  /       | /       |      / $$   |  $$      \  /      \       $$$  \$$ |/  |  /  |/     \/    \ $$      \  /      \  /      \ 
$$ |/    |$$ |  $$ |/$$$$$$  |/$$$$$$$/ /$$$$$$$/       $$$$$$/   $$$$$$$  |/$$$$$$  |      $$$$  $$ |$$ |  $$ |$$$$$$ $$$$  |$$$$$$$  |/$$$$$$  |/$$$$$$  |
$$ |$$$$ |$$ |  $$ |$$    $$ |$$      \ $$      \         $$ | __ $$ |  $$ |$$    $$ |      $$ $$ $$ |$$ |  $$ |$$ | $$ | $$ |$$ |  $$ |$$    $$ |$$ |  $$/ 
$$ \__$$ |$$ \__$$ |$$$$$$$$/  $$$$$$  | $$$$$$  |        $$ |/  |$$ |  $$ |$$$$$$$$/       $$ |$$$$ |$$ \__$$ |$$ | $$ | $$ |$$ |__$$ |$$$$$$$$/ $$ |      
$$    $$/ $$    $$/ $$       |/     $$/ /     $$/         $$  $$/ $$ |  $$ |$$       |      $$ | $$$ |$$    $$/ $$ | $$ | $$ |$$    $$/ $$       |$$ |      
 $$$$$$/   $$$$$$/   $$$$$$$/ $$$$$$$/  $$$$$$$/           $$$$/  $$/   $$/  $$$$$$$/       $$/   $$/  $$$$$$/  $$/  $$/  $$/ $$$$$$$/   $$$$$$$/ $$/                


"""



game_option = False
while game_option is False:
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

    def number():
        number_rand = random.randrange(100)
        return number_rand

    number = number()

    print(number)

    easy_level = 10
    hard_level = 5


    if difficulty == "easy":
        game_option = True
        guess_over = False
        while guess_over is False:
            guessing = f"You have {easy_level} attempts remaining to guess the number."
            print(guessing)
            guess = int(input("Make a guess: "))

            if easy_level > 1:
                if guess < number:
                    print("Too low\nGuess again.")
                    easy_level -= 1
                elif guess > number:
                    print("Too high\nGuess again.")
                    easy_level -= 1
                else:
                    print(f"You got it! the answer is {number}")
                    guess_over = True
            else:
                print("You have lost your guesses, Game over.")
                guess_over = True

    elif difficulty == "hard":
        game_option = True
        guess_over = False
        while guess_over is False:
            guessing = f"You have {hard_level} attempts remaining to guess the number."
            print(guessing)
            guess = int(input("Make a guess: "))

            if hard_level > 1:
                if guess < number:
                    hard_level -=1
                    print("Too low\nGuess again.")
                elif guess > number:
                    hard_level -= 1
                    print("Too high\nGuess again")
                else:
                    print(f"You got it! the answer is {number}")
                    guess_over = True

            else:
                print("You have run out of guesses, Game over.")
                guess_over = True


    else:
        print("You did not choose from the given options. Try again - Run it again.")