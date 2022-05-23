# 2021-2022 LSGI3315 GIS Engineering - Assignment 2
# Lab 5 - Spatial Analysis in ArcPy
# Year 4 Student: Tang Justin Hayse Chi Wing G. - 20016345D

# Import ArcPy Package on PyCharm
import arcpy
from arcpy.sa import *
from arcpy import env

# Overwrite the output of ArcGIS Environment
env.overwriteOutput = True

# Task 1 - Environmental Setting
try:
    # Check out the ArcGIS Spatial Analyst Extension License.
    if arcpy.CheckExtension("Spatial") == "Available":
        arcpy.CheckOutExtension("Spatial")
    else:
        # raise a customized exception
        raise Exception('License Error')

except:
    print("ERROR: Spatial Analyst license is unavailable")
    exit(-1)

try:
    # Set Workspace to the Geodatabase on ArcGIS Pro
    env.workspace = env.scratchWorkspace = R'C:\Users\justi\Downloads\LSGI3315_20016345D_Lab5\Lab5_Material\Lab5_Student\Sch_location.gdb'
    # set the cell size and extent of conducting analysis in arcpy
    env.cellSize = R'C:\Users\justi\Downloads\LSGI3315_20016345D_Lab5\Lab5_Material\Lab5_Student\Sch_location.gdb\elevation'
    env.extent = R'C:\Users\justi\Downloads\LSGI3315_20016345D_Lab5\Lab5_Material\Lab5_Student\Sch_location.gdb\elevation'

except:
    print('ERROR: Some input datasets for setting environment are unavailable')
    exit(-1)

print('Task 1: cellSize:', env.cellSize, '\nExtent:', env.extent)


# Task 2 - Slope and Euclidean Distance
def Distance_Slope(Input_File, Slope_Dist_Output):
    '''
    This Function is for : (1) deriving the slope of the research area
    and (2) figuring out the Euclidean distance from each pixel to its nearest school and recreational site.
    :param Input_File: The dictionary with key as data type, and the value as the associated file name.
    :param Slope_Dist_Output: The dictionary with key as (output) data type, and the value as the associated file name.
    '''

    # Derive the slope from elevation, and save it in geodatabase.(add almost 2 lines below)
    out_slope = Slope(Input_File['DEM'], "DEGREE", 0.3048)  # Output_measurement: DEGREE and Z factor is 0.3048
    out_slope.save(Slope_Dist_Output['slope'])

    print("Task 2: Slope Processed")

    # Derive the Euclidean distance to schools, and save it in geodatabase.(almost 2 lines)
    out_schDistance = EucDistance(Input_File['schools'])
    out_schDistance.save(Slope_Dist_Output['schools'])

    print("Task 2: School Distance Derived")

    # Derive the Euclidean distance to recreational sites, and save it in geodatabase.(almost 2 lines)
    out_recDistance = EucDistance(Input_File['rec_sites'])
    out_recDistance.save(Slope_Dist_Output['rec_sites'])

    print("Task 2: Recreation Distance Derived")


# Task 3 - Slicing and Reclassifying
def Reclassification(Slope_Dist_Output, Reclass_Dict, Reclass_Level):
    '''
    This function is for slicing and reclassifying the derived datasets (e.g., slope, distance to school).
    :param Slope_Dist_Output: The dictionary with key as data type, and the value as the associated file name.
    :param Reclass_Dict: The dictionary with key as (output) data type, and the value as the associated file name.
    :param Reclass_Level: A number describing how many levels are used to distinguish the suitability of each pixel
    '''

    # Use a for loop to finish a reversed remap value which applies higher new values to the values
    # representing the suitable place.(add 2~5 lines)
    Reverse_Table = []
    for i in range(Reclass_Level):
        Reverse_Table.append([i + 1, Reclass_Level - i])
    myRemapVal = RemapValue(Reverse_Table)

    # Slice the slope and reverse the values apply higher new values which are representing less steep slope
    # by reclassifying. Then save the reclassified result in geodatabase.(almost 3 lines)
    outSlice_slope = Slice(Slope_Dist_Output['slope'], Reclass_Level, "EQUAL_INTERVAL")
    outreclass_slope = Reclassify(outSlice_slope, "Value", myRemapVal)
    outreclass_slope.save(Reclass_Dict['slope'])
    print("Task 3: Slope Reclassified")

    # Slice the distance to recreational sites and reverse the values to represent that
    # the higher value, the nearer distance to recreation site.
    # Then save the reclassified result in geodatabase.(almost 3 lines)
    outSlice_rec = Slice(Slope_Dist_Output['rec_sites'], Reclass_Level, "EQUAL_INTERVAL")
    outreclass_rec = Reclassify(outSlice_rec, "Value", myRemapVal)
    outreclass_rec.save(Reclass_Dict['rec_sites'])

    print("Task 3: Recreation Distance Reclassified")

    # Slice the distance to schools. Then save the sliced result in geodatabase.(almost 2 lines)
    outSlice_school = Slice(Slope_Dist_Output['schools'], Reclass_Level, "EQUAL_INTERVAL")
    outSlice_school.save(Reclass_Dict['schools'])

    print("Task 3: School Distance Reclassified")


