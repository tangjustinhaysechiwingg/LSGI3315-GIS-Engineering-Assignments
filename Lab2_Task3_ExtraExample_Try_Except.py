# LSGI3315 Lab 2 20016345D Task 3 - Extra Example: Try and Except
import sys  # Import a Module "sys" to obtain the type of Exception

RandomList = [0, 'y', 1]  # A List contains three values/string

for Each_Value in RandomList:  # Loop through the values in "Random List"
    try:  # Exception can be handled by "Try" Statement
        print("The entry is", Each_Value)  # Print each value from "Random List"
        Output = 1 / int(Each_Value)  # The formula used: 1/n
        break  # Terminate the loop in which the statement is placed

    except:  # if any exception occurs, it is caught by except block
        print ("Oh! The", sys.exc_info()[0], "occurs.")  # Print the type of Error from "sys"
        print ("Go for the Next Entry. \n")  # Print for continuing the Next Entry

print("The reciprocal of", Each_Value, "is", Output)  # Print the output if the input is normal
