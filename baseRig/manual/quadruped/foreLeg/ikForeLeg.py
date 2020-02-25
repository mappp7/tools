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
        self.clavicleTempJointList = [ 'L_template_clavicle_JNT', 'L_template_clavicleTip_JNT' ]
        self.foreLegTempJointList = [ '%s_template_shoulder_JNT' % self.side, '%s_template_edbow_JNT' % self.side, '%s_template_wrist_JNT' % self.side, '%s_template_foot1_JNT' % self.side, '%s_template_foot2_JNT' % self.side, '%s_template_footTip_JNT' % self.side ]
        self.footTemplateLocList = [ '%s_foreLeg_inSideRollTemple' % self.side, '%s_foreLeg_outSideRollTemple' % self.side, '%s_foreLeg_heelRollTemple' % self.side, '%s_foreLeg_toeRollTemple' % self.side, '%s_foreLeg_footTwistTemple' % self.side, '%s_foreLeg_ballRollTemple' % self.side, '%s_foreLeg_toeTabTemple' % self.side ]
        
        self.clavicleIkJointList = []
        self.IkForeLegJointList = []
        self.subIkJointList = []
        
        self.pivotList = []#[u'L_inSideRoll_PIVOT', u'L_outSideRoll_PIVOT', u'L_heelRoll_PIVOT', u'L_toeRoll_PIVOT', u'L_footTwist_PIVOT', u'L_ballRoll_PIVOT', u'L_toeTab_PIVOT']
        self.pivotNulList = []
        
    def createIkForeLegJoint(self):
        # 조인트를 만들고 리스트를 만듬
        for x in range( len(self.clavicleTempJointList) ):
            RN = self.clavicleTempJointList[x].replace( 'template', 'IK' )
            ikJoint = cmds.joint( n=RN )
            self.clavicleIkJointList.append( ikJoint )

            POsnap( ikJoint, self.clavicleTempJointList[x] )
        print self.clavicleTempJointList
        zeroRotJoint( self.clavicleIkJointList )
        cmds.select( cl=True )
        
        print '_____________________________________________________________________________________________________________________________________________________________________________'
        
        for x in range( len(self.foreLegTempJointList) ):
            RN = self.foreLegTempJointList[x].replace( 'template', 'IK' )
            ikJoint = cmds.joint( n=RN )
            self.IkForeLegJointList.append( ikJoint )
            
            POsnap( ikJoint, self.foreLegTempJointList[x] )
        zeroRotJoint( self.IkForeLegJointList )
        
        print self.clavicleIkJointList, self.IkForeLegJointList
        print '_____________________________________________________________________________________________________________________________________________________________________________'
        
    def createSubIkForeLegJoint(self):
        # separate duplicate for subIkSolver
        dList = cmds.duplicate( self.IkForeLegJointList[0], renameChildren=True )
        for x in range( len( dList ) ):
            rN = cmds.rename( dList[x], dList[x].replace( 'IK', 'rig' )[0:-1] )
            self.subIkJointList.append(rN)
        cmds.delete( self.subIkJointList[4] )
        cmds.parent( self.subIkJointList[3], self.subIkJointList[1] )
        cmds.delete( self.subIkJointList[2] )
        del self.subIkJointList[4:]
        del self.subIkJointList[-2]
        
    def createIK(self):
        # create IK
        RPs = ikHandleMaker( self.IkForeLegJointList[0], self.IkForeLegJointList[2], 'ikRPsolver' )
        self.RPsName = cmds.rename( RPs[0], self.IkForeLegJointList[0].replace( 'JNT', 'RP_HDL' ) )
        RPsEffectorName = cmds.rename( RPs[1], self.IkForeLegJointList[0].replace( 'JNT', 'RP_IKEFFECTOR' ) )
        
        SCs1 = ikHandleMaker( self.IkForeLegJointList[2], self.IkForeLegJointList[3], 'ikSCsolver' )
        self.SCs1Name = cmds.rename( SCs1[0], self.IkForeLegJointList[2].replace( 'JNT', 'SC_HDL' ) )
        SCs1EffectorName = cmds.rename( SCs1[1], self.IkForeLegJointList[2].replace( 'JNT', 'SC_IKEFFECTOR' ) )
        
        SCs2 = ikHandleMaker( self.IkForeLegJointList[3], self.IkForeLegJointList[4], 'ikSCsolver' )
        self.SCs2Name = cmds.rename( SCs2[0], self.IkForeLegJointList[3].replace( 'JNT', 'SC_HDL' ) )
        SCs2EffectorName = cmds.rename( SCs2[1], self.IkForeLegJointList[3].replace( 'JNT', 'SC_IKEFFECTOR' ) )
        
        SCs3 = ikHandleMaker( self.IkForeLegJointList[4], self.IkForeLegJointList[5], 'ikSCsolver' )
        self.SCs3Name = cmds.rename( SCs3[0], self.IkForeLegJointList[4].replace( 'JNT', 'SC_HDL' ) )
        SCs3EffectorName = cmds.rename( SCs3[1], self.IkForeLegJointList[4].replace( 'JNT', 'SC_IKEFFECTOR' ) )
        
        
        G_RP = ikHandleMaker( self.subIkJointList[0], self.subIkJointList[2], 'ikRPsolver' )
        self.G_RPName = cmds.rename( G_RP[0], self.subIkJointList[0].replace( 'JNT', 'RP_HDL' ) )
        G_RPEffectorName = cmds.rename( G_RP[1], self.subIkJointList[0].replace( 'JNT', 'RP_IKEFFECTOR' ) )
        
        
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
        
        cmds.parent( self.SCs1Name, self.G_RPName )
        cmds.parent( self.SCs2Name, self.pivotList[5] )
        cmds.parent( self.SCs3Name, self.pivotList[-1] )
        
        self.wristPivotName = cmds.group( em=True, n='L_wistRoll_PIVOT' )
        self.wristPos = cmds.xform( self.IkForeLegJointList[3], t=True, ws=True, q=True )
        cmds.move( self.wristPos[0], self.wristPos[1], self.wristPos[2], self.wristPivotName )
        cmds.parent( self.wristPivotName, self.subIkJointList[2] )
        
        cmds.parent( self.RPsName, self.wristPivotName )
        
        homeNul( self.wristPivotName )
        
        
        
        
        
    def createController(self):
        # create controller
        foreLegControllerName = controllerShape( self.IkForeLegJointList[3].replace( 'foot1_JNT', 'foreLeg_CON' ), 'cube', 'blue' )
        cmds.move( self.wristPos[0], self.wristPos[1], self.wristPos[2], foreLegControllerName )
        
        shoulderContollerName = controllerShape( self.IkForeLegJointList[0].replace( 'JNT', 'CON' ), 'rombus', 'blue' )
        shoulderPos = cmds.xform( self.IkForeLegJointList[0], t=True, ws=True, q=True )
        cmds.move( shoulderPos[0], shoulderPos[1], shoulderPos[2], shoulderContollerName )
        
        elbowPVContollerName = controllerShape( self.IkForeLegJointList[1].replace( 'JNT', 'CON' ), 'sphere', 'blue' )
        elbowPVPos = cmds.xform( self.IkForeLegJointList[1], t=True, ws=True, q=True )
        cmds.move( elbowPVPos[0], elbowPVPos[1], elbowPVPos[2], elbowPVContollerName )
        
        # controller homeNull
        homeNul( foreLegControllerName )
        shoulderContollerNul = homeNul( shoulderContollerName )
        homeNul( elbowPVContollerName )
        
        # constraints & grouping
        cmds.parent( self.pivotNulList[0], foreLegControllerName )
        
        cmds.pointConstraint( self.clavicleIkJointList[1], self.IkForeLegJointList[0] )
        cmds.pointConstraint( self.clavicleIkJointList[1], self.subIkJointList[0] )
        
        cmds.poleVectorConstraint( elbowPVContollerName, self.G_RPName )
        cmds.poleVectorConstraint( elbowPVContollerName, self.RPsName )
        
        # add attr
        cmds.addAttr( foreLegControllerName, longName='foot', at='enum', en='Controls', keyable=True )
        cmds.setAttr( '%s.foot' % foreLegControllerName, lock=True )
        
        #########################################################################################################################
        # create clavicle controller
        clavicleControllerName = controllerShape( self.clavicleIkJointList[0].replace( 'JNT', 'CON' ), 'cube', 'blue' )
        Psnap( clavicleControllerName, self.clavicleIkJointList[0] )
        clavicleControllerRotZNul = homeNul( clavicleControllerName, clavicleControllerName.replace( '_CON', 'RotZ_NUL' ) )
        clavicleControllerNul = homeNul( clavicleControllerRotZNul, clavicleControllerName.replace( '_CON', '_NUL' ) )
        
        # create clavicle
        cmds.aimConstraint( foreLegControllerName, clavicleControllerRotZNul, mo=True, worldUpType='none', skip=['x', 'y'] )
        
        cmds.setKeyframe( '%s.rz' % clavicleControllerRotZNul )
        cmds.disconnectAttr( 'pairBlend1_inRotateZ1.output', 'pairBlend1.inRotateZ1' )
        cmds.delete( 'pairBlend1_inRotateZ1' )
        
        cmds.rename( 'pairBlend1', 'L_clvicleRotZ_PBD' )
        
        # add attr autoClavicle
        cmds.addAttr( foreLegControllerName, longName='auto', at='enum', en='Shoulder', keyable=True )
        cmds.setAttr( '%s.foot' % foreLegControllerName, lock=True )
        cmds.addAttr( foreLegControllerName, longName='front', at='double', keyable=True, attributeType='float', min=0, max=1, dv=0.5 )
        
        # connection
        cmds.connectAttr( '%s.front' % foreLegControllerName, '%s.blendAim1' % clavicleControllerRotZNul )
        
        
        clavicleSc = ikHandleMaker( self.clavicleIkJointList[0], self.clavicleIkJointList[1], 'ikSCsolver' )
        clavicleScName = cmds.rename( clavicleSc[0], self.clavicleIkJointList[0].replace( 'JNT', 'SC_HDL' ) )
        clavicleScEffectorName = cmds.rename( clavicleSc[1], self.clavicleIkJointList[0].replace( 'JNT', 'SC_IKEFFECTOR' ) )
        
        cmds.pointConstraint( clavicleControllerName, self.clavicleIkJointList[0], mo=True )
        
        cmds.parent( clavicleScName, clavicleControllerName )
        
        cmds.pointConstraint( shoulderContollerName, clavicleScName, mo=True )
        
        cmds.parent( shoulderContollerNul, clavicleControllerName )
        

        # create foot controller             wristPivotName
        wristRollCONT = controllerShape( self.wristPivotName.replace( 'PIVOT', 'CON' ), 'cube', 'yellow' )
        cvNum = cmds.getAttr( '%s.spans' % wristRollCONT ) + cmds.getAttr( '%s.degree' % wristRollCONT )
        cmds.select( '%s.cv[0:%s]' % ( wristRollCONT, cvNum-1 ) )
        cmds.scale( 0.5, 0.5, 0.5 )
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
        
        #cmds.connectAttr( '%s.vis' % haindLegControllerName, '%s.visibility' % self.pivotNulList[0] )        

            
            
def quadrupedForeLegRun():
    IFL = ikForeLeg('L')
    IFL.createIkForeLegJoint()
    IFL.createSubIkForeLegJoint()
    IFL.createIK()
    IFL.createReverseFoot()
    IFL.createController()
    #IFL.cleanUpScene()
    
quadrupedForeLegRun()
