def fizz_buzz(a):
    if (a % 3 == 0) and (a % 5 == 0): #in cases of such programming, we put the and value or both values to be checked first
        return "fizzbuzz"               # so that all the conditions are satisfied
    if (a % 3) == 0:
        return "fizz"
    if (a % 5) == 0:
        return "buzz"
    else:
        return f"{a} is divisible by neither 3 nor 5."

a = int(input("Enter a number: "))
print(fizz_buzz(a))
