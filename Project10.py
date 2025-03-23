print(r""" 
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""
)
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operation = {"+": add, "-": subtract, "*": multiply, "/": divide}

Calculator = True
while Calculator is True:
    user_num = float(input("Type the first number: "))
    user_op = input(" * \n - \n + \n / \n Pick an operation: ")
    user_num2 = float(input("What's the next number: "))

    ans_1 = float(operation[user_op](user_num, user_num2))

    print(f"{user_num} {user_op} {user_num2} = {ans_1}")

    Calculator_2 = True
    while Calculator_2 is True:
        user_con = input(f"Type 'y' to continue calculating with {ans_1}, or type 'n' to start a new calculation: ").lower()

        if user_con == 'n':
            print("\n" * 20)
            break
        else:
            user_num_con = float(input("What's the next number: "))
            user_op_2 = input(" * \n - \n + \n / \n Pick an operation: ")
            ans_2 = operation[user_op_2](ans_1, user_num_con)
            print(f"{ans_1} {user_op_2} {user_num_con} = {ans_2}")
            continue








