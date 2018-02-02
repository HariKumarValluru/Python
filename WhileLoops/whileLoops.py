# for i in range(10):
#     print("i is now {}".format(i))

# i = 0
# while i < 10:
#     print("i is now {}".format(i))
# i += 1

# available_exits = ['East', "West", "North", "South"]
# choosen_exit = ''
# while choosen_exit not in available_exits:
#     choosen_exit = input("Please choose a direction: ")
# print("aren't you glade you got out there!")

# available_exits = ['East', "West", "North", "South"]
# choosen_exit = ''
# while choosen_exit not in available_exits:
#     choosen_exit = input("Please choose a direction: ")
#     if choosen_exit == "quit":
#         print("Game Over!")
#         break
# else:
#     print("aren't you glade you got out there!")

import random

highest = 10
answer = random.randint(1, highest)

print("Please guess a number between 1 to {}: ".format(highest))
guess = int(input())

if guess != answer:
    if guess < answer:
        print("Please guess higher: ")
    else:
        print("Please guess lower: ")
    guess = int(input())
    if guess == answer:
        print("Well done, you guessed it!")
    else:
        print("Sorry, you have not guessed correctly")
else:
    print("You got it in first time")
