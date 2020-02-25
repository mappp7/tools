#######################################    propRig_Create.CON (SingleButton)   ########################################
#                                                                                                                     #
#  propRigTool                                                                                                        #
#  Create.CON (Single Button)                                                                                         #
#  (15. DEC. 2017)                                                                                                    #
#                                                                                                                     #
#######################################################################################################################

import maya.cmds as cmds
import site
site.addsitedir('/dexter/Cache_DATA/CRT/riggingTeamShelf/propRigTool/propRigTool_set')
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
    
#__________ Create CON (separate) __________#  
def create_CON_separate () :
    selObjs_S = cmds.ls(selection=True) # S : Single # 
    if 'GRP' in selObjs_S[0] :  # SGC : Sing Group Controller #
        for SGCC in range(len(selObjs_S)) : # SGCC : Single Group Controller Constraint #
            # Bounding Box : centerPivot
            SGC_bbInfo = cmds.xform(selObjs_S[SGCC], worldSpace=True, query=True, boundingBox=True)
            SGC_bbCT_X = (SGC_bbInfo[0] + SGC_bbInfo[3]) / 2.0
            SGC_bbCT_Y = (SGC_bbInfo[1] + SGC_bbInfo[4]) / 2.0
            SGC_bbCT_Z = (SGC_bbInfo[2] + SGC_bbInfo[5]) / 2.0
            # Bounding Box : Size
            SGC_bbsX = cmds.getAttr ("%s.boundingBoxSizeX" %selObjs_S[SGCC]) /1.5
            SGC_bbsY = cmds.getAttr ("%s.boundingBoxSizeY" %selObjs_S[SGCC]) /1.5
            SGC_bbsZ = cmds.getAttr ("%s.boundingBoxSizeZ" %selObjs_S[SGCC]) /1.5
            selObjs_SGC = cmds.curve (degree=1, p=[(-1, 1, -1), (1, 1, -1), (1, 1, 1), (-1, 1, 1), (-1, -1, 1), (-1, -1, -1), (-1, 1, -1), (-1, 1, 1), (-1, -1, 1), (1, -1, 1), (1, 1, 1), (1, 1, -1), (1, -1, -1), (1, -1, 1), (1, -1, -1), (-1, -1, -1)]) 
            CL.con_overrideColor_SET ()
            selObjs_SGC_rename = cmds.rename (selObjs_S[SGCC].replace ('GRP', 'CON'))
            selObjs_SGC_NUL = cmds.group (em=1, n=selObjs_SGC_rename.replace ('CON', 'NUL'))
            cmds.parent (selObjs_SGC_rename, selObjs_SGC_NUL)
            cmds.scale (SGC_bbsX, SGC_bbsY, SGC_bbsZ, selObjs_SGC_NUL)
            cmds.move (SGC_bbCT_X, SGC_bbCT_Y, SGC_bbCT_Z, selObjs_SGC_NUL)
            cmds.makeIdentity (selObjs_SGC_NUL, apply=1, s=1)
            cmds.parent (selObjs_SGC_NUL, 'control_GRP')
            cmds.parentConstraint (selObjs_SGC_rename, selObjs_S[SGCC], mo=1)
            cmds.scaleConstraint (selObjs_SGC_rename, selObjs_S[SGCC], mo=1)
    else :
        for i in selObjs_S :
            # Bounding Box : centerPivot
            sepaCON_bbInfo = cmds.xform(i, worldSpace=True, query=True, boundingBox=True)
            sepaCON_bbCT_X = (sepaCON_bbInfo[0] + sepaCON_bbInfo[3]) / 2.0
            sepaCON_bbCT_Y = (sepaCON_bbInfo[1] + sepaCON_bbInfo[4]) / 2.0
            sepaCON_bbCT_Z = (sepaCON_bbInfo[2] + sepaCON_bbInfo[5]) / 2.0
            # Bounding Box : Size
            sepaCON_bbsX = cmds.getAttr ("%s.boundingBoxSizeX" %i) /1.5
            sepaCON_bbsY = cmds.getAttr ("%s.boundingBoxSizeY" %i) /1.5
            sepaCON_bbsZ = cmds.getAttr ("%s.boundingBoxSizeZ" %i) /1.5
            # CON
            sepaCON = cmds.curve (degree=1, p=[(-1, 1, -1), (1, 1, -1), (1, 1, 1), (-1, 1, 1), (-1, -1, 1), (-1, -1, -1), (-1, 1, -1), (-1, 1, 1), (-1, -1, 1), (1, -1, 1), (1, 1, 1), (1, 1, -1), (1, -1, -1), (1, -1, 1), (1, -1, -1), (-1, -1, -1)]) 
            sepaCON_rename = cmds.rename (i.replace ('PLY', 'CON'))
            CL.con_overrideColor_SET ()       
            sepaCON_NUL = cmds.group (em=True, n=i.replace ('PLY', 'NUL'))
            cmds.parent (sepaCON_rename, sepaCON_NUL)
            cmds.scale (sepaCON_bbsX, sepaCON_bbsY, sepaCON_bbsZ, sepaCON_NUL)     
            cmds.move (sepaCON_bbCT_X, sepaCON_bbCT_Y, sepaCON_bbCT_Z, sepaCON_NUL)        
            cmds.makeIdentity (sepaCON_NUL, apply=1, s=1)
            cmds.parent (sepaCON_NUL, 'control_GRP')
            cmds.parentConstraint (sepaCON_rename, i, mo=1)
            cmds.scaleConstraint (sepaCON_rename, i, mo=1)
        
    con_ChannelBox ()
    cmds.select (deselect = True)
    

