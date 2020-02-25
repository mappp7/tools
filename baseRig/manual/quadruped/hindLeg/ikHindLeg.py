#encoding=utf-8

# hindLeg
import maya.cmds as cmds
from util.homeNul import *
from util.snap import *
from util.ikHandleMaker import * # ikHandleMaker( 'starJoint', 'endJoint', 'solver', '*gCurve' )
from util.controller import *
from util.zeroRotJoint import *


class ikHindLeg:
    def __init__( self, side ): # side = [ 'L', 'C', 'R']
    
        self.side = side
        
        self.tempList = []
        
        if self.side == 'R':
            # mirrorJoint
            cmds.mirrorJoint( 'L_template_hip_JNT', mirrorYZ=True, mirrorBehavior=True, searchReplace=[ 'L_', 'R_' ] )
            # duplicate footTemplate
            DR = cmds.duplicate( 'L_hindFootLocatorTemplate_GRP',renameChildren=True )
            cmds.scale( -1, 1, 1, DR[0] )
            for x in range(len(DR)):
                uniqueName = cmds.rename( DR[x], DR[x].replace( 'L_', 'R_' )[0:-1] )
                self.tempList.append(uniqueName)
        
        self.hindLegTempJointList = [ '%s_template_hip_JNT' % self.side, '%s_template_knee_JNT' % self.side, '%s_template_ankle_JNT' % self.side, '%s_template_ball_JNT' % self.side, '%s_template_toe_JNT' % self.side, '%s_template_toeTip_JNT' % self.side ]
        self.footTemplateLocList = [ '%s_hindLeg_inSideRollTemple' % self.side, '%s_hindLeg_outSideRollTemple' % self.side, '%s_hindLeg_heelRollTemple' % self.side, '%s_hindLeg_toeRollTemple' % self.side, '%s_hindLeg_footTwistTemple' % self.side, '%s_hindLeg_ballRollTemple' % self.side, '%s_hindLeg_toeTabTemple' % self.side ]
        
        self.IkHindLegJointList = []
        self.subIkJointList = []
        
        self.pivotList = []#[u'L_inSideRoll_PIVOT', u'L_outSideRoll_PIVOT', u'L_heelRoll_PIVOT', u'L_toeRoll_PIVOT', u'L_footTwist_PIVOT', u'L_ballRoll_PIVOT', u'L_toeTab_PIVOT']
        self.pivotNulList = []            
        
    def createIkHindLegJoint(self):
        # 조인트를 만들고 리스트를 만듬
        for x in range( len(self.hindLegTempJointList) ):
            RN = self.hindLegTempJointList[x].replace( 'template', 'IK' )
            ikJoint = cmds.joint( n=RN )
            self.IkHindLegJointList.append( ikJoint )
            
            POsnap( ikJoint, self.hindLegTempJointList[x] )
        zeroRotJoint( self.IkHindLegJointList )
        
    def createSubIkHindLegJoint(self):
        # separate duplicate for subIkSolver
        dList = cmds.duplicate( self.IkHindLegJointList[0], renameChildren=True )
        for x in range( len( dList ) ):
            rN = cmds.rename( dList[x], dList[x].replace( 'IK', 'rig' )[0:-1] )
            self.subIkJointList.append(rN)
        cmds.delete( self.subIkJointList[4] )
        del self.subIkJointList[4:]
        
    def createIK(self):
        # create IK
        RPs = ikHandleMaker( self.IkHindLegJointList[0], self.IkHindLegJointList[2], 'ikRPsolver' )
        self.RPsName = cmds.rename( RPs[0], self.IkHindLegJointList[0].replace( 'JNT', 'RP_HDL' ) )
        RPsEffectorName = cmds.rename( RPs[1], self.IkHindLegJointList[0].replace( 'JNT', 'RP_IKEFFECTOR' ) )
            
        # subRP
        sRPs = ikHandleMaker( self.subIkJointList[1], self.subIkJointList[3], 'ikRPsolver' )
        self.sRPsName = cmds.rename( sRPs[0], self.subIkJointList[0].replace( 'JNT', 'RP_HDL' ) )
        sRPsEffectorName = cmds.rename( sRPs[1], self.subIkJointList[0].replace( 'JNT', 'SS_IKEFFECTOR' ) )
        
        # sc
        self.SCsNameList = []
        for x in range(3):
            SCs = ikHandleMaker( self.IkHindLegJointList[x+2], self.IkHindLegJointList[x+3], 'ikSCsolver' )
            SCsName = cmds.rename( SCs[0], self.IkHindLegJointList[x+2].replace( 'JNT', 'SC_HDL' ) )
            SCsEffectorName = cmds.rename( SCs[1], self.IkHindLegJointList[x+2].replace( 'JNT', 'SC_IKEFFECTOR' ) )
            
            self.SCsNameList.append( SCsName )
            
    def createReverseFoot(self):
        # create foot temple
        pivotPos = cmds.xform( self.IkHindLegJointList[-2], t=True, ws=True, q=True )
        
        FTT = cmds.spaceLocator( n=self.footTemplateLocList[4] )
        cmds.move( pivotPos[0], pivotPos[1], pivotPos[2], FTT[0] )
        
        BRT = cmds.spaceLocator( n=self.footTemplateLocList[5] )
        POsnap( BRT[0], self.IkHindLegJointList[-2] )
        
        TTT = cmds.spaceLocator( n=self.footTemplateLocList[6] )
        POsnap( TTT[0], self.IkHindLegJointList[-2] )
        
        
        # create pivot positon
        for x in range( len( self.footTemplateLocList ) ):
            PL = cmds.group( em=True, n=self.footTemplateLocList[x].replace( 'Temple', '_PIVOT' ) )
            POsnap( PL, self.footTemplateLocList[x] )
            
            self.pivotList.append(PL)
            
        for x in range( len( self.pivotList ) - 1 ):
            cmds.parent( self.pivotList[x+1], self.pivotList[x] )
            
        for x in range( len( self.pivotList ) ):
            PH = homeNul( self.pivotList[x] )
            
            self.pivotNulList.append(PH)
            
        cmds.parent( self.pivotNulList[-1], self.pivotList[4] )
        
        cmds.delete( self.footTemplateLocList[4:7] )
        
        # parenting handle
        cmds.parent( self.sRPsName, self.pivotList[5] )
        
        cmds.parent( self.SCsNameList[0], self.sRPsName )
        cmds.parent( self.SCsNameList[1], self.pivotList[5] )
        cmds.parent( self.SCsNameList[2], self.pivotList[-1] )
        
        
        self.anklePivotName = cmds.group( em=True, n='%s_ankleRoll_PIVOT' % self.side )
        self.anklePos = cmds.xform( self.IkHindLegJointList[3], t=True, ws=True, q=True )
        cmds.move( self.anklePos[0], self.anklePos[1], self.anklePos[2], self.anklePivotName )
        
        cmds.delete( cmds.aimConstraint( self.subIkJointList[2], self.anklePivotName, aimVector=[ 0, 1, 0 ], upVector=[ 0, 0, 1 ], worldUpType='vector', worldUpVector=[ 0, 1, 0 ] ) )
        
        cmds.parent( self.anklePivotName, self.subIkJointList[2] )
        
        cmds.parent( self.RPsName, self.anklePivotName )
        
        homeNul( self.anklePivotName )
        
    def createController(self):
        # create controller
        haindLegControllerName = controllerShape( self.IkHindLegJointList[3].replace( 'ball_JNT', 'hindLeg_CON' ), 'cube', 'blue' )
        cmds.move( self.anklePos[0], self.anklePos[1], self.anklePos[2], haindLegControllerName )
        
        hipControllerName = controllerShape( self.IkHindLegJointList[0].replace( 'JNT', 'CON' ), 'cube', 'blue' )
        POsnap( hipControllerName, self.IkHindLegJointList[0] )
        
        hipWorldControllerName = controllerShape( self.IkHindLegJointList[0].replace( 'JNT', 'world_CON' ), 'cube', 'blue' )
        Psnap( hipWorldControllerName, self.IkHindLegJointList[0] )
        
        kneePVContollerName = cmds.spaceLocator( n=self.IkHindLegJointList[1].replace( 'JNT', 'LOC' ) )[0]
        kneePVPos = cmds.xform( self.IkHindLegJointList[0], t=True, ws=True, q=True )
        cmds.move( kneePVPos[0], kneePVPos[1], kneePVPos[2] + 20, kneePVContollerName )
        
        anklePVContollerName = controllerShape( self.IkHindLegJointList[2].replace( 'JNT', 'CON' ), 'sphere', 'blue' )
        anklePVPos = cmds.xform( self.IkHindLegJointList[2], t=True, ws=True, q=True )
        cmds.move( anklePVPos[0], anklePVPos[1], anklePVPos[2], anklePVContollerName )
        
        # controller homeNull
        homeNul( haindLegControllerName )
        hipNul = homeNul( hipControllerName )
        hipRotZNul = homeNul( hipControllerName, hipNul.replace( 'hip', 'hipRotZ' ) )
        hipNulWorldNul = homeNul( hipWorldControllerName )
        kneePVNul = homeNul( kneePVContollerName )
        homeNul( anklePVContollerName )
        
        # constraints & grouping
        cmds.parent( self.pivotNulList[0], haindLegControllerName )
        cmds.parent( kneePVNul, hipControllerName )
        cmds.parent( hipNul, hipWorldControllerName )
        
        if self.side != 'R' :
            cmds.aimConstraint( haindLegControllerName, hipRotZNul, mo=True, weight=1, aimVector=[ 1, 0, 0 ], upVector=[ 0, 1, 0 ], worldUpType='none', skip=[ 'x', 'y' ] )
        else :
            cmds.aimConstraint( haindLegControllerName, hipRotZNul, mo=True, weight=1, aimVector=[ -1, 0, 0 ], upVector=[ 0, 1, 0 ], worldUpType='none', skip=[ 'x', 'y' ] )
        
        cmds.pointConstraint( hipControllerName, self.IkHindLegJointList[0] )
        cmds.pointConstraint( hipControllerName, self.subIkJointList[0] )
        cmds.orientConstraint( hipControllerName, self.subIkJointList[0] )
        
        cmds.poleVectorConstraint( anklePVContollerName, self.sRPsName )
        cmds.poleVectorConstraint( kneePVContollerName, self.RPsName )
        
        # addAttr & connection
        cmds.addAttr( haindLegControllerName, longName='auto', at='enum', en='Angle', keyable=True )
        cmds.setAttr( '%s.auto' % haindLegControllerName, lock=True )
        cmds.addAttr( haindLegControllerName, longName='front', at='double', keyable=True, attributeType='float', min=0, max=1, dv=0.5 )
        
        cmds.addAttr( haindLegControllerName, longName='subController', at='enum', en='Visibility', keyable=True )
        cmds.setAttr( '%s.subController' % haindLegControllerName, lock=True )
        cmds.addAttr( haindLegControllerName, longName='vis', at='bool', keyable=True )
        
        cmds.setKeyframe( '%s.rz' % hipRotZNul )
        cmds.disconnectAttr( 'pairBlend1_inRotateZ1.output', 'pairBlend1.inRotateZ1' )
        cmds.delete( 'pairBlend1_inRotateZ1' )
        cmds.rename( 'pairBlend1', hipRotZNul.replace( 'NUL', 'PBD' ) )
        cmds.connectAttr ( '%s.front' % haindLegControllerName, '%s.blendAim1' % hipRotZNul )
        
        # create foot controller
        ankleRollCONT = controllerShape( self.anklePivotName.replace( 'PIVOT', 'CON' ), 'cube', 'yellow' )
        cvNum = cmds.getAttr( '%s.spans' % ankleRollCONT ) + cmds.getAttr( '%s.degree' % ankleRollCONT )
        cmds.select( '%s.cv[0:%s]' % ( ankleRollCONT, cvNum-1 ) )
        cmds.scale( 0.5, 0.5, 0.5 )
        cmds.select( cl=True )
        cmds.parent( '%sShape' % ankleRollCONT, self.anklePivotName, r=True, s=True )
        cmds.delete( ankleRollCONT )
        ankleRollCON = cmds.rename( self.anklePivotName, self.anklePivotName.replace( 'PIVOT', 'CON' ) )
        
        for x in range( len( self.pivotList ) ):
            CONT = controllerShape( self.pivotList[x].replace( 'PIVOT', 'CON' ), 'cube', 'yellow' )
            cvNum = cmds.getAttr( '%s.spans' % CONT ) + cmds.getAttr( '%s.degree' % CONT )
            cmds.select( '%s.cv[0:%s]' % ( CONT, cvNum-1 ) )
            cmds.scale( 0.5, 0.5, 0.5 )
            cmds.select( cl=True )
            cmds.parent( '%sShape' % CONT, self.pivotList[x], r=True, s=True )
            cmds.delete( CONT )
            ankleRollCON = cmds.rename( self.pivotList[x], self.pivotList[x].replace( 'PIVOT', 'CON' ) )
        
        cmds.connectAttr( '%s.vis' % haindLegControllerName, '%s.visibility' % self.pivotNulList[0] )
        
    def cleanUpScene(self):
        if len(self.tempList) == 0:
            pass
        else:
            cmds.delete( self.tempList )
        
        
def quadrupedHindLegRun():
    IHL = ikHindLeg('R')
    IHL.createIkHindLegJoint()
    IHL.createSubIkHindLegJoint()
    IHL.createIK()
    IHL.createReverseFoot()
    IHL.createController()
    IHL.cleanUpScene()
    
quadrupedHindLegRun()