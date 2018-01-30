# name = input("Please enter your name: ")
# age = int(input("How old are you, {}? ".format(name)))
# print(age)
#
# if age >= 18:
#     print("You are old enough to vote")
# else:
#     print("Please come back in {} years".format(18-age))

print("Please guess the number from 1 to 10")
guess = int(input())
if guess <= 5:
    print("Plese guess higher")
    guess = int(input())
    if guess == 5:
        print("Well done, you guessed it")
    else:
        print("Sorry, you have not guessed correctly")
elif guess >= 5:
    print("Please guess lower")
    guess = int(input())
    if guess == 5:
        print("Well done, you guessed it")
    else:
        print("Sorry, you have not guessed correctly")
else:
    print("You got it first time")