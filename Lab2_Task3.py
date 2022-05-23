# LSGI3315 Lab 2 20016345D Task 3 - Reading .plt file (20016345d_TANG.plt)
def read_points_from_file(name_of_file):
    point_list = []  # Define an empty list

    try:

        f = open(name_of_file)
        for index, line in enumerate(f):  # Using File Method readlines() ro read each line
            if index > 5:  # Using index leap over description line in .plt file
                line_elements = line.replace('\n', '').split(",")

                lat = float(line_elements[0])  # Latitude of Points
                lon = float(line_elements[1])  # Longitude of Points
                alt = float(line_elements[3])  # Altitude of Points
                date = line_elements[5]  # Acquired Point Date
                time = line_elements[6]  # Acquired Point Time
                temp = [lat, lon, alt, date, time]  # Feature of one point
                point_list.append(temp)  # Append each row to point list
        print("Finished Reading Trajectories")  # Print the sentence when it finishes reading file
        f.close()
        return point_list
    except IOError:
        print("File cannot access.")  # Print the sentence when the file cannot access
        return


if __name__ == '__main__':
    your_filename = '20016345d_TANG.plt'  # The given file name: 20016345D_TANG.plt
    Points_list = read_points_from_file(your_filename)
    for points in Points_list:  # Modified to "For loop" to read all data in a .plt file
        print(points)  # Print each point in a .plt file
    print("There are", len(Points_list), "of points in .plt file")
