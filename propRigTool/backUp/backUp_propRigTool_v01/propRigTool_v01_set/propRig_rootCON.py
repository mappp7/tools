############################################    propRig_Create.ROOT CON   #############################################
#                                                                                                                     #
#  propRigTool                                                                                                        #
#  Create.ROOT CON                                                                                                    #
#  (13. DEC. 2017)                                                                                                    #
#                                                                                                                     #
#######################################################################################################################

import maya.cmds as cmds
import site
site.addsitedir('/dexter/Cache_DATA/CRT/riggingTeamShelf/propRigTool/propRigTool_set')
import propRig_color as CL;	reload(CL)
                                                                                                                 


#__________ Organize Controller ChannelBox __________#
def con_ChannelBox () :
    cmds.select ('*_CON')
    cmds.select ('place_CON', 'direction_CON', 'move_CON', deselect=1)
    selected_CON = cmds.ls(sl=1)
    for LnH in selected_CON :
        cmds.setAttr ('%s.sx' %LnH, lock=True, keyable=False)
        cmds.setAttr ('%s.sy' %LnH, lock=True, keyable=False)
        cmds.setAttr ('%s.sz' %LnH, lock=True, keyable=False)
        cmds.setAttr ('%s.v' %LnH, lock=True, keyable=False) 

#__________ Bounding Box Info __________#  
propRig_bbsX = []
propRig_bbsY = []
propRig_bbsZ = []
propRig_bbX_CT = []
propRig_bbY_CT = []
propRig_bbZ_CT = []

def boundingBox_Info () :
    sel_temp = cmds.ls(sl=1)
    bbInfo_TP = cmds.xform(sel_temp, worldSpace=True, query=True, boundingBox=True)
    bbX_CT_TP = (bbInfo_TP[0] + bbInfo_TP[3]) / 2.0; propRig_bbX_CT.append (bbX_CT_TP)
    bbY_CT_TP = (bbInfo_TP[1] + bbInfo_TP[4]) / 2.0; propRig_bbY_CT.append (bbY_CT_TP)
    bbZ_CT_TP = (bbInfo_TP[2] + bbInfo_TP[5]) / 2.0; propRig_bbZ_CT.append (bbZ_CT_TP)
    bbsX_TP = cmds.getAttr ("%s.boundingBoxSizeX" % sel_temp[0]) / 1.5; propRig_bbsX.append(bbsX_TP)
    bbsY_TP = cmds.getAttr ("%s.boundingBoxSizeY" % sel_temp[0]) / 1.5; propRig_bbsY.append(bbsY_TP)
    bbsZ_TP = cmds.getAttr ("%s.boundingBoxSizeZ" % sel_temp[0]) / 1.5; propRig_bbsZ.append(bbsZ_TP)

#__________ Create Root CON __________#     
def create_rootCON () :
    selectedCON = cmds.ls(sl=1)
    selectedCON_NUL = cmds.listRelatives (selectedCON, p=1)
    selectedCON_copy = cmds.duplicate (selectedCON)
    cmds.parent (selectedCON_copy, w=1)
    tempGRP = cmds.group(em=1, n=selectedCON[0].replace('CON', 'tempGRP'))
    cmds.parent (selectedCON_copy, tempGRP)
    tempGRP_bbInfo = cmds.xform(tempGRP, worldSpace=1, query=1, boundingBox=1)
    tempGRP_bbInfo_X = (tempGRP_bbInfo[0] + tempGRP_bbInfo[3]) / 2.0
    tempGRP_bbInfo_Y = (tempGRP_bbInfo[1] + tempGRP_bbInfo[4]) / 2.0
    tempGRP_bbInfo_Z = (tempGRP_bbInfo[2] + tempGRP_bbInfo[5]) / 2.0
    tempGRP_bbsX = cmds.getAttr("%s.boundingBoxSizeX" %tempGRP)/ 1.8
    tempGRP_bbsY = cmds.getAttr("%s.boundingBoxSizeY" %tempGRP)/ 1.8
    tempGRP_bbsZ = cmds.getAttr("%s.boundingBoxSizeZ" %tempGRP)/ 1.8
    rootCON = cmds.curve (degree=1, p=[(-1, 1, -1), (1, 1, -1), (1, 1, 1), (-1, 1, 1), (-1, -1, 1), (-1, -1, -1), (-1, 1, -1), (-1, 1, 1), (-1, -1, 1), (1, -1, 1), (1, 1, 1), (1, 1, -1), (1, -1, -1), (1, -1, 1), (1, -1, -1), (-1, -1, -1)])
    rootCON_rename_01 = cmds.rename ('root_%s'%tempGRP)
    rootCON_rename_02 = cmds.rename (rootCON_rename_01.replace('tempGRP', 'CON'))
    rootNUL = cmds.group(em=1, n=rootCON_rename_02.replace('CON', 'NUL'))
    cmds.parent (rootCON_rename_02, rootNUL)
    cmds.scale (tempGRP_bbsX, tempGRP_bbsY, tempGRP_bbsZ, rootNUL)
    cmds.move (tempGRP_bbInfo_X, tempGRP_bbInfo_Y, tempGRP_bbInfo_Z, rootNUL)
    cmds.makeIdentity (rootNUL, apply=1, s=1)
    CL.con_overrideColor_SET ()
    cmds.parent (rootNUL, 'control_GRP')
    cmds.delete (tempGRP)
    for m in selectedCON_NUL :
        cmds.parentConstraint (rootCON_rename_02, m, mo=1)
    con_ChannelBox ()
    cmds.select (deselect = True)
        

