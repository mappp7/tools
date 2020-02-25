import maya.cmds as cmds
import site
site.addsitedir('/dexter/Cache_DATA/CRT/member/youngmin/YM_00_scripts/myScripts/checker')
from Checker_v01_w03 import*

##################################################    MODEL CHECK    ##################################################
#                                                                                                                     #
#                                                                                                                     # 
#                                                                                                                     #
# sameNameCheck #

def import_CheckerTool () :
    checker()
#                                                                                                                     #
#                                                                                                                     # 
#                                                                                                                     #
##################################################    MODEL CHECK    ##################################################





#####################################################    Group    #####################################################
#                                                                                                                     #
#                                                                                                                     # 
#                                                                                                                     #
#__________ found top group __________#                                                                               #
def found_topGRP () :                                                                                                 #
    temp_selected = cmds.ls(sl=True)    			    															  #
    if cmds.listRelatives (temp_selected, allParents = 1) is None :
        return temp_selected[0]
    else:
        temp_selected_list_01 = cmds.listRelatives (temp_selected, fullPath=True, parent=True)
        temp_selected_list_02 = temp_selected_list_01[0].split('|')[1]        
        return temp_selected_list_02

#__________ create Rig_group _________#                                                                                                                   #
def Create_propRig_group():    
    top = found_topGRP()
       
    # dxRig 
    selectedPLY_dxRig = cmds.ls(sl=True)
    selectedPLY_dxRig_nameList = selectedPLY_dxRig[0].split('_')
    createNode_dxRig = cmds.createNode ( 'dxRig', n=top.replace( 'model', 'rig' ) )
    cmds.setAttr ('%s.assetName' % createNode_dxRig, selectedPLY_dxRig_nameList[0], type="string")  
    cmds.setAttr ('%s.rigType' %createNode_dxRig, 1)  
    # noneTransform
    cmds.group (em=True, n='geometry_GRP')
    cmds.group (n='noneTrnasform_GRP')
    cmds.parent (top, 'geometry_GRP')
    # transform
    cmds.group (em=True, n='transform_GRP')
    cmds.group (em=True, n='control_GRP')
    cmds.group (em=True, n='joint_GRP')
    cmds.parent ('control_GRP', 'joint_GRP', 'transform_GRP')  
    # worldCON
    #__place__#    
    placeCON = cmds.circle (nr=(0, 1, 0), c=(0, 0, 0), r=(6), n='place_CON')
    cmds.DeleteHistory (placeCON)
    placeCON_Shape = cmds.listRelatives(placeCON[0], shapes=1)
    cmds.setAttr ("%s.overrideEnabled" %placeCON_Shape[0], 1)
    cmds.setAttr ("%s.overrideColor" %placeCON_Shape[0], 6)
    cmds.addAttr (longName ='globalScale', defaultValue=1.0)
    cmds.setAttr ('place_CON.globalScale', keyable=True)
    cmds.group (n='place_NUL')    
    #__direction__#
    directionCON = cmds.circle (nr=(0, 1, 0), c=(0, 0, 0), r=(5.4), n='direction_CON')
    cmds.DeleteHistory (directionCON)
    directionCON_Shape = cmds.listRelatives(directionCON[0], shapes=1)
    cmds.setAttr ("%s.overrideEnabled" %directionCON_Shape[0], 1)
    cmds.setAttr ("%s.overrideColor" %directionCON_Shape[0], 17)
    cmds.group (n='direction_NUL')
    #__move__#
    moveCON = cmds.circle (nr=(0, 1, 0), c=(0, 0, 0), r=(4.8), n='move_CON')
    cmds.DeleteHistory (moveCON)
    moveCON_Shape = cmds.listRelatives(moveCON[0], shapes=1)
    cmds.setAttr ("%s.overrideEnabled" %moveCON_Shape[0], 1)
    cmds.setAttr ("%s.overrideColor" %moveCON_Shape[0], 13)
    cmds.group (n='move_NUL')   
    # connected btw World_CON
    cmds.parent ('move_NUL', 'direction_CON')
    cmds.parent ('direction_NUL', 'place_CON')
    # move_CON > transform_GRP 
    cmds.parentConstraint ('move_CON', 'transform_GRP', mo=1)
    # GlobalScale
    cmds.connectAttr ('place_CON.globalScale', 'transform_GRP.sx')
    cmds.connectAttr ('place_CON.globalScale', 'transform_GRP.sy')
    cmds.connectAttr ('place_CON.globalScale', 'transform_GRP.sz')   
    # parent 
    cmds.parent ('place_NUL', 'transform_GRP', 'noneTrnasform_GRP', createNode_dxRig)                                 
    cmds.select (clear =True )
    # channelBox
    cmds.select ('*_CON') 
    selected_worldCON = cmds.ls(sl=1)
    for z in selected_worldCON :
        cmds.setAttr ("%s.sx" %z, lock=True, keyable=False)
        cmds.setAttr ("%s.sy" %z, lock=True, keyable=False)
        cmds.setAttr ("%s.sz" %z, lock=True, keyable=False)
        cmds.setAttr ("%s.v" %z, lock=True, keyable=False)
    cmds.select(deselect=1)        										    										  #
