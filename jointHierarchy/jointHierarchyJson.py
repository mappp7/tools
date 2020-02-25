import json
import os

jsonPath = os.path.abspath('/show/god/shot/YAC/YAC_1020/ani/pub/data/YAC_1020_ani_v01.json')

with open(jsonPath, 'r') as o:
    jsonData = json.load(o)
    
a = jsonData["AlembicCache"]["reference"]