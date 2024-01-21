#Todays teach assignment
#Welcome to the velocity calculator. Please enter the following:
#m = mass (in kg)
#g = acceleration due to gravity (9.8 m/s^2 on Earth, 24 m/s^2 on Jupiter)
#t = time (in seconds)
#p = density of fluid (1.3 kg/m^3 for air, 1000 kg/m^3 for water)
#A = cross sectional area of projectile (in square meters)
#C = drag constant (0.5 for sphere, 1.1 for cylinder falling on it’s side. You could look it up for other shapes.)


#Your inner value of  c = (1 / 2) * p * A * C (round 3 decimal places)

#Your overall velocity is: v(t) = sqrt(mg/c) * (1 - exp((-sqrt(mgc)/m)t))

import math

# Welcome to the velocity calculator. Please enter the following:
print('Welcome to the velocity calculator. Please enter the following values for a: ')
print('Laptop, Car, Loaf of Bread:')
print('')
# Mass (in kg): 5
mass = float(input('Mass (in kg): '))
# Gravity (in m/s^2, 9.8 for Earth, 24 for Jupiter): 9.8
gravity = float(input('Gravity (in m/s^2, 9.8 for Earth, 24 for Jupiter): '))

# Time (in seconds): 10
time_passed = float(input('Time (in seconds): '))
# Density of the fluid (in kg/m^3, 1.3 for air, 1000 for water): 1.3
density_of_fluid = float(input("Density of the fluid ('in kg/m^3, 1.3 for air, 1000 for water): '"))
                               
# Cross sectional area (in m^2): 0.01

cross_sectional_area = float(input('Cross sectional area (in m^2, ): '))
# Drag constant (0.5 for sphere, 1.1 for cylinder): 0.5
drag= float(input("Drag constant (0.5 for sphere, 1.1 for cylinder): "))
                               
                               
c = 0.5 * density_of_fluid * cross_sectional_area * drag

velocity = math.sqrt(mass*gravity/c)*(1-math.exp(-1*math.sqrt(mass*gravity*c)/mass)*time_passed)
                               
                               
# The inner value of c is: 0.003                             
# The velocity after 10.0 seconds is: 67.512 m/s
print(f"Your inner value of c is: {c:.3f}")
print(f"The velocity after 10.0 seconds is: {velocity:.3f} m/s")

print()
#     Try determining the velocity for a few different objects that you know. For example, you might try a bowling ball, a loaf of bread, and a skydiver.

#     Hints: You can find the cross sectional area of a bowling ball by using its radius and calculating the area (pi*r^2). You can approximate the drag 
#     constant for a loaf of bread by thinking about it as a cylinder. Do your best to estimate the cross sectional area of a skydiver.
#     Are they falling head first or lying flat? You can look up values for the drag constant of a skydiver.

#     Compare the difference in velocities for two different gravity values (Earth and Jupiter), assuming everything else is the same.

#     For one of the objects you picked, see if you can determine how long it takes to reach "terminal velocity" which is the fastest that the object will travel, 
#      by entering different values for "t" to see where it stops increasing.

#     Check your guess for the terminal velocity by using Python to compute the terminal velocity, which can be found by determining the velocity v(t) as time t 
#     approaches infinity. This results in the equation for terminal velocity:

#     v_terminal = sqrt(mg/c)





























