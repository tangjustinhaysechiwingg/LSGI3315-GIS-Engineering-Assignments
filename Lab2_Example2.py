# LSGI3315 Lab 2 20016345D Example 2 - Default Argument
def items_to_string(args=[10, 20, 30, 40, 50]):
    str_list = []  # Define an empty set

    print(args)  # Print input arguments of this function

    for arg in args:  # Iterate through all input arguments, convert them to string
        str_list.append(str(arg))
    str_list.append("the end")  # Insert the string value at the end of str_list
    return str_list  # The string is then add into str_list


if __name__ == '__main__':
    c1 = items_to_string()
    print(c1)
    c2 = items_to_string([10.1, 20.1, 30.1, 40.1, 50.1])
    print(c2)
