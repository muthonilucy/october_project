# creating a dictionary about an item
item_1 = {'color': 'green', 'size': 15}
print(item_1['color'])
print(item_1)

# adding new information to the dictionary
print("\nAdding new information about height and width to the dictionary")
item_1['height'] = 10
item_1['width'] = 12
print(item_1)

# start with empty dictionary
print("\nyou can start with an empty dictionary")
item_2 = {}
item_2['weight'] = '30kg'
item_2['color'] = 'yellow'
item_2['texture'] = 'rough'
item_1['height'] = 12
print(item_2)

# for loop
print("\nFor loop:")
for key, value in item_2.items():
    # print("\nKey: " + key)
    # print("\nValue: " + value)
    print("\nkey: " + key + " value: " + value)
