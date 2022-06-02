import os
import geopandas
import json
from shapely.geometry import Point
import folium
from flask import render_template, request, jsonify, current_app, Blueprint, session, g
from werkzeug.utils import secure_filename
from gc import collect
import os, time, json
import pandas as pd
from geopy import distance

def map_distance(filepath):
    """
    takes the path to the shapefile as an arg and returns a folium map object
    Or maybe.... we can make it return the html for the map...
    idk
    """
    #read zipfile 
    zipfile = f"zip://{filepath}"
    test_1 = geopandas.read_file(zipfile)

    #read and set LAT/LON from geometry
    test_1 = test_1.assign(
        LAT = test_1.apply(lambda row: row['geometry'].centroid.y, axis = 1),
        LON = test_1.apply(lambda row: row['geometry'].centroid.x, axis = 1),
    )

    # sccwrp lat longs
    sccwrp_coords = (33.707, -117.913)

    #create column of average distance
    test_1['dist_from_sccwrp'] = test_1.apply(
        lambda row:
        #geopy.distance.distance(sccwrp_coords, (row['LAT'],row['LON'])).miles,
        distance.distance(sccwrp_coords, (row['LAT'],row['LON'])).miles,
        axis = 1
    )

    test_mean=test_1["dist_from_sccwrp"].mean() #get mean of average distance (from the column)

    #print out the distance result for user of SCCWRP distance and shapefile distance 
    print(f'The Average distance between SCCWRP and from the center of your uploaded shapefile is: {test_mean} in miles.')

    # initialize the map thingy
    map = folium.Map(location=[41.9,-97.3], zoom_start = 4)

    # read in the shape file
    data_gdf = geopandas.read_file(filepath)

    # add cool stuff
    folium.Marker([33.697900,-117.920720],
                popup='SCCWRP',
                icon=folium.Icon(color='green')
                ).add_to(map)

    # more cool stuff
    folium.GeoJson(data=data_gdf["geometry"]).add_to(map)

    return map, test_mean
