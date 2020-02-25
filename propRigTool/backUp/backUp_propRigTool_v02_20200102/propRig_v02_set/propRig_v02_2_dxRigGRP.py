##############################################    propRig_dxRig.Group    ##############################################
#                                                                                                                     #
#  propRigTool v02.01 (2019. 12. 30)                                                                                  #                      
#  create dxrig for prop rig                                                                                          #
#                                                                                                                     #
#######################################################################################################################
import maya.cmds as cmds


#__________ classify DAG  _________#
def selected () :

    tempSel = cmds.select (ado = 1 )
    deselect_temp = cmds.select ('HdImaging', d = 1)
    tempSel_list = cmds.ls ( sl = 1)

    if tempSel_list[0] =='HdImaging' :
        tempSel_list.remove ( 'HdImaging' )
        return tempSel_list
    
    else :
        return tempSel_list


#__________ create Rig_group _________#                                                                                                                       
def createNode_dxRig () :
    selList = selected ()
    rigGRPname = '_rig_GRP'
    
    if selList[0].find ('model') is -1 : # if selList[0] = USD #         
        create_dxRig = cmds.createNode ('dxRig', n = selList[0] + rigGRPname )
        return create_dxRig

    else : # if selList[0] = 'GRP' #
        selList_split = selList[0].split ('_')
        create_dxRig = cmds.createNode ('dxRig', n = selList_split[0] + rigGRPname)
        return create_dxRig


#__________ setAttr rigGRP _________#
def setAttrRigGRP () :
    rigGRP = createNode_dxRig ()
    rigGRP_nameSplit = rigGRP.split ('_')
    cmds.setAttr ( '%s.assetName' %rigGRP, rigGRP_nameSplit[0], type = 'string')
    cmds.setAttr ( '%s.rigType' %rigGRP, 1 )
    return rigGRP

#__________ structure the rigGRP _________#        
def build_rigGRP () :
    
    # noneTransform
    sel_List = selected ()

    
    #__placeCON__#    
    placeCON = cmds.circle (nr=(0, 1, 0), c=(0, 0, 0), r=(6), n='place_CON')
    cmds.DeleteHistory (placeCON)
    placeCON_Shape = cmds.listRelatives(placeCON[0], shapes=1)
    cmds.setAttr ("%s.overrideEnabled" %placeCON_Shape[0], 1)
    cmds.setAttr ("%s.overrideColor" %placeCON_Shape[0], 6)
    cmds.addAttr (longName ='globalScale', defaultValue=1.0)
    cmds.setAttr ('place_CON.globalScale', keyable=True)
    cmds.group (n='place_NUL')
    #__directionCON__#
    directionCON = cmds.circle (nr=(0, 1, 0), c=(0, 0, 0), r=(5.4), n='direction_CON')
    cmds.DeleteHistory (directionCON)
    directionCON_Shape = cmds.listRelatives(directionCON[0], shapes=1)
    cmds.setAttr ("%s.overrideEnabled" %directionCON_Shape[0], 1)
    cmds.setAttr ("%s.overrideColor" %directionCON_Shape[0], 17)
    cmds.group (n='direction_NUL')
    #__moveCON__#
    moveCON = cmds.circle (nr=(0, 1, 0), c=(0, 0, 0), r=(4.8), n='move_CON')
    cmds.DeleteHistory (moveCON)
    moveCON_Shape = cmds.listRelatives(moveCON[0], shapes=1)
    cmds.setAttr ("%s.overrideEnabled" %moveCON_Shape[0], 1)
    cmds.setAttr ("%s.overrideColor" %moveCON_Shape[0], 13)
    cmds.group (n='move_NUL')   
    #    DAG worldCON    #
    cmds.parent ('move_NUL', 'direction_CON')
    cmds.parent ('direction_NUL', 'place_CON')    
    #    Tranform    #
    cmds.group (em=True, n='transform_GRP')
    cmds.group (em=True, n='control_GRP')
    cmds.group (em=True, n='joint_GRP')
    cmds.parent ('control_GRP', 'joint_GRP', 'transform_GRP')  
    cmds.group (em=True, n='geometry_GRP')
    cmds.group (n='noneTrnasform_GRP')
    dxRigGRP = setAttrRigGRP ()
    cmds.parent ('place_NUL', 'transform_GRP', 'noneTrnasform_GRP', dxRigGRP) 
    

    
    # channelBox
    cmds.select ('*_CON') 
    selected_worldCON = cmds.ls(sl=1)
    for z in selected_worldCON :
        cmds.setAttr ("%s.sx" %z, lock=True, keyable=False)
        cmds.setAttr ("%s.sy" %z, lock=True, keyable=False)
        cmds.setAttr ("%s.sz" %z, lock=True, keyable=False)
        cmds.setAttr ("%s.v" %z, lock=True, keyable=False)
    cmds.select(deselect=1)        	


    # move_CON > transform_GRP 
    cmds.parentConstraint ('move_CON', 'transform_GRP', mo=1)
    # GlobalScale
    cmds.connectAttr ('place_CON.globalScale', 'transform_GRP.sx')
    cmds.connectAttr ('place_CON.globalScale', 'transform_GRP.sy')
    cmds.connectAttr ('place_CON.globalScale', 'transform_GRP.sz')
    for par_ in range ( len (sel_List ) ) :
        cmds.parent (sel_List[par_], 'geometry_GRP')   


        
    cmds.select (cl = 1)



    



    
    
						  