def create_CON_separate_CT () :
    selObjs_S_CT = cmds.ls(selection=True) # S : Single # 
    if 'GRP' in selObjs_S_CT[0] :  # SGC : Sing Group Controller #
        for SGCC in range(len(selObjs_S_CT)) : # SGCC : Single Group Controller Constraint #
            # Bounding Box
            bbInfo_CT = cmds.xform(selObjs_S_CT[SGCC], worldSpace=True, query=True, boundingBox=True)
            bbCT_X = (bbInfo_CT[0] + bbInfo_CT[3]) / 2.0
            bbCT_Y = (bbInfo_CT[1] + bbInfo_CT[4]) / 2.0
            bbCT_Z = (bbInfo_CT[2] + bbInfo_CT[5]) / 2.0
            bbsX = cmds.getAttr ("%s.boundingBoxSizeX" %selObjs_S_CT[SGCC]) /1.5
            bbsY = cmds.getAttr ("%s.boundingBoxSizeY" %selObjs_S_CT[SGCC]) /1.5
            bbsZ = cmds.getAttr ("%s.boundingBoxSizeZ" %selObjs_S_CT[SGCC]) /1.5
            # CON.group 
            selObjs_SGC_CT = cmds.curve (degree=1, p=[(-1, 1, -1), (1, 1, -1), (1, 1, 1), (-1, 1, 1), (-1, -1, 1), (-1, -1, -1), (-1, 1, -1), (-1, 1, 1), (-1, -1, 1), (1, -1, 1), (1, 1, 1), (1, 1, -1), (1, -1, -1), (1, -1, 1), (1, -1, -1), (-1, -1, -1)]) 
            CL.con_overrideColor_SET ()
            selObjs_SGC_rename_CT = cmds.rename (selObjs_S_CT[SGCC].replace ('GRP', 'CON'))
            selObjs_SGC_NUL_CT = cmds.group (em=1, n=selObjs_SGC_rename_CT.replace ('CON', 'NUL'))
            cmds.parent (selObjs_SGC_rename_CT, selObjs_SGC_NUL_CT)
            cmds.scale (bbsX, bbsY, bbsZ, selObjs_SGC_NUL_CT)
            cmds.move (bbCT_X, bbCT_Y, bbCT_Z, selObjs_SGC_NUL_CT)
            cmds.move (0, 0, 0, "%s.scalePivot" %selObjs_SGC_NUL_CT, "%s.rotatePivot" %selObjs_SGC_NUL_CT)
            cmds.move (0, 0, 0, "%s.scalePivot" %selObjs_SGC_rename_CT, "%s.rotatePivot" %selObjs_SGC_rename_CT)   
            cmds.makeIdentity (selObjs_SGC_NUL_CT, apply=1)
            cmds.parent (selObjs_SGC_NUL_CT, 'control_GRP')
            cmds.parentConstraint (selObjs_SGC_rename_CT, selObjs_S_CT[SGCC], mo=1)
            cmds.scaleConstraint (selObjs_SGC_rename_CT, selObjs_S_CT[SGCC], mo=1)
    else :
        for e in selObjs_S_CT :
            # Bounding Box : centerPivot
            bbInfo_CT = cmds.xform(e, worldSpace=True, query=True, boundingBox=True)
            bbCT_X_CT = (bbInfo_CT[0] + bbInfo_CT[3]) / 2.0
            bbCT_Y_CT = (bbInfo_CT[1] + bbInfo_CT[4]) / 2.0
            bbCT_Z_CT = (bbInfo_CT[2] + bbInfo_CT[5]) / 2.0
            bbsX_CT = cmds.getAttr ("%s.boundingBoxSizeX" %e) /1.5  
            bbsY_CT = cmds.getAttr ("%s.boundingBoxSizeY" %e) /1.5
            bbsZ_CT = cmds.getAttr ("%s.boundingBoxSizeZ" %e) /1.5
            # CON
            sepaCON_CT = cmds.curve (degree=1, p=[(-1, 1, -1), (1, 1, -1), (1, 1, 1), (-1, 1, 1), (-1, -1, 1), (-1, -1, -1), (-1, 1, -1), (-1, 1, 1), (-1, -1, 1), (1, -1, 1), (1, 1, 1), (1, 1, -1), (1, -1, -1), (1, -1, 1), (1, -1, -1), (-1, -1, -1)]) 
            CL.con_overrideColor_SET ()    
            sepaCON_rename_CT = cmds.rename (e.replace ('PLY', 'CON'))
            sepaCON_NUL_CT = cmds.group (em=True, n=e.replace ('PLY', 'NUL'))
            cmds.parent (sepaCON_rename_CT, sepaCON_NUL_CT)
            cmds.scale (bbsX_CT, bbsY_CT, bbsZ_CT, sepaCON_NUL_CT)     
            cmds.move (bbCT_X_CT, bbCT_Y_CT, bbCT_Z_CT, sepaCON_NUL_CT) 
            cmds.move (0, 0, 0, "%s.scalePivot" %sepaCON_NUL_CT, "%s.rotatePivot" %sepaCON_NUL_CT)
            cmds.move (0, 0, 0, "%s.scalePivot" %sepaCON_rename_CT, "%s.rotatePivot" %sepaCON_rename_CT)   
            cmds.makeIdentity (sepaCON_NUL_CT, apply=1)
            cmds.parent (sepaCON_NUL_CT, 'control_GRP')
            cmds.parentConstraint (sepaCON_rename_CT, e, mo=1)
            cmds.scaleConstraint (sepaCON_rename_CT, e, mo=1)
        
    con_ChannelBox ()
    cmds.select (deselect = True)
  
    
