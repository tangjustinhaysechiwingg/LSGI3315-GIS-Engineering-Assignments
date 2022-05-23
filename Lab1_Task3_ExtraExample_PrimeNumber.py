# LSGI3315 20016345D Lab1 Task3 - Extra Example - Indentation
i = 2
while i < 100:
    j = 2
    while j <= (i / j):
        if not (i % j):
            break
        j = j + 1
    if j > i / j:
        print i, (" is prime number")
    i = i + 1
print ("This is the end of finding prime number!")
