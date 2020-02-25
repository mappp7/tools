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
    if len(JLine[0].split('R_')) > 1:
        for x in range(len(JLine)):
            if x < len(JLine)-1:
                y= x+1
                cmds.parent(JLine[y],JLine[x])
                
        for a in range(len(JLine)):
            if a < len(JLine)-1:
                b = a+1
                c = 'L_' + JLine[a].split('R_')[1]
                d = 'L_' + JLine[b].split('R_')[1]
                cmds.parent(d,c)
    else:
        for x in range(len(JLine)):
           if x < len(JLine) -1:
               y= x+1
               cmds.parent(JLine[y],JLine[x]) 
               
                
def parentFunc():           
    

    for i in dirList:
        parentJoint(i)
    cmds.parent(JL[dirList[1]][0],JL[dirList[0]][4])
    cmds.parent('L_' + JL[dirList[1]][0].split('R_')[1],JL[dirList[0]][4])
    
    for o in dirList[2:7]:
        b = JL['%s' %o ][0]
        cmds.parent(b,JL[dirList[1]][-1])
        a = 'L_' + b.split('R_')[1]
        cmds.parent(a,'L_' + JL[dirList[1]][-1].split('R_')[1])
        
    cmds.parent('R_Skin_leg_JNT','C_Skin_hip_JNT')
    cmds.parent('L_Skin_leg_JNT','C_Skin_hip_JNT')

def unParentFunc():    
    s = []
    for p in dirList:
        for l in JL[p]:
            
            if len(l.split('R_')) > 1:
                cmds.parent(l,w=True)
                s.append(l)
                k = 'L_' + l.split('R_')[1]
                cmds.parent(k,w=True)
                
                s.append(k)
            else:
                cmds.parent(l,w=True)
                s.append(l)
                
    for q in s:        
        cmds.parent(q,'geometry_GRP')            

#parentFunc()
#unParentFunc()
        
        
    