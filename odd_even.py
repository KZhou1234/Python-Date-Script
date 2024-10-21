# Write a Python script that takes a number as input and prints whether it is odd or even.

number = input("Please enter a integer here: \n")
if(int(number) % 2 == 0):
    print(f"The number {number} is even.")
else:
    print(f"The number {number} is odd.")