drinks = ['soda','milk','tea','juice']
print(drinks[0])
#print(drinks)

#to replace the first word in the list..
drinks[0] = 'coke'

print(drinks)

#adding items to a list
drinks.append('coffee')
print(drinks)

#removing an item from a list using del
del drinks[0]
print(drinks)

#removing an item using pop function
statement = 'take not of the next method'
print(statement)
print(drinks)
popped_drink = drinks.pop()
print(popped_drink)
