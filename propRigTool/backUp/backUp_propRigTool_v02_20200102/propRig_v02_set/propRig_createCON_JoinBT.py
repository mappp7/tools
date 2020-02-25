########################################    propRig_Create.CON (Join Button)  #########################################
#                                                                                                                     #
#  propRigTool                                                                                                        #
#  Create.CON (Join Button)                                                                                           #
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
    
#__________ Create CON (Combine) __________# 
def create_CON_combine () :
    selObjs_J = cmds.ls(selection=True) # J : Join # 
    if 'GRP' in selObjs_J[0] :  # JGC : Join Group Controller #
        cmds.select (selObjs_J, r=1)
        selobjs_PGRP = cmds.listRelatives (p=1) # PGRP : Parent GRP
        selobjs_J_tempGRP = cmds.group (n=selObjs_J[0].replace('GRP', 'tempGRP'))
        boundingBox_Info ()
        selobjs_JGC = cmds.curve (degree=1, p=[(-1, 1, -1), (1, 1, -1), (1, 1, 1), (-1, 1, 1), (-1, -1, 1), (-1, -1, -1), (-1, 1, -1), (-1, 1, 1), (-1, -1, 1), (1, -1, 1), (1, 1, 1), (1, 1, -1), (1, -1, -1), (1, -1, 1), (1, -1, -1), (-1, -1, -1)]) 
        CL.con_overrideColor_SET ()
        selobjs_JGC_rename = cmds.rename (selObjs_J[0].replace('GRP', 'CON'))
        selobjs_JGC_NUL = cmds.group (em=1, n=selobjs_JGC_rename.replace('CON', 'NUL'))
        cmds.parent (selobjs_JGC_NUL, selobjs_JGC_rename)
        cmds.move (0, 0, 0, selobjs_JGC_NUL, ls=1)
        cmds.parent (selobjs_JGC_NUL, w=1)
        cmds.parent (selobjs_JGC_rename, selobjs_JGC_NUL)
        cmds.scale (propRig_bbsX[-1], propRig_bbsY[-1], propRig_bbsZ[-1], selobjs_JGC_NUL)
        cmds.move (propRig_bbX_CT[-1], propRig_bbY_CT[-1], propRig_bbZ_CT[-1], selobjs_JGC_NUL)
        cmds.makeIdentity (selobjs_JGC_NUL, a=1, s=1)
        cmds.parent (selobjs_JGC_NUL, 'control_GRP')
        cmds.parent (selObjs_J, selobjs_PGRP)
        cmds.delete (selobjs_J_tempGRP)
        for JGCC in selObjs_J :
            cmds.parentConstraint (selobjs_JGC_rename, JGCC, mo=1)
            cmds.scaleConstraint (selobjs_JGC_rename, JGCC, mo=1)
    
    else :
        selObjs_JC = cmds.duplicate (selObjs_J) # JC : Join_Copy #
        selObjs_JC_temp = cmds.polyUnite(selObjs_JC, mergeUVSets=1, constructionHistory=True, n=selObjs_J[0].replace('PLY', 'RE'))
        cmds.delete (selObjs_JC_temp, ch=1) # like a historyDelete and delete emptyGroup, Also Node Check
        cmds.select (selObjs_JC_temp[0])
        boundingBox_Info ()
        cmds.select (deselect=1)    
        selObjs_JPC = cmds.curve (degree=1, p=[(-1, 1, -1), (1, 1, -1), (1, 1, 1), (-1, 1, 1), (-1, -1, 1), (-1, -1, -1), (-1, 1, -1), (-1, 1, 1), (-1, -1, 1), (1, -1, 1), (1, 1, 1), (1, 1, -1), (1, -1, -1), (1, -1, 1), (1, -1, -1), (-1, -1, -1)]) 
        # JPC : Join_PLY_CON #
        CL.con_overrideColor_SET () 
        selObjs_JPC_rename = cmds.rename (selObjs_J[0].replace('PLY', 'CON'))    
        selObjs_JPC_NUL = cmds.group (em=1, n=selObjs_JPC_rename.replace('CON', 'NUL'))
        cmds.parent (selObjs_JPC_rename, selObjs_JPC_NUL)
        cmds.scale (propRig_bbsX[-1], propRig_bbsY[-1], propRig_bbsZ[-1], selObjs_JPC_NUL)
        cmds.move (propRig_bbX_CT[-1], propRig_bbY_CT[-1], propRig_bbZ_CT[-1], selObjs_JPC_NUL)
        cmds.makeIdentity (selObjs_JPC_NUL, apply=1, s=1)
        cmds.delete (selObjs_JC_temp[0])
        cmds.parent (selObjs_JPC_NUL, 'control_GRP')
        for JPCC in selObjs_J : # JPCC : Join PLY Controller Constraints #
            cmds.parentConstraint (selObjs_JPC_rename, JPCC, mo=1)
            cmds.scaleConstraint (selObjs_JPC_rename, JPCC, mo=1)
            
    con_ChannelBox ()
    cmds.select (deselect=1)
    

