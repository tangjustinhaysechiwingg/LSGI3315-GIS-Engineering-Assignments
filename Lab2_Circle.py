# LSGI3315 Lab 2 20016345D Task 2 - Define a Function
def Calculate_Circle_Area(N=None):  # Define a Function
    if N is None:
        N = [0, 1, 2, 3, 4]
    Radius_list = []  # An empty list

    PI = 3.1415926  # Assign a value to "PI" variable

    for Radius in N:  # For loop to compute Area of Circle
        Area = PI * (Radius**2)  # An equation of computing Area of Circle
        Radius_list.append(Area)

    return Radius_list  # Return value is a list containing the Area of Circles
