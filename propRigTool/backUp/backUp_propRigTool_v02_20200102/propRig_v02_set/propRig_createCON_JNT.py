############################################    propRig_Create.CON (JNT)   ############################################
#                                                                                                                     #
#  propRigTool                                                                                                        #
#  Create.CON (JNT)                                                                                                   #
#  (13. DEC. 2017)                                                                                                    #
#                                                                                                                     #
#######################################################################################################################

import maya.cmds as cmds
import site
site.addsitedir('/dexter/Cache_DATA/CRT/riggingTeamShelf/propRigTool/propRigTool_v02_set')
import propRig_v02_3_conSet_color as CL;		reload(CL)
                                                                                                                 


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



######################################################    JNT    ######################################################
#                                                                                                                     # 
#                                                       Single                                                        #
#                                                                                                                     # 
def create_JNT_separate () :                                                                                          #
    sepaJNT_selPLY = cmds.ls (sl=True)
    for a in sepaJNT_selPLY :
        # Bounding Box : centerPivot 
        sepaJNT_selPLY_bbInfo = cmds.xform(a, worldSpace=True, query=True, boundingBox=True)
        sepaJNT_bbCT_X = (sepaJNT_selPLY_bbInfo[0] + sepaJNT_selPLY_bbInfo[3]) / 2.0 
        sepaJNT_bbCT_Y = (sepaJNT_selPLY_bbInfo[1] + sepaJNT_selPLY_bbInfo[4]) / 2.0 
        sepaJNT_bbCT_Z = (sepaJNT_selPLY_bbInfo[2] + sepaJNT_selPLY_bbInfo[5]) / 2.0 
        # create joint
        cmds.select (deselect=True)
        sepaJNT_selPLY_nameList = a.split('_')
        sepaJNT = cmds.joint (p=(sepaJNT_bbCT_X, sepaJNT_bbCT_Y, sepaJNT_bbCT_Z), n=a.replace('PLY', 'JNT'))
        sepaJNT_rename = cmds.rename('C_Skin_%s' % sepaJNT)
        cmds.joint (sepaJNT_rename, edit=True, radius = 0.5)
        # skinBind 
        cmds.select (a, replace=True)   
        cmds.select (sepaJNT_rename, add=True)
        cmds.SmoothBindSkin (toSelectedBones = True)
        # Bounding Box : Size
        sepaJNT_bbsX = cmds.getAttr ("%s.boundingBoxSizeX" % a) / 1.5
        sepaJNT_bbsY = cmds.getAttr ("%s.boundingBoxSizeY" % a) / 1.5
        sepaJNT_bbsZ = cmds.getAttr ("%s.boundingBoxSizeZ" % a) / 1.5
        # CON
        cmds.select (deselect = True)
        sepaJNT_CON = cmds.curve (degree=1, p=[(-1, 1, -1), (1, 1, -1), (1, 1, 1), (-1, 1, 1), (-1, -1, 1), (-1, -1, -1), (-1, 1, -1), (-1, 1, 1), (-1, -1, 1), (1, -1, 1), (1, 1, 1), (1, 1, -1), (1, -1, -1), (1, -1, 1), (1, -1, -1), (-1, -1, -1)]) 
        sepaJNT_CON_rename = cmds.rename (a.replace ('PLY', 'CON'))
        CL.con_overrideColor_SET () 
        sepaJNT_NUL = cmds.group (em=True, n=a.replace ('PLY', 'NUL'))
        cmds.parent (sepaJNT_CON_rename, sepaJNT_NUL)
        cmds.scale (sepaJNT_bbsX, sepaJNT_bbsY, sepaJNT_bbsZ, sepaJNT_NUL)
        cmds.move (sepaJNT_bbCT_X, sepaJNT_bbCT_Y, sepaJNT_bbCT_Z, sepaJNT_NUL)
        cmds.makeIdentity (sepaJNT_NUL, apply=1, s=1)
        cmds.parentConstraint (sepaJNT_CON_rename, sepaJNT_rename, mo=1)
        cmds.parent (sepaJNT_rename, 'joint_GRP')
        cmds.setAttr ('joint_GRP.visibility', 0)
        cmds.parent (sepaJNT_NUL, 'control_GRP')

    con_ChannelBox ()
    cmds.select (deselect=1)
    

