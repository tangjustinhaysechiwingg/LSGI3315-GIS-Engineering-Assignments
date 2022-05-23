############################################################################
############################ Updated Version ###############################
############################################################################

# LSGI3315 GIS Engineering Lab 4 - Main Task (First Part of Assignment 2)
# ArcPy for Basic GIS Data Operations
# LSGI Year 4 Student: Tang Justin Hayse Chi Wing G. - 20016345D

# import math, arcpy and pyproj packages
import pyproj  # For computing the Coordinate Conversion (Task 2)
import arcpy  # Python side package enables customization of ArcGIS Pro (All Tasks)
import math  # For computing Euclidean Distance (Task 5)

#  Setup the ArcPy workplace environment
arcpy.env.workspace = r'C:\Users\justi\Downloads\LSGI3315_20016345D_Lab4_V7\LSGI3315_20016345D_Lab4_V7.gdb'

# Print the first sentence to indicate the Python script successfully runs
print("\nThe Python Script takes approximately one minute to execute...... Please wait.......\n")


class Trajectory:  # Lab 4 - Modify the Class "Trajectory"

    def __init__(self, workspace):  # Define an initialization function
        self.points = []  # Create a new instance variable to store a "list" of point - under WGS_1984
        self.beijing_point_list = []  # Create a new instance variable to store a "list" of point - under Beijing_1954
        self.workspace = workspace  # Create a new instance variable "workspace"

    def read_points_from_file(self, filename):  # Task 2 - Coordinate Conversion
        point_list = []  # The pair of coordinate under WGS84 coordinate system
        beijing_point_list = []  # The pair of coordinate under Beijing_1954_3_Degree_GK_CM_117E coordinate system
        crs_4326 = pyproj.CRS("EPSG:4326")  # Definition of WGS_84
        crs_2436 = pyproj.CRS("EPSG:2436")  # Definition of Beijing_1954_3_Degree_GK_CM_117E
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
                    WGS84_points = [lat, lon, alt, date, time]  # Feature of one point
                    point_list.append(WGS84_points)  # Append each row to point line
                    # Keep the above python statement in this function unchanged
                    transformer = pyproj.Transformer.from_crs(crs_4326, crs_2436)  # transform
                    y, x = transformer.transform(lat, lon)  # Transforming coordinate from WGS_1984 to Beijing_1954
                    # the points under Beijing_1954_3_Degree_GK_CM_117E Coordinate System
                    Beijing_1954_points = [y, x, alt, date, time]
                    beijing_point_list.append(Beijing_1954_points)  # Append x, y to point_list instead of lat and lon
                    # the points are now under Beijing_1954_3_Degree_GK_CM_117E Coordinate System
            f.close()
            return beijing_point_list  # Return the updated Beijing List

        except IOError:

            print("The File cannot access.")
            return

    def points_counting(self):  # It is done in previous Lab 3
        beijing_point_list = self.read_points_from_file(Reading_Points_from_File)
        print("Reading Trajectory Completed")
        return len(beijing_point_list)

    def Cal_Distance(self):  # Task 5 - Calculate Euclidean Distance
        beijing_point_list = self.read_points_from_file(Reading_Points_from_File)
        i = 0
        j = 1
        total = 0

        for _ in beijing_point_list:  # Use for loop to traverse all trajectory points

            begin_lat = beijing_point_list[i][0]  # The y coordinate of first trajectory point
            begin_lon = beijing_point_list[i][1]  # The x coordinate of first trajectory point

            end_lat = beijing_point_list[j][0]  # The y coordinate of last trajectory point
            end_lon = beijing_point_list[j][1]  # The x coordinate of last trajectory point

            # Modify the function to compute its Euclidean Distance under new Beijing 1954 Coordinate system
            Euclidean_distance = math.sqrt((end_lon - begin_lon) ** 2 + (end_lat - begin_lat) ** 2)

            i += 1  # Continue reading the second point
            j += 1  # Continue reading the next consecutive point
            total += Euclidean_distance  # Sum up the total Euclidean distance

            if j == len(beijing_point_list):  # Break the for loop when the variable j = the total number of points
                break

        print("\nFinished Calculating Distance")
        return total  # Return the total Euclidean distance result

    def Point_to_FeatureClass(self):  # Task 3 - Point to Feature Class
        arcpy.env.workspace = self.workspace  # Specify the workplace of this function using self.workplace
        beijing_point_list = self.read_points_from_file(Reading_Points_from_File)
        point_geom_list = []
        spatial_reference = arcpy.SpatialReference(2436)  # Define the geometry information:spatial_reference
        a = 0
        i = 1

        for _ in beijing_point_list:  # Use a for loop to traverse all points in the point_list

            # The properties of each point feature should include ID, X and Y.
            point_all = arcpy.Point(X=beijing_point_list[a][1], Y=beijing_point_list[a][0], ID=i)
            print("Point", i, "Properties:")
            print("ID: ", point_all.ID)  # Print the ID of the Trajectory Point Property
            print("X: ", point_all.X)  # Print the X coordinate
            print("Y: ", point_all.Y)  # Print the Y coordinate
            print('\n')  # Giving the Space to other print statements

            a += 1  # Continue reading the second point
            i += 1  # Continue reading the next consecutive point

            # Define Geometry information, "spatial_reference"
            point_geometry_all = arcpy.PointGeometry(point_all, spatial_reference)
            point_geom_list.append(point_geometry_all)  # Append the geometry

        arcpy.CopyFeatures_management(point_geom_list, r'Trajectory_20016345D')  # Copy the features by ArcPy
        print("Complete Creating a Point Feature Class")  # Print the completed statement

    def Add_Attribute(self):  # Task 4 - Managing Attribute Table
        beijing_point_list = self.read_points_from_file(Reading_Points_from_File)
        arcpy.env.workspace = self.workspace  # Specify the workplace of this function using self.workplace

        feature_class_filename = r'C:\Users\justi\Downloads\LSGI3315_20016345D_Lab4_V7\LSGI3315_20016345D_Lab4_V7.gdb\Trajectory_20016345D'
        # Use AddField_management to add two attribute fields of point feature class, named Date and Time
        # Set the parameter field_type, field_is_nullable, field_is_required as DATE, Nullable and Non_Required
        arcpy.AddField_management(feature_class_filename, 'Date', 'DATE', field_is_nullable="Nullable",
                                  field_is_required="Non_Required")
        arcpy.AddField_management(feature_class_filename, 'Time', 'DATE', field_is_nullable="Nullable",
                                  field_is_required="Non_Required")

        feat_rows = arcpy.UpdateCursor(feature_class_filename)  # Use UpdateCursor to update row

        for (index, row) in enumerate(feat_rows):  # Use For loop to update values of items in each row

            row.setValue('Date', beijing_point_list[index][3])  # Use setValue to update Date
            row.setValue('Time', beijing_point_list[index][4])  # Use setValue to update Time

            feat_rows.updateRow(row)  # Update all rows

        print("Complete Adding Attributes")  # Print the completed statement

    def MBG(self):  # Task 5 - Define a new ArcPy function: Minimum Bounding Box

        # Set the "traj_pnt_name" and trace the previously copied point feature
        traj_pnt_name = r'C:\Users\justi\Downloads\LSGI3315_20016345D_Lab4_V7\LSGI3315_20016345D_Lab4_V7.gdb\Trajectory_20016345D'
        # Set the "mbg_name" to construct the minimum bounding geometry
        mbg_name = r'C:\Users\justi\Downloads\LSGI3315_20016345D_Lab4_V7\LSGI3315_20016345D_Lab4_V7.gdb\MBG'
        #  Call the "MinimumBoundingGeometry_management" provided by ArcPy Package
        arcpy.MinimumBoundingGeometry_management(traj_pnt_name, mbg_name, "ENVELOPE", "ALL")

        # Print the last completed statement
        print("The trajectory points and minimum bounding box (shapefile) are imported to ArcGIS Pro \n")
        print("This is the END of LSGI3315 Lab 4 (The First Part of Assignment 2). Thank you for running this code!")


if __name__ == '__main__':
    workspace = r'C:\Users\justi\Downloads\LSGI3315_20016345D_Lab4_V7\LSGI3315_20016345D_Lab4_V7.gdb'
    output_trajectory_point_name = 'Trajectory_Points'
    MBG_name = 'MBG_of_Traj'

    traj = Trajectory(workspace)

    Reading_Points_from_File = '20016345d_TANG.plt'
    num_of_point = traj.points_counting()
    print("Number of Points: ", num_of_point)
    distance = traj.Cal_Distance()
    print("Total Euclidean distance of the trajectory is %.3f" % distance, "Meters")
    print("\nPlease wait, the trajectory points are loading...")

    traj.Point_to_FeatureClass()
    traj.Add_Attribute()
    traj.MBG()
