# What is the length of a side of the square? 5
# The area of the square is: 25.0
# What is the length of rectangle? 6
# What is the width of the rectangle? 7
# The area of the rectangle is: 42.0
# What is the radius of the circle? 5
# The area of the circle is: 78.5

length_of_square = int(input('What is the length of a side of the square? '))
length_of_square
print(f'The area of the squarre is: {length_of_square*length_of_square}')
print()
length_of_rectangle = int(input('What is the length of the rectangle? '))
width_of_rectangle = int(input('What is the width of the rectangle? '))
print(f'The area of the rectangle is {length_of_rectangle*width_of_rectangle}')
print()
radius_of_circle = int(input('What is the radius of the circle? '))
print(f'The area of the circle is {float(3.141592653589*radius_of_circle**2)}')