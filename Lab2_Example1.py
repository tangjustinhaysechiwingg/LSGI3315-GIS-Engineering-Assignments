# LSGI3315 Lab 2 20016345D Example 1 - Required Argument
# Producing Fibonacci Series

# Define a Function
def function(N):  # N = Integer Number

    fibonacci = []
    x, y = 0, 1  # initialize first and second terms
    while x < N:  # while loop for the n terms
        fibonacci.append(x)
        x, y = y, x + y  # Recurrent relation
    return fibonacci  # the list of Fibonacci Series


if __name__ == '__main__':  # Call the function just defined
    fib_list = function(3000)
    print(fib_list)  # Print the output: Fibonacci Series