#                                                                                                                     #
#                                                                                                                     # 
#                                                                                                                     #
#####################################################    Group    #####################################################





############################################    radioButton : Node Type    ############################################
#                                                                                                                     #
#                                                                                                                     # 
#                                                                                                                     #
def create_SingleCON () :
    xx = 0
    rb0 = cmds.radioButton (RButton_Constraints, q=1, sl=1)
    rb1 = cmds.radioButton (RButton_JointBinding, q=1, sl=1)
    rb2 = cmds.radioButton (RButton_None, q=1, sl=1)
    if rb0 == True :
        xx == 0
        create_CON_separate ()       
    if rb1 == True :
        xx == 1
        create_JNT_separate ()
    if rb2 == True :
        xx == 2
        create_CON_separate_noConnect () 

def create_JoinCON () :
    xx = 0
    rb0 = cmds.radioButton (RButton_Constraints, q=1, sl=1)
    rb1 = cmds.radioButton (RButton_JointBinding, q=1, sl=1)
    rb2 = cmds.radioButton (RButton_None, q=1, sl=1)
    if rb0 == True :
        xx == 0
        create_CON_combine ()       
    if rb1 == True :
        xx == 1
        create_JNT_combine ()
    if rb2 == True :
        xx == 2
        create_CON_combine_noConnect ()

def create_SingleCON_CT () :
    xx = 0
    rb0 = cmds.radioButton (RButton_Constraints, q=1, sl=1)
    rb1 = cmds.radioButton (RButton_JointBinding, q=1, sl=1)
    rb2 = cmds.radioButton (RButton_None, q=1, sl=1)
    if rb0 == True :
        xx == 0
        create_CON_separate_CT ()
    if rb1 == True :
        xx == 1
        create_JNT_separate_CT ()
    if rb2 == True :
        xx == 2
        create_CON_separate_CT_noConnect ()

def create_JoinCON_CT () :
    xx = 0
    rb0 = cmds.radioButton (RButton_Constraints, q=1, sl=1)
    rb1 = cmds.radioButton (RButton_JointBinding, q=1, sl=1)
    rb2 = cmds.radioButton (RButton_None, q=1, sl=1)
    if rb0 == True :
        xx == 0
        create_CON_combine_CT ()       
    if rb1 == True :
        xx == 1
        create_JNT_combine_CT ()
    if rb2 == True :
        xx == 2
        create_CON_combine_CT_noConnect ()       
#                                                                                                                     #
#                                                                                                                     # 
#                                                                                                                     #
############################################    radioButton : Node Type    ############################################


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
        con_overrideColor_SET () 
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
        con_overrideColor_SET ()    
        sepaJNT_NUL_CT = cmds.group (em=1, n=b.replace ('PLY', 'NUL'))
        cmds.parent (sepaJNT_CON_rename_CT, sepaJNT_NUL_CT)
        cmds.scale (sepaJNT_bbsX_CT, sepaJNT_bbsY_CT, sepaJNT_bbsZ_CT, sepaJNT_NUL_CT)
        cmds.move (sepaJNT_bbCT_X_CT, sepaJNT_bbCT_Y_CT, sepaJNT_bbCT_Z_CT, sepaJNT_NUL_CT)
        cmds.move (0, 0, 0, "%s.scalePivot" %sepaJNT_NUL_CT, "%s.rotatePivot" %sepaJNT_NUL_CT)
        cmds.move (0, 0, 0, "%s.scalePivot" %sepaJNT_CON_rename_CT, "%s.rotatePivot" %sepaJNT_CON_rename_CT)
        cmds.makeIdentity (sepaJNT_NUL_CT, apply=1, s=1)
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
    con_overrideColor_SET ()
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
    con_overrideColor_SET ()
    combJNT_NUL_CT = cmds.group (em=True, n=combJNT_selPLY_CT[0].replace('PLY', 'NUL'))
    cmds.parent (combJNT_CON_rename_CT, combJNT_NUL_CT)
    cmds.scale (propRig_bbsX[-1], propRig_bbsY[-1], propRig_bbsZ[-1], combJNT_NUL_CT)
    cmds.move (propRig_bbX_CT[-1], propRig_bbY_CT[-1], propRig_bbZ_CT[-1], combJNT_NUL_CT)
    cmds.move (0, 0, 0, "%s.scalePivot" %combJNT_NUL_CT, "%s.rotatePivot" %combJNT_NUL_CT)
    cmds.move (0, 0, 0, "%s.scalePivot" %combJNT_CON_rename_CT, "%s.rotatePivot" %combJNT_CON_rename_CT)
    cmds.makeIdentity (combJNT_NUL_CT, apply=1, s=1)
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





