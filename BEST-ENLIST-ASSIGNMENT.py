# strings
#how to print a value:
print("30 days 30 hour Challenge")
print('30 days 30 hour Challenge')
#Assigning string to variables
Hours = "thirty"
print(Hours)

#indexing using strings
Days = "Thirty days"
print(Days[0])

#How to print the particular character from certain text?
Challenge = "i will win"
print(Challenge[7:10])
#print the length of character
Challenge = "i will win"
print(len(Challenge))

#Convert string into lowercase
Challenge  = "i will win"
print(Challenge.lower())

#string concatenation
a = "30 Days"
b = "30 hours"
c = a+b
print(c)

#Adding space in between string of concatenation
a = "30 days"
b = "30 hour challenge"
c = a + " " + b
print(c)

#casefold() - usage
text = "Thirty Days And Thirty Hours"
x = text.casefold()
print(x)

#capitalize
text = "thirty days and thirty hours"
x = text.capitalize()
print(x)

#find
text = "Thirty days and thirty hours"
x = text.find("t")
print(x)

#isalpha
text = "Thirty Days And Thirty Hours"
x = text.isalpha()
print(x)

#isalnum
text = "Thirty Days And Thirty Hours"
x = text.isalnum()
print(x)