# hindLeg

import maya.cmds as cmds
import maya.mel as mel
from baseRig.util.homeNul import *
from baseRig.util.ikHandleMaker import * # ikHandleMaker( 'starJoint', 'endJoint', 'solver', '*gCurve' )
from baseRig.util.controller import *



##################################################
def pSnap( childOBJ, parentOBJ ):
    cmds.parent( childOBJ, parentOBJ )
    cmds.setAttr( '%s.translateX' % childOBJ, 0 )
    cmds.setAttr( '%s.translateY' % childOBJ, 0 )
    cmds.setAttr( '%s.translateZ' % childOBJ, 0 )
    cmds.setAttr( '%s.rotateX' % childOBJ, 0 )
    cmds.setAttr( '%s.rotateY' % childOBJ, 0 )
    cmds.setAttr( '%s.rotateZ' % childOBJ, 0 )
    cmds.parent( childOBJ, w=True )
##################################################


def L_ikHindLegOP():

    hindLegIkJointList = [ 'L_IK_hip_JNT', 'L_IK_knee_JNT', 'L_IK_ankle_JNT', 'L_IK_ball_JNT', 'L_IK_toe_JNT', 'L_IK_toeTip_JNT' ]

    footTemplateLocLict = [ 'L_hindLeg_inSideRollTemple', 'L_hindLeg_outSideRollTemple', 'L_hindLeg_heelRollTemple', 'L_hindLeg_toeRollTemple', 'L_hindLeg_footTwistTemple', 'L_hindLeg_ballRollTemple', 'L_hindLeg_toeTabTemple' ]

    # separate duplicate for ikSpringSolver
    sSJointList = []
    dList = cmds.duplicate( hindLegIkJointList[0], renameChildren=True )
    for x in range( len( dList ) ):
        rN = cmds.rename( dList[x], dList[x].replace( 'IK', 'rig' )[0:-1] )
        sSJointList.append(rN)
    cmds.delete( sSJointList[4] )
    del sSJointList[4:]

    # create IK
    RPs = ikHandleMaker( hindLegIkJointList[0], hindLegIkJointList[2], 'ikRPsolver' )
    RPsName = cmds.rename( RPs[0], hindLegIkJointList[0].replace( 'JNT', 'RP_HDL' ) )
    RPsEffectorName = cmds.rename( RPs[1], hindLegIkJointList[0].replace( 'JNT', 'RP_IKEFFECTOR' ) )

    SCs1 = ikHandleMaker( hindLegIkJointList[2], hindLegIkJointList[3], 'ikSCsolver' )
    SCs1Name = cmds.rename( RPs[0], hindLegIkJointList[2].replace( 'JNT', 'SC_HDL' ) )
    SCs1EffectorName = cmds.rename( RPs[1], hindLegIkJointList[2].replace( 'JNT', 'SC_IKEFFECTOR' ) )

    SCs2 = ikHandleMaker( hindLegIkJointList[3], hindLegIkJointList[4], 'ikSCsolver' )
    SCs2Name = cmds.rename( RPs[0], hindLegIkJointList[3].replace( 'JNT', 'SC_HDL' ) )
    SCs2EffectorName = cmds.rename( RPs[1], hindLegIkJointList[3].replace( 'JNT', 'SC_IKEFFECTOR' ) )

    SCs3 = ikHandleMaker( hindLegIkJointList[4], hindLegIkJointList[5], 'ikSCsolver' )
    SCs3Name = cmds.rename( RPs[0], hindLegIkJointList[4].replace( 'JNT', 'SC_HDL' ) )
    SCs3EffectorName = cmds.rename( RPs[1], hindLegIkJointList[4].replace( 'JNT', 'SC_IKEFFECTOR' ) )

    mel.eval( 'ikSpringSolver;' )
    Ss = cmds.ikHandle ( sj=sSJointList[0], ee=sSJointList[3], sol='ikSpringSolver' )
    SsName = cmds.rename( RPs[0], sSJointList[0].replace( 'JNT', 'SS_HDL' ) )
    SsEffectorName = cmds.rename( RPs[1], sSJointList[0].replace( 'JNT', 'SS_IKEFFECTOR' ) )

    ####################################################################################################################################

    IST = footTemplateLocLict[0]
    OST = footTemplateLocLict[1]
    HRT = footTemplateLocLict[2]
    TRT = footTemplateLocLict[3]

    FTT = footTemplateLocLict[4]

    BRT = footTemplateLocLict[5]

    TTT = cmds.spaceLocator( n=footTemplateLocLict[6] )
    pSnap( TTT[0], hindLegIkJointList[-2] )

    ####################################################################################################################################

    # create pivot positon
    pivotList = []
    pivotNulList = []

    for x in range( len( footTemplateLocLict ) ):
        PL = cmds.group( em=True, n=footTemplateLocLict[x].replace( 'Temple', '_PIVOT' ) )
        pSnap( PL, footTemplateLocLict[x] )

        pivotList.append(PL)

    for x in range( len( pivotList ) - 1 ):
        cmds.parent( pivotList[x+1], pivotList[x] )

    for x in range( len( pivotList ) ):
        PH = homeNul( pivotList[x] )
        pivotNulList.append(PH)



    cmds.parent( SCs2Name, pivotList[5] )
    cmds.parent( SCs3Name, pivotList[-1] )

    anklePivotName = cmds.group( em=True, n='L_ankleRoll_main_PIVOT' )
    anklePos = cmds.xform( hindLegIkJointList[3], t=True, ws=True, q=True )
    cmds.move( anklePos[0], anklePos[1], anklePos[2], anklePivotName )
    cmds.parent( anklePivotName, sSJointList[2] )

    homeNul( anklePivotName )

    # create controller
    haindLegControllerName = controllerShape( hindLegIkJointList[3].replace( 'ball_JNT', 'hindLeg_CON' ), 'cube', 'blue' )
    cmds.move( anklePos[0], anklePos[1], anklePos[2], haindLegControllerName )

    hipContollerName = controllerShape( hindLegIkJointList[0].replace( 'JNT', 'CON' ), 'cube', 'blue' )
    hipPos = cmds.xform( hindLegIkJointList[0], t=True, ws=True, q=True )
    cmds.move( hipPos[0], hipPos[1], hipPos[2], hipContollerName )

    kneePVContollerName = controllerShape( hindLegIkJointList[1].replace( 'JNT', 'CON' ), 'sphere', 'blue' )
    kneePVPos = cmds.xform( hindLegIkJointList[1], t=True, ws=True, q=True )
    cmds.move( kneePVPos[0], kneePVPos[1], kneePVPos[2], kneePVContollerName )

    # controller homeNull
    homeNul( haindLegControllerName )
    homeNul( hipContollerName )
    homeNul( kneePVContollerName )

    # constraints & grouping
    cmds.parent( pivotNulList[0], haindLegControllerName )

    cmds.pointConstraint( hipContollerName, hindLegIkJointList[0] )
    cmds.pointConstraint( hipContollerName, sSJointList[0] )

    cmds.poleVectorConstraint( kneePVContollerName, SsName )
    cmds.poleVectorConstraint( sSJointList[1], RPsName )

    cmds.parent( SsName, pivotList[5] )

    cmds.parent( RPsName, anklePivotName )





    # add Attr
    cmds.addAttr( haindLegControllerName, longName='foot', at='enum', en='Controls', keyable=True )
    cmds.setAttr( '%s.foot' % haindLegControllerName, lock=True )

    cmds.addAttr( haindLegControllerName, longName='leg', at='enum', en='Angle', keyable=True )
    cmds.setAttr( '%s.leg' % haindLegControllerName, lock=True )
    cmds.addAttr( haindLegControllerName, longName='angle', at='double', keyable=True, attributeType='float', min=-10, max=10, dv=0 )

    SAB0 = cmds.createNode( 'setRange', n=haindLegControllerName.replace( '_CON', 'SAB0_RNG' ) )
    SAB1 = cmds.createNode( 'setRange', n=haindLegControllerName.replace( '_CON', 'SAB1_RNG' ) )

    cmds.setAttr( '%s.minX' % SAB0, 0 )
    cmds.setAttr( '%s.maxX' % SAB0, 1 )
    cmds.setAttr( '%s.oldMinX' % SAB0, -10 )
    cmds.setAttr( '%s.oldMaxX' % SAB0, 10 )

    cmds.setAttr( '%s.minX' % SAB1, 1 )
    cmds.setAttr( '%s.maxX' % SAB1, 0 )
    cmds.setAttr( '%s.oldMinX' % SAB1, -10 )
    cmds.setAttr( '%s.oldMaxX' % SAB1, 10 )

    cmds.connectAttr( '%s.angle' % haindLegControllerName, '%s.valueX' % SAB0 )
    cmds.connectAttr( '%s.outValue.outValueX' % SAB0, '%s.springAngleBias[0].springAngleBias_FloatValue' % SsName )

    cmds.connectAttr( '%s.angle' % haindLegControllerName, '%s.valueX' % SAB1 )
    cmds.connectAttr( '%s.outValue.outValueX' % SAB1, '%s.springAngleBias[1].springAngleBias_FloatValue' % SsName )
