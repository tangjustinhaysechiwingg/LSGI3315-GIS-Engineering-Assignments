# LSGI3315 Lab 2 20016345D Task 1 - Calculation of Area of Circle
def Circle():  # Define a function

    PI = 3.1415926  # Assign a value to "PI" variable

    Area = PI * (Radius**2)  # An equation of computing Area of Circle

    return Area  # Return the Area of Circle


if __name__ == '__main__':

    Radius = 5.5  # Set a variable "Radius" with value 5.5
    print('The area is:', Circle())  # Print the output on screen
