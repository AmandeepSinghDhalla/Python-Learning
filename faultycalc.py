print("Calcuation's for two numbers")

print("Enter first number: ")
num1 = int(input())
print("Enter second number: ")
num2 = int(input())
print("What calculation do you want '+','-', '*' or '/'")
operator = input()

if num1 == 45 and num2 == 3 and operator == '*':
    print("Answer: 555")
elif num1 == 56 and num2 == 9 and operator == '+':
    print("Answer: 77")
elif num1 == 56 and num2 == 6 and operator == '/':
    print("Answer: 4")
elif operator == '+':
    print(num1 + num2)
elif operator == '-':
    print(num1 - num2)
elif operator == '*':
    print(num1 * num2)
elif operator == '/':
    print(num1 / num2)