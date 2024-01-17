# How old are you? 25
# On your next birthday, you will be 26

# How many egg cartons do you have? 3
# You have 36 eggs

# How many cookies do you have? 18
# How many people are there? 8
# Each person may have 2.25 cookies

age = int(input('How old are you? '))
age = age + 1
print("On your next birthday, you will be " + str(age) + " years old.")

print(" ")

egg_cartons = int(input('How many egg cartons do you have? '))
egg_cartons = egg_cartons + 1
print(f'You have {egg_cartons} egg cartons.')

print(" ")

cookies = int(input('How many cookies do you have? '))
cookies = cookies + 1
people = int(input('How many people are there? '))
cookie_fraction = cookies/people
print('Each person will have ' + str(float(cookie_fraction)) + ' cookies.')