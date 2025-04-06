import random
from Project13a import data
from Project13b import logo, vs


def a_b_format_draft():
    a_result = data[number_rand_1]
    b_result = data[number_rand_2]
    a_format = f'{a_result["name"]}, {a_result["description"]}, from {a_result["country"]}.'
    a_follower = f'{a_result["follower_count"]}'
    b_format = f'{b_result["name"]}, {b_result["description"]}, from {b_result["country"]}.'
    b_follower = f'{b_result["follower_count"]}'
    return a_format, b_format, int(a_follower), int(b_follower)


def compare_followers(a,b):
    if a < b:
        return "b"
    else:
        return "a"






current_score = 0
game_over = False
while game_over is False:
    number_rand_1 = random.randint(0, len(data) - 1)
    number_rand_2 = random.randint(0, len(data) - 1)

    if number_rand_1 == number_rand_2:
        number_rand_1 = random.randint(0, len(data) - 1)

    def right_answer():
        if compare_followers(a_b_format_draft()[2], a_b_format_draft()[3]) == "b":
            return a_b_format_draft()[1]
        else:
            return a_b_format_draft()[0]


    compare_a = f"Compare A: {a_b_format_draft()[0]}"
    compare_b = f"Against B: {a_b_format_draft()[1]}"

    com_follow = compare_followers(a_b_format_draft()[2],a_b_format_draft()[3])

    print(logo)
    print(compare_a)
    print(vs)
    print(compare_b)

    followers_choice = input("Who has more followers? Type 'A' or 'B': ").lower()


    correct = True
    while correct is True:
        if followers_choice == com_follow:
            current_score += 1
            print(f"You're Right! Current score: {current_score} ")
            compare_a = f"Compare A: {right_answer()}"
            number_rand_2 = random.randint(0, len(data) - 1)
            compare_b = f"Against B: {a_b_format_draft()[1]}"
            com_follow = compare_followers(a_b_format_draft()[2], a_b_format_draft()[3])
        else:
            print(f"Sorry, that's wrong. Final score: {current_score}")
            game_over = True
            correct = False
            exit()


        print(compare_a)
        print(vs)
        print(compare_b)
        followers_choice = input("Who has more followers? Type 'A' or 'B': ").lower()




