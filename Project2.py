# print("hello"[4])
# print(1234)

# print(len("Hello"))
# print(type("Hello"))
# print(type(1234))
# print(type(12.34))
# print(type(True))

# print("Number of letters in your name: " + str(len(input("Enter your name: "))))

# print(3*(3+3)/3-3)

print("Welcome to the tip calculator")
Bill = float(input("What was the total bill? "))


Tip = int(input("How much tip would you like to give? 10, 12 or 15? "))
Adj_Tip = (Tip / 100)+1
Adj_Bill= (Bill*Adj_Tip)

People = int(input("How many people to split the bill? "))
Final_cal = (Adj_Bill / People)
Adj_Final = round(Final_cal,2)


print(f"Each person should pay: ${Adj_Final}")