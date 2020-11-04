#calculate area and height of a triangle with given 3 sides and base
import math

a = 5 #triangle with 3 sides a. b and c
b = 6
c = 7
base = 2.5

s = (a + b +c)/2 #semi-perimeter triangle  
area = math.sqrt(s*(s-a)*(s-b)*(s-c)) #area triangle
h = s*(area/base) #height triangle

print("Area of triangle is ", area)
print("Height of triangle is ", h)
