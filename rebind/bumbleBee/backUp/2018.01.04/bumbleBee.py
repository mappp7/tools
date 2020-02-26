#encoding=utf-8
#!/usr/bin/env python
#-------------------------------------------------------------------------------
#
#   Dexter Rigging Team
#
#       yunhyuk.jung
#
#   2017.10.23 v02_w02
#-------------------------------------------------------------------------------

import os
import maya.cmds as cmds
import maya.mel as mel 
import maya.OpenMayaUI as omui

from manual.biped.importTemplate import *
from manual.biped.mirrorTemplateJoints import *
from manual.biped.bipedRig import *
from manual.biped.extraJoint import *
from manual.biped.extraRig import *
from manual.biped.addLocalSpacetoHandSub import *
from manual.biped.poleVec_fix import*
from manual.biped.addRigCommand import *

from util.zeroOut import *
from util.controller import *
from util.undoCommand import undo
from util.path_rig import *

import json
import sys
import site
site.addsitedir('/dexter/Cache_DATA/CRT/RiggingRnD/Quadruped/script')
import tuple as TP
reload( TP )

from Qt import QtGui, QtCore, QtWidgets, load_ui
from Qt.QtGui import *
from Qt.QtCore import *
from Qt.QtWidgets import *

import xml.etree.ElementTree as xml
from cStringIO import StringIO

basePath = os.path.abspath( __file__ + '/../' )
#print basePath
uiFile   = os.path.join( basePath, 'bumbleBee.ui' )
#print uiFile


class uiMainWindow( QtWidgets.QMainWindow ):
    def __init__(self, parent=None):
        super(uiMainWindow, self).__init__(parent)
        #self.setupUi(self)
        self.ui = load_ui(uiFile)
        self.path = path_rig()
        self.connectSocket()
        self.iconColor()
        self.checkToggle()
        #self.qR = quadrupedRigClass()

# connectSocket ---------------------------------------------------------------------------------------------------
   
    def connectSocket(self):
        # biped
        self.ui.biped_temp_BTN.clicked.connect(self.importBipedTemplete)
        self.ui.biped_build_BTN.clicked.connect(self.buildBiped_cmd)
        self.ui.zeroOut_BTN.clicked.connect(self.zeroOut_cmd)
        self.ui.mirrorJoints_BTN.clicked.connect(self.mirrorJoints_cmd)
        self.ui.biped_ex_neck_BTN.clicked.connect(self.biped_ex_neck_cmd)
        self.ui.biped_ex_shoulder_BTN.clicked.connect(self.biped_ex_shoulder_cmd)
        self.ui.biped_ex_arm_BTN.clicked.connect(self.biped_ex_arm_cmd)
        self.ui.biped_ex_finger_BTN.clicked.connect(self.biped_ex_finger_cmd)
        self.ui.biped_ex_leg_BTN.clicked.connect(self.biped_ex_leg_cmd)
        self.ui.biped_ex_build_BTN.clicked.connect(self.buildExtraRig_cmd)
        # quadruped
        self.ui.quad_neck_BTN.clicked.connect(self.neckRigOP)
        self.ui.quad_temp_BTN.clicked.connect(self.importTemplateJoint)
        self.ui.quad_spine_BTN.clicked.connect(self.spineRigOP)
        self.ui.quad_forelegL_BTN.clicked.connect(self.L_foreLegOP)
        self.ui.quad_forelegR_BTN.clicked.connect(self.R_foreLegOP)
        self.ui.quad_hindlegL_BTN.clicked.connect(self.L_hindLegOP)
        self.ui.quad_hindlegR_BTN.clicked.connect(self.R_hindLegOP)
        self.ui.quad_tail_BTN.clicked.connect(self.tailOP)
        self.ui.quad_setup_BTN.clicked.connect(self.finishOP)
        self.ui.connect( self.ui.advTailNum_CMB, QtCore.SIGNAL('activated(QString)'), self.checkToggle )
        # path rig
        self.ui.createPathTempJoints_BTN.clicked.connect(self.createPathTempJoints_cmd)
        self.ui.setBodyDivJoints_BTN.clicked.connect(self.setBodyDivJoints_cmd)
        self.ui.setRig_BTN.clicked.connect(self.setRig_cmd)
        self.ui.pathCurveSet_BTN.clicked.connect(self.pathCurveSet_cmd)
        self.ui.makeLocOnCurve_BTN.clicked.connect(self.makeLocOnCurve_cmd)
        # util
        self.ui.add_Local_to_handSub_BTN.clicked.connect(self.addLocalSpacetoHandSub_cmd)
        self.ui.add_snapSet_BTN.clicked.connect(self.addSnapSet)
        self.ui.movePVnull_BTN.clicked.connect(self.fix_cmd)
 
    def checkToggle(self):
        if self.ui.advTailNum_CMB.currentText() == 'Normal':
            self.ui.advTailNum_SPB.setEnabled(False)
        else:   
            self.ui.advTailNum_SPB.setEnabled(True)
