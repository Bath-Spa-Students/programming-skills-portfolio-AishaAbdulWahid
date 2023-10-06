# Q4. Compute the area of triangle.
a = float(input("Enter length of first side: "))
b = float(input("Enter the length of second side: "))
c = float(input("Enter the length of third side: "))

# Calculate the semi-perimeter
s = (a + b + c)/2

# Calculate the area using Heron's formula
area = (s *(s-a)*(s-b)*(s-c))**0.5

print("The area of the triangle is %0.2f",area)

# Alternate method to calculate the Area of Triangle
b = int(input("Enter the base: "))
h = int(input("Enter the height: "))

Area = b*h/2
print("area =", Area)
