# for x in range(1,21):
#     if x%2 != 0:
#         print(x)#prints odd numbers

# give a margin that the numbers skip
for y in range(0,100,5):
    print(y)

# start from 100 to 0 with margin on 10
print("\nNext set of numbers")
for z in range(100,0,-10):
    print(z)

# prime numbers
print("\nPrime numbers")
for prime in range(0, 100):
    if prime == 2 or prime == 3 or prime == 5 or prime == 7:
        print(prime)
    elif prime % 2 != 0 and prime % 3 != 0 and prime % 5 != 0 and prime % 7 != 0 and prime != 1:
        print(prime)