# iconColor ---------------------------------------------------------------------------------------------------
   
    def iconColor(self):
        setIconPath = '/dexter/Cache_DATA/CRT/riggingTeamShelf/bumbleBee/icon/'
        self.ui.zeroOut_BTN.setIcon(QtGui.QIcon('%szeroOut.jpg' %setIconPath))
        self.ui.mirrorJoints_BTN.setIcon(QtGui.QIcon('%smirrorJoints.jpg' %setIconPath))
        self.ui.biped_build_BTN.setIcon(QtGui.QIcon('%sbuild2.jpg' %setIconPath))
        self.ui.biped_temp_BTN.setIcon(QtGui.QIcon('%simportBipedTemp.jpg' %setIconPath))
        self.ui.biped_ex_build_BTN.setIcon(QtGui.QIcon('%sbuild3.jpg' %setIconPath))
        self.ui.biped_ex_neck_BTN.setIcon(QtGui.QIcon('%sex_neck.jpg' %setIconPath))
        self.ui.biped_ex_finger_BTN.setIcon(QtGui.QIcon('%sex_finger.jpg' %setIconPath))
        self.ui.biped_ex_leg_BTN.setIcon(QtGui.QIcon('%sex_leg.jpg' %setIconPath))
        self.ui.biped_ex_arm_BTN.setIcon(QtGui.QIcon('%sex_arm.jpg' %setIconPath))
        self.ui.biped_ex_shoulder_BTN.setIcon(QtGui.QIcon('%sex_shoulder.jpg' %setIconPath))
        self.ui.quad_temp_BTN.setIcon(QtGui.QIcon('%squad_importTemp.jpg' %setIconPath))
        self.ui.quad_neck_BTN.setIcon(QtGui.QIcon('%squad_neck.jpg' %setIconPath))
        self.ui.quad_spine_BTN.setIcon(QtGui.QIcon('%squad_spine.jpg' %setIconPath))
        self.ui.quad_forelegL_BTN.setIcon(QtGui.QIcon('%squad_foreLeg_L.jpg' %setIconPath))
        self.ui.quad_forelegR_BTN.setIcon(QtGui.QIcon('%squad_foreLeg_L.jpg' %setIconPath))
        self.ui.quad_hindlegL_BTN.setIcon(QtGui.QIcon('%squad_hindLeg_L.jpg' %setIconPath))
        self.ui.quad_hindlegR_BTN.setIcon(QtGui.QIcon('%squad_hindLeg_L.jpg' %setIconPath))
        self.ui.quad_tail_BTN.setIcon(QtGui.QIcon('%squad_tail.jpg' %setIconPath))
        self.ui.quad_setup_BTN.setIcon(QtGui.QIcon('%squad_setup.jpg' %setIconPath))
        self.ui.interacteFoot_BTN.setIcon(QtGui.QIcon('%sinteracteFoot.jpg' %setIconPath))
        self.ui.createPathTempJoints_BTN.setIcon(QtGui.QIcon('%screatePathTempJoints.jpg' %setIconPath))
        self.ui.setBodyDivJoints_BTN.setIcon(QtGui.QIcon('%ssetBodyDivJoints.jpg' %setIconPath))
        self.ui.setRig_BTN.setIcon(QtGui.QIcon('%ssetRig.jpg' %setIconPath))
        self.ui.pathCurveSet_BTN.setIcon(QtGui.QIcon('%spathCurveSet.jpg' %setIconPath))
        self.ui.makeLocOnCurve_BTN.setIcon(QtGui.QIcon('%smakeLocOnCurve.jpg' %setIconPath))
    
