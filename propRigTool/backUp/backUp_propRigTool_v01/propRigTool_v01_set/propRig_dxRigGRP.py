##############################################    propRig_dxRig.Group    ##############################################
#                                                                                                                     #
#  propRigTool                                                                                                        #
#  create dxrig for prop rig                                                                                          #
#  (13. DEC. 2017)                                                                                                    #
#                                                                                                                     #
#######################################################################################################################

import maya.cmds as cmds


#__________ found top group __________#    
def found_topGRP () :                                                                                                 
    cmds.select ('*_PLY')
    temp_selected = cmds.ls(sl=True)    			    															  
    if cmds.listRelatives (temp_selected, allParents = 1) is None :
        return temp_selected[0]
    else:
        temp_selected_list_01 = cmds.listRelatives (temp_selected, fullPath=True, parent=True)
        temp_selected_list_02 = temp_selected_list_01[0].split('|')[1]        
        return temp_selected_list_02                                                                           

#__________ create Rig_group _________#                                                                                                                   
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
    cmds.select(deselect=1)        										    										  

