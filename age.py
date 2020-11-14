print("Enter age between 7 and 80: ")

while True:
    age = int(input())
    if 7 < age <= 80:
        break
if 8 <= age <= 17:
    print("You are underage.")
elif 18 <= age <=80:
    print("You can drive.")
else:
    print("Invalid response!")
