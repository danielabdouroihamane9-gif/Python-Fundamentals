#12 STRING METHODS:
''' Length (len) '''
name = input("Enter your full name: ")
result = len(name)
print(result)

''' Find (X.find) the first latter and (X.rfind) the last latter, start counting by 0 '''
result = name.find("a")
result1 = name.rfind("d")
print(result)
print(result1)

''' Capitalize (X.capitalize) the first letter and (X.upper) all the latters or the opposite lowercase all (X.lower)  '''
result = name.capitalize()
result1 = name.upper()
result2 = name.lower()
print(result)
print(result1)
print(result2)

''' Digit number (X.isdigit) it will return by True(if only numbers) or False(if contains latters) and Opposite(X.isalpha) / both (X.isalnum) '''
name = "bro124"
result = name.isdigit()
name1 = "Abdou"
result1 =  name1.isalpha()
print(result)
print(result1)

''' Counting (X.count) it will give how many are there.'''
phone_number = "1-452-869-5803"
result = phone_number.count("-")
print(result)

''' Replacement (X.replace) it will change the old value given to a new one'''
phone_number = "1-452-869-5803"
result1 = phone_number.replace("-", " ")
print(result1)

''' Variety of string methods: tape this'''
print(help(str))


# EXERCISE: For String Methods.
'''          validate user input exercise
        1. username is no more than 12 characters
        2. username must not contain spaces
        3. username must not contain digits
'''
username = input("Enter your full name: ")

if len(username) > 12:
    print("Your name is more than 12 characters!")
elif not username.find(" ") == -1:
    print("Your name contains spaces!")
elif not username.isalpha() == True:
    print("Your name contains digits")
else:
    print(f"Hello {username}!")