######################################################    CON    ######################################################
#                                                                                                                     # 
#                                                       Single                                                        #
#                                                                                                                     # 
def create_CON_separate () :
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
        con_overrideColor_SET ()       
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
        con_overrideColor_SET ()       
        sepaCON_NUL_CT = cmds.group (em=True, n=e.replace ('PLY', 'NUL'))
        cmds.parent (sepaCON_rename_CT, sepaCON_NUL_CT)
        cmds.scale (sepaCON_bbsX_CT, sepaCON_bbsY_CT, sepaCON_bbsZ_CT, sepaCON_NUL_CT)     
        cmds.move (sepaCON_bbCT_X_CT, sepaCON_bbCT_Y_CT, sepaCON_bbCT_Z_CT, sepaCON_NUL_CT) 
        cmds.move (0, 0, 0, "%s.scalePivot" %sepaCON_NUL_CT, "%s.rotatePivot" %sepaCON_NUL_CT)
        cmds.move (0, 0, 0, "%s.scalePivot" %sepaCON_rename_CT, "%s.rotatePivot" %sepaCON_rename_CT)   
        cmds.makeIdentity (sepaCON_NUL_CT, apply=1, s=1)
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
        con_overrideColor_SET ()       
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
        con_overrideColor_SET ()       
        sepaCON_NUL_CT = cmds.group (em=True, n=e.replace ('PLY', 'NUL'))
        cmds.parent (sepaCON_rename_CT, sepaCON_NUL_CT)
        cmds.scale (sepaCON_bbsX_CT, sepaCON_bbsY_CT, sepaCON_bbsZ_CT, sepaCON_NUL_CT)     
        cmds.move (sepaCON_bbCT_X_CT, sepaCON_bbCT_Y_CT, sepaCON_bbCT_Z_CT, sepaCON_NUL_CT) 
        cmds.move (0, 0, 0, "%s.scalePivot" %sepaCON_NUL_CT, "%s.rotatePivot" %sepaCON_NUL_CT)
        cmds.move (0, 0, 0, "%s.scalePivot" %sepaCON_rename_CT, "%s.rotatePivot" %sepaCON_rename_CT)   
        cmds.makeIdentity (sepaCON_NUL_CT, apply=1, s=1)
        cmds.parent (sepaCON_NUL_CT, 'control_GRP')    
    con_ChannelBox ()
    cmds.select (deselect = True)
    
#                                                                                                                     # 
#                                                                                                                     #     
#                                                          JOIN                                                       #
#                                                                                                                     # 
#                                                                                                                     # 
def create_CON_combine () :
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
    con_overrideColor_SET ()
    combCON_NUL = cmds.group (em=True, n=combCON_selPLY[0].replace('PLY', 'NUL'))
    cmds.parent (combCON_reName, combCON_NUL)
    cmds.scale (propRig_bbsX[-1], propRig_bbsY[-1], propRig_bbsZ[-1], combCON_NUL)
    cmds.move (propRig_bbX_CT[-1], propRig_bbY_CT[-1], propRig_bbZ_CT[-1], combCON_NUL)
    cmds.makeIdentity (combCON_NUL, apply=1, s=1)
    con_ChannelBox ()
    cmds.delete (combCON_tempPLY[0])
    cmds.parent (combCON_NUL, 'control_GRP')
    for c in combCON_selPLY :
        cmds.parentConstraint (combCON_reName, c, mo=1)
        cmds.scaleConstraint (combCON_reName, c, mo=1)
    cmds.select (deselect=1)
    