# biped ---------------------------------------------------------------------------------------------------
    
    @undo
    def importBipedTemplete(self): 
        i = importTemplate()
        i.simpleBiped()
        self.setTailJointsCmd()

    @undo
    def buildBiped_cmd(self):  # biped
        b=bipedRig()
        b.build()
        self.addLocalSpacetoHandSub_cmd()
        self.fix_cmd()
        self.addSnapSet()
    
    @undo
    def addSnapSet(self):
        addRigCommand()
    
    @undo
    def zeroOut_cmd(self):
        z = zeroOut()
        hireSel = []
        sel = cmds.ls(sl=True)
        for i in sel:
            #del hireSel[0:len(hireSel)]
            cmds.select("%s" %i, hierarchy=True, add=True )
            ee = cmds.ls(sl=1)
            for j in ee:
              z.zeroOutJoint(j)
    @undo
    def mirrorJoints_cmd(self):  # biped
        m=mirrorTemplateJoints()
        hireSel = []
        sel = cmds.ls(sl=True)
        for i in sel:
            del hireSel[0:len(hireSel)]
            cmds.select("%s" %i, hierarchy=True, add=True )
            ee = cmds.ls(sl=1)
            hireSel.append(ee)
        for e in hireSel[0]:
            cmds.refresh()
            m.similarPose(e)

    def buildExtraRig_cmd(self):  # biped
        er=extraRig()
        er.attachWindow()
    def biped_ex_neck_cmd(self):  # biped
        ex=extraJoint()
        ex.neck()
    def biped_ex_shoulder_cmd(self):  # biped
        ex=extraJoint()
        ex.shoulder()
    def biped_ex_arm_cmd(self):  # biped
        ex=extraJoint()
        ex.arm()
    def biped_ex_finger_cmd(self):  # biped
        ex=extraJoint()
        ex.finger()
    def biped_ex_leg_cmd(self):  # biped
        ex=extraJoint()
        ex.leg()
    @undo
    def controlerScale(self, controlerList, scaleValue ):
        for x in controlerList:
            controlerShapeName = cmds.listRelatives ( x, s=True )[0]
            CRV_span_num = cmds. getAttr ( controlerShapeName+'.spans' )    
            cmds.select ( x+'.cv[0:%s]' %(CRV_span_num)) 
            cmds.scale ( scale_value, scale_value, scale_value, r=1 )
        cmds.select ( cl=1 )
    @undo
    def controlerRotate(self, controlerList, x, y, z ):        
        for i in controlerList:
            controlerShapeName = cmds.listRelatives ( i, s=True )[0]
            CRV_span_num = cmds. getAttr ( controlerShapeName+'.spans' ) 
            cmds.select ( '%s.cv[0:%s]' % (i, CRV_span_num), r=1 )
            cmds.rotate ( x, y, z, os=1, ocp=1, r=1 )
            cmds.select ( cl=1 )




