#What we need:
#----------------------------------------
#[LAST NAME], [first name]
#[Job title]
#ID: [id number]

#[email address]
#[phone number]
#[eye color]
#[height]
#----------------------------------------
#The stretch challenges for this activity are:

#    Add hair color and eye color and put them both on the same line in the display.

  
print('Please enter the following information:')

first_name = input ('First name: ')
last_name = input('Last name: ')
job_title = input('Job title: ')
id_number = input('ID number: ')

email = input('email: ')
phone_number = input('Phone Number: ')
eye_color = input('Eye color: ')
height = input('Height in feet: ')
hair_color = input('What is your hair color? ')
favorite_color = input('Favorite color: ')
month = input('What month did you begin working: ')
training_status = input('Have you done advanced training? ')

print('Your ID is: ')
print('--------------------------------------')
print(f'{last_name.upper()}, {first_name.capitalize()}')
print(f'{job_title.capitalize()}')
print(f'{id_number}')
print('   ')
print(f'{email.lower()}')
print(f'{phone_number}') 
print(f'Hair: {hair_color:15} Eyes: {eye_color.capitalize()}')
print(f'Month: {height:14} Training: {training_status}')
print('--------------------------------------')
      
      