# LSGI3315 20016345D Lab1 Task2 The Speed Difference between List and Tuple
import platform
import time

print(platform.python_version())
start_time = time.time()
b_list = list(range(10000000))
end_time = time.time()
print("Instantiation time for LIST:", end_time - start_time)

start_time = time.time()
b_tuple = tuple(range(10000000))
end_time = time.time()
print("Instantiation time for TUPLE:", end_time - start_time)

# LSGI3315 20016345D Lab1 Task2 List (Speed)
start_time = time.time()
for item in b_list:
    aa = b_list[20000]
end_time = time.time()
print("Lookup time for LIST: ", end_time - start_time)

# LSGI3315 20016345D Lab1 Task2 Tuple (Speed)
start_time = time.time()
for item in b_tuple:
    aa = b_tuple[20000]
end_time = time.time()
print("Lookup time for TUPLE: ", end_time - start_time)

