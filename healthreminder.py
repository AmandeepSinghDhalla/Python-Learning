from time import time
import pygame
import datetime

# Main function
def main():  # initialising time to play reminder
    towater = time()
    toeye = time()
    toexercise = time()
    eyetime = 35*60
    exercisetime = 40*60
    watertime = 45*60
    while True:
        if time() - towater > watertime:
            water()
        elif time() - toeye > eyetime:
            eye_exercise()
        elif time() - toexercise > exercisetime:
            physical_exercise()

def getdate():
    return datetime.datetime.now()

# To drink a total of 3.5-liter water after some time interval between 9-5 pm.
# For Water, the user should enter “Drank”
def water():
    print("Water Alert, drink 200 ml water")
    pygame.mixer.init()
    pygame.mixer.music.load("water.mp3")
    pygame.mixer.music.play()
    while True:
        stp = input("Enter stop to stop music: ")
        if stp == 'stop':
            pygame.mixer.music.stop()
            break
    print("Enter 'Drank' when done.")
    while True:
        ans = input("Enter: ")
        in1 = ans.capitalize()
        if in1 == 'Drank':
            break
    with open("log.txt", "a") as f:
        wat = f"Water drank at {getdate()}"
        f.write(f"{wat}")
        f.write("\n")

# To do eye exercise after every 30 minutes.
# For Eye Exercise, the user should enter “EyeDone”
def eye_exercise():
    print("Eye exercise Alert, do some exercise to rest your eyes")
    pygame.mixer.init()
    pygame.mixer.music.load("eye.mp3")
    pygame.mixer.music.play()
    while True:
        stp = input("Enter stop to stop music: ")
        if stp == 'stop':
            pygame.mixer.music.stop()
            break
    print("Enter 'Eyedone' when done.")
    while True:
        ans = input("Enter: ")
        in1 = ans.capitalize()
        if in1 == 'Eyedone':
            break
    with open("log.txt", "a") as f:
        ee = f"Eye Exercise done at {getdate()}"
        f.write(f"{ee}")
        f.write("\n")

# To perform physical activity after every 45 minutes.
# For Physical Exercise, the user should enter “ExDone”
def physical_exercise():
    print("Physical exercise Alert, do some exercise to free your body")
    pygame.mixer.init()
    pygame.mixer.music.load("physical.mp3")
    pygame.mixer.music.play()
    while True:
        stp = input("Enter stop to stop music: ")
        if stp == 'stop':
            pygame.mixer.music.stop()
            break
    print("Enter 'Exdone' when done.")
    while True:
        ans = input("Enter: ")
        in1 = ans.capitalize()
        if in1 == 'Exdone':
            break
    with open("log.txt", "a") as f:
        pe = f"Physical Exercise done at {getdate()}"
        f.write(f"{pe}")
        f.write("\n")

main()