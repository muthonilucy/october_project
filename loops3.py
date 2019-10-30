circles = [7,8,9,45,2,13,34,31,21]
#to store results after calculations
#empty list to add data into
results = []
for radius in circles:
    area = 3.14*radius**2
    print(area,"area of a circle whose radius is",radius)
    results.append(area)#adds the data into the empty list
print(results)