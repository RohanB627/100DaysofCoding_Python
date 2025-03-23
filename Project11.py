cards = [11,2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
import random



def print_all():
    print(f" Your cards: {random_cards_user}, current score: {adding_random_cards_user}")
    print(f" Computer's first card: {random_cards_computer}")

def final_hand():
    print(f"   Your cards: {random_cards_user}, Final score: {adding_random_cards_user}")
    print(f"   Computer's Final hand: {random_cards_computer}, Final score: {adding_random_cards_computer}")



game_over = False
while game_over is False:
    comp_1 = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
    adding_random_cards_user = 0
    adding_random_cards_computer = 0

    if comp_1 == "n":
        exit()
    elif comp_1 == "y":
        game_over = False
        print("""
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
""")
        random_cards_user = random.sample(cards, 2)
        random_cards_computer = [random.choice(cards)]

    # adding user cards
        for x in random_cards_user:
            adding_random_cards_user += x
        print_all()

        for x in random_cards_computer:
            adding_random_cards_computer +=x

    another_card = True
    while another_card is True:
        if adding_random_cards_user < 21:
            hit_me = input("Type 'y' to get another card, type 'n' to pass: ").lower()
            if hit_me == "y":
                random_another_card_user = random.choice(cards)
                adding_random_cards_user += random_another_card_user
                random_cards_user.append(random_another_card_user)
                print_all()

                if adding_random_cards_user > 21:
                    if 11 in random_cards_user:
                        random_cards_user.remove(11)
                        random_cards_user.append(1)
                        final_hand()
                    else:
                        final_hand()
                        print("You went over. You  lose")
                        break

                elif adding_random_cards_user == adding_random_cards_computer:
                    print("Draw")
                    break


                elif adding_random_cards_computer == 21:
                    print("Computer got Blackjack!, You lose")
                    break


                elif adding_random_cards_user == 21:
                    print("You got Blackjack! You won! ")
                    break


                elif adding_random_cards_user > adding_random_cards_computer:
                    print("You win!")
                    break

                elif adding_random_cards_user < adding_random_cards_computer:
                    print("You Lose")
                    break

            else:
                while adding_random_cards_computer < 17:
                    random_another_card_computer = random.choice(cards)
                    adding_random_cards_computer += random_another_card_computer
                    random_cards_computer.append(random_another_card_computer)
                final_hand()

                if adding_random_cards_computer > 21:
                    if 11 in random_cards_computer:
                        random_cards_computer.remove(11)
                        random_cards_computer.append(1)
                        final_hand()
                    else:
                        final_hand()
                        print("Computer went over. You win!")
                        break

                elif adding_random_cards_user == adding_random_cards_computer:
                    print("Draw")
                    break


                elif adding_random_cards_computer == 21:
                    print("Computer got Blackjack!, You lose")
                    break


                elif adding_random_cards_user == 21:
                    print("You got Blackjack! You won! ")
                    break


                elif adding_random_cards_user > adding_random_cards_computer:
                    print("You win!")
                    break

                elif adding_random_cards_user < adding_random_cards_computer:
                    print("You Lose")
                    break










