import json
import os
import maya.cmds as cmds

jsonPath = os.path.abspath('/dexter/Cache_DATA/CRT/member/taewoo/scripts/jointHierarchy/jointList.json')

dirList = ['hipList','shoulderList','indexList','middleList','ringList','pinkyList','thumbList','legList']

with open(jsonPath, 'r') as o:
    JD = json.load(o)
JL = JD["jointList"]

def parentJoint(listName):
    
    JLine = JL[listName]
    if JLine[0].split('R_') > 1:
        for x in range(len(JLine)):
            if len(JLine) > x > 0:
                y= x+1
                cmds.parent(JLine[y],JLine[X])
                
        for a in range(len(JLine)):
            if len(JLine) > a > 0:
                b = a+1
                c = 'L_' + JLine[a].split('R_')[1]
                d = 'L_' + JLine[b].split('R_')[1]
                cmds.parent(d,c)
    else:
        for x in range(len(JLine)):
           if len(JLine) > x > 0:
               y= x+1
               cmds.parent(JLine[y],JLine[X])           
                
def parentFunc():           
    for i in dirList:
        parentJoint(i)
    cmds.parent(JL[dirList[1]][0],JL[dirList[0]][4])
    for o in dirList[2:7]:
        cmds.parent(o[0],JL[dirList[1]][-1])
        a = 'L_' + o[0].split('R_')[1]
        cmds.parent(a,JL[dirList[1]][-1])
        
    cmds.parent('R_Skin_leg_JNT','C_Skin_hip_JNT')
    cmds.parent('L_Skin_leg_JNT','C_Skin_hip_JNT')
    
parentFunc()
        
        
    