def create_CON_combine_CT () :
    combCON_selPLY_CT = cmds.ls(selection=True)
    combCON_selPLY_copy_CT = cmds.duplicate (combCON_selPLY_CT)
    combCON_tempPLY_CT = cmds.polyUnite(combCON_selPLY_copy_CT, mergeUVSets=1, constructionHistory=True, n=combCON_selPLY_CT[0].replace('PLY', 'RE'))
    cmds.delete (combCON_tempPLY_CT, ch=1) # like a historyDelete and delete emptyGroup, Also Node Check
    # CON
    combCON_CT = cmds.curve (degree=1, p=[(-1, 1, -1), (1, 1, -1), (1, 1, 1), (-1, 1, 1), (-1, -1, 1), (-1, -1, -1), (-1, 1, -1), (-1, 1, 1), (-1, -1, 1), (1, -1, 1), (1, 1, 1), (1, 1, -1), (1, -1, -1), (1, -1, 1), (1, -1, -1), (-1, -1, -1)]) 
    combCON_rename_CT = cmds.rename (combCON_selPLY_CT[0].replace('PLY', 'CON'))
    combCON_Shape_CT = cmds.listRelatives (combCON_rename_CT, shapes=1)
    con_overrideColor_SET ()
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
    for d in combCON_selPLY_CT :
        cmds.parentConstraint (combCON_rename_CT, d, mo=1)
        cmds.scaleConstraint (combCON_rename_CT, d, mo=1)
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
    con_overrideColor_SET ()
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
    con_overrideColor_SET ()
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
#                                                                                                                     #    
#                                                                                                                     #
#                                                                                                                     #
######################################################    CON    ######################################################    
    




###################################################    ROOT CON    ####################################################
#                                                                                                                     # 
#                                                       Single                                                        #
#                                                                                                                     #
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
    con_overrideColor_SET ()
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
    cmds.makeIdentity (rootNUL_CT, apply=1, s=1)
    con_overrideColor_SET ()
    cmds.parent (rootNUL_CT, 'control_GRP')
    cmds.delete (tempGRP_CT)
    for n in selectedCON_NUL_CT :
        cmds.parentConstraint (rootCON_rename_02_CT, n, mo=1)
    con_ChannelBox ()
    cmds.select (deselect = True)
#                                                                                                                     #    
#                                                                                                                     #
#                                                                                                                     #
###################################################    ROOT CON    #################################################### 



    
    
#####################################################    COLOR    #####################################################
#                                                                                                                     #
#                                                                                                                     # 
#                                                                                                                     #
def con_overrideColor_SET () :
    colorNumber = int(cmds.textField('colorValueTF', query=True, tx=True))
    selected_CON = cmds.ls(sl=1)
    selected_CONShapes = cmds.listRelatives (selected_CON, shapes=True)
    for colorSET in selected_CONShapes :
        cmds.setAttr ('%s.overrideEnabled' % colorSET, 1)
        cmds.setAttr ('%s.overrideColor' % colorSET, colorNumber)
        
                                                                                                                            
def colorSet (a) :
    colorNumber = a
    selectSomething = cmds.ls(sl=1)
    something_shape = cmds.listRelatives (selectSomething, s=1)
    if cmds.nodeType (something_shape[0]) == 'mesh' :
        cmds.textField ('colorValueTF', edit=1, tx=colorNumber)
        
    if cmds.nodeType (something_shape[0]) == 'nurbsCurve' :
        cmds.textField ('colorValueTF', edit=1, tx=colorNumber)
        selectedCON = cmds.ls(sl=1)
        selectedCON_Shape = cmds.listRelatives (selectedCON, shapes=1)
        for l in selectedCON_Shape :
            cmds.setAttr("%s.overrideEnabled" %l, 1)
            cmds.setAttr("%s.overrideColor" %l, colorNumber)

    else :
        cmds.textField('colorValueTF', edit=1, tx=colorNumber)
        
def selectionHighliting_ON () :
    cmds.modelEditor ('modelPanel4', e=1, sel=1)
    
def selectionHighliting_OFF () :
    cmds.modelEditor ('modelPanel4', e=1, sel=0)
        
#                                                                                                                     #
#                                                                                                                     # 
#                                                                                                                     #
#####################################################    COLOR    ##################################################### 






#####################################################    EXTRA    #####################################################
#                                                                                                                     #
#                                                                                                                     # 
# 
def selectHierarchy () :
    sel_selectHierarchy = cmds.ls(sl=1)
    cmds.select (hi=1)

