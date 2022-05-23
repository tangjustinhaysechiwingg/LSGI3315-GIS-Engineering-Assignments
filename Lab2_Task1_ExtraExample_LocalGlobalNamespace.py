# LSGI3315 Lab 2 20016345D Task 1 -Extra Example: Local and Global Namespace
x = 'Global Namespace x'  # Assign the string in "Global Namespace"


def Testing_namespace():  # Define an Enclosing Namespace
    x = '*** Second: Enclosing Namespace x'  # Assign the string in "Enclosing Namespace"

    def Local_namespace():  # Define a Local Namespace
        x = 'Local Namespace x'  # Assign the string in "Local Namespace"
        print('*** First:', x)  # Print The output from "Local Namespace"

    Local_namespace()  # Call "Local_namespace"
    print(x)  # Print the output from "Enclosing Namespace"


Testing_namespace()
print('*** Final:', x)  # Print the output from "Global Namespace"
