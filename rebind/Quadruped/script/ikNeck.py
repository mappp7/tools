#encoding=utf-8
import maya.cmds as cmds

from baseRig.util.snap import *
from baseRig.util.controller import *

from baseRig.util.homeNul import *
from baseRig.util.attach import *

from baseRig.util.fkControllerMaker import *

from baseRig.util.ikHandleMaker import *
from baseRig.util.curveToLocatorFix import *


def zeroRotJoint( jointList ):

    for x in range( len(jointList) ):

        oX = cmds.getAttr( '%s.rotateX' % jointList[x] )
        oY = cmds.getAttr( '%s.rotateY' % jointList[x] )
        oZ = cmds.getAttr( '%s.rotateZ' % jointList[x] )

        cmds.setAttr( '%s.jointOrientX' % jointList[x], oX )
        cmds.setAttr( '%s.jointOrientY' % jointList[x], oY )
        cmds.setAttr( '%s.jointOrientZ' % jointList[x], oZ )

        cmds.setAttr( '%s.rotateX' % jointList[x], 0 )
        cmds.setAttr( '%s.rotateY' % jointList[x], 0 )
        cmds.setAttr( '%s.rotateZ' % jointList[x], 0 )


class ikNeckClass:
    def __init__(self):
        # 스파인 리스트
        self.spineTempJointList = [ 'C_template_neck1_JNT', 'C_template_neck2_JNT', 'C_template_neck3_JNT', 'C_template_neck4_JNT', 'C_template_neck5_JNT', 'C_template_neck6_JNT', 'C_template_head_JNT', 'C_template_headTip_JNT' ]
        self.spineJointList = []
        self.spineControllerList = []
        self.spineControllerNulList = []
        self.spineConstraintList = []

        self.locatorNulList = []

    def createIkSpineJoint(self):
        # 조인트를 만들고 리스트를 만듬
        if cmds.objExists( 'C_FK_root_JNT' ) != True:
            for x in range( len(self.spineTempJointList) ):
                RN = self.spineTempJointList[x].replace( 'template', 'IK' )
                spineJoint = cmds.joint( n=RN )
                self.spineJointList.append( spineJoint )

                POsnap( spineJoint, self.spineTempJointList[x] )
            print self.spineJointList
        else:
            duFkJoint = cmds.duplicate( 'C_FK_root_JNT', renameChildren=True )
            cmds.parent( duFkJoint[0], w=True )
            cmds.delete( duFkJoint[ len(duFkJoint)/2:] )
            for x in range( len(duFkJoint)/2 ):
                spineJoint = cmds.rename( duFkJoint[x], duFkJoint[x].replace( 'FK', 'IK' )[:-1] )
                self.spineJointList.append( spineJoint )

    def createIkSpineController(self):
        #rootCon = fkControllerMaker( 'cross', 'yellow', [self.spineJointList[0]] )
        neck1Con = fkControllerMaker( 'cube', 'yellow', [self.spineJointList[0]] )
        headCon = fkControllerMaker( 'cube', 'yellow', [self.spineJointList[-2]] )

        #self.spineControllerList = rootCon[0][0], neck1Con[0][0], headCon[0][0]
        self.spineControllerNulList = neck1Con[1][0], headCon[1][0]
        self.spineConstraintList = neck1Con[2][0], headCon[2][0]

        cmds.delete( self.spineConstraintList )
        """
        for each in range( len(self.spineControllerNulList)-1 ):
            cmds.delete( cmds.aimConstraint( self.spineJointList[each+1], self.spineControllerNulList[each], aimVector=[0,1,0], upVector=[0,0,-1], worldUpType='vector', worldUpVector=[0,1,0]  ) )
        cmds.delete( cmds.aimConstraint( self.spineJointList[-2], self.spineControllerNulList[-1], aimVector=[0,-1,0], upVector=[0,0,-1], worldUpType='vector', worldUpVector=[0,1,0]  ) )
        """
        #self.hipCon = controllerShape( 'C_IK_hip_CON', 'cube', 'yellow' )

        #POsnap( self.hipCon, self.spineJointList[0] )
        #hipConNul = homeNul( self.hipCon )
        """
        cmds.delete( cmds.aimConstraint( self.spineJointList[2], hipConNul, aimVector=[0,1,0], upVector=[0,0,-1], worldUpType='vector', worldUpVector=[0,1,0]  ) )
        """


        # 'C_IK_hip_CON' pivot moving~~
        """
        lowBodyPos = cmds.xform( neck1Con[0], ws=True, t=True, q=True )
        cmds.move( lowBodyPos[0], lowBodyPos[1], lowBodyPos[2], '%s.rotatePivot' % self.hipCon )
        cmds.move( lowBodyPos[0], lowBodyPos[1], lowBodyPos[2], '%s.rotatePivot' % hipConNul )

        hipConCvN = cmds.getAttr( '%s.spans' % self.hipCon )
        cmds.select( '%s.cv[0:%s]' % ( self.hipCon, hipConCvN ) )
        cmds.scale( 0.8, 0.8, 0.8, ocp=True )
        cmds.select( cl=True )
        """
        # Add Sub Controller
        print self.spineControllerNulList
        self.lowBodySubCon = controllerShape( 'C_IK_neck1Sub_CON', 'cube', 'yellow' )
        self.upBodySubCon = controllerShape( 'C_IK_headSub_CON', 'cube', 'yellow' )


        lowBodySubConCvN = cmds.getAttr( '%s.spans' % self.lowBodySubCon )
        cmds.select( '%s.cv[0:%s]' % ( self.lowBodySubCon, lowBodySubConCvN ) )
        cmds.scale( 0.8, 0.8, 0.8, ocp=True )
        cmds.select( cl=True )
        upBodySubConCvN = cmds.getAttr( '%s.spans' % self.upBodySubCon )
        cmds.select( '%s.cv[0:%s]' % ( self.upBodySubCon, upBodySubConCvN ) )
        cmds.scale( 0.8, 0.8, 0.8, ocp=True )
        cmds.select( cl=True )

        self.lowBodySubConNul = homeNul( self.lowBodySubCon )
        self.upBodySubConNul = homeNul( self.upBodySubCon )

        POsnap( self.lowBodySubConNul, neck1Con[0][0] )
        POsnap( self.upBodySubConNul, headCon[0][0] )

        cmds.parent( self.lowBodySubConNul, neck1Con[0][0] )
        cmds.parent( self.upBodySubConNul, headCon[0][0] )

        #cmds.parent( hipConNul, self.lowBodySubCon )

        #........................................................................................
        #print self.spineControllerList#(u'C_IK_root_CON', u'C_IK_spine1_CON', u'C_IK_chest_CON')
        self.lowBody = 'C_IK_neck1_CON'
        self.upBody = 'C_IK_head_CON'

        self.lowBodyNul = 'C_IK_neck1_NUL'
        self.upBodyNul = 'C_IK_head_NUL'
        #........................................................................................

    def createIkSpineSet(self):
        IKH = ikHandleMaker( self.spineJointList[0], self.spineJointList[-2], 'ikSplineSolver' )
        print IKH
        IKH = [u'ikHandle1', u'effector1', u'curve1']
        handleName = cmds.rename( IKH[0], 'C_IK_neck_HDL')
        effectorName = cmds.rename( IKH[1], 'C_IK_neck_EFFECTOR')
        curveName = cmds.rename( IKH[2], 'C_IK_neck_CRV')

        cmds.rebuildCurve( curveName, s=2, d=3 )

        locatorName = curveToLocatorFix( curveName )
        print locatorName
        #cmds.parent( curveName, w=True )

        for x in range(len(locatorName)):
            NUL = homeNul( locatorName[x] )
            self.locatorNulList.append(NUL)

        # Advanced Twist Controls Set
        upLoc = cmds.spaceLocator( n=self.upBody.replace( 'CON', 'aTwist_LOC' ) )
        cmds.delete ( cmds.parentConstraint ( self.spineJointList[-2], upLoc ) )
        cmds.parent( upLoc ,self.upBodySubCon )
        #[u'C_IK_root_JNT', u'C_IK_spine1_JNT', u'C_IK_spine2_JNT', u'C_IK_spine3_JNT', u'C_IK_chest_JNT']
        lowLoc = cmds.spaceLocator( n=self.lowBody.replace( 'CON', 'aTwist_LOC' ) )
        cmds.delete ( cmds.parentConstraint ( self.spineJointList[0], lowLoc ) )
        cmds.parent( lowLoc ,self.lowBodySubCon )

        cmds.setAttr( '%s.dTwistControlEnable' % handleName, 1 )
        cmds.setAttr( '%s.dWorldUpType' % handleName, 4 )
        cmds.setAttr( '%s.dWorldUpAxis' % handleName, 0 )

        cmds.setAttr( '%s.dWorldUpVectorX' % handleName, 0 )
        cmds.setAttr( '%s.dWorldUpVectorY' % handleName, 1 )
        cmds.setAttr( '%s.dWorldUpVectorZ' % handleName, 0 )
        cmds.setAttr( '%s.dWorldUpVectorEndX' % handleName, 0 )
        cmds.setAttr( '%s.dWorldUpVectorEndY' % handleName, 1 )
        cmds.setAttr( '%s.dWorldUpVectorEndZ' % handleName, 0 )

        cmds.connectAttr( '%s.worldMatrix' % lowLoc[0], '%s.dWorldUpMatrix' % handleName )
        cmds.connectAttr( '%s.worldMatrix' % upLoc[0], '%s.dWorldUpMatrixEnd' % handleName )

        #
        cmds.orientConstraint( self.upBodySubCon, self.spineJointList[-2], mo=True )


        #print self.locatorNulList[u'C_IK_spine1_NUL', u'C_IK_spine2_NUL', u'C_IK_spine3_NUL', u'C_IK_spine4_NUL']
        AP_low0 = attachPart( self.lowBodySubCon, self.locatorNulList[0], 'translate', 'rotate', 'scale', 'shear' )
        AP_low1 = attachPart( self.lowBodySubCon, self.locatorNulList[1], 'translate', 'rotate', 'scale', 'shear' )

        AP_up4 = attachPart( self.upBodySubCon, self.locatorNulList[3], 'translate', 'rotate', 'scale', 'shear' )
        AP_up5 = attachPart( self.upBodySubCon, self.locatorNulList[4], 'translate', 'rotate', 'scale', 'shear' )

        #cmds.parentConstraint( self.hipCon, self.spineJointList[0], mo=True )
        """
        #......
        AP_lowBoy = attachPart( self.spineControllerList[0], self.lowBodyNul, 'translate', 'rotate', 'scale', 'shear' )
        AP_upBoy = attachPart( self.spineControllerList[0], self.upBodyNul, 'translate', 'rotate', 'scale', 'shear' )
        """
        #...
        #noneScaleSpineGroup = cmds.group( handleName, curveName, self.locatorNulList[0], self.locatorNulList[1], self.locatorNulList[2], self.locatorNulList[3],
        #                                                         self.locatorNulList[4], self.locatorNulList[5], name='noneScaleSpine_GRP' )
        """
        cmds.parent( noneScaleSpineGroup, 'noneScale_GRP' )

        cmds.parent( self.spineJointList[0], 'C_IK_spineJoint_GRP' )

        cmds.parent( self.spineControllerNulList[0], 'C_move_CON' )

        cmds.parent( self.lowBodyNul, 'C_IK_spineController_GRP' )
        cmds.parent( self.upBodyNul, 'C_IK_spineController_GRP' )

        cmds.parent( AP_low0, 'C_IK_spineAttach_GRP' )
        cmds.parent( AP_low1, 'C_IK_spineAttach_GRP' )
        cmds.parent( AP_low2, 'C_IK_spineAttach_GRP' )
        cmds.parent( AP_up3, 'C_IK_spineAttach_GRP' )
        cmds.parent( AP_up4, 'C_IK_spineAttach_GRP' )
        cmds.parent( AP_up5, 'C_IK_spineAttach_GRP' )

        cmds.parent( AP_lowBoy, 'C_IK_spineAttach_GRP' )
        cmds.parent( AP_upBoy, 'C_IK_spineAttach_GRP' )
        """
        spineMiddleCon = controllerShape( 'C_IK_neckMiddle_CON', 'hexagon', 'yellow' )
        print spineMiddleCon
        #Psnap( spineMiddleCon, self.locatorNulList[2] )
        cmds.delete( cmds.parentConstraint( self.upBody, self.lowBody, spineMiddleCon ) )
        cmds.delete( cmds.orientConstraint( self.lowBody, spineMiddleCon ) )

        spineMiddleConNul = homeNul( spineMiddleCon )

        cmds.parentConstraint( self.upBodySubCon, self.lowBodySubCon, spineMiddleConNul, mo=True )
        attachPart( spineMiddleCon, self.locatorNulList[2], 'translate', 'rotate', 'scale', 'shear' )

        ##############################################################################################

        cmds.delete ( cmds.parentConstraint ( 'C_IK_head_JNT','C_FK_head_NUL' ) )
        cmds.delete ( cmds.parentConstraint ( 'C_IK_neck1_JNT','C_FK_neck1_NUL' ) )
        cmds.delete ( cmds.parentConstraint ( 'C_IK_neck3_JNT','C_FK_neck2_NUL' ) )
        cmds.delete ( cmds.parentConstraint ( 'C_IK_neck5_JNT','C_FK_neck3_NUL' ) )

    	# hierarchy of neck nul
        cmds.parent('C_FK_head_NUL', 'C_FK_neck3_NUL')
        cmds.parent('C_FK_neck3_NUL', 'C_FK_neck2_NUL')
        cmds.parent('C_FK_neck2_NUL', 'C_FK_neck1_NUL')






def ikNeckOP():
    IS = ikNeckClass()
    IS.createIkSpineJoint()

    ################################################################
    cmds.select( 'C_IK_neck1_JNT', hi=True )
    jointList = cmds.ls( sl=True, typ='joint' )
    zeroRotJoint( jointList )

    ################################################################
    IS.createIkSpineController()
    IS.createIkSpineSet()
