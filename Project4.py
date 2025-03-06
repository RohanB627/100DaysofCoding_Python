import random

# random_number = random.randint(0,1)
# if random_number == 0:
#     print("Heads")
# else:
#     pri nt("Tails")

# friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
# ran_name = random.choice(friends)
# print(ran_name) 

print("Welcome to Rock, Paper and Scissors Competition with the computer!")
User_choose = int(input('What do you choose? Type "0" for Rock, "1" for Paper or "2" for Scissors\n'))


rock = ('''                                  88         
                                  88         
                                  88         
8b,dPPYba,  ,adPPYba,   ,adPPYba, 88   ,d8   
88P'   "Y8 a8"     "8a a8"     "" 88 ,a8"    
88         8b       d8 8b         8888[      
88         "8a,   ,a8" "8a,   ,aa 88`"Yba,   
88          `"YbbdP"'   `"Ybbd8"' 88   `Y8a  ''')

paper = ('''
8b,dPPYba,  ,adPPYYba, 8b,dPPYba,   ,adPPYba, 8b,dPPYba,  
88P'    "8a ""     `Y8 88P'    "8a a8P_____88 88P'   "Y8  
88       d8 ,adPPPPP88 88       d8 8PP""""""" 88          
88b,   ,a8" 88,    ,88 88b,   ,a8" "8b,   ,aa 88          
88`YbbdP"'  `"8bbdP"Y8 88`YbbdP"'   `"Ybbd8"' 88          
88                     88                                 
88                     88 ''')

scissors = ('''                     88                                                       
                     ""                                                       
                                                                              
,adPPYba,  ,adPPYba, 88 ,adPPYba, ,adPPYba,  ,adPPYba,  8b,dPPYba, ,adPPYba,  
I8[    "" a8"     "" 88 I8[    "" I8[    "" a8"     "8a 88P'   "Y8 I8[    ""  
 `"Y8ba,  8b         88  `"Y8ba,   `"Y8ba,  8b       d8 88          `"Y8ba,   
aa    ]8I "8a,   ,aa 88 aa    ]8I aa    ]8I "8a,   ,a8" 88         aa    ]8I  
`"YbbdP"'  `"Ybbd8"' 88 `"YbbdP"' `"YbbdP"'  `"YbbdP"'  88         `"YbbdP"'  ''')

items = [rock, paper, scissors]

print("\nYou chose: \n\n", items[User_choose])

computer_choose = random.randint(0,2)
print("\nComputer chose: \n", items[computer_choose])

# Rock 0 beats scissors 
# Scissors 2 beats paper
# Paper 1 beats rock

if User_choose == 0 and computer_choose == 2:
    print("\nYou win!")
elif User_choose == 1 and computer_choose == 0:
    print("\nYou win")
elif User_choose == 2 and computer_choose == 1:
    print("\nYou win")
elif User_choose == 0 and computer_choose == 0:
    print("\nIt's a Draw, Try again?")
elif User_choose == 1 and computer_choose == 1:
    print("\nIt's a Draw, Try again?")
elif User_choose == 2 and computer_choose == 2:
    print("\nIt's a Draw, Try again?")
else:
    print("\nComputer wins")




