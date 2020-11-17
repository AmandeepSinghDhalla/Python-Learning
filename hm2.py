def main():
    print("Enter 1 to log and 2 to retrive")
    opt3 = int(input())
    if opt3 == 1:
        log()
    elif opt3 == 2:
        read()

def getdate():
    import datetime
    return datetime.datetime.now()

def log():
    print("1 for Harry, 2 for Rohan, 3 for Hammad")
    opt1 = int(input())
    print("Input 1 for Diet and 2 for Exercise")
    opt2 = int(input())
    if opt1 == 1 and opt2 == 1:
        with open("harry_diet.txt", "a") as f:
            hd = input("Enter: ")
            f.write(f"{hd}")
            f.write("\n")
            print("Log added sucessfully!")
    elif opt1 == 1 and opt2 == 2:
        with open("harry_exercise.txt", "a") as f:
            he = input("Enter: ")
            f.write(f"{he}")
            f.write("\n")
            print("Log added sucessfully!")
    elif opt1 == 2 and opt2 == 1:
        with open("rohan_diet.txt", "a") as f:
            rd = input("Enter: ")
            f.write(f"{rd}")
            f.write("\n")
            print("Log added sucessfully!")
    elif opt1 == 2 and opt2 == 2:
        with open("rohan_exercise.txt", "a") as f:
            re = input("Enter: ")
            f.write(f"{re}")
            f.write("\n")
            print("Log added sucessfully!")
    elif opt1 == 3 and opt2 == 1:
        with open("hammad_diet.txt", "a") as f:
            had = input("Enter: ")
            f.write(f"{had}")
            f.write("\n")
            print("Log added sucessfully!")
    elif opt1 == 3 and opt2 == 2:
        with open("hammad_exercise.txt", "a") as f:
            hae = input("Enter: ")
            f.write(f"{hae}")
            f.write("\n")
            print("Log added sucessfully!")

def read():
    print("1 for Harry, 2 for Rohan, 3 for Hammad")
    opt1 = int(input())
    print("Input 1 for Diet and 2 for Exercise")
    opt2 = int(input())
    if opt1 == 1 and opt2 == 1:
        with open("harry_diet.txt") as f:
            hd = f.read()
            print("At Date and Time", str(getdate()))
            print(hd)
    elif opt1 == 1 and opt2 == 2:
        with open("harry_exercise.txt") as f:
            he = f.read()
            print("At Date and Time", str(getdate()))
            print(he)
    elif opt1 == 2 and opt2 == 1:
        with open("rohan_diet.txt") as f:
            rd = f.read()
            print("At Date and Time", str(getdate()))
            print(rd)
    elif opt1 == 2 and opt2 == 2:
        with open("rohan_exercise.txt") as f:
            re = f.read()
            print("At Date and Time", str(getdate()))
            print(re)
    elif opt1 == 3 and opt2 == 1:
        with open("hammad_diet.txt") as f:
            had = f.read()
            print("At Date and Time", str(getdate()))
            print(had)
    elif opt1 == 3 and opt2 == 2:
        with open("hammad_exercise.txt") as f:
            hae = f.read()
            print("At Date and Time", str(getdate()))
            print(hae)

main()