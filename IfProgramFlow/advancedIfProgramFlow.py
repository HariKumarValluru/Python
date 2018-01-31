# age = int(input("How old are you? "))
# if age >= 16 and age <=65:
# if 16 <= age <=65:
#     print("Have a good day at work")
# if age < 16 or age > 65:
#     print("Enjoy your free time")
# else:
#     print("Have a good day at work")

# x = input("Please enter your name: ")
# if x:
#     print('You have entered "{}"'.format(x))
# else:
#     print("You did not enter anything")

# print(not False)
# print(not True)

parrot = "Norwegian Blue"

letter = input("Enter a character: ")

if letter in parrot:
    print("Give me an {}, Bob".format(letter))
else:
    print("I don't need that letter")

if letter not in parrot:
    print("I don't need that letter")
else:
    print("Give me an {}, Bob".format(letter))