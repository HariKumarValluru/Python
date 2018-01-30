greeting = "Hari"
_myName = "Naga"
Hari24 = "Venkata"
Hari_Kumar = "Anil"
Greeting = "Hello"
print(Greeting + ' ' + greeting)

age = 27
print(age)
#print(Greeting + age)

# data types
a = 12
b = 3
print (a+b)
print (a-b)
print(a*b)
print(a/b)
print (a//b) # if we want to trun the value into integer we use //
print(a%b)

#loop
for i in range(1, a//b):
    print(i)

print(a+b/3-4*12) # multiplication and division has higher precedence
print(8/2*3)
print(8*3/2)

print ((((a+b)/3) - 4)*12)

c = a+b
d = c/3
e = d - 4
print(e*12)

parrot = "Norwegian Blue"
print(parrot)
print(parrot[0])
print(parrot[4])
print(parrot[-1]) # we will get the last letter of the string
print(parrot[0:6]) # we will get starting six characters from the string
print(parrot[:6]) # same as above
print(parrot[6:]) # we will get all character from sixth letter
print(parrot[-4:-2])
print(parrot[0:6:2]) # 2 is the how many characters we have to skip
print(parrot[0:6:3]) # 3 is the how many characters we have to skip

number = "9,223,372,584,444,554,766"
print(number[1::4])

numbers = '1, 2, 3, 4, 5, 6, 7, 8, 9'
print(numbers[0::3])

string = "he's"
string2 = "probably"
print (string+" "+string2)
print("Hello " *5)
print("Hello " *(5 +4))

today = "Friday"
print("day" in today) # finding characters in a string
print("fri" in today)
print("thrus" in today)