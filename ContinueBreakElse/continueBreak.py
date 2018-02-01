# Continue example
# shoppingList = ['milk', 'pasta', 'eggs', 'spam', 'bread', 'rice']
# for item in shoppingList:
#     if item == 'spam':
#         continue
#     print('Buy '+item)

# Break example 1

#
# shoppingList = ['milk', 'pasta', 'eggs', 'spam', 'bread', 'rice']
# for item in shoppingList:
#     if item == 'spam':
#         break
#     print('Buy '+item)

# Break example 2

# meal = ['egg', 'backon', 'spam', 'sausages']
# nastyFoodItem = ""
# for item in meal:
#     if item == 'spam':
#         nasty_item = item
#         break
# if nasty_item:
#     print("Can't I have anything without spam in it")

# else example (else will be used in for loops)

meal = ['egg', 'beckon', 'beans', 'sausages']
nasty_food_item = ""
for item in meal:
    if item == 'spam':
        nasty_food_item = item
        break
else:
    print("I will have plate of them, then, please")

if nasty_food_item:
    print("Can't I have anything without spam in it")
