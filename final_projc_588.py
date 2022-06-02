#Batch processing dozens of files in GIS

#Name: Natalie Marcom
#Campus ID:
#Final Project Code
#GEO 488/588

####################################
#Take CSV file of crimes from 2019 in Los Angeles County, add XY coordinates and turn it into
#a layer file
####################################

import arcpy

from arcpy import env

arcpy.env.workspace = r"C:\\Users\\Giant Toddler\\OneDrive\\Documents\\SPRING 2021\\Final\\final_" #csv crime folder

env.overwrite = True

XFieldName = 'LONGITUDE'
YFieldName = 'LATITUDE'
outFolder = "C:\\SPRING 2021\\Final\final_"
spatialRef = arcpy.SpatialReference(4326)
out_Layer = "crimes_layer2019"
csvFilePath = r"C:\\SPRING 2021\\Final\\2019-CRIMES.csv"
newLayerName = r"C:\\2019-crimes.lyr"


arcpy.MakeXYEventLayer_management(csvFilePath, XFieldName, YFieldName, out_Layer, arcpy.SpatialReference(4326), "")

arcpy.SaveToLayerFile_management(out_Layer, newLayerName)

#################################################################

#Clip streetlight point shapefile,enriched population shapefile,residential shapefile
#enriched income, enriched race and crime point shapefile to city of Carson polygon

#################################################################


from arcpy import env

arcpy.env.workspace = r"C:\\" #clipped folder
env.overwrite = True

i = 0 #i starts from 0
for fc in arcpy.ListFeatureClasses():
                cityShapefile = r"C:\\SPRING 2021\\Final\\final_\\new\\city\\city_poly.shp" #polygon of the city of Carson
                outfc = "Clipped" + str(i) #renames each clipped file in the folder "Clipped + a number"
                arcpy.Clip_analysis(fc, cityShapefile, outfc) #clip_analysis infeature,overlay file, outfeature
                i = i+1 #iterate over the shapefiles in the folder
                print fc

###############################################################
                
#Create 150 ft Buffer of clipped resident shapefile and crime shapefiles
                
###############################################################

import arcpy
from arcpy import env

arcpy.env.workspace = r"C:\\"
env.overwrite = True

i = 0
for fc in arcpy.ListFeatureClasses():
                outfc = "Buffer" + str(i) #renames each buffer file in the folder "Buffer + a number"
                arcpy.Buffer_analysis(fc,outfc, "150 Feet", "FULL", "ROUND", "NONE", "", "Planar") #buffer_analysis within 150 ft
                i = i+1 #iterate over the shapefiles in the folder
                print fc
                
##################################################################

#Create 150 ft, 350 ft, 550 ft buffer of residential and crime shapefiles

###################################################################


from arcpy import env
import os
arcpy.env.workspace = r"C:\\" #buffer folder
env.overwrite = True

for fc in arcpy.ListFeatureClasses():
                distances = ['150 feet', '350 feet', '550 feet']
                desc = arcpy.Describe(fc)
                for distance in distances:
                                outfile = "C:\\" + desc.baseName + str(distance)
                                arcpy.Buffer_analysis(fc, outfile, distance,  "FULL", "ROUND", "NONE","","Planar")
                                print fc