def create_CON_separate_noConnect () :
    sepaCON_selPLY = cmds.ls(selection=True)
    for i in sepaCON_selPLY :
        # Bounding Box : centerPivot
        sepaCON_bbInfo = cmds.xform(i, worldSpace=True, query=True, boundingBox=True)
        sepaCON_bbCT_X = (sepaCON_bbInfo[0] + sepaCON_bbInfo[3]) / 2.0
        sepaCON_bbCT_Y = (sepaCON_bbInfo[1] + sepaCON_bbInfo[4]) / 2.0
        sepaCON_bbCT_Z = (sepaCON_bbInfo[2] + sepaCON_bbInfo[5]) / 2.0
        # Bounding Box : Size
        sepaCON_bbsX = cmds.getAttr ("%s.boundingBoxSizeX" %i) /1.5
        sepaCON_bbsY = cmds.getAttr ("%s.boundingBoxSizeY" %i) /1.5
        sepaCON_bbsZ = cmds.getAttr ("%s.boundingBoxSizeZ" %i) /1.5
        # CON
        sepaCON = cmds.curve (degree=1, p=[(-1, 1, -1), (1, 1, -1), (1, 1, 1), (-1, 1, 1), (-1, -1, 1), (-1, -1, -1), (-1, 1, -1), (-1, 1, 1), (-1, -1, 1), (1, -1, 1), (1, 1, 1), (1, 1, -1), (1, -1, -1), (1, -1, 1), (1, -1, -1), (-1, -1, -1)]) 
        sepaCON_rename = cmds.rename (i.replace ('PLY', 'CON'))
        CL.con_overrideColor_SET ()       
        sepaCON_NUL = cmds.group (em=True, n=i.replace ('PLY', 'NUL'))
        cmds.parent (sepaCON_rename, sepaCON_NUL)
        cmds.scale (sepaCON_bbsX, sepaCON_bbsY, sepaCON_bbsZ, sepaCON_NUL)     
        cmds.move (sepaCON_bbCT_X, sepaCON_bbCT_Y, sepaCON_bbCT_Z, sepaCON_NUL)        
        cmds.makeIdentity (sepaCON_NUL, apply=1, s=1)
        cmds.parent (sepaCON_NUL, 'control_GRP')     
    con_ChannelBox ()
    cmds.select (deselect = True)
    

