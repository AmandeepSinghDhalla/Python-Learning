print('Guess a number between 1 and 25')
print("You will only get 9 guesses!")
total_guess = 0

while total_guess <= 9:
    gn = int(input())

    if gn < 13:
        total_guess += 1
        print("You guessed smaller number, try again!")
        print(f"Total guesses used: {total_guess}")
        continue
    elif gn > 13:
        total_guess += 1
        print("You guessed larger number, try again!")
        print(f"Total guesses used: {total_guess}")
        continue
    else:
        print("Congrats, you guessed correct number.")
        print(f"Total guesses used: {total_guess}")
        break
if total_guess > 9:
    print("Game over! You used all your guesses")
