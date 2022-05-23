import arcpy

arcpy.env.workspace = r'C:\Users\justi\Downloads\LSGI3315_20016345D_Lab5'
output_path = r'C:\Users\justi\Downloads\LSGI3315_20016345D_Lab5'
output_name = 'LSGI3315_20016345D_Lab5.gdb'

arcpy.CreateFileGDB_management(output_path, output_name)