def create_rootCON_CT () :
    selectedCON_CT = cmds.ls(sl=1)
    selectedCON_NUL_CT = cmds.listRelatives (selectedCON_CT, p=1)
    selectedCON_copy_CT = cmds.duplicate (selectedCON_CT)
    cmds.parent (selectedCON_copy_CT, w=1)
    tempGRP_CT = cmds.group(em=1, n=selectedCON_CT[0].replace('CON', 'tempGRP'))
    cmds.parent (selectedCON_copy_CT, tempGRP_CT)
    tempGRP_bbInfo_CT = cmds.xform(tempGRP_CT, worldSpace=1, query=1, boundingBox=1)
    tempGRP_bbInfo_X_CT = (tempGRP_bbInfo_CT[0] + tempGRP_bbInfo_CT[3]) / 2.0
    tempGRP_bbInfo_Y_CT = (tempGRP_bbInfo_CT[1] + tempGRP_bbInfo_CT[4]) / 2.0
    tempGRP_bbInfo_Z_CT = (tempGRP_bbInfo_CT[2] + tempGRP_bbInfo_CT[5]) / 2.0
    tempGRP_bbsX_CT = cmds.getAttr("%s.boundingBoxSizeX" %tempGRP_CT)/ 1.8
    tempGRP_bbsY_CT = cmds.getAttr("%s.boundingBoxSizeY" %tempGRP_CT)/ 1.8
    tempGRP_bbsZ_CT = cmds.getAttr("%s.boundingBoxSizeZ" %tempGRP_CT)/ 1.8
    rootCON_CT = cmds.curve (degree=1, p=[(-1, 1, -1), (1, 1, -1), (1, 1, 1), (-1, 1, 1), (-1, -1, 1), (-1, -1, -1), (-1, 1, -1), (-1, 1, 1), (-1, -1, 1), (1, -1, 1), (1, 1, 1), (1, 1, -1), (1, -1, -1), (1, -1, 1), (1, -1, -1), (-1, -1, -1)])
    rootCON_rename_01_CT = cmds.rename ('root_%s'%tempGRP_CT)
    rootCON_rename_02_CT = cmds.rename (rootCON_rename_01_CT.replace('tempGRP', 'CON'))
    rootNUL_CT = cmds.group(em=1, n=rootCON_rename_02_CT.replace('CON', 'NUL'))
    cmds.parent (rootCON_rename_02_CT, rootNUL_CT)
    cmds.scale (tempGRP_bbsX_CT, tempGRP_bbsY_CT, tempGRP_bbsZ_CT, rootNUL_CT)
    cmds.move (tempGRP_bbInfo_X_CT, tempGRP_bbInfo_Y_CT, tempGRP_bbInfo_Z_CT, rootNUL_CT)
    cmds.move (0, 0, 0, "%s.scalePivot" % rootNUL_CT, "%s.rotatePivot" % rootNUL_CT)
    cmds.move (0, 0, 0, "%s.scalePivot" % rootCON_rename_02_CT, "%s.rotatePivot" % rootCON_rename_02_CT) 
    cmds.makeIdentity (rootNUL_CT, apply=1)
    CL.con_overrideColor_SET ()
    cmds.parent (rootNUL_CT, 'control_GRP')
    cmds.delete (tempGRP_CT)
    for n in selectedCON_NUL_CT :
        cmds.parentConstraint (rootCON_rename_02_CT, n, mo=1)
    con_ChannelBox ()
    cmds.select (deselect = True)