def create_CON_combine_CT () :
    selObjs_J_CT = cmds.ls(sl=1)
    if 'GRP' in selObjs_J_CT[0] :
        selobjs_PGRP_CT = cmds.listRelatives (selObjs_J_CT, p=1) # PGRP : Parent GRP
        selobjs_J_CT_tempGRP = cmds.group (n=selObjs_J_CT[0].replace ('GRP', 'tempGRP'))
        boundingBox_Info () # JGC : Join Group CON
        selobjs_JGC_CT = cmds.curve (degree=1, p=[(-1, 1, -1), (1, 1, -1), (1, 1, 1), (-1, 1, 1), (-1, -1, 1), (-1, -1, -1), (-1, 1, -1), (-1, 1, 1), (-1, -1, 1), (1, -1, 1), (1, 1, 1), (1, 1, -1), (1, -1, -1), (1, -1, 1), (1, -1, -1), (-1, -1, -1)]) 
        CL.con_overrideColor_SET ()
        selobjs_JGC_CT_rename = cmds.rename (selObjs_J_CT[0].replace ('GRP', 'CON'))
        selobjs_JGC_CT_NUL = cmds.group (em=1, n=selobjs_JGC_CT_rename.replace ('CON', 'NUL'))
        cmds.parent (selobjs_JGC_CT_NUL, selobjs_JGC_CT_rename)
        cmds.move (0, 0, 0, selobjs_JGC_CT_NUL, ls=1)
        cmds.rotate (0, 0, 0, selobjs_JGC_CT_NUL)
        cmds.scale (1, 1, 1, selobjs_JGC_CT_NUL, ls=1)
        cmds.parent (selobjs_JGC_CT_NUL, w=1)
        cmds.parent (selobjs_JGC_CT_rename, selobjs_JGC_CT_NUL)
        cmds.scale (propRig_bbsX[-1], propRig_bbsY[-1], propRig_bbsZ[-1], selobjs_JGC_CT_NUL)
        cmds.move (propRig_bbX_CT[-1], propRig_bbY_CT[-1], propRig_bbZ_CT[-1], selobjs_JGC_CT_NUL)
        cmds.move (0, 0, 0, "%s.scalePivot" %selobjs_JGC_CT_NUL, "%s.rotatePivot" %selobjs_JGC_CT_NUL)
        cmds.move (0, 0, 0, "%s.scalePivot" %selobjs_JGC_CT_rename, "%s.rotatePivot" %selobjs_JGC_CT_rename)
        cmds.makeIdentity (selobjs_JGC_CT_NUL, a=1)
        cmds.parent (selobjs_JGC_CT_NUL, 'control_GRP')
        cmds.parent (selObjs_J_CT, selobjs_PGRP_CT)
        cmds.delete (selobjs_J_CT_tempGRP)
        for JGCC in selObjs_J_CT :
            cmds.parentConstraint (selobjs_JGC_CT_rename, JGCC, mo=1)
            cmds.scaleConstraint (selobjs_JGC_CT_rename, JGCC, mo=1)
        
    else :                
        combCON_selPLY_copy_CT = cmds.duplicate (selObjs_J_CT)
        combCON_tempPLY_CT = cmds.polyUnite(combCON_selPLY_copy_CT, mergeUVSets=1, constructionHistory=True, n=selObjs_J_CT[0].replace('PLY', 'RE'))
        cmds.delete (combCON_tempPLY_CT, ch=1) # like a historyDelete and delete emptyGroup, Also Node Check
        # CON
        combCON_CT = cmds.curve (degree=1, p=[(-1, 1, -1), (1, 1, -1), (1, 1, 1), (-1, 1, 1), (-1, -1, 1), (-1, -1, -1), (-1, 1, -1), (-1, 1, 1), (-1, -1, 1), (1, -1, 1), (1, 1, 1), (1, 1, -1), (1, -1, -1), (1, -1, 1), (1, -1, -1), (-1, -1, -1)]) 
        combCON_rename_CT = cmds.rename (selObjs_J_CT[0].replace('PLY', 'CON'))
        combCON_Shape_CT = cmds.listRelatives (combCON_rename_CT, shapes=1)
        CL.con_overrideColor_SET ()
        combCON_NUL_CT = cmds.group (em=True, n=selObjs_J_CT[0].replace('PLY', 'NUL'))
        cmds.parent (combCON_rename_CT, combCON_NUL_CT)
        cmds.select (combCON_tempPLY_CT[0])
        boundingBox_Info ()
        cmds.scale (propRig_bbsX[-1], propRig_bbsY[-1], propRig_bbsZ[-1], combCON_NUL_CT)
        cmds.move (propRig_bbX_CT[-1], propRig_bbY_CT[-1], propRig_bbZ_CT[-1], combCON_NUL_CT)
        cmds.move (0, 0, 0, "%s.scalePivot" %combCON_NUL_CT, "%s.rotatePivot" %combCON_NUL_CT)
        cmds.move (0, 0, 0, "%s.scalePivot" %combCON_rename_CT, "%s.rotatePivot" %combCON_rename_CT)    
        cmds.makeIdentity (combCON_NUL_CT, apply=1)
        cmds.delete (combCON_tempPLY_CT[0])
        cmds.parent (combCON_NUL_CT, 'control_GRP')
        for d in selObjs_J_CT :
            cmds.parentConstraint (combCON_rename_CT, d, mo=1)
            cmds.scaleConstraint (combCON_rename_CT, d, mo=1)
            
    con_ChannelBox ()
    cmds.select (deselect=1)
    
        
