# LSGI3315 20016345D Lab1 Task3 - Indentation

# List the given "radius list"
Radius_List = [5.1, 1.3, 0.85, 2.2, 7.583, 25.6]
# Assign values to the variable: "Radius"
PI = 3.1415926
radius = 0
# For Loop to compute area of circle based on the above data
for radius in Radius_List:

    # An Equation to calculate the area of the circle
    Area = PI * (radius ** 2)

    # If the area of circle is greater than or equal to 15, print the index of the corresponding radius and area value
    if Area >= 15:
        print"The Area of the circle is:", Area, "and the index of the corresponding radius is in:", Radius_List.index(radius)
    # If the area of circle is smaller than 15, print the area value
    else:
        print"The Area of the circle is:", Area

    radius += 1
