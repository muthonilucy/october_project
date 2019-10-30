text = "I have KES 40 in my account"

# convert to upper case
print(text.upper())
# lower case
print(text.lower())

# replace function a value and specifies how many times
print(text.replace("40", "3000"))

# slicing a word
print(text[0:7])

message = "NEM2343213 Confirmed. You have received KES 3829 from Lucy 0726628638 on 10/10/2019. New MPESA balance is " \
          "KES 40090 "

# pos_is specifies the position of the word is
# index function tells us what position the word is, is located
pos_is = message.index(" is ") + 3
print("Mpesa Balance: ", message[pos_is:])

# find out position of received cash
pos_KES = message.index("KES")
pos_from = message.index("from")
amount = message[pos_KES:pos_from]
print("amount received: ", amount)

# replacing the words
print("amount received: ", amount.replace("KES",""))

# for a character in a word, no spaces are required
pos_fr = message.index(" on ")
pos_07 = message.index("07")
number = message[pos_07:pos_fr]
print("number is: ", number)

# slicing 10character backwards
print(message[pos_fr-11: pos_fr])

# replace function
