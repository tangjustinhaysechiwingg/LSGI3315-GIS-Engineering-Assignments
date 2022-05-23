# LSGI3315 Lab 3 20016345D - Example 2: Great-circle distance method in geopy
from geopy.distance import great_circle  # from <module> import <function>

PolyU = (22.304241, 114.179812)  # The coordinate of the Hong Kong Polytechnic University
HKUST = (22.337489, 114.262878)  # The coordinate of the Hong Kong University of Science and Technology
dis = great_circle(PolyU, HKUST).kilometers  # Compute the great-circle distance between two universities

print('The great-circle distance between two universities is %f km.' % dis)  # Print the result
