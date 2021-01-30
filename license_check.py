print("Program to check weather you can drive in India or not")
print("Enter age between 7 and 80: ")

while True:
    age = int(input())
    if (7 > age or age > 80):
        print("Invalid response!")
    elif (7 < age <= 80):
        break

if 8 <= age <= 17:
    print("You are underage. You cannot drive.")
elif 18 <= age <= 65:
    print("You can drive.")
    print("You eligible to drive, apply for driving license if not available.")
elif 65<= age <= 80:
    print("You are senior citizen and can drive. But chacha jaan aram se")
    print("You eligible to drive, apply for driving license if not available.")