# quadruped ---------------------------------------------------------------------------------------------------

    def createHindLegTempJoint(self, side):
        jointNamelist = [ '%s_template_hip_JNT' %side, '%s_template_knee_JNT' %side, '%s_template_ankle_JNT' %side, '%s_template_ball_JNT' %side, '%s_template_toe_JNT' %side, '%s_template_toeTip_JNT' %side ]
        templateJoint = []
        for x in range( len(jointNamelist) ):
            eachJoint = cmds.joint ( jointNamelist[x], n=jointNamelist[x].replace( 'template', 'IK' ) )
            templateJoint.append(eachJoint)
        for x in range( len(templateJoint)-1 ):
            cmds.parent( templateJoint[x+1], templateJoint[x] )
        cmds.parent( templateJoint[0], w=True )
        cmds.select( cl=True )

    def importTemplateJoint( self, *args ):
        cmds.file( '/dexter/Cache_DATA/CRT/RiggingRnD/Quadruped/script/template.mb', i=True, type='mayaBinary', mergeNamespacesOnClash=False, rpr='clash', options='v=0', pr=True )
        self.tailJointNum = int(self.ui.tailNum_SPB.text())
        root_joint = cmds.joint ( p=( 0, 0, 0 ), n='C_template_tail1_JNT' )
        cmds.parent ( root_joint, 'templateJoint_GRP' )
        for x in range(int(self.tailJointNum)-1):
            cJoint = cmds.joint ( p=(0, 0, 0), n='C_template_tail%s_JNT' %(x+2) )
            pJoint = cmds.listRelatives ( p=1 )
            cmds.joint ( pJoint, e=1, zso=1, oj='xyz', sao='yup')
            cmds.select ( cJoint )
        cmds.select ( 'C_template_tail1_JNT', hi=1 )
        tailJointList = cmds.ls ( sl=1 )
        for x in tailJointList:
            cmds.setAttr ( x+'.tx', 2 )
        cmds.setAttr ( 'C_template_tail1_JNT.jointOrientY', 90 )
        cmds.setAttr ( 'C_template_tail1_JNT.tx', 0 )
        cmds.setAttr ( 'C_template_tail1_JNT.ty', 15 )
        cmds.setAttr ( 'C_template_tail1_JNT.tz', -11 )
        cmds.select ( cl=1 )

    def setTailJointsCmd(self,*args):
        #  advTail_CKB
        #self.tailConNum = int(self.ui.tailNum_SPB.text())
        tailJointNum = int(self.ui.tailNum_SPB.text())
        root_joint = cmds.joint ( p=( 0, 0, 0 ), n='C_template_tail1_JNT' )
        cmds.parent ( root_joint, 'templateJoint_GRP' )
        for x in range(int(tailJointNum)-1):
            cJoint = cmds.joint ( p=(0, 0, 0), n='C_template_tail%s_JNT' %(x+2) )
            pJoint = cmds.listRelatives ( p=1 )
            cmds.joint ( pJoint, e=1, zso=1, oj='xyz', sao='yup')
            cmds.select ( cJoint )
        cmds.select ( 'C_template_tail1_JNT', hi=1 )
        tailJointList = cmds.ls ( sl=1 )
        for x in tailJointList:
            cmds.setAttr ( x+'.tx', 2 )
        cmds.setAttr ( 'C_template_tail1_JNT.jointOrientY', 90 )
        cmds.setAttr ( 'C_template_tail1_JNT.tx', 0 )
        cmds.setAttr ( 'C_template_tail1_JNT.ty', 15 )
        cmds.setAttr ( 'C_template_tail1_JNT.tz', -11 )
        cmds.select ( cl=1 )

    def setAdvancedTailSysCmd(self,*args):
        import advance_tail
        reload( advance_tail )
        IS = advance_tail.tailRigClass()
        #sel_type = cmds.optionMenu ( 'bind_joint_type', q=1, v=1 )
        self.tailConNum = int(self.ui.tailNum_SPB.text())

    def neckRigOP( self, *args ):
        import ikNeck
        ikNeck.ikNeckOP()
        import fkAddNeck
        fkAddNeck.fkAddNeckOP()
        import add_SS_neck
        add_SS_neck.add_SS_neckOP()
        import advance_neck
        advance_neck.neckAdvanveOP()
      
    def spineRigOP( self, *args ):
        import ikSpine
        ikSpine.ikSpineOP()    
        import fkAddSpine
        fkAddSpine.fkAddSpineOP()
        import add_SS_spine
        add_SS_spine.add_SS_spineOP()

    def L_foreLegOP( self, *args ):
        import L_foreLeg    
        L_foreLeg.ForeLegOP()

    def R_foreLegOP( self, *args ):
        import R_foreLeg 
        R_foreLeg.ForeLegOP() 
    
    def L_hindLegOP( self, *args ):
        self.createHindLegTempJoint('L')
        import L_ikHindLeg
        L_ikHindLeg.L_ikHindLegOP()
        import pivotToController
        pivotToController.pivotToControllerOP('L')  

    def R_hindLegOP( self, *args ):
        self.createHindLegTempJoint('R')
        import R_ikHindLeg
        R_ikHindLeg.R_ikHindLegOP()
        import pivotToController
        pivotToController.pivotToControllerOP('R')

    def tailOP( self, *args ):
        import advance_tail
        reload( advance_tail )
        type = self.ui.advTailNum_CMB.currentText() 
        jointNum = self.ui.advTailNum_SPB.text() 
        advance_tail.tailOP(type,int(jointNum))
        #self.setAdvancedTailSysCmd()

    def finishOP( self, *args ):
        self.etc_set()
        self.create_skin_joint()

    def create_skin_joint( self ):
        tempJoint_rootList = [ 'R_template_clavicle_JNT','C_template_root_JNT','C_template_neck1_JNT','L_template_clavicle_JNT','L_template_hip_JNT','R_template_hip_JNT', 'C_template_tail1_JNT' ]
        if self.ui.advTailNum_CMB.currentText() is not 'Normal':
            del tempJoint_rootList[-1]
        for x in tempJoint_rootList:    
            IKJoint = x.replace( 'template', 'IK' )
            cmds.select ( IKJoint, hi=1 )
            IKJointList = cmds.ls ( sl=1 )
            DJointList = cmds.duplicate( x, renameChildren=1 )
            for y in range(len(DJointList)):
                skinJoint = cmds.rename ( DJointList[y], DJointList[y].replace('template', 'Skin')[0:-1] )
                cmds.parentConstraint ( IKJointList[y], skinJoint )
        cmds.parent('C_Skin_neck1_JNT', 'C_Skin_chest_JNT')
        cmds.parent('L_Skin_clavicle_JNT', 'C_Skin_chest_JNT')
        cmds.parent('R_Skin_clavicle_JNT', 'C_Skin_chest_JNT')
        cmds.parent('L_Skin_hip_JNT', 'C_Skin_root_JNT')
        cmds.parent('R_Skin_hip_JNT', 'C_Skin_root_JNT')
        cmds.parent('C_Skin_root_JNT', 'SkinJoint_GRP')
        if self.ui.advTailNum_CMB.currentText() is 'Normal':
            cmds.parent( 'C_Skin_tail1_JNT', 'C_Skin_root_JNT' )
        else:
            cmds.parent('Skin_tail1_JNT','C_Skin_root_JNT')

    def etc_set( self ):        
        ### attribute
        # sup con vis
        for x in range(8):
            cmds.addAttr ( TP.AA['PL'][x], ln='sub_con_vis', at='enum', en='off:on:' )
            cmds.setAttr ( TP.AA['PL'][x]+'.sub_con_vis', e=1, keyable=1 )
            cmds.connectAttr ( TP.AA['PL'][x]+'.sub_con_vis', TP.AA['CL'][x]+'.visibility' )
        # FK / IK switch
        for x in range(2):
            switchCon = controllerShape( TP.conVis['key'][x][0]+'_CON', 'cross', 'yellow' )
            switchNul = cmds.group ( switchCon, n=TP.conVis['key'][x][0]+'_NUL' )
            cmds.delete ( cmds.pointConstraint ( TP.conVis['key'][x][1], switchNul ) )
            cmds.parent( switchNul, TP.conVis['key'][x][1] )
            cmds.move( 5, 0, 0, ws=1, r=1 )
            cmds.addAttr ( switchCon, ln=TP.conVis['attr'][0], at='enum', en='off:on:' )
            cmds.setAttr ( switchCon+'.'+TP.conVis['attr'][0], e=1, keyable=1 )
            cmds.addAttr ( switchCon, ln=TP.conVis['attr'][1], at='enum', en='off:on:' )
            cmds.setAttr ( switchCon+'.'+TP.conVis['attr'][1], e=1, keyable=1 )
        for x in range(2):
            top_list = TP.conVis['vis'][x]
            for y in top_list:
                for z in y:
                    if len(y)==1:
                        cmds.connectAttr( TP.conVis['key'][x][0]+'_CON.'+TP.conVis['attr'][0], z+'.visibility' )
                    else:
                        cmds.connectAttr( TP.conVis['key'][x][0]+'_CON.'+TP.conVis['attr'][1], z+'.visibility' )
                    cmds.setAttr ( TP.conVis['key'][x][0]+'_CON.IK_con_vis', 1 )
        ### Parent node
        cmds.group ( p='noneTransform_GRP', em=1, n='locator_GRP' )
        cmds.parent ( TP.noneTrans_list, 'locator_GRP' )
        cmds.parent ( TP.attach_list, 'attach_GRP' )
        cmds.parent ( TP.auxillary_list, 'auxillary_GRP' )
        cmds.parent ( TP.neck_list, 'C_neck_GRP' )
        cmds.parent ( TP.spine_list, 'C_spine_GRP' )
        cmds.parent ( TP.L_foreLeg_list, 'L_foreLeg_GRP' )
        cmds.parent ( TP.R_foreLeg_list, 'R_foreLeg_GRP' )
        cmds.parent ( TP.L_hindLeg_list, 'L_hindLeg_GRP' )
        cmds.parent ( TP.R_hindLeg_list, 'R_hindLeg_GRP' )
        cmds.delete ( TP.delete_list )
        cmds.select ( TP.noneTrans_list, r=1)
        cmds.select ( 'templateJoint_GRP' , tgl=1)
        cmds.select ( TP.hide_list , tgl=1)
        cmds.HideSelectedObjects ()
        if self.ui.advTailNum_CMB.currentText() == 'Normal':
            cmds.parent ( TP.tail_list, 'C_tail_GRP' )
            cmds.select ( TP.hide_list2 , r=1 )
            cmds.select ( 'tail_aim_vector_LOC',tgl=1 )
            cmds.HideSelectedObjects ()
        else:
            cmds.parent ( 'Skin_tail1_JNT', 'SkinJoint_GRP' )
            cmds.parent ( 'tail1_NUL', 'FKControl_GRP')
            cmds.parent ( 'tail_curve_locator_GRP', 'attach_GRP')
            cmds.select ( TP.hide_list2[0:-2] , r=1)
            cmds.HideSelectedObjects ()

        ### Rotate controler
        self.controlerRotate( TP.rotate_con_list_A, 0, 0, -90 )
        self.controlerRotate( TP.rotate_con_list_B, -90, 0, 0 )
        
        ### controler Color
        for x in TP.R_con_list:
            conShapeName = cmds.listRelatives ( x, s=1 )[0]
            cmds.setAttr ( conShapeName+'.overrideEnabled', 1 )
            cmds.setAttr ( conShapeName+'.overrideColor', 13 )
        for x in TP.switch_con_list:
            conShapeName = cmds.listRelatives ( x, s=1 )[0]
            cmds.setAttr ( conShapeName+'.overrideEnabled', 1 )
            cmds.setAttr ( conShapeName+'.overrideColor', 14 )

        ### controler Scale
        for x in TP.scale_con_list:
            scale_value = 2
            CRV_shape_name = cmds.listRelatives (x, s=1)[0]
            CRV_span_num = cmds. getAttr ( CRV_shape_name+'.spans' )    
            cmds.select ( x+'.cv[0:%s]' %(CRV_span_num)) 
            cmds.scale ( scale_value, scale_value, scale_value, r=1 )

        ### controler Parent 
        if self.ui.advTailNum_CMB.currentText() == 'Normal':
            for x in range(2):
                PL = TP.parent_list['PL'][x]
                for y in TP.parent_list['CL'][x]:
                    print y
                    cmds.parentConstraint ( PL, y, mo=1 )
        else:
            del TP.parent_list['CL'][0][3]
            for x in range(2):
                PL = TP.parent_list['PL'][x]
                for y in TP.parent_list['CL'][x]:
                    print y
                    cmds.parentConstraint ( PL, y, mo=1 )
        ### hindLeg Parent 
        cmds.setAttr ( 'L_rig_hip_JNT.inheritsTransform', 0 )
        cmds.setAttr ( 'R_rig_hip_JNT.inheritsTransform', 0 )
        itemList = [ '.sx', '.sy', '.sz' ]
        for x in TP.targetjointList:
            for y in itemList:
                cmds.connectAttr ( 'place_CON.globalScale', x+y )

