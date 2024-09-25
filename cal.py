# This function adds two numbers def add(x, y):
return x + Y
# This function subtracts two numbers def subtract(x, y): return x -y
# This function multiplies two numbers def multiply(x, y): return x * Y
# This function divides two numbers def divide(x, y): return x / y
print("Select operation.") print("l .Add") print("2.Subtract") print("3.Multiply") print("4.Divide")
while True:
# take input from the user choice = input("Enter choice(l /2/3/4): ")
# check if choice is one of the four options if choice in (I l l, 1 21, 1 3 1, 14 1): try:
numl =   first number: ")) num2 = float(input("Enter second number: ")) except ValueError:
print("lnvalid input. Please enter a number.") continue
if choice 	I l  print(numl, "+", num2, - add(numl, num2)) elif choice 2 
	print(numl,	, num2,	, subtract(numl, num2))
elif choice 1 3  print(numl, * , num2, , multiply(numl, num2))
1
elif choice 	4  print(numl, "/", num2,	divide(numl , num2))
# check if user wants another calculation # break the while loop if answer is no next_calculation = input("Let Is do next calculation? (yes/no): ") if next calculation "no". break else:
print("lnvalid Input")
