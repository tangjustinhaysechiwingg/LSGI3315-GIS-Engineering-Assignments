# LSGI3315 Lab 3 20016345D - Example 1: geocoders method in geopy
from geopy.geocoders import GoogleV3  # from <module> import <function>

google_api_key = 'AIzaSyBHFSokShlBf4gYAhwJaMlSJEKfUpc5IhE'  # The given Google API Key

geo_locator = GoogleV3(google_api_key)
location = 'The Hong Kong Polytechnic University, Hung Hom, Hong Kong'  # Name of place
address = geo_locator.geocode(location)

print('Location:', location)  # Print the inputted location name
print('Address:', address.address)  # Print the Address of the location
print('Coordinate:(%f, %f)' % (address.latitude, address.longitude))  # Print the coordinate of the location
