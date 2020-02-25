#  /////////////////////////////////////////////////////////////////////
# ///                    1. build rigGRP                            ///
#///////////////////////////////////////////////////////////////////// 

import maya.cmds as cmds

def buildrigGRP () :        
    
    ###############################
    ###     'world con' info    ###
    ###############################
    grid_ct = (0, 0, 0) 
    pr = (5) # pr : placeCON radius #
    #------------------------------------#
    
    placeCON = cmds.circle (nr = (0, 1, 0), c = grid_ct, r = pr, n = 'place_CON' ) # flag : -nr (normal : The normal of the plane in which the circle will lie ) #
    placeNUL = cmds.group (n = 'place_NUL')
    direction_NUL = cmds.parent ( (cmds.group ( (cmds.circle (nr = (0, 1, 0), c = grid_ct, r = (pr*0.875), n = 'direction_CON' )), n = 'direction_NUL') ), 'place_CON' )
    move_NUL = cmds.parent ( (cmds.group ( (cmds.circle (nr = (0, 1, 0), c = grid_ct, r = ((pr*0.875)*.875), n = 'move_CON' )), n = 'move_NUL') ), 'direction_CON')
    
    #------------------------------------#
    transformGRP = cmds.group (em=1, n = 'transform_GRP')
    cmds.parent ( (cmds.group (em=1, n='control_GRP')), (cmds.group (em=1, n='joint_GRP')), transformGRP)
    #------------------------------------#
    noneTransformGRP = cmds.group (em=1, n = 'noneTransform_GRP')
    cmds.parent ( (cmds.group (em=1, n='geometry_GRP')), (cmds.group (em=1, n='auxiliry_GRP')), noneTransformGRP )
    #------------------------------------#
    
    dxRigNode = cmds.createNode ('dxRig')
    cmds.parent ( placeNUL, transformGRP, noneTransformGRP, dxRigNode), cmds.select(deselect=1)