name = input("Please enter your name: ")
age = int(input("How old are you, {}?: ".format(name)))
if name and (18 <= age <=30):
    print('Welcome to club 18-30 holidays, {}'.format(name))
else:
    print("I'm Sorry, our holidays are only for seriously cool people")