def create_CON_separate_CT_noConnect () :
    sepaCON_selPLY_CT = cmds.ls(selection=True)
    for e in sepaCON_selPLY_CT :
        # Bounding Box : centerPivot
        sepaCON_bbInfo_CT = cmds.xform(e, worldSpace=True, query=True, boundingBox=True)
        sepaCON_bbCT_X_CT = (sepaCON_bbInfo_CT[0] + sepaCON_bbInfo_CT[3]) / 2.0
        sepaCON_bbCT_Y_CT = (sepaCON_bbInfo_CT[1] + sepaCON_bbInfo_CT[4]) / 2.0
        sepaCON_bbCT_Z_CT = (sepaCON_bbInfo_CT[2] + sepaCON_bbInfo_CT[5]) / 2.0
        # Bounding Box : Size
        sepaCON_bbsX_CT = cmds.getAttr ("%s.boundingBoxSizeX" %e) /1.5  
        sepaCON_bbsY_CT = cmds.getAttr ("%s.boundingBoxSizeY" %e) /1.5
        sepaCON_bbsZ_CT = cmds.getAttr ("%s.boundingBoxSizeZ" %e) /1.5
        # CON
        sepaCON_CT = cmds.curve (degree=1, p=[(-1, 1, -1), (1, 1, -1), (1, 1, 1), (-1, 1, 1), (-1, -1, 1), (-1, -1, -1), (-1, 1, -1), (-1, 1, 1), (-1, -1, 1), (1, -1, 1), (1, 1, 1), (1, 1, -1), (1, -1, -1), (1, -1, 1), (1, -1, -1), (-1, -1, -1)]) 
        sepaCON_rename_CT = cmds.rename (e.replace ('PLY', 'CON'))
        CL.con_overrideColor_SET ()       
        sepaCON_NUL_CT = cmds.group (em=True, n=e.replace ('PLY', 'NUL'))
        cmds.parent (sepaCON_rename_CT, sepaCON_NUL_CT)
        cmds.scale (sepaCON_bbsX_CT, sepaCON_bbsY_CT, sepaCON_bbsZ_CT, sepaCON_NUL_CT)     
        cmds.move (sepaCON_bbCT_X_CT, sepaCON_bbCT_Y_CT, sepaCON_bbCT_Z_CT, sepaCON_NUL_CT) 
        cmds.move (0, 0, 0, "%s.scalePivot" %sepaCON_NUL_CT, "%s.rotatePivot" %sepaCON_NUL_CT)
        cmds.move (0, 0, 0, "%s.scalePivot" %sepaCON_rename_CT, "%s.rotatePivot" %sepaCON_rename_CT)   
        cmds.makeIdentity (sepaCON_NUL_CT, apply=1)
        cmds.parent (sepaCON_NUL_CT, 'control_GRP')    
    con_ChannelBox ()
    cmds.select (deselect = True)
    
