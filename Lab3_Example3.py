# LSGI3315 Lab 3 20016345D - Example 3: Calculate Spherical distance using geopy.great_circle
import geopy.distance as geod  # from <module> import <function>


def cal_distance(point1, point2):  # Define a Function of computing sphere distance from two points
    dis = geod.great_circle(point1, point2).meters  # using geopy.great_circle to compute point(latitude, longitude)
    return dis  # Return the spherical distance between two points


if __name__ == '__main__':
    HK_International_Airport_lon = 113.918480  # The longitude of the Hong Kong International Airport
    HK_International_Airport_lat = 22.308046   # The latitude of Hong Kong Disneyland
    HK_Disney_Land_lon = 114.041931  # The longitude of the Hong Kong International Airport
    HK_Disney_Land_lat = 22.312771   # The latitude of Hong Kong Disneyland
    point_begin = (HK_International_Airport_lat, HK_International_Airport_lon)  # The point begins at (long,lat)
    point_end = (HK_Disney_Land_lat, HK_Disney_Land_lon)  # The point ends at (long,lat)
    dist = cal_distance(point_begin, point_end)  # Call the function of "cal_distance"
    print('The distance between the Hong Kong International Airport and the Hong Kong Disneyland is %f meters' % dist)
