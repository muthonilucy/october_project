guestlist = ['lucy','mercy','johnson','kennedy','wesley','Pamela']
#prints out the last item in the list will not be able to attend
print('Unfortunately'+' '+guestlist[-1].title()+' '+'will not be able to attend')

#print a different person to attend instead
removedguest = guestlist.pop()
print(guestlist)
#display removed guest
print('we are replacing '+removedguest.title()+' with charles')

#adding charles into the list as number 4
guestlist.insert(-3,'Charles')
print(guestlist)

#sorting a list
print('\nOriginal list')
print(guestlist)

print('\nTemporarily sorted list')
print(sorted(guestlist))

data12 = len(guestlist)
print(data12)
