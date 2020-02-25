#encoding=utf-8

# foreLeg
import maya.cmds as cmds
from util.homeNul import *
from util.snap import *
from util.ikHandleMaker import * # ikHandleMaker( 'starJoint', 'endJoint', 'solver', '*gCurve' )
from util.controller import *
from util.zeroRotJoint import *


class ikForeLeg:
    def __init__( self, side ): # side = [ 'L', 'C', 'R']
    
        self.side = side
        
        #self.tempList = []
        """
        if self.side == 'R':
            # mirrorJoint
            cmds.mirrorJoint( 'L_template_hip_JNT', mirrorYZ=True, mirrorBehavior=True, searchReplace=[ 'L_', 'R_' ] )
            # duplicate footTemplate
            DR = cmds.duplicate( 'L_foreFootLocatorTemplate_GRP',renameChildren=True )
            cmds.scale( -1, 1, 1, DR[0] )
            for x in range(len(DR)):
                uniqueName = cmds.rename( DR[x], DR[x].replace( 'L_', 'R_' )[0:-1] )
                self.tempList.append(uniqueName)
        """
        self.foreLegTempJointList = [ '%s_template_clavicle_JNT' % self.side, '%s_template_shoulder_JNT' % self.side, '%s_template_edbow_JNT' % self.side, '%s_template_wrist_JNT' % self.side, '%s_template_foot1_JNT' % self.side, '%s_template_foot2_JNT' % self.side, '%s_template_footTip_JNT' % self.side ]
        self.footTemplateLocList = [ '%s_foreLeg_inSideRollTemple' % self.side, '%s_foreLeg_outSideRollTemple' % self.side, '%s_foreLeg_heelRollTemple' % self.side, '%s_foreLeg_toeRollTemple' % self.side, '%s_foreLeg_footTwistTemple' % self.side, '%s_foreLeg_ballRollTemple' % self.side, '%s_foreLeg_toeTabTemple' % self.side ]
        
        self.IkForeLegJointList = []
        self.subIkJointList = []
        
        self.pivotList = []#[u'L_inSideRoll_PIVOT', u'L_outSideRoll_PIVOT', u'L_heelRoll_PIVOT', u'L_toeRoll_PIVOT', u'L_footTwist_PIVOT', u'L_ballRoll_PIVOT', u'L_toeTab_PIVOT']
        self.pivotNulList = []
        
    def createIkForeLegJoint(self):
        # 조인트를 만들고 리스트를 만듬
        
        print '_____________________________________________________________________________________________________________________________________________________________________________'
        
        for x in range( len(self.foreLegTempJointList) ):
            RN = self.foreLegTempJointList[x].replace( 'template', 'IK' )
            ikJoint = cmds.joint( n=RN )
            self.IkForeLegJointList.append( ikJoint )
            
            POsnap( ikJoint, self.foreLegTempJointList[x] )
        zeroRotJoint( self.IkForeLegJointList )
        
        print self.IkForeLegJointList
        print '_____________________________________________________________________________________________________________________________________________________________________________'
        
    def createSubIkForeLegJoint(self):
        # separate duplicate for subIkSolver
        dList = cmds.duplicate( self.IkForeLegJointList[0], renameChildren=True )
        for x in range( len( dList ) ):
            rN = cmds.rename( dList[x], dList[x].replace( 'IK', 'subIk' )[0:-1] )
            self.subIkJointList.append(rN)
        cmds.delete( self.subIkJointList[5] )
        
        del self.subIkJointList[-2]
        
        print self.subIkJointList
        
    def createIK(self):
        # create IK
        RPs = ikHandleMaker( self.IkForeLegJointList[1], self.IkForeLegJointList[3], 'ikRPsolver' )
        self.RPsName = cmds.rename( RPs[0], self.IkForeLegJointList[1].replace( 'JNT', 'RP_HDL' ) )
        RPsEffectorName = cmds.rename( RPs[1], self.IkForeLegJointList[1].replace( 'JNT', 'RP_IKEFFECTOR' ) )
        
        RP1 = ikHandleMaker( self.IkForeLegJointList[3], self.IkForeLegJointList[4], 'ikRPsolver' )
        self.RP1Name = cmds.rename( RP1[0], self.IkForeLegJointList[3].replace( 'JNT', 'RP_HDL' ) )
        RP1EffectorName = cmds.rename( RP1[1], self.IkForeLegJointList[3].replace( 'JNT', 'RP_IKEFFECTOR' ) )
        
        SCs2 = ikHandleMaker( self.IkForeLegJointList[4], self.IkForeLegJointList[5], 'ikSCsolver' )
        self.SCs2Name = cmds.rename( SCs2[0], self.IkForeLegJointList[4].replace( 'JNT', 'SC_HDL' ) )
        SCs2EffectorName = cmds.rename( SCs2[1], self.IkForeLegJointList[4].replace( 'JNT', 'SC_IKEFFECTOR' ) )
        
        SCs3 = ikHandleMaker( self.IkForeLegJointList[5], self.IkForeLegJointList[6], 'ikSCsolver' )
        self.SCs3Name = cmds.rename( SCs3[0], self.IkForeLegJointList[5].replace( 'JNT', 'SC_HDL' ) )
        SCs3EffectorName = cmds.rename( SCs3[1], self.IkForeLegJointList[5].replace( 'JNT', 'SC_IKEFFECTOR' ) )
        
        
        G_RP = ikHandleMaker( self.subIkJointList[1], self.subIkJointList[4], 'ikRPsolver' )
        self.G_RPName = cmds.rename( G_RP[0], self.subIkJointList[1].replace( 'JNT', 'RP_HDL' ) )
        G_RPEffectorName = cmds.rename( G_RP[1], self.subIkJointList[1].replace( 'JNT', 'RP_IKEFFECTOR' ) )
        
    def createReverseFoot(self):
        # create foot temple
        pivotPos = cmds.xform( self.IkForeLegJointList[-2], t=True, ws=True, q=True )
        
        FTT = cmds.spaceLocator( n=self.footTemplateLocList[4] )
        cmds.move( pivotPos[0], pivotPos[1], pivotPos[2], FTT[0] )
        
        BRT = cmds.spaceLocator( n=self.footTemplateLocList[5] )
        POsnap( BRT[0], self.IkForeLegJointList[-2] )
        
        TTT = cmds.spaceLocator( n=self.footTemplateLocList[6] )
        POsnap( TTT[0], self.IkForeLegJointList[-2] )
        
        
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
        cmds.parent( self.G_RPName, self.pivotList[5] )
        
        cmds.parent( self.RP1Name, self.pivotList[5] )
        cmds.parent( self.SCs2Name, self.pivotList[5] )
        cmds.parent( self.SCs3Name, self.pivotList[-1] )
        
        self.wristPivotName = cmds.group( em=True, n='L_wistRoll_PIVOT' )
        self.wristPos = cmds.xform( self.IkForeLegJointList[4], t=True, ws=True, q=True )
        cmds.move( self.wristPos[0], self.wristPos[1], self.wristPos[2], self.wristPivotName )
        cmds.delete( cmds.aimConstraint( self.subIkJointList[3], self.wristPivotName, aimVector=[ 0, 1, 0 ], upVector=[ 0, 0, 1 ], worldUpType='vector', worldUpVector=[ 0, 1, 0 ] ) )
        #cmds.parent( self.wristPivotName, self.subIkJointList[2] )
        
        cmds.parent( self.RPsName, self.wristPivotName )
        
        self.wristPivotNameNul = homeNul( self.wristPivotName )
        print self.wristPivotNameNul
        
    def createController(self):
        # create controller
        foreLegControllerName = controllerShape( self.IkForeLegJointList[4].replace( 'foot1_JNT', 'foreLeg_CON' ), 'cube', 'blue' )
        cmds.move( self.wristPos[0], self.wristPos[1], self.wristPos[2], foreLegControllerName )
        
        clavicleControllerName = controllerShape( self.IkForeLegJointList[0].replace( 'JNT', 'CON' ), 'cube', 'blue' )
        shoulderPos = cmds.xform( self.IkForeLegJointList[0], t=True, ws=True, q=True )
        shoulderRot = cmds.xform( self.IkForeLegJointList[0], ro=True, ws=True, q=True )
        cmds.move( shoulderPos[0], shoulderPos[1], shoulderPos[2], clavicleControllerName )
        cmds.rotate( shoulderRot[0], shoulderRot[1], shoulderRot[2], clavicleControllerName )
        
        clavicleWorldControllerName = controllerShape( self.IkForeLegJointList[0].replace( 'JNT', 'world_CON' ), 'cube', 'blue' )
        cmds.move( shoulderPos[0], shoulderPos[1], shoulderPos[2], clavicleWorldControllerName )
        
        elbowPVContollerName = controllerShape( self.IkForeLegJointList[2].replace( 'JNT', 'CON' ), 'sphere', 'blue' )
        elbowPVPos = cmds.xform( self.IkForeLegJointList[2], t=True, ws=True, q=True )
        cmds.move( elbowPVPos[0], elbowPVPos[1], elbowPVPos[2], elbowPVContollerName )
        
        # controller homeNull
        homeNul( foreLegControllerName )
        shoulderContollerNul = homeNul( clavicleControllerName )
        elbowPVContollerNameNul = homeNul( elbowPVContollerName )
        cmds.select( elbowPVContollerNameNul )
        cmds.move( -5, r=True, z=True )
        
        clavicleWorldControllerNul = homeNul( clavicleWorldControllerName )
        
        # constraints & grouping
        cmds.parent( self.pivotNulList[0], foreLegControllerName )
        cmds.parent( shoulderContollerNul, clavicleWorldControllerName )
        
        # add attr
        cmds.addAttr( foreLegControllerName, longName='foot', at='enum', en='Controls', keyable=True )
        cmds.setAttr( '%s.foot' % foreLegControllerName, lock=True )
        
        #########################################################################################################################
        # create clavicleControllerRotZNul
        clavicleControllerRotZNul = homeNul( clavicleControllerName, clavicleControllerName.replace( '_CON', 'RotZ_NUL' ) )
        
        # create clavicle
        cmds.aimConstraint( foreLegControllerName, clavicleControllerRotZNul, mo=True, worldUpType='none', skip=['x', 'y'] )
        
        cmds.setKeyframe( '%s.rz' % clavicleControllerRotZNul )
        cmds.disconnectAttr( 'pairBlend1_inRotateZ1.output', 'pairBlend1.inRotateZ1' )
        cmds.delete( 'pairBlend1_inRotateZ1' )
        
        cmds.rename( 'pairBlend1', 'L_clvicleRotZ_PBD' )
        
        # add attr autoClavicle
        cmds.addAttr( foreLegControllerName, longName='auto', at='enum', en='Shoulder', keyable=True )
        cmds.setAttr( '%s.auto' % foreLegControllerName, lock=True )
        cmds.addAttr( foreLegControllerName, longName='front', at='double', keyable=True, attributeType='float', min=0, max=1, dv=0.5 )
        
        # connection
        cmds.connectAttr( '%s.front' % foreLegControllerName, '%s.blendAim1' % clavicleControllerRotZNul )
        
        # parentConstraint
        cmds.parentConstraint( clavicleControllerName, self.IkForeLegJointList[0], mo=True )
        cmds.parentConstraint( clavicleControllerName, self.subIkJointList[0], mo=True )
        
        # create foot controller
        wristRollCONT = controllerShape( self.wristPivotName.replace( 'PIVOT', 'CON' ), 'cube', 'yellow' )
        cvNum = cmds.getAttr( '%s.spans' % wristRollCONT ) + cmds.getAttr( '%s.degree' % wristRollCONT )
        cmds.select( '%s.cv[0:%s]' % ( wristRollCONT, cvNum-1 ) )
        cmds.scale( 1.5, 1.5, 1.5 )
        cmds.select( cl=True )
        cmds.parent( '%sShape' % wristRollCONT, self.wristPivotName, r=True, s=True )
        cmds.delete( wristRollCONT )
        wristRollCON = cmds.rename( self.wristPivotName, self.wristPivotName.replace( 'PIVOT', 'CON' ) )
        
        for x in range( len( self.pivotList ) ):
            CONT = controllerShape( self.pivotList[x].replace( 'PIVOT', 'CON' ), 'cube', 'yellow' )
            cvNum = cmds.getAttr( '%s.spans' % CONT ) + cmds.getAttr( '%s.degree' % CONT )
            cmds.select( '%s.cv[0:%s]' % ( CONT, cvNum-1 ) )
            cmds.scale( 0.5, 0.5, 0.5 )
            cmds.select( cl=True )
            cmds.parent( '%sShape' % CONT, self.pivotList[x], r=True, s=True )
            cmds.delete( CONT )
            wristRollCON = cmds.rename( self.pivotList[x], self.pivotList[x].replace( 'PIVOT', 'CON' ) )
            
        # create spaceLocator
        shoulderLOC = cmds.spaceLocator( n=self.subIkJointList[1].replace( 'JNT', 'PV_LOC' ) )
        shoulderLocatorNUL = homeNul( shoulderLOC[0] )
        Psnap( shoulderLocatorNUL, self.subIkJointList[1] )
        cmds.setAttr( '%s.translateZ' % shoulderLOC[0], -5 )
        
        wristRollLOC = cmds.spaceLocator( n=wristRollCONT.replace( 'CON', 'PV_LOC' ) )
        wristRollLocatorNUL = homeNul( wristRollLOC[0] )
        cmds.parent( wristRollLocatorNUL, wristRollCONT )
        Psnap( wristRollLocatorNUL, wristRollCONT )
        cmds.setAttr( '%s.translateZ' % wristRollLOC[0], -5 )
        
        # pole Vector Constrain
        cmds.poleVectorConstraint( shoulderLOC, self.G_RPName )
        cmds.poleVectorConstraint( elbowPVContollerName, self.RPsName )
        cmds.poleVectorConstraint( wristRollLOC, self.RP1Name )
        
        # 
        cmds.parentConstraint( self.subIkJointList[-2], self.wristPivotNameNul, mo=True )
        
        cmds.setKeyframe( '%s.rx' % self.wristPivotNameNul )
        cmds.setKeyframe( '%s.ry' % self.wristPivotNameNul )
        cmds.setKeyframe( '%s.rz' % self.wristPivotNameNul )
        
        cmds.disconnectAttr( 'pairBlend1_inRotateX1.output', 'pairBlend1.inRotateX1' )
        cmds.disconnectAttr( 'pairBlend1_inRotateY1.output', 'pairBlend1.inRotateY1' )
        cmds.disconnectAttr( 'pairBlend1_inRotateZ1.output', 'pairBlend1.inRotateZ1' )
        
        cmds.delete( 'pairBlend1_inRotateX1', 'pairBlend1_inRotateY1', 'pairBlend1_inRotateZ1' )
        
        cmds.rename( 'pairBlend1', 'L_clvicleRotZ_PBD' )
        
        #
        cmds.addAttr( wristRollCONT, longName='wristRoll', at='enum', en='Lock', keyable=True )
        cmds.setAttr( '%s.wristRoll' % wristRollCONT, lock=True )
        cmds.addAttr( wristRollCONT, longName='fallowRotate', at='double', keyable=True, attributeType='float', min=0, max=1, dv=1 )
        
        cmds.connectAttr( '%s.fallowRotate' % wristRollCONT, '%s.blendParent1' % self.wristPivotNameNul )    
        
        #cmds.connectAttr( '%s.vis' % haindLegControllerName, '%s.visibility' % self.pivotNulList[0] )      
        
        cmds.select( cl=True )  
        
        
def quadrupedForeLegRun():
    IFL = ikForeLeg('L')
    IFL.createIkForeLegJoint()
    IFL.createSubIkForeLegJoint()
    IFL.createIK()
    IFL.createReverseFoot()
    IFL.createController()
    #IFL.cleanUpScene()
    
    
quadrupedForeLegRun()