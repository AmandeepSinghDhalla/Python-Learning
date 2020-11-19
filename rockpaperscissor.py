import random

list = ["Rock", "Paper", "Scissor"]

i = 0
cw = 0
uw = 0

while i < 10:
    print("Game of Rock Paper Scissor")
    print("Put either one Rock Paper Scissor")
    comp = random.choice(list)
    in1 = input()
    user = in1.capitalize()
    if comp == user:
        print(f"Computer played {comp}")
        print("Match Draw!")
        print()
        i += 1
    elif comp == 'Rock' and user == 'Paper':
        print(f"Computer played {comp}")
        uw += 1
        print(f"You won. Score Computer: {cw} Player: {uw}")
        print()
        i += 1
    elif user == 'Rock' and comp == 'Paper':
        print(f"Computer played {comp}")
        cw += 1
        print(f"Computer won. Score Computer: {cw} Player: {uw}")
        print()
        i += 1
    elif comp == 'Rock' and user == 'Scissor':
        print(f"Computer played {comp}")
        cw += 1
        print(f"Computer won. Score Computer: {cw} Player: {uw}")
        print()
        i += 1
    elif user == 'Rock' and comp == 'Scissor':
        print(f"Computer played {comp}")
        uw += 1
        print(f"You won. Score Computer: {cw} Player: {uw}")
        print()
        i += 1
    elif user == 'Paper' and comp == 'Scissor':
        print(f"Computer played {comp}")
        cw += 1
        print(f"Computer won. Score Computer: {cw} Player: {uw}")
        print()
        i += 1
    elif comp == 'Paper' and user == 'Scissor':
        print(f"Computer played {comp}")
        uw += 1
        print(f"You won. Score Computer: {cw} Player: {uw}")
        print()
        i += 1

print(f"Final Score Computer: {cw} Player: {uw}")