# util ---------------------------------------------------------------------------------------------------    

    @undo
    def addLocalSpacetoHandSub_cmd(self):  # biped
        addLocalSpacetoHandSub('L')
        addLocalSpacetoHandSub('R')
    @undo
    def fix_cmd(self):  # biped
        cp_cmd('L')
        cp_cmd('R')
    @undo
    def createPathTempJoints_cmd(self):
        self.path.createPathTempJoints()
    @undo
    def setBodyDivJoints_cmd(self):
        num = int(self.ui.setBodyDivJoints_SPB.text())
        self.path.setBodyDivJoints(num)  # insert default div joints num 
    @undo
    def setRig_cmd(self):
        num = int(self.ui.setRig_SPB.text())
        self.path.setRig(num) # insert skin Div 
    @undo
    def pathCurveSet_cmd(self):
        num = int(self.ui.pathCurveSet_SPB.text())
        self.path.pathCurveSet(30) # path set  - insert add curve length
    @undo
    def makeLocOnCurve_cmd(self):
        self.path.makeLocOnCurve() 

    def fitToRig_cmd(self):  # biped
        self.importCON_JSON()

    def importCON_JSON(self):
        # self.mayaFolder2 = cmds.fileDialog2(fm=3, caption = "Set")[0]
        # filePath = self.mayaFolder + self.JsonName +'.json'
        basicFilter = "*.json"
        filePath = cmds.fileDialog2(ff=basicFilter, dialogStyle=1,fm=1,rf=True)
        # load
        F = open( str(filePath[0]) )
        self.loadedData = json.load( F )
        F.close() 

        jsonKeys = self.loadedData.keys()

        for i in jsonKeys:
            print i
            transformList = self.loadedData[i].keys()
            transformList = transformList.replace('_temp_LOC','_JNT' )
            for j in transformList:
                print j
                trasformAttr = self.loadedData[i][j]
                for k in range(len(trasformAttr)):
                    print trasformAttr
                    cmds.setAttr('%s.%sX' %(i,j) , '%s' %trasformAttr[k])


#---------------------------------------------------------------------------------------------------------------------

def OPEN():
    global Window
    try:
        Window.close()
        Window.deleteLater()
    except: pass
    Window = uiMainWindow()
    Window.ui.show()

    
