# list is mutable
print("lists")
scores = [45, 32, 54, 31, 43, 55, 34, 65, 75, 34, 76, 23]
print(scores[0])
# slicing a list
print(scores[:4])
scores.append(89)
print(scores[-1])

# tuple values cannot be changed ie immutable
print("\nTuples")
marks = (23, 45, 64, 65, 21, 56, 76, 75, 79)
print(marks[0])
# slicing a tuple
print(marks[:4])

# dictionaries key values pairs
print("\nDictionaries")
people = {
    'jane': 23,
    'Ann': 25,
    'Kim': 45,
    'simon': 12,
    'kate': 90
}
print(people)
# error handling
try:
    print(people['janes'])
except:
    # print("Could not print")
    pass

# set ensures everything occurs once, with no repetition
print("\nSet")
results = {10, 10, 10, 38, 27, 37, 27, 28, 48, 48, 38, 29, 19, 19, 29, 11, 21, 11, 30, 43}
print(results)
try:
    print(results[0])
except:
    print("oops error")
print("Printing a values:")
print(results.pop())

results2 = set([34, 23, 45, 12, 10, 10, 19, 19, 19, 2, 60, 48])
# isdisjoint
print(results.isdisjoint(results2))
# common values within the two sets
print("common values in the two sets")
print(results.intersection(results2))