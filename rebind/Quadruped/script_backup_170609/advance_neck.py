import maya.cmds as cmds
import maya.mel as mel


def neckAdvanveOP():
    

    headPosition = cmds.xform ( 'C_IK_head_CON', q=1, rp=1, ws=1 )
    neckPosition = cmds.xform ( 'C_IK_neck1_CON', q=1, rp=1, ws=1 )
    
    neckFollowCRV = cmds.curve ( p=( headPosition, headPosition, neckPosition, neckPosition) )
    neckFollowCRV = cmds.rename ( neckFollowCRV, 'neck_follow_CRV' )
    
    neckFollowCRVShape = cmds.listRelatives ( neckFollowCRV, s=1 )[0]
    
    cmds.connectAttr ( 'C_IK_head_aTwist_LOCShape.worldPosition[0]', neckFollowCRVShape+'.controlPoints[0]' )
    cmds.connectAttr ( 'C_IK_head_aTwist_LOCShape.worldPosition[0]', neckFollowCRVShape+'.controlPoints[1]' )
    cmds.connectAttr ( 'C_IK_neck1_aTwist_LOCShape.worldPosition[0]', neckFollowCRVShape+'.controlPoints[2]' )
    cmds.connectAttr ( 'C_IK_neck1_aTwist_LOCShape.worldPosition[0]', neckFollowCRVShape+'.controlPoints[3]' )
    
    NULList = [ 'C_IK_neck_CRV2_NUL', 'C_IK_neck_CRV4_NUL' ]
    LOCList = [ 'C_IK_neck_CRV2_LOC', 'C_IK_neck_CRV4_LOC' ]
    
    cmds.parent ( LOCList, w=1 )
    


    for x in range(2):
        NPC = cmds.createNode ( 'nearestPointOnCurve', n='neck_follow%s_NPC' %(x+2) )
        LOCShape = cmds.listRelatives ( LOCList[x], s=1 )[0]
        cmds.connectAttr ( LOCShape+'.worldPosition[0]', NPC+'.inPosition' )    
        cmds.connectAttr ( neckFollowCRVShape+'.worldSpace[0]', NPC+'.inputCurve' )
        parameterValue = cmds.getAttr ( NPC+'.parameter' )
        cmds.delete ( NPC )
        
        PCV = cmds.createNode ( 'pointOnCurveInfo', n='neck_follow%s_PCV' %(x+2) )
        cmds.connectAttr ( neckFollowCRVShape+'.worldSpace[0]', PCV+'.inputCurve' )
        cmds.setAttr ( PCV+'.turnOnPercentage', 1 )
        cmds.setAttr ( PCV+'.parameter', parameterValue )
        
        cmds.connectAttr ( PCV+'.position', NULList[x]+'.translate', f=1 )
        
        cmds.parent ( LOCList[x], NULList[x] )
        
    cmds.parent ( 'neck_follow_CRV', 'auxillary_GRP' )
    
    
    rotateNUL = cmds.group ( 'C_IK_neckMiddle_CON', n='C_IK_neckMiddle_rotate_NUL' )
    
    upLOC = cmds.spaceLocator ( n='neck_up_LOC' )[0]

    cmds.delete ( cmds.parentConstraint ( 'C_IK_neck1Sub_CON', 'neck_up_LOC', mo=0 ) )
    cmds.parent (  upLOC, 'C_IK_neck1Sub_CON'  )
    
    cmds.select ( upLOC )
    cmds.move ( 0, 5, 0, r=1, os=1, wd=1 )
    
    cmds.aimConstraint ( 'C_IK_headSub_CON', 'C_IK_neckMiddle_rotate_NUL', mo=1, wut='object',  wuo=upLOC )
    
    cmds.delete ( 'C_IK_neckMiddle_NUL_parentConstraint1' )
    cmds.pointConstraint ( 'C_IK_headSub_CON', 'C_IK_neck1Sub_CON', 'C_IK_neckMiddle_NUL', mo=1 )
    
    
    



    


