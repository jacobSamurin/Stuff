import math

a,b,c = input("Enter the coefficients of a, b and c separated by commas: ")

d = b**2-4*a*c # discriminant

x = (-b + math.sqrt(d)) / (2 * a)
print(x)
input("Press enter to exit.")