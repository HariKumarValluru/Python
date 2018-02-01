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