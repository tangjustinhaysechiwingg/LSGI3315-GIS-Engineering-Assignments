# LSGI3315 Lab 3 20016345D - Task: A class for Reading Given .plt Trajectory File

class Trajectory:  # Create a Class named Trajectory

    def __init__(self):  # (i) Define an initialization function
        self.points = []  # (i) The instance variables store a "list" of points

    def Read_Points_from_File(self, filename):  # (ii) Define a function named "Read_Points_from_File(self, filename)"
        point_list = []  # Define an empty list

        try:

            f = open(filename)
            for index, line in enumerate(f):  # Using File Method readlines() to read each line
                if index > 5:  # Using index loop over description line in .plt file
                    line_elements = line.replace('\n', '').split(",")

                    lat = float(line_elements[0])  # Latitude of Points
                    lon = float(line_elements[1])  # Longitude of Points
                    alt = float(line_elements[3])  # Altitude of Points
                    date = line_elements[5]  # Acquired Point Date
                    time = line_elements[6]  # Acquired Point Time
                    temp = [lat, lon, alt, date, time]  # Feature of one point
                    point_list.append(temp)  # Append each row to point list

            f.close()
            return point_list

        except IOError:

            print("File can't access.")  # Print the statement when the file cannot be accessed
            return

    def Points_Counting(self):  # (iii) Define a function named "Point_Counting(self)"
        Points_list = self.Read_Points_from_File(Reading_Points_from_File)  # Read the points in the .plt file
        print("Reading Trajectories Completed")  # Print the statement once reading trajectories is completed
        return len(Points_list)  # Return the output

    def Cal_Distance(self):  # (iv) Define a function named "Cal_Distance(self)"
        from geopy.distance import great_circle  # from <geopy module> import <great-circle function>

        Points_list = self.Read_Points_from_File(Reading_Points_from_File)

        i = 0
        j = 1
        total = 0

        for _ in Points_list:  # Use a For loop to traverse all trajectory points

            begin_lat = Points_list[i][0]  # The latitude of first point
            begin_lon = Points_list[i][1]  # The longitude of first point

            begin_pt = (begin_lat, begin_lon)  # The coordinate of first point in .plt file

            end_lat = Points_list[j][0]  # The latitude of consecutive point
            end_lon = Points_list[j][1]  # The longitude of consecutive point

            end_pt = (end_lat, end_lon)  # The coordinate of consecutive point in .plt file

            dis = great_circle(begin_pt, end_pt).meters  # The great circle distance between first and consecutive point

            i += 1  # continue reading the second point
            j += 1  # continue reading the next consecutive point
            total += dis  # sum up the distance

            if j == len(Points_list):  # End up the for loop when the variable j is equal to the total number of points
                print('The total distance is:', total, 'm')  # print the total distance of the whole trajectory
                break  # Break the for loop statement when j equals to the total number of point

        return total


if __name__ == '__main__':
    tra = Trajectory()
    Reading_Points_from_File = '20016345d_TANG.plt'  # The given file name: 20016345d_TANG.plt
    num = tra.Points_Counting()  # Call the Function of "Points_counting"
    print("Number of Points:", num)  # Print the total number of points in .plt file
    distance = tra.Cal_Distance()  # Call the Function of "Cal_Distance"
