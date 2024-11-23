# Asking the user to input three different intergers
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))

# Print the sum of all numbers
sum_all = num1 + num2 +num3
print(f"The sum of all the numbers is: {sum_all}")

# Print the first number minus the second number 
difference = num1 - num2
print(f"The first number minus the second number is: {difference}")

# Print third number multiplied by the first number
multiply = num3 * num1
print(f"The third number multiplied by the first number is: {multiply}")

# Print the sum of all three numbers divided by the third number
division = sum_all / num3
print(f"The sum of all three numbers divided by the third number is: {division}")
