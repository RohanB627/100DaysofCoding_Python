# # print("Welcome to Odd and Even calculator.")
# # Number = int(input("Enter the Number: "))
# # Result = Number % 2 

# # if Result == 1:
# #     print("Odd")
# # else:
# #     print("Even")

# print("Welcome to the Python Pizza Deliveries!")
# bill = 0
# size = str(input("What size of Pizza do you want? S, M or L: "))
# if size == "L":
#     bill = 25
# elif size == "M":
#     bill = 20
# else:
#     bill = 15
# print(bill)

# Pepperoni = input("Do you want pepperoni on your pizza? Type Y or N: ")
# if Pepperoni == "Y":
#     if size == "S":
#         bill += 2
#     else:
#         bill += 3
# else:
#     bill += 0
# print(bill)

# extra_cheese = input("Do you want extra cheese? Type Y or N: ")
# if extra_cheese == "Y":
#     bill += 1
# else:
#     bill += 0

# print(f"Your final bill is Euro {bill}")

# print("Welcome to the rollercoster!")
# height = int(input("What is your height in cm? "))
# bill = 0

# if height >= 120:
#     print("you can ride the rollercoaster!")
#     age = int(input("What is your age? "))
#     if age < 12:
#         bill = 5
#         print ("Child tickets are Euro: 5")
#     elif age <=18:
#         bill =7
#         print("Youth tickets are Euro: 7")
#     elif age>=45 and age<=55:
#         bill = 0
#         print ("you already are on a rollercoster! so you can ride this one for free! ")
#     else: 
#         bill = 12

# print(f"your ticket is {bill}")


print('''

              ,
          _,-""-._
        ,"        ".
       /    ,-,  ,"\
      "    /   \ | o|
      \    `-o-"  `-',
       `,   _.--'`'--`
         `--`---'                    |   _)
           ,' '      _  /  _ \  ` \   _ \ |  -_)
         ./ ,  `,    ___|\___/_|_|_|_.__/_|\___|
         / /     \
        (_)))_ _,"
           _))))_,
  --------(_,-._)))-------------------------------
''')
print("Welcome to the Zombie running game")
print("your mission is to survive!")
# you can also use .lower() next to the sentence it will allow the input to be taken as lower case in the "First" variable


First = input('Choose left or right? Type "left" or "right" ')
if First == "left" or First == "Left":
    print("OMG! there are more zombies....")
    run_hide = input("Do you want to run or hide? Type run or hide ")
    if run_hide == "run" or run_hide == "Run":
        print("oh no! what have you done! they can hear you now because of your heel shoes and running towards you!")
        opportunity = input('Phew! you outran the horde! but there is a mysterious figure coming towards you? Do you want to "wait" or "hide"? ')
        if opportunity == "wait" or opportunity == "Wait":
            print("the mysterious figure is a human! and he is a part of the SWAT team here to save you! Hurrah you are saved! You win! ")
        else: 
            print ("You hid next to the zombie, and he is awake! he likes the smell of you, so he bites you and you become a zombie, Game over! ")
    else:
      print("Oh no, there was a zombie lying next to the spot you were hiding...he bit you and you became a zombie, Game over")
else:
    print("the zombie knew you would take this step so found you and He bit you and you became a zombie!, Game over. ")
