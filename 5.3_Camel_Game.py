'''CAMEL
GAME
----------
The
pseudo - code
for how to code this game is in Chapter 5 of the Python Jedi bo
'''

import random

print("Welcome to Camel!")
print("You have borrowed a camel to make your way across the desert.")
print("The natives chasing you to get their camel back")
print()

Miles_Traveled = 0
Thirst = 0
Camel_Tiredness = 0
Natives_Traveled = -20
Full_canteen = random.randrange(3, 12)
canteen = Full_canteen
done = False

while not done:
    nativesBehind = Miles_Traveled - Natives_Traveled

    print()
    print("A. Drink from your canteen.")
    print("B. Ahead at moderate speed.")
    print("C. Ahead full speed.")
    print("D. Stop for the night.")
    print("E. Status check")
    print("Q. Quit.")
    print()
    userInput1 = input("Your choice? ")
    userInput = userInput1.lower()

#A. Drink from your canteen
    if userInput == "a" and not done:
        if canteen == 0:
            print("No water left, you can't take drink.")
        else:
            canteen -= 1
            Thirst = 0
            print("You have quenched your thirst but you only have",canteen,"drink(s) left.")

#B. Ahead at moderate speed
    elif userInput == "b":
        moderateSpeed = random.randrange(5, 12)
        print("You traveled ",moderateSpeed,"miles!")
        Thirst += 1
        Miles_Traveled += moderateSpeed
        Natives_Traveled += random.randrange(7, 14)
        Camel_Tiredness += 1

#C. Ahead full speed
    elif userInput == "c":
        fullSpeed = random.randrange(10, 20)
        print("You traveled ",fullSpeed,"miles!")
        Thirst += 1
        Miles_Traveled += fullSpeed
        Natives_Traveled += random.randrange(7, 14)
        Camel_Tiredness += random.randrange(1, 3)

#D. Stop for the night
    elif userInput == "d":
        Camel_Tiredness = 0
        print("Your camel is happy and fullu rested")
        Natives_Traveled += random.randrange(7, 14)

#E. Status check
    elif userInput == "e":
        print("Miles traveled: ",Miles_Traveled)
        print("Drinks in canteen: ",canteen)
        print("Your camel has ",Camel_Tiredness,"amount of Tiredness.")
        print("The natives are ",nativesBehind,"miles behind you.")

#Q. Quit
    elif userInput == "q":
        done = True

# 1 in 20 chance of finding an oasis
    if random.randrange(1, 20) == 20 and not done:
        Camel_Tiredness = 0
        Thirst = 0
        canteen = Full_canteen
        print("You found an oasis! Both you and your camels to drinks and your canteen is full.")

    if Miles_Traveled >= 200 and not done:
        print("You Won! You crossed the desert successfully!")
        done = True

# watch out for Natives
    if Natives_Traveled >= Miles_Traveled and not done:
        print("The natives caught you.")
        done = True
    elif nativesBehind <= 15 and not done:
        print("The natives are getting close!")

# check if user is thirsty
    if Thirst > 6 and not done:
        print("You died of thirst!")
        done = True
    elif Thirst > 4 and not done:
        print("You are thirsty")

# Check Camel
    if Camel_Tiredness > 8 and not done:
        print("Your camel is dead.")
        done = True
    elif Camel_Tiredness > 5 and not done:
        print("Your camel is Tired.")
