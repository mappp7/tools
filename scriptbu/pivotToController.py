from util.controller import *
from util.homeNul import *


def pivotToControllerOP(mySide):
    myColor = 'blue'
    if mySide == 'R':
        myColor = 'red'
    else:
        pass

    anklePivotName =  '%s_ankleRoll_main_PIVOT' % mySide
    pivotList = [ '%s_hindLeg_inSideRoll_PIVOT'% mySide, '%s_hindLeg_outSideRoll_PIVOT'% mySide, '%s_hindLeg_heelRoll_PIVOT'% mySide, '%s_hindLeg_toeRoll_PIVOT'% mySide, '%s_hindLeg_footTwist_PIVOT'% mySide, '%s_hindLeg_ballRoll_PIVOT'% mySide, '%s_hindLeg_toeTab_PIVOT'% mySide ]
    pivotNulList = [ '%s_inSideRoll_hindLeg_NUL'% mySide ]
    # create foot controller
    ankleRollCONT = controllerShape( anklePivotName.replace( 'PIVOT', 'CON' ), 'cube', myColor )
    cvNum = cmds.getAttr( '%s.spans' % ankleRollCONT ) + cmds.getAttr( '%s.degree' % ankleRollCONT )
    cmds.select( '%s.cv[0:%s]' % ( ankleRollCONT, cvNum-1 ) )
    cmds.scale( 0.5, 0.5, 0.5 )
    cmds.select( cl=True )
    cmds.parent( '%sShape' % ankleRollCONT, anklePivotName, r=True, s=True )
    cmds.delete( ankleRollCONT )
    ankleRollCON = cmds.rename( anklePivotName, anklePivotName.replace( 'PIVOT', 'CON' ) )

    for x in range( len( pivotList ) ):
        CONT = controllerShape( pivotList[x].replace( 'PIVOT', 'CON' ), 'cube', myColor )
        cvNum = cmds.getAttr( '%s.spans' % CONT ) + cmds.getAttr( '%s.degree' % CONT )
        cmds.select( '%s.cv[0:%s]' % ( CONT, cvNum-1 ) )
        cmds.scale( 0.5, 0.5, 0.5 )
        cmds.select( cl=True )
        cmds.parent( '%sShape' % CONT, pivotList[x], r=True, s=True )
        cmds.delete( CONT )
        ankleRollCON = cmds.rename( pivotList[x], pivotList[x].replace( 'PIVOT', 'CON' ) )
        
        
        
        
    # 2018/ 01.15 >>  taehoon : change controller hierarchy!!!
    cmds.parent( '%s_hindLeg_toeTab_NUL' % mySide, '%s_hindLeg_footTwist_CON' % mySide )




    # make ankle controller by main ankle controller
    myParent = '%s_rig_ball_JNT' % mySide
    myMainCon = '%s_ankleRoll_main_CON' % mySide
    myMainNul = '%s_ankleRoll_main_NUL' % mySide
    
    myAimParnt = '%s_template_ankle_JNT' % mySide
    myAimUp = '%s_template_knee_JNT' % mySide
    
    myCon = controllerShape( myMainCon.replace( 'main_CON', 'CON' ), 'cube', myColor )
    myNul = homeNul( myCon )
    
    cmds.delete ( cmds.parentConstraint( myParent, myNul, mo=0 ) )
    cmds.delete ( cmds.aimConstraint ( myAimParnt, myNul, aim=( 1, 0, 0 ), u=( 0, 1, 0 ), wut='object', wuo=myAimUp ) )
    
    cmds.parentConstraint( myParent, myNul, mo=1 )
    cmds.parentConstraint( myCon, myMainNul, mo=1 )
	
    cmds.parent ( '%s_IK_ankle_SC_HDL' % mySide, myCon )
    