def create_CON_combine_noConnect () :
    combCON_selPLY = cmds.ls(selection=True)
    combCON_selPLY_copy = cmds.duplicate (combCON_selPLY)
    combCON_tempPLY = cmds.polyUnite(combCON_selPLY_copy, mergeUVSets=1, constructionHistory=True, n=combCON_selPLY[0].replace('PLY', 'RE'))
    cmds.delete (combCON_tempPLY, ch=1) # like a historyDelete and delete emptyGroup, Also Node Check
    cmds.select (combCON_tempPLY[0])
    boundingBox_Info ()
    cmds.select (deselect=1)    
    # CON
    combCON = cmds.curve (degree=1, p=[(-1, 1, -1), (1, 1, -1), (1, 1, 1), (-1, 1, 1), (-1, -1, 1), (-1, -1, -1), (-1, 1, -1), (-1, 1, 1), (-1, -1, 1), (1, -1, 1), (1, 1, 1), (1, 1, -1), (1, -1, -1), (1, -1, 1), (1, -1, -1), (-1, -1, -1)]) 
    combCON_reName = cmds.rename (combCON_selPLY[0].replace('PLY', 'CON'))
    combCON_Shape = cmds.listRelatives (combCON_reName, shapes=1)
    CL.con_overrideColor_SET ()
    combCON_NUL = cmds.group (em=True, n=combCON_selPLY[0].replace('PLY', 'NUL'))
    cmds.parent (combCON_reName, combCON_NUL)
    cmds.scale (propRig_bbsX[-1], propRig_bbsY[-1], propRig_bbsZ[-1], combCON_NUL)
    cmds.move (propRig_bbX_CT[-1], propRig_bbY_CT[-1], propRig_bbZ_CT[-1], combCON_NUL)
    cmds.makeIdentity (combCON_NUL, apply=1, s=1)
    con_ChannelBox ()
    cmds.delete (combCON_tempPLY[0])
    cmds.parent (combCON_NUL, 'control_GRP')
    cmds.select (deselect=1)
    

def create_CON_combine_CT_noConnect () :
    combCON_selPLY_CT = cmds.ls(selection=True)
    combCON_selPLY_copy_CT = cmds.duplicate (combCON_selPLY_CT)
    combCON_tempPLY_CT = cmds.polyUnite(combCON_selPLY_copy_CT, mergeUVSets=1, constructionHistory=True, n=combCON_selPLY_CT[0].replace('PLY', 'RE'))
    cmds.delete (combCON_tempPLY_CT, ch=1) # like a historyDelete and delete emptyGroup, Also Node Check
    # CON
    combCON_CT = cmds.curve (degree=1, p=[(-1, 1, -1), (1, 1, -1), (1, 1, 1), (-1, 1, 1), (-1, -1, 1), (-1, -1, -1), (-1, 1, -1), (-1, 1, 1), (-1, -1, 1), (1, -1, 1), (1, 1, 1), (1, 1, -1), (1, -1, -1), (1, -1, 1), (1, -1, -1), (-1, -1, -1)]) 
    combCON_rename_CT = cmds.rename (combCON_selPLY_CT[0].replace('PLY', 'CON'))
    combCON_Shape_CT = cmds.listRelatives (combCON_rename_CT, shapes=1)
    CL.con_overrideColor_SET ()
    combCON_NUL_CT = cmds.group (em=True, n=combCON_selPLY_CT[0].replace('PLY', 'NUL'))
    cmds.parent (combCON_rename_CT, combCON_NUL_CT)
    cmds.select (combCON_tempPLY_CT[0])
    boundingBox_Info ()
    cmds.scale (propRig_bbsX[-1], propRig_bbsY[-1], propRig_bbsZ[-1], combCON_NUL_CT)
    cmds.move (propRig_bbX_CT[-1], propRig_bbY_CT[-1], propRig_bbZ_CT[-1], combCON_NUL_CT)
    cmds.move (0, 0, 0, "%s.scalePivot" %combCON_NUL_CT, "%s.rotatePivot" %combCON_NUL_CT)
    cmds.move (0, 0, 0, "%s.scalePivot" %combCON_rename_CT, "%s.rotatePivot" %combCON_rename_CT)    
    cmds.makeIdentity (combCON_NUL_CT, apply=1, s=1)
    con_ChannelBox ()
    cmds.delete (combCON_tempPLY_CT[0])
    cmds.parent (combCON_NUL_CT, 'control_GRP')
    cmds.select (deselect=1)