# Task 4 - Weighting and Combining Datasets
def Weighted_Overlay(Input_File, Reclass_Dict, Influence, Slp_remapvalue, Sch_remapvalue, Rec_remapvalue,
                     Landuse_remapvalue):
    '''
    This function is for weighted overlaying and combining reclassified datasets.
    :param Input_File: The dictionary with key as data type, and the value as the associated file name.
    :param Reclass_Dict: The dictionary with key as data type, and the value as the associated file name.
    :param Influence: The Influence Value for each dataset in Weighted Overlay.
    :param Slp_remapvalue,Sch_remapvalue,Landuse_remapvalue: The remap value of corresponding datasets.
    '''
    # Derive the suitable weights for different datasets, using the function provided to you: Scaled_Weights. (almost 3 lines)
    slope_wgh = Scaled_Weights(Reclass_Level, Slp_remapvalue)
    dis_sch_wgh = Scaled_Weights(Reclass_Level, Sch_remapvalue)
    dis_rec_wgh = Scaled_Weights(Reclass_Level, Rec_remapvalue)

    # Combine the slope, the distance to schools, the distance to recreational sites and land use map using function weighted overlay.
    # And save the result of weighted overlay in geodatabase.(at least 12 lines)
    outSuit = WeightedOverlay(WOTable(
        [
            [Reclass_Dict['slope'], Influence['slope'], 'VALUE', RemapValue(slope_wgh)],
            [Reclass_Dict['schools'], Influence['schools'], 'VALUE', RemapValue(dis_sch_wgh)],
            [Reclass_Dict['rec_sites'], Influence['rec_sites'], 'VALUE', RemapValue(dis_rec_wgh)],
            [Input_File['landuse'], Influence['landuse'], 'LANDUSE', RemapValue([
                ["Brush/transitional", Landuse_remapvalue["Brush/transitional"]],
                ["Water", Landuse_remapvalue["Water"]],
                ["Barren_land", Landuse_remapvalue["Barren_land"]],
                ["Built_up", Landuse_remapvalue["Built_up"]],
                ["Agriculture", Landuse_remapvalue["Agriculture"]],
                ["Forest", Landuse_remapvalue["Forest"]],
                ["Wetlands", Landuse_remapvalue["Wetlands"]]])]

        ], [1, 10, 1]))
    outSuit.save("Weighted_out")
    print("Task 4: Weighted Overlay Completed")


