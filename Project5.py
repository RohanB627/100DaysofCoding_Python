# student_score = [180,124,165,173,189,169,146]

# max = 0
# for score in student_score:
#     if score > max:
#         max = score
# print(max)

# total = []
# for number in range (1,101,1):
#     total.append(number)
#     # total = number =+ number
# print(sum(total))



# Fizz_Buzz = 0
# for number in range(1,101):
#     Fizz_Buzz =+ number
#     if number % 3 == 0 and number % 5 == 0:
#         print ("FizzBuzz")
#         continue
#     elif number % 3 == 0:
#         print("Fizz")
#         continue
#     elif number % 5 == 0  :
#         print("Buzz")
#         continue
#     print(Fizz_Buzz)

import random
letters =['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['0', '1', '2','3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '£', '$', '%', '^', '(', ')']

print ("Welcome to the PyPassword Generator!")
nr_letter = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like in your password?\n"))
nr_numbers = int(input("How many numbers would you like in your password?\n") )

rand_letters = random.sample(letters,nr_letter)
rand_symbols = random.sample(symbols,nr_symbols)
rand_numbers = random.sample(numbers,nr_numbers)

fin_pass = ""
new_pass = rand_letters + rand_symbols + rand_numbers
rand_new_pass = random.shuffle(new_pass)
new_fin_pass = fin_pass.join(new_pass)
print(f"\nYour new password should be: {new_fin_pass}")