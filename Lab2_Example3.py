# LSGI3315 Lab 2 20016345D Example 3 - Variable-length Argument (Non-keyword)
def return_set_size(*args):
    x = set()  # Define an empty set
    # Iterate through all the input arguments and add them into x
    for arg in args:
        x.add(arg)

    return len(x)  # return the size of the set


if __name__ == '__main__':
    s1 = return_set_size(1, 2, 3, 4, 5, 6)
    s2 = return_set_size(1, 1, 2, 1, 2, 1)
    s3 = return_set_size(1, 'x', 2.1, 'z', 'y', 'x')
    print("The size of the sets are:", s1, s2, s3)
