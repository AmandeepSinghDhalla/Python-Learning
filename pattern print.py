print("Enter height between 1 and 8")

while True:
    height = int(input())
    if 1 <= height <= 8:
        break

print("Pick either True or False")
tf = input()
x = tf.capitalize()

if x == str(True):
    for i in range(1, height + 1):
        for j in range(1, i + 1):
            print("*", end="")
        print()
elif x == str(False):
    for i in range(1, height + 1):
        for j in range(1, ((height + 2)- i)):
            print("*", end="")
        print()
