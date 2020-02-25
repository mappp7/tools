#encoding=utf-8
import maya.cmds as cmds

from util.snap import *
from util.controller import *

from util.homeNul import *
from util.attach import *

from util.fkControllerMaker import *

from util.ikHandleMaker import *
from util.curveToLocatorFix import *

from util.zeroRotJoint import *
from util.getAssetRoot import *


class ikSpine:
    def __init__(self):
        # 스파인 리스트
        self.spineTempJointList = [ 'C_template_root_JNT', 'C_template_spine1_JNT', 'C_template_spine2_JNT', 'C_template_spine3_JNT', 'C_template_spine4_JNT', 'C_template_spine5_JNT', 'C_template_spine6_JNT', 'C_template_chest_JNT' ]
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
        rootCon = fkControllerMaker( 'cross', 'yellow', [self.spineJointList[0]] )
        spine1Con = fkControllerMaker( 'cube', 'yellow', [self.spineJointList[1]] )
        chestCon = fkControllerMaker( 'cube', 'yellow', [self.spineJointList[-1]] )
        
        self.spineControllerList = rootCon[0][0], spine1Con[0][0], chestCon[0][0]
        self.spineControllerNulList = rootCon[1][0], spine1Con[1][0], chestCon[1][0]
        self.spineConstraintList = rootCon[2][0], spine1Con[2][0], chestCon[2][0]
        
        cmds.delete( self.spineConstraintList )
        """
        for each in range( len(self.spineControllerNulList)-1 ):
            cmds.delete( cmds.aimConstraint( self.spineJointList[each+1], self.spineControllerNulList[each], aimVector=[0,1,0], upVector=[0,0,-1], worldUpType='vector', worldUpVector=[0,1,0]  ) )
        cmds.delete( cmds.aimConstraint( self.spineJointList[-2], self.spineControllerNulList[-1], aimVector=[0,-1,0], upVector=[0,0,-1], worldUpType='vector', worldUpVector=[0,1,0]  ) )
        """
        self.hipCon = controllerShape( 'C_IK_hip_CON', 'cube', 'yellow' )
        #print self.spineJointList[1]
        POsnap( self.hipCon, self.spineJointList[0] )
        hipConNul = homeNul( self.hipCon )
        """
        cmds.delete( cmds.aimConstraint( self.spineJointList[2], hipConNul, aimVector=[0,1,0], upVector=[0,0,-1], worldUpType='vector', worldUpVector=[0,1,0]  ) )
        """
        #cmds.parent( hipConNul, self.spineControllerList[1] )
        
        # 'C_IK_hip_CON' pivot moving~~
        lowBodyPos = cmds.xform( spine1Con[0], ws=True, t=True, q=True )
        cmds.move( lowBodyPos[0], lowBodyPos[1], lowBodyPos[2], '%s.rotatePivot' % self.hipCon )
        cmds.move( lowBodyPos[0], lowBodyPos[1], lowBodyPos[2], '%s.rotatePivot' % hipConNul )
        
        hipConCvN = cmds.getAttr( '%s.spans' % self.hipCon )
        cmds.select( '%s.cv[0:%s]' % ( self.hipCon, hipConCvN ) )
        cmds.scale( 0.8, 0.8, 0.8, ocp=True )
        cmds.select( cl=True )
        
        # Add Sub Controller
        print self.spineControllerNulList
        self.lowBodySubCon = controllerShape( 'C_IK_lowBodySub_CON', 'cube', 'yellow' )
        self.upBodySubCon = controllerShape( 'C_IK_upBodySub_CON', 'cube', 'yellow' )
        
        
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
        
        POsnap( self.lowBodySubConNul, spine1Con[0][0] )
        POsnap( self.upBodySubConNul, chestCon[0][0] )
        
        cmds.parent( self.lowBodySubConNul, spine1Con[0][0] )
        cmds.parent( self.upBodySubConNul, chestCon[0][0] )
        
        cmds.parent( hipConNul, self.lowBodySubCon )
        
        #........................................................................................
        #print self.spineControllerList#(u'C_IK_root_CON', u'C_IK_spine1_CON', u'C_IK_chest_CON')
        self.lowBody = cmds.rename( self.spineControllerList[1], 'C_IK_lowBody_CON' )
        self.upBody = cmds.rename( self.spineControllerList[2], 'C_IK_upBody_CON' )
        
        self.lowBodyNul = cmds.rename( self.spineControllerNulList[1], 'C_IK_lowBody_NUL' )
        self.upBodyNul = cmds.rename( self.spineControllerNulList[2], 'C_IK_upBody_NUL' )
        #........................................................................................

    def createIkSpineSet(self):
        IKH = ikHandleMaker( self.spineJointList[1], self.spineJointList[-1], 'ikSplineSolver' )
        print IKH
        IKH = [u'ikHandle1', u'effector1', u'curve1']
        handleName = cmds.rename( IKH[0], 'C_IK_spine1_HDL')
        effectorName = cmds.rename( IKH[1], 'C_IK_spine1_EFFECTOR')
        curveName = cmds.rename( IKH[2], 'C_IK_spine1_CRV')
        
        cmds.rebuildCurve( curveName, s=2, d=3 )
        
        locatorName = curveToLocatorFix( curveName )
        print locatorName
        cmds.parent( curveName, w=True )
        
        for x in range(len(locatorName)):
            NUL = homeNul( locatorName[x] )
            self.locatorNulList.append(NUL)
            
        # Advanced Twist Controls Set
        upLoc = cmds.spaceLocator( n=self.upBody.replace( 'CON', 'aTwist_LOC' ) )
        POsnap( upLoc, self.spineJointList[-1] )
        cmds.parent( upLoc ,self.upBodySubCon )
        #[u'C_IK_root_JNT', u'C_IK_spine1_JNT', u'C_IK_spine2_JNT', u'C_IK_spine3_JNT', u'C_IK_chest_JNT']
        lowLoc = cmds.spaceLocator( n=self.lowBody.replace( 'CON', 'aTwist_LOC' ) )
        POsnap( lowLoc, self.spineJointList[1] )
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
        cmds.orientConstraint( self.upBodySubCon, self.spineJointList[-1], mo=True )
        

        #print self.locatorNulList[u'C_IK_spine1_NUL', u'C_IK_spine2_NUL', u'C_IK_spine3_NUL', u'C_IK_spine4_NUL']
        AP_low0 = attachPart( self.lowBodySubCon, self.locatorNulList[0], 'translate', 'rotate', 'scale', 'shear' )
        AP_low1 = attachPart( self.lowBodySubCon, self.locatorNulList[1], 'translate', 'rotate', 'scale', 'shear' )
        
        AP_up4 = attachPart( self.upBodySubCon, self.locatorNulList[3], 'translate', 'rotate', 'scale', 'shear' )
        AP_up5 = attachPart( self.upBodySubCon, self.locatorNulList[4], 'translate', 'rotate', 'scale', 'shear' )

        cmds.parentConstraint( self.hipCon, self.spineJointList[0], mo=True )
        
        #......
        AP_lowBoy = attachPart( self.spineControllerList[0], self.lowBodyNul, 'translate', 'rotate', 'scale', 'shear' )
        AP_upBoy = attachPart( self.spineControllerList[0], self.upBodyNul, 'translate', 'rotate', 'scale', 'shear' )
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
        spineMiddleCon = controllerShape( 'C_IK_spineMiddle_CON', 'hexagon', 'yellow' )
        print spineMiddleCon 
        #POsnap( spineMiddleCon, self.locatorNulList[2] )
        cmds.delete( cmds.parentConstraint( self.upBody, self.lowBody, spineMiddleCon ) )
        spineMiddleConNul = homeNul( spineMiddleCon )
        
        cmds.parentConstraint( self.upBodySubCon, self.lowBodySubCon, spineMiddleConNul, mo=True )
        attachPart( spineMiddleCon, self.locatorNulList[2], 'translate', 'rotate', 'scale', 'shear' )

def quadrupedSpineRun():
    # Run command
    IS = ikSpine()
    IS.createIkSpineJoint()
    ################################################################
    targetObject = getAssetRoot() 
    ################################################################
    #rootJointSelect = cmds.ls( sl=True )
    cmds.select( targetObject, hi=True )
    jointList = cmds.ls( sl=True, typ='joint' )
    
    zeroRotJoint( jointList )
    ################################################################
    IS.createIkSpineController()
    IS.createIkSpineSet()