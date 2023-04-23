# 1 Calculator to calculate area of the rectangle. area = length x width

length = int(input("Enter the length of the rectangle please. Only numerical value \n"))
width = int(input("Enter the width of the rectangle please. Only numerical value \n"))

area = length * width

print(f"The rectangle area is {area} ")

# 2 This algebra monster, equation to solve a3 – b3,
# formula: (a – b)(a2 + ab + b2)

a = int(input("Let\'s give a number for a \n"))
b = int(input("Thank you. Now Let\'s give a number for b \n"))
formula = (a - b) * (a**2 + a*b + b**2)
print(f"The result of the equation a3 – b3 is: {formula}")

# 3 Area of Circle π × r2

pi = 3.14
r = float(input("What is the circle radius ? \n"))
circle_area = pi * (r**2)
rounded_circle_area = round(circle_area, 2)
print(f"The circle area is {rounded_circle_area} ")


# 4 Volume of the Sphere -> attached

pi = 3.14
r = float(input("Let\'s give a number for the radius \n"))
volume = 4/3 * pi * (r**3)
rounded_volume = round(volume, 2)
print(f"The volume of the sphere is {rounded_volume} ")

# 5 This equation x2 +  y2 +  z2 – 3xyz
# formula: (x + y + z)(x2 +  y2 +  z2 – xy – yz -xz)

x = float(input("Give a number for x please \n"))
y = float(input("Give a number for y please \n"))
z = float(input("Give a number for z please \n"))
formula1 = (x + y + z) * (x**2 + y**2 + z**2 - x*y - y*z - x*z)
print(f"The result of the equation x2 +  y2 +  z2 – 3xyz is: {formula1}")