def localRotationAxes (a) :
    sel_whatever = cmds.ls(sl=1)
    for d in sel_whatever :
        cmds.setAttr ("%s.displayLocalAxis" %d, a)
#def localRotationAxes_OFF () :
#    sel_whatever = cmds.ls(sl=1)
#    for e in sel_whatever :
#        cmds.toggle (localAxis=0)

def zeroOut () :
    selectJNT = cmds.ls(sl=1)
    for a in selectJNT :
        createNUL = cmds.group (em=1, n=a.replace('JNT', 'NUL'))
        cmds.parent (createNUL, a)
        cmds.makeIdentity (createNUL, t=1, r=1)
        cmds.parent (createNUL, w=1)
        cmds.parent (a, createNUL)
        cmds.makeIdentity (a, t=1, r=1)    
        cmds.setAttr ("%s.jointOrientX" %a, 0) 
        cmds.setAttr ("%s.jointOrientY" %a, 0) 
        cmds.setAttr ("%s.jointOrientZ" %a, 0)
        cmds.parent (a, w=1)
        cmds.delete (createNUL)

def center_JNT () :
    selectPLY = cmds.ls(sl=1)
    for b in selectPLY :
        bbInfo = cmds.xform(b, worldSpace=True, query=True, boundingBox=True)
        bbCT_X = (bbInfo[0] + bbInfo[3]) / 2.0 
        bbCT_Y = (bbInfo[1] + bbInfo[4]) / 2.0 
        bbCT_Z = (bbInfo[2] + bbInfo[5]) / 2.0 
        # create joint
        cmds.select (deselect=True)
        selectJNT_nameList = b.split('_')
        sepaJNT = cmds.joint (p=(bbCT_X, bbCT_Y, bbCT_Z), n=b.replace('PLY', 'JNT'))
        cmds.joint (sepaJNT, edit=True, radius = 0.5)
                
def deleteConstraint () :
    selectSomething = cmds.ls(sl=1, fl=1)
    for d in selectSomething :
        cmds.delete (d, cn=1)
        
def snap () :
    sel_snap = cmds.ls(sl=1)
    cmds.parentConstraint (sel_snap[0], sel_snap[1], mo=0)
    cmds.delete (sel_snap[1], cn=1)
    
def attachLOC () :        
    sel_something = cmds.ls(sl=1)
    cmds.select (deselect=1)
    for e in sel_something :
        sel_something_nameList = e.split('_')
        del sel_something_nameList[-1]
        sel_something_rename = '_'.join(sel_something_nameList)
        createLOC = cmds.spaceLocator (n='%s_attach_LOC' %sel_something_rename)
        cmds.parentConstraint (e, createLOC, mo=0)
        cmds.delete (createLOC, cn=1)
        
def createNUL () :
    sel = cmds.ls(sl=1)
    cmds.select (deselect=1)
    for d in sel :
        sel_nameList = d.split('_')
        del sel_nameList[-1]
        sel_reName = '_'.join(sel_nameList)
        createNUL = cmds.group (em=1, n='%s_NUL' %sel_reName)
        cmds.parentConstraint (d, createNUL, mo=0)
        sel_cn = cmds.pickWalk (d='down'); cmds.delete (sel_cn)
        cmds.parent (d, createNUL)
        
#                                                                                                                     #
#                                                                                                                     # 
#                                                                                                                     #
#####################################################    EXTRA    #####################################################