def create_JNT_separate_CT () :
    sepaJNT_selPLY_CT = cmds.ls (sl=1)
    for b in sepaJNT_selPLY_CT :
        # Bounding Box : centerPivot 
        sepaJNT_selPLY_bbInfo_CT = cmds.xform(b, worldSpace=1, query=1, boundingBox=1)
        sepaJNT_bbCT_X_CT = (sepaJNT_selPLY_bbInfo_CT[0] + sepaJNT_selPLY_bbInfo_CT[3]) / 2.0 
        sepaJNT_bbCT_Y_CT = (sepaJNT_selPLY_bbInfo_CT[1] + sepaJNT_selPLY_bbInfo_CT[4]) / 2.0 
        sepaJNT_bbCT_Z_CT = (sepaJNT_selPLY_bbInfo_CT[2] + sepaJNT_selPLY_bbInfo_CT[5]) / 2.0 
        cmds.select (deselect=1)
        # create joint
        sepaJNT_CT = cmds.joint (p=(sepaJNT_bbCT_X_CT, sepaJNT_bbCT_X_CT, sepaJNT_bbCT_X_CT), n=b.replace('PLY', 'JNT'))
        cmds.joint (sepaJNT_CT, edit=True, radius = 0.5)
        sepaJNT_rename_CT = cmds.rename('C_Skin_%s' % sepaJNT_CT)
        # skinBind 
        cmds.select (b, replace=1)   
        cmds.select (sepaJNT_rename_CT, add=1)
        cmds.SmoothBindSkin (toSelectedBones = 1)
        # Bounding Box : Size
        sepaJNT_bbsX_CT = cmds.getAttr ("%s.boundingBoxSizeX" % b) / 1.5
        sepaJNT_bbsY_CT = cmds.getAttr ("%s.boundingBoxSizeY" % b) / 1.5
        sepaJNT_bbsZ_CT = cmds.getAttr ("%s.boundingBoxSizeZ" % b) / 1.5
        cmds.select (deselect = 1)
        # CON
        sepaJNT_CON_CT = cmds.curve (degree=1, p=[(-1, 1, -1), (1, 1, -1), (1, 1, 1), (-1, 1, 1), (-1, -1, 1), (-1, -1, -1), (-1, 1, -1), (-1, 1, 1), (-1, -1, 1), (1, -1, 1), (1, 1, 1), (1, 1, -1), (1, -1, -1), (1, -1, 1), (1, -1, -1), (-1, -1, -1)]) 
        sepaJNT_CON_rename_CT = cmds.rename (b.replace ('PLY', 'CON'))
        CL.con_overrideColor_SET ()    
        sepaJNT_NUL_CT = cmds.group (em=1, n=b.replace ('PLY', 'NUL'))
        cmds.parent (sepaJNT_CON_rename_CT, sepaJNT_NUL_CT)
        cmds.scale (sepaJNT_bbsX_CT, sepaJNT_bbsY_CT, sepaJNT_bbsZ_CT, sepaJNT_NUL_CT)
        cmds.move (sepaJNT_bbCT_X_CT, sepaJNT_bbCT_Y_CT, sepaJNT_bbCT_Z_CT, sepaJNT_NUL_CT)
        cmds.move (0, 0, 0, "%s.scalePivot" %sepaJNT_NUL_CT, "%s.rotatePivot" %sepaJNT_NUL_CT)
        cmds.move (0, 0, 0, "%s.scalePivot" %sepaJNT_CON_rename_CT, "%s.rotatePivot" %sepaJNT_CON_rename_CT)
        cmds.makeIdentity (sepaJNT_NUL_CT, apply=1)
        cmds.parentConstraint (sepaJNT_CON_rename_CT, sepaJNT_rename_CT, mo=1)
        cmds.parent (sepaJNT_rename_CT, 'joint_GRP')
        cmds.setAttr ('joint_GRP.visibility', 0)
        cmds.parent (sepaJNT_NUL_CT, 'control_GRP')       
        
    con_ChannelBox ()
    cmds.select (deselect=1)
    
    
#                                                                                                                     # 
#                                                                                                                     #     
#                                                          JOIN                                                       #
#                                                                                                                     # 
#                                                                                                                     # 
def create_JNT_combine () :
    combJNT_selPLY = cmds.ls (sl=True)
    combJNT_selPLY_copy = cmds.duplicate (combJNT_selPLY)
    combJNT_tempPLY = cmds.polyUnite(combJNT_selPLY_copy, mergeUVSets=1, constructionHistory=True, n=combJNT_selPLY[0].replace('PLY', 'RE'))
    cmds.delete (combJNT_tempPLY, ch=1) # like a historyDelete and delete emptyGroup, Also Node Check
    cmds.select (combJNT_tempPLY[0])
    boundingBox_Info ()
    cmds.select (deselect=True)
    # create joint
    combJNT = cmds.joint (p=(propRig_bbX_CT[-1], propRig_bbY_CT[-1], propRig_bbZ_CT[-1]), n=combJNT_selPLY[0].replace('PLY', 'JNT'))
    cmds.joint (combJNT, edit=True, radius = 0.5)
    combJNT_rename = cmds.rename('C_Skin_%s' % combJNT)
    # skinBind 
    cmds.select (combJNT_selPLY, replace=True)   
    cmds.select (combJNT_rename, add=True)
    cmds.SmoothBindSkin (toSelectedBones = True)
    # CON
    cmds.select (deselect = True)
    combJNT_CON = cmds.curve (degree=1, p=[(-1, 1, -1), (1, 1, -1), (1, 1, 1), (-1, 1, 1), (-1, -1, 1), (-1, -1, -1), (-1, 1, -1), (-1, 1, 1), (-1, -1, 1), (1, -1, 1), (1, 1, 1), (1, 1, -1), (1, -1, -1), (1, -1, 1), (1, -1, -1), (-1, -1, -1)]) 
    combJNT_CON_rename = cmds.rename (combJNT_selPLY[0].replace('PLY', 'CON'))
    combJNT_CONShape = cmds.listRelatives (combJNT_CON_rename, shapes=True)
    CL.con_overrideColor_SET ()
    combJNT_NUL = cmds.group (em=True, n=combJNT_selPLY[0].replace('PLY', 'NUL'))
    cmds.parent (combJNT_CON_rename, combJNT_NUL)
    cmds.scale (propRig_bbsX[-1], propRig_bbsY[-1], propRig_bbsZ[-1], combJNT_NUL)
    cmds.move (propRig_bbX_CT[-1], propRig_bbY_CT[-1], propRig_bbZ_CT[-1], combJNT_NUL)  
    cmds.makeIdentity (combJNT_NUL, apply=1, s=1)
    con_ChannelBox ()
    cmds.delete (combJNT_tempPLY[0])     
    cmds.parentConstraint (combJNT_CON_rename, combJNT_rename, mo=1)
    cmds.parent (combJNT_rename, 'joint_GRP')
    cmds.setAttr ('joint_GRP.visibility', 0)
    cmds.parent (combJNT_NUL, 'control_GRP')
    cmds.select (deselect=True)
    
    
