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
    elif (comp == 'Rock' or user == 'Rock') and (user == 'Paper' or comp == 'Paper'):
        print(f"Computer played {comp}")
        if comp == 'Rock':
            uw += 1
            print(f"You won. Score Computer: {cw} Player: {uw}")
        elif user == 'Rock':
            cw += 1
            print(f"Computer won. Score Computer: {cw} Player: {uw}")
        print()
        i += 1
    elif (comp == 'Rock' or user == 'Rock') and (user == 'Scissor' or comp == 'Scissor'):
        print(f"Computer played {comp}")
        if comp == 'Rock':
            cw += 1
            print(f"Computer won. Score Computer: {cw} Player: {uw}")
        elif user == 'Rock':
            uw += 1
            print(f"You won. Score Computer: {cw} Player: {uw}")
        print()
        i += 1
    elif (user == 'Paper' or comp == 'Paper') and (comp == 'Scissor' or user == 'Scissor'):
        print(f"Computer played {comp}")
        if comp == 'Paper':
            uw += 1
            print(f"You won. Score Computer: {cw} Player: {uw}")
        elif user == 'Paper':
            cw += 1
            print(f"Computer won. Score Computer: {cw} Player: {uw}")
        print()
        i += 1
print(f"Final Score Computer: {cw} Player: {uw}")
