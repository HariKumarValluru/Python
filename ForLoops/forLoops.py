# for i in range(1,20):
#     print("i is now {}".format(i))
#
# number = "9,114,665,224,744,811";
# for i in range(0, len(number)):
#     print(number[i])

# number = "9,114,665,224,744,811"
# for i in range(0, len(number)):
#     if number[i] in '0123456789':
#         print(number[i],end='')

number = "9,114,665,224,744,811"
cleanedNumber = ""
for i in range(0, len(number)):
    if number[i] in '0123456789':
        cleanedNumber = cleanedNumber + number[i]
newNumber = int(cleanedNumber)
print(newNumber)

number = "9,114,665,224,744,811"
cleanedNumber = ""
for char in number:
    if char in '0123456789':
        cleanedNumber = cleanedNumber + char
newNumber = int(cleanedNumber)
print(newNumber)

for state in ['not pinin','no more','a stiff','bereft of life']:
    print("This parrot is "+state)

for i in range(0,100,5):
    print("i is {}".format(i))

for i in range(1,12):
    for j in range(1,13):
        print("{1} times {0} is {2}".format(i,j,i*j))
    print("===============")