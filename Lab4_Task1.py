# LSGI3315 GIS Engineering Lab 4 - Task 1 (First Part of Assignment 2)
# ArcPy for Basic GIS Data Operations
# LSGI Year 4 Student: Tang Justin Hayse Chi Wing G. - 20016345D
import arcpy

arcpy.env.workspace = r'C:\Users\justi\Downloads\LSGI3315_20016345D_Lab4_V7'
output_path = r'C:\Users\justi\Downloads\LSGI3315_20016345D_Lab4_V7'
output_name = 'LSGI3315_20016345D_Lab4_V7.gdb'
arcpy.CreateFileGDB_management(output_path, output_name)