# Task 5 - Selecting Optimal Sites
def Filter_FinalSite(Final_Site, Input_File):
    '''
    This function is for recommending the optimal candidate locations based on some more certeria.
    :param Final_Site: The name of output polygon feature class showing the optimal candidate locations.
    :param Input_File: The dictionary with key as data type(input file), and the value as the associated file name.
    :return:
    '''
    # Find the maximum pixel value within the research area, and make a conditional evaluation on each of the input cells.
    # Then save the result of conditional evaluation in geodatabase.(almost 3 lines)
    Target = "Weighted_out"
    Value_Max = arcpy.GetRasterProperties_management(Target, "MAXIMUM")
    outCon = Con(Target, Target, "", "VALUE = " + str(Value_Max))
    outCon.save("Max")

    print("Task 5: Conditional Filter Completed")

    # Make a majority filter for the result of conditional evaluation.
    # Then save the result of majority filter in geodatabase.(almost 2 lines)
    outMajFilt = MajorityFilter(outCon, "EIGHT", "MAJORITY")
    outMajFilt.save("fit")

    print("Task 5: Majority Filter Completed")

    # Convert the result of majority filter(raster) to polygon feature class. (almost 1 line)
    arcpy.RasterToPolygon_conversion(outMajFilt, "area_out", "SIMPLIFY", "Value")

    # Create a feature layer from the polygon feature class. Select Layer By Location and Attribute under some certeria.
    # (almost 3 lines)
    arcpy.MakeFeatureLayer_management("area_out", "poly_out")
    arcpy.SelectLayerByLocation_management("poly_out", "INTERSECT", Input_File['roads'], "", "NEW_SELECTION")
    arcpy.SelectLayerByAttribute_management("poly_out", "SUBSET_SELECTION", '"Shape_Area">=40469')

    print("Task 5: Final Feature Selection: Completed")

    # Copy the selected layered to a new polygon feature class. (almost 1 line)
    arcpy.CopyFeatures_management("poly_out", Final_Site)
    print("Task 5: Selected Final School Site! Check the Output on ArcGIS Geodatabase")
    print("Task 6: Modify the parameters on the Main Function below. Thank you!\n")
    print("This is the END of LSGI3315 Lab 5 (Spatial Analysis in ArcPy). Thank you for running this programme! :)")


# You are not required to modify this function
def Scaled_Weights(Reclass_Level, Overlay_Weight):
    # This functions is for weight arrangement, at the End of Weight would be ["NODATA", "NODATA"].
    # param: Reclass_level is the level of reclassification;
    #        Overlay_Weight is the initialized weights of different datasets.
    # Return Value is a RemapValue list, lists in a list.
    Weight_List = []
    for i in range(Reclass_Level):
        Weight_List.append([i + 1, Overlay_Weight[i]])
    Weight_List.append(["NODATA", "NODATA"])
    return Weight_List


# The main function has already been completed.
# After you finish the function above, please run this Python script (without modifying the main function)
if __name__ == '__main__':

    # Statement of the Remap value of Slope, Distance of school and Recreation.
    Slope_remapvalue, Sch_remapvalue, Rec_remapvalue = [], [], []

    # Set the Level of Reclassification.
    Reclass_Level = 10

    # This Dictionary contains the names of influence value for different datasets.
    # Modify the parameters in Task 6
    Influence_Val = {
        "slope": 20,
        "rec_sites": 33,
        "schools": 25,
        "landuse": 22
    }

    # This Dictionary contains the names of input files.
    Input_File = {
        "DEM": "elevation",
        "landuse": "landuse",
        "rec_sites": "rec_sites",
        "schools": "schools",
        "roads": "roads"
    }

    # This Dictionary contains the names of Slope and Euclidean distance.
    Slope_Dist_Output = {
        "slope": "slope",
        "schools": "school_dis",
        "rec_sites": "rec_dis"
    }

    # This Dictionary contains the names of datasets after reclassifying.
    Reclass_Dict = {
        "slope": "slope_reclass",
        "schools": "school_reclass",
        "rec_sites": "recreation_reclass"
    }

    # This Dictionary contains the Weights of different land use type.
    # Modify the parameters in Task 6
    Landuse_rmv = {
        "Brush/transitional": 5,
        "Water": "Restricted",
        "Barren_land": 10,
        "Built_up": 5,
        "Agriculture": 6,
        "Forest": 9,
        "Wetlands": "Restricted"
    }

    # This for loop is for initializing Weights of Slope, distance of school and distance of recreation.
    for i in range(Reclass_Level):
        Slope_remapvalue.append(i + 1)
        Sch_remapvalue.append(i + 1)
        Rec_remapvalue.append(i + 1)

    Slope_remapvalue[0] = "Restricted"
    Slope_remapvalue[1] = "Restricted"
    Slope_remapvalue[2] = "Restricted"

    # The name of Final School Site.
    Final_Site = "Final_Site_Task6_4"

    Distance_Slope(Input_File, Slope_Dist_Output)
    Reclassification(Slope_Dist_Output, Reclass_Dict, Reclass_Level)
    Weighted_Overlay(Input_File, Reclass_Dict, Influence_Val, Slope_remapvalue, Sch_remapvalue, Rec_remapvalue,
                     Landuse_rmv)
    Filter_FinalSite(Final_Site, Input_File)