###################################################    Window GUI    ##################################################
#                                                                                                                     # 
#                                                                                                                     # 
#                                                                                                                     # 
#__________ Create Window __________#                                                                                 #
def propRigWindow () :
    propRig_Window = 'propRig_v01'                                                                                             #
    if cmds.window (propRig_Window, q=1, ex=1):                                                                                #
        cmds.deleteUI (propRig_Window)    
    
    cmds.window (propRig_Window, h=50)
    
    #__________ 1. Model Check __________#
    cmds.columnLayout (adj=1, bgc=([0.2, 0.2, 0.2]), parent = propRig_Window)
    cmds.frameLayout (l='Model Check', collapsable=1, collapse=1, bgc=[0.7, 0.3, 0.3])
    cmds.separator (st='single')
    cmds.text ('1. MODEL CHECK', font='obliqueLabelFont', h=15)
    cmds.separator (st='single')
    cmds.rowColumnLayout (numberOfColumns=3, columnWidth=[(1,50), (2,180), (3,50)])
    cmds.text (" ")
    cmds.button (l='Run Checker Tool ', w=150, h=30, bgc=([1, 0.8, 0.8]), c = 'import_CheckerTool ()')
    cmds.text (" ")
    cmds.separator (st='none', h=15)
    cmds.setParent ('..')

    #__________ 2. dxRig setting __________#
    cmds.columnLayout (adj=1, bgc=([0.2, 0.2, 0.2]), parent = propRig_Window)
    cmds.frameLayout (l='Create dxRig Node', collapsable=1, collapse=1, bgc=[0.75, 0.6, 0.15])
    cmds.separator (st='single', bgc=([0.5, 0.5, 0.1]))
    cmds.text ('2. CREATE dxRig NODE', font='obliqueLabelFont', h=20)
    cmds.separator (st='single', bgc=([0.5, 0.5, 0.1]))
    cmds.rowColumnLayout (numberOfColumns=3, columnWidth=[(1,50), (2,180), (3,50)])
    cmds.text (" ")
    cmds.button (l='Must Select Something !', w=150, h=30, bgc=([1, 0.87, 0.76]), c = 'Create_propRig_group()') 
    cmds.text (" ")
    cmds.separator (st='none', h=20)
    cmds.setParent('..')
    
    #__________ 3. Controller Setting __________#
    cmds.columnLayout (adj=1, bgc=([0.2, 0.2, 0.2]), parent = propRig_Window)
    conSet_frameLayout = cmds.frameLayout (l='Create Controller', collapsable=1, collapse=1, bgc=[0.4, 0.55, 0.3])
    cmds.separator (st='none')
    cmds.separator (st='single', bgc=([0.5, 0.5, 0.25]))
    cmds.text ('3. CON SETTING', font='obliqueLabelFont', h=20, bgc=([0.7, 0.9, 0.7]))
    cmds.separator (st='single', bgc=([0.5, 0.5, 0.25]))
    # subCON #
    #cmds.rowColumnLayout (numberOfColumns=3, columnWidth=[(1,90), (2,90), (3,90)])
    #cmds.text('sub CON   :', h=40, font='obliqueLabelFont')
    #cmds.radioCollection()
    #RButton_SUBCon_no = cmds.radioButton ('createWith', l='Create with')
    #RButton_SUBCon = cmds.radioButton ('add', l='Add')
    
    # NodeType #
    cmds.rowColumnLayout (numberOfColumns=4, columnWidth=[(1,70), (2,75), (3,85), (4,50)])
    cmds.text ('Node Type   :', font='obliqueLabelFont')
    cmds.separator (st='none')
    cmds.separator (st='none')
    cmds.separator (st='none')
    cmds.setParent('..')
    cmds.rowColumnLayout (numberOfColumns=4, columnWidth=[(1,20), (2,85), (3,100), (4,70)])
    cmds.separator (st='none')
    cmds.radioCollection()
    
    global RButton_Constraints, RButton_JointBinding, RButton_None
    RButton_Constraints = cmds.radioButton (l='Constraint')
    RButton_JointBinding = cmds.radioButton (l='Joint Binding')
    RButton_None = cmds.radioButton (l='None')
    
    cmds.separator (st='none', h=10)
    
    # COLOR #
    color_frameLayout = cmds.frameLayout (l=" ", p=conSet_frameLayout)
    cmds.rowColumnLayout (numberOfColumns=4, columnWidth=[(1,70), (2, 70), (3, 10), (4,120)])
    
    cmds.separator (st="none", h=5)
    cmds.separator (st="none", h=5)
    cmds.separator (st="none", h=5)
    cmds.separator (st="none", h=5)
    
    cmds.text ('Color    :', font='obliqueLabelFont')
    cmds.textField ('colorValueTF', tx="0", ed=0)
    cmds.text (" ")
    cmds.checkBox (l='selection Highlighting', onCommand='selectionHighliting_ON ()', offCommand='selectionHighliting_OFF ()', v=1)
    
    cmds.separator (st='none')
    cmds.separator (st='none')
    cmds.separator (st='none')
    cmds.separator (st='single', bgc=([0.5, 0.5, 0.2]))
    
    cmds.columnLayout (adj=1, h=100, p=color_frameLayout)
    cmds.rowColumnLayout (numberOfColumns=5, columnWidth= [(1,56), (2,56), (3,56), (4,56), (5,56)])
    cmds.button(l='13', bgc=[1, 0, 0], c='colorSet (13)')
    cmds.button(l='4', bgc=[0.608, 0, 0.157], c='colorSet (4)')
    cmds.button(l='31', bgc=[0.631, 0.188, 0.412], c='colorSet (31)')
    cmds.button(l='30', bgc=[0.435, 0.188, 0.627], c='colorSet (30)')
    cmds.button(l='20', bgc=[1, 0.686, 0.686], c='colorSet (20)')
    cmds.button(l='17', bgc=[1, 1, 0], c='colorSet (17)')
    cmds.button(l='22', bgc=[1, 1, 0.384], c='colorSet (22)')
    cmds.button(l='25', bgc=[0.62, 0.627, 0.188], c='colorSet (25)')
    cmds.button(l='26', bgc=[0.408, 0.627, 0.188], c='colorSet (26)')
    cmds.button(l='23', bgc=[0, 0.6, 0.325], c='colorSet (23)')
    cmds.button(l='6', bgc=[0, 0, 1], c='colorSet (6)')
    cmds.button(l='29', bgc=[0.188, 0.404, 0.627], c='colorSet (29)')
    cmds.button(l='28', bgc=[0.188, 0.627, 0.627], c='colorSet (28)')
    cmds.button(l='18', bgc=[0.388, 0.863, 1], c='colorSet (18)')
    cmds.button(l='19', bgc=[0.263, 1, 0.635], c='colorSet (19)')
    cmds.button(l='16', bgc=[1, 1, 1], c='colorSet (16)')
    cmds.button(l='24', bgc=[0.627, 0.412, 0.188], c='colorSet (24)')
    cmds.button(l='10', bgc=[0.537, 0.278, 0.2], c='colorSet (10)')
    cmds.button(l='21', bgc=[0.89, 0.675, 0.475], c='colorSet (21)')
    cmds.button(l='default', bgc=[0.467, 0.467, 0.467], c='colorSet (0)')
    #cmds.button(l='1', bgc=[0, 0, 0], c='colorSet (1)')
    #cmds.button(l='2', bgc=[0.247, 0.247, 0.247], c='colorSet (2)')
    #cmds.button(l='3', bgc=[0.498, 0.498, 0.498], c='colorSet (3)')
    #cmds.button(l='5', bgc=[0, 0.016, 0.373], c='colorSet (5)')
    #cmds.button(l='7', bgc=[0, 0.275, 0.094], c='colorSet (7)')
    #cmds.button(l='8', bgc=[0.145, 0, 0.263], c='colorSet (8)')
    #cmds.button(l='9', bgc=[0.78, 0, 0.78], c='colorSet (9)')
    #cmds.button(l='11', bgc=[0.243, 0.133, 0.122], c='colorSet (11)')
    #cmds.button(l='12', bgc=[0.6, 0.145, 0], c='colorSet (12)')
    #cmds.button(l='14', bgc=[0, 1, 0], c='colorSet (14)')
    #cmds.button(l='15', bgc=[0, 0.255, 0.6], c='colorSet (15)')
    #cmds.button(l='27', bgc=[0.188, 0.627, 0.365], c='colorSet (27)')
    
    # conSet #
    con_frameLayout = cmds.frameLayout (l=" ", p=conSet_frameLayout)
    cmds.rowColumnLayout (numberOfColumns=4, columnWidth=[(1,140), (2,68), (3, 3), (4,68)])
    
    cmds.text ('<    Pivot Centre    >')
    cmds.separator( h=30)
    cmds.separator( h=30)
    cmds.separator( h=30)
    
    cmds.text (' +       MODELING     :', font='obliqueLabelFont')
    cmds.button (l='Single', h=30, backgroundColor=([0.2, 1, 0]), c='create_SingleCON ()')
    cmds.separator (st='none')
    cmds.button (l='Join',h=30, backgroundColor=([0.2, 1, 0]), c='create_JoinCON ()')
    
    cmds.separator (st='none', h=3)
    cmds.separator (st='none')
    cmds.separator (st='none')
    cmds.separator (st='none')
    
    cmds.text (' +       GRID              :', font='obliqueLabelFont')
    cmds.button (l='Single', h=30,  backgroundColor=([1, 1, 1]), c='create_SingleCON_CT ()')
    cmds.separator (st='none')
    cmds.button (l='Join',h=30, backgroundColor=([1, 1, 1]), c='create_JoinCON_CT ()')
    
    cmds.separator (st='none', h=30)
    cmds.setParent ('..')
    
    
    cmds.setParent ('..')
    
    #__________ 4. ROOT CON __________#
    cmds.columnLayout (adj=1, p=conSet_frameLayout)
    #cmds.separator (st='none', h=10)
    cmds.separator (st='single', bgc=([0.5, 0.3, 0.5]))
    
    cmds.text ('4. ROOT_CON', font='obliqueLabelFont', h=20, bgc=([0.8, 0.8, 1]))
    #cmds.text ('4. ROOT CON', font='obliqueLabelFont', h=20, bgc=([0.6, 0.4, 1]))
    cmds.separator (st='none', h=7)
    cmds.separator (st='single', bgc=([0.5, 0.3, 0.5]))
    cmds.rowColumnLayout (numberOfColumns=2, columnWidth=[(1,140), (2,140)])
    cmds.text ('<    Pivot Centre    >')
    cmds.separator( h=30)
    cmds.text (' +       MODELING    :', font='obliqueLabelFont')
    cmds.button (l='Create', h=30, backgroundColor=([0.6, 0.4, 1]), c='create_rootCON ()')
    cmds.text (' +       GRID              :', font='obliqueLabelFont')
    cmds.button (l='Create', h=30,  backgroundColor=([1, 1, 1]), c='create_rootCON_CT ()')
    cmds.separator (st='none', h=20)
    cmds.setParent ('..')
    
    
    
    #__________ 5. EXTRA __________#
    cmds.columnLayout (adj=1, bgc=([0.2, 0.2, 0.2]), parent = propRig_Window)
    cmds.frameLayout (l='EXTRA', collapsable=1, collapse=1, bgc=[0.3, 0.46, 0.5])
    cmds.rowColumnLayout (numberOfColumns=4, columnWidth=[(1, 2), (2,136), (3,4), (4, 136)])
    
    
    
    cmds.separator (st='none')
    cmds.button (l='SELECT Hierarchy', h=30, bgc=[0.5, 0.5, 0.5], c='selectHierarchy ()')
    cmds.separator (st='none')
    cmds.button (l='DELETE Constraints', h=30, bgc=[0.5, 0.5, 0.5], c='deleteConstraint ()')
    cmds.separator (st='none', h=2)
    cmds.separator (st='none')
    cmds.separator (st='none')
    cmds.separator (st='none')

    cmds.separator (st='none')
    cmds.button (l='attach LOC', h=30, bgc=[0.5, 0.5, 0.5], c=('attachLOC ()'))
    cmds.separator (st='none')
    cmds.button (l='create NUL', h=30, bgc=[0.5, 0.5, 0.5], c=('createNUL ()'))
    cmds.separator (st='none', h=2)
    cmds.separator (st='none')
    cmds.separator (st='none')
    cmds.separator (st='none')
    
    cmds.separator (st='none')
    cmds.button (l='LRA ON', h=30, bgc=[0.5, 0.5, 0.5], c=('localRotationAxes (1)'))
    cmds.separator (st='none')
    cmds.button (l='LRA OFF', h=30, bgc=[0.5, 0.5, 0.5], c=('localRotationAxes (0)'))
    cmds.separator (st='none', h=2)
    cmds.separator (st='none')
    cmds.separator (st='none')
    cmds.separator (st='none')
    
    cmds.separator (st='none')
    cmds.button (l='CENTER JOINT', h=30, bgc=[0.5, 0.5, 0.5], c='center_JNT ()')
    cmds.separator (st='none')
    cmds.button (l='JNT ZERO OUT', h=30, bgc=[0.5, 0.5, 0.5], c='zeroOut ()')
    cmds.separator (st='none', h=2)
    cmds.separator (st='none')
    cmds.separator (st='none')
    cmds.separator (st='none')
    

    
    cmds.separator (st='none')
    cmds.button (l='SNAP', h=30, bgc=[0.5, 0.5, 0.5], c=('snap ()'))
    cmds.separator (st='none')
    cmds.separator (st='none')
    cmds.separator (st='none', h=2)
    cmds.separator (st='none')
    cmds.separator (st='none')
    cmds.separator (st='none')
    
    
    
    
    
    
    
    # window GUI : Size
    cmds.window (propRig_Window, e=1, width=290, sizeable=1)
    cmds.showWindow(propRig_Window) 
    
propRigWindow()                                                                                                      #
#                                                                                                                     # 
#                                                                                                                     # 
#                                                                                                                     # 
###################################################    Window GUI    ##################################################      