def create_JNT_combine_CT () :
    combJNT_selPLY_CT = cmds.ls (sl=True)
    combJNT_selPLY_copy_CT = cmds.duplicate (combJNT_selPLY_CT)
    combJNT_tempPLY_CT = cmds.polyUnite(combJNT_selPLY_copy_CT, mergeUVSets=1, constructionHistory=True, n=combJNT_selPLY_CT[0].replace('PLY', 'RE'))
    cmds.delete (combJNT_tempPLY_CT, ch=1) # like a historyDelete and delete emptyGroup, Also Node Check
    cmds.select (combJNT_tempPLY_CT[0])
    boundingBox_Info ()
    cmds.select (deselect=True)
    # create joint
    combJNT_CT = cmds.joint (p=(propRig_bbX_CT[-1], propRig_bbY_CT[-1], propRig_bbZ_CT[-1]), n=combJNT_selPLY_CT[0].replace('PLY', 'JNT'))
    cmds.joint (combJNT_CT, edit=True, radius = 0.5)
    combJNT_rename_CT = cmds.rename('C_Skin_%s' % combJNT_CT)
    # skinBind 
    cmds.select (combJNT_selPLY_CT, replace=True)   
    cmds.select (combJNT_rename_CT, add=True)
    cmds.SmoothBindSkin (toSelectedBones = True)
    # CON
    cmds.select (deselect=1)
    combJNT_CON_CT = cmds.curve (degree=1, p=[(-1, 1, -1), (1, 1, -1), (1, 1, 1), (-1, 1, 1), (-1, -1, 1), (-1, -1, -1), (-1, 1, -1), (-1, 1, 1), (-1, -1, 1), (1, -1, 1), (1, 1, 1), (1, 1, -1), (1, -1, -1), (1, -1, 1), (1, -1, -1), (-1, -1, -1)])
    combJNT_CON_rename_CT = cmds.rename (combJNT_selPLY_CT[0].replace('PLY', 'CON'))
    combJNT_CONShape_CT = cmds.listRelatives (combJNT_CON_rename_CT, shapes=True)
    CL.con_overrideColor_SET ()
    combJNT_NUL_CT = cmds.group (em=True, n=combJNT_selPLY_CT[0].replace('PLY', 'NUL'))
    cmds.parent (combJNT_CON_rename_CT, combJNT_NUL_CT)
    cmds.scale (propRig_bbsX[-1], propRig_bbsY[-1], propRig_bbsZ[-1], combJNT_NUL_CT)
    cmds.move (propRig_bbX_CT[-1], propRig_bbY_CT[-1], propRig_bbZ_CT[-1], combJNT_NUL_CT)
    cmds.move (0, 0, 0, "%s.scalePivot" %combJNT_NUL_CT, "%s.rotatePivot" %combJNT_NUL_CT)
    cmds.move (0, 0, 0, "%s.scalePivot" %combJNT_CON_rename_CT, "%s.rotatePivot" %combJNT_CON_rename_CT)
    cmds.makeIdentity (combJNT_NUL_CT, apply=1)
    con_ChannelBox ()
    cmds.delete (combJNT_tempPLY_CT[0])     
    cmds.parentConstraint (combJNT_CON_rename_CT, combJNT_rename_CT, mo=1)
    cmds.parent (combJNT_rename_CT, 'joint_GRP')
    cmds.setAttr ('joint_GRP.visibility', 0)
    cmds.parent (combJNT_NUL_CT, 'control_GRP')
    cmds.select (deselect=True)
#                                                                                                                     #    
#                                                                                                                     #
#                                                                                                                     #
######################################################    JNT    ######################################################


