import maya.cmds as cmds
import baseRig.util.homeNul as HN

# Node base PV position !

# 3 joint list
#jnt = cmds.ls( sl=True, type='joint' )

def nodePVconnect( jnt ):
    #decomposeMatrix
    rootJdecompose = cmds.createNode( 'decomposeMatrix', n=jnt[0].replace( 'JNT', 'DCM' ) )
    middleJdecompose = cmds.createNode( 'decomposeMatrix', n=jnt[1].replace( 'JNT', 'DCM' ) )
    tipJdecompose = cmds.createNode( 'decomposeMatrix', n=jnt[2].replace( 'JNT', 'DCM' ) )

    #connections
    cmds.connectAttr( '%s.worldMatrix[0]' % jnt[0], '%s.inputMatrix' % rootJdecompose )
    cmds.connectAttr( '%s.worldMatrix[0]' % jnt[1], '%s.inputMatrix' % middleJdecompose )
    cmds.connectAttr( '%s.worldMatrix[0]' % jnt[2], '%s.inputMatrix' % tipJdecompose )

    #plusMinusAverage
    sumPMA = cmds.createNode( 'plusMinusAverage', n='%sPos_sum_%sPos_PMA' % ( jnt[0].replace( '_JNT', '' ), jnt[2].replace( '_JNT', '' ) )  )
    cmds.setAttr( '%s.operation' % sumPMA, 1 )

    #connections
    cmds.connectAttr( '%s.outputTranslate' % rootJdecompose, '%s.input3D[0]' % sumPMA )
    cmds.connectAttr( '%s.outputTranslate' % tipJdecompose, '%s.input3D[1]' % sumPMA )

    #multiplyDivide
    divideSumPMA = cmds.createNode( 'multiplyDivide', n=sumPMA.replace( 'PMA', 'halfDvide_MPD' ) )
    cmds.setAttr( '%s.operation' % divideSumPMA, 2 )
    cmds.setAttr( '%s.input2X' % divideSumPMA, 2 )
    cmds.setAttr( '%s.input2Y' % divideSumPMA, 2 )
    cmds.setAttr( '%s.input2Z' % divideSumPMA, 2 )

    #connections
    cmds.connectAttr( '%s.output3D' % sumPMA, '%s.input1' % divideSumPMA )

    #plusMinusAverage( calculate vector )
    VT = cmds.createNode( 'plusMinusAverage', n='to_%s_vector_PMA' % jnt[1].replace( 'JNT', 'joint' ) )
    cmds.setAttr( '%s.operation' % VT, 2 )

    #connections
    cmds.connectAttr( '%s.outputTranslate' % middleJdecompose, '%s.input3D[0]' % VT )
    cmds.connectAttr( '%s.output' % divideSumPMA, '%s.input3D[1]' % VT )

    # offset
    offsetVector = cmds.createNode( 'multiplyDivide', n='%s_MPD' % VT.replace( 'PMA', 'offset' ) )
    cmds.connectAttr( '%s.output3D' % VT, '%s.input1' % offsetVector )

    #plusMinusAverage( middleJ + offset + vector )
    PVposition = cmds.createNode( 'plusMinusAverage', n='%s_vector_PMA' % divideSumPMA.replace( 'MPD', 'sum' ) )
    cmds.setAttr( '%s.operation' % PVposition, 1 )

    #connections
    cmds.connectAttr( '%s.output' % divideSumPMA, '%s.input3D[0]' % PVposition )
    cmds.connectAttr( '%s.output' % offsetVector, '%s.input3D[1]' % PVposition )

    # finish
    loc = cmds.spaceLocator( n=jnt[1].replace( 'JNT', 'pv_LOC' ) )
    cmds.connectAttr( '%s.output3D' % PVposition, '%s.translate' % loc[0] )

    homeN = HN.homeNul( loc[0] )
    return homeN
