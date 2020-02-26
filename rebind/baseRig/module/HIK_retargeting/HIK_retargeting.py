#encoding=utf-8
#!/usr/bin/env python
#-------------------------------------------------------------------------------
#
#   Dexter Rigging Team
#
#   yunhyuk.jung ( m114m1a1@gmail.com )
#
#   2016.09.03.v02.w01
#-------------------------------------------------------------------------------

import os

from PySide import QtCore, QtGui

from shiboken import wrapInstance

import maya.cmds as cmds
import maya.OpenMayaUI as omui
import maya.mel as mel
import maya.OpenMaya as om
import subprocess
from functools import partial


import xml.etree.ElementTree as xml
import pysideuic
from cStringIO import StringIO

basePath = os.path.abspath( __file__ + '/../' )
print basePath
uiFile   = os.path.join( basePath, 'HIK_retargeting.ui' )
print uiFile

def maya_main_window():
    main_window_ptr = omui.MQtUtil.mainWindow()
    return wrapInstance(long(main_window_ptr), QtGui.QWidget)

def loadUiType(uiFile):
    parsed = xml.parse(uiFile)
    widget_class = parsed.find('widget').get('class')
    form_class = parsed.find('class').text

    with open(uiFile, 'r') as f:
        o = StringIO()
        frame = {}

        pysideuic.compileUi(f, o, indent=0)
        pyc = compile(o.getvalue(), '<string>', 'exec')
        exec pyc in frame

        #Fetch the base_class and form class based on their type in the xml from designer
        form_class = frame['Ui_%s'%form_class]
        base_class = eval('QtGui.%s'%widget_class)
    return form_class, base_class

form_class, base_class = loadUiType(uiFile)

class uiMainWindow( form_class, base_class ):
    def __init__(self, parent=maya_main_window()):
        super(uiMainWindow, self).__init__(parent)
        self.setupUi(self)

        mel.eval('HIKCharacterControlsTool;')
        # attatch List 
        self.moduleJoint_list = ['C_Skin_hip_JNT','C_Skin_spine1_JNT','C_Skin_spine2_JNT','C_Skin_spine3_JNT','C_Skin_chest_JNT','C_Skin_neck_JNT','C_Skin_head_JNT','L_Skin_shoulder_JNT','L_Skin_upArm_JNT','L_Skin_foreArm_JNT','L_Skin_hand_JNT','L_Skin_middle1_JNT','R_Skin_shoulder_JNT','R_Skin_upArm_JNT','R_Skin_foreArm_JNT','R_Skin_hand_JNT','R_Skin_middle1_JNT','L_Skin_leg_JNT','L_Skin_lowLeg_JNT','L_Skin_foot_JNT','L_Skin_ball_JNT','R_Skin_leg_JNT','R_Skin_lowLeg_JNT','R_Skin_foot_JNT','R_Skin_ball_JNT']
        self.HIKJoint_list = ['Hips','Spine','Spine1','Spine2','Spine3','Neck','Head','LeftShoulder','LeftArm','LeftForeArm','LeftHand','LeftFingerBase','RightShoulder','RightArm','RightForeArm','RightHand','RightFingerBase','LeftUpLeg','LeftLeg','LeftFoot','LeftToeBase','RightUpLeg','RightLeg','RightFoot','RightToeBase']
        self.FKController_list = ['root_CON','C_IK_lowBody_CON','C_IK_upBodyRot1_CON','C_IK_upBodyRot2_CON','C_IK_upBody_CON','C_IK_neck_CON','C_IK_head_CON','L_FK_shoulder_CON','L_FK_upArm_CON','L_FK_foreArm_CON','L_FK_hand_CON','R_FK_shoulder_CON','R_FK_upArm_CON','R_FK_foreArm_CON','R_FK_hand_CON','L_FK_leg_CON','L_FK_lowLeg_CON','L_FK_foot_CON','R_FK_leg_CON','R_FK_lowLeg_CON','R_FK_foot_CON']
        self.HIK_attatch_toFK_list = ['Hips','Spine','Spine1','Spine2','Spine3','Neck','Head','LeftShoulder','LeftArm','LeftForeArm','LeftHand','RightShoulder','RightArm','RightForeArm','RightHand','LeftUpLeg','LeftLeg','LeftFoot','RightUpLeg','RightLeg','RightFoot']
        self.IKController_list = ['root_CON','C_IK_lowBody_CON','C_IK_upBodyRot1_CON','C_IK_upBodyRot2_CON','C_IK_upBody_CON','C_IK_neck_CON','C_IK_head_CON','L_FK_shoulder_CON','L_IK_hand_CON','R_FK_shoulder_CON','R_IK_hand_CON','L_IK_foot_CON','R_IK_foot_CON','L_IK_handVec_CON','R_IK_handVec_CON','L_IK_footVec_CON','R_IK_footVec_CON']
        self.HIK_attatch_toIK_list = ['Hips','Spine','Spine1','Spine2','Spine3','Neck','Head','LeftShoulder','LeftHand','RightShoulder','RightHand','LeftFoot','RightFoot']
        self.IKPOV_list = [['LeftUpLeg','LeftLeg','LeftFoot','L_IK_footVec_CON'],['RightUpLeg','RightLeg','RightFoot','R_IK_footVec_CON'],['LeftArm','LeftForeArm','LeftHand','L_IK_handVec_CON'],['RightArm','RightForeArm','RightHand','R_IK_handVec_CON']]
        self.delConstraints = []
        self.connectionSlot()
        self.checkToggled()
        self.checkToggled_timeSlider()
        self.getSourceHIK_list = []
        self.getTargetHIK_list = []
        self.targetNS = []
   
    def connectionSlot(self):

        self.targetChar_RDB.clicked.connect(self.checkToggled)
        self.sourceChar_RDB.clicked.connect(self.checkToggled)
        self.mocap_RDB.clicked.connect(self.checkToggled)
        self.rig_RDB.clicked.connect(self.checkToggled)
        self.timeSlider_RDB.clicked.connect(self.checkToggled_timeSlider)
        self.startEnd_RDB.clicked.connect(self.checkToggled_timeSlider)
        self.reloadHIK_BTN.clicked.connect(self.reloadHIKtoList)
        self.importHIK_BTN.clicked.connect(self.importHIK)
        self.selSource_BTN.clicked.connect(self.getSourceHIK)
        self.selTarget_BTN.clicked.connect(self.getTargetHIK)
        self.run_BTN.clicked.connect(self.runRetargeting)
        self.animBrowser_BTN.clicked.connect(self.openAnimBrowser)
        self.smartBake_BTN.clicked.connect(self.doSmartBake)

        self.connect( self.mirrorAnim_CMB, QtCore.SIGNAL('activated(QString)'), self.mirrorAnim )

    def getNamespace(self): # get character nameSpace
        if len(cmds.ls(sl=1)) == 1:
            sel = cmds.ls(sl=True)[0]
            self.nsChar = sel.rsplit(':')[0]
        else:
            cmds.warning('"select Character!!"')  

    def openAnimBrowser(self):
        fileFolderPath = '/tactic/library/ani/MotionCapture/'
        subprocess.Popen( ['xdg-open', fileFolderPath] )
        
    def checkToggled(self):
        if self.targetChar_RDB.isChecked() == True:
            self.FK_RDB.setEnabled(True)
            self.IK_RDB.setEnabled(True)
            self.mocap_RDB.setEnabled(False)
            self.rig_RDB.setEnabled(False)
        else:   
            self.FK_RDB.setEnabled(False)
            self.IK_RDB.setEnabled(False)
            self.mocap_RDB.setEnabled(True)
            self.rig_RDB.setEnabled(True)
        if self.mocap_RDB.isChecked() == True:
            self.animBrowser_BTN.setEnabled(True)
            self.smartBake_BTN.setEnabled(False)
            self.smartBake_LAB.setEnabled(False)
        else:
            self.animBrowser_BTN.setEnabled(False)
            self.smartBake_BTN.setEnabled(True)
            self.smartBake_LAB.setEnabled(True)

    def checkToggled_timeSlider(self):
        if self.timeSlider_RDB.isChecked() == True:
            self.start_LIN.setEnabled(False)
            self.end_LIN.setEnabled(False)
            self.timeSlider_LAB.setEnabled(True)
        else:
            self.start_LIN.setEnabled(True)
            self.end_LIN.setEnabled(True)
            self.timeSlider_LAB.setEnabled(False)

    def HIKtoFK(self):  # HIK constraint FK_CON
        for i in range(len(self.FKController_list)):
            self.toFK_Const = cmds.parentConstraint( "%s:%s" %(self.nsChar,self.HIK_attatch_toFK_list[i]) ,"%s:%s" %(self.nsChar,self.FKController_list[i]), mo = 1 , w = 1 )
            self.delConstraints.append(self.toFK_Const[0])
            cmds.setAttr('%s:R_armBlend_CON.FKIKBlend' %self.nsChar , 0)
            cmds.setAttr('%s:L_armBlend_CON.FKIKBlend' %self.nsChar , 0)
            cmds.setAttr('%s:R_legBlend_CON.FKIKBlend' %self.nsChar , 0)
            cmds.setAttr('%s:L_legBlend_CON.FKIKBlend' %self.nsChar , 0)  

    def HIKtoIK(self): # HIK constraint IK_CON
        for i in range(len(self.IKController_list)):
            self.toIK_Const = cmds.parentConstraint( "%s:%s" %(self.nsChar,self.HIK_attatch_toIK_list[i]) ,"%s:%s" %(self.nsChar,self.IKController_list[i]), mo = 1 , w = 1 )
            self.delConstraints.append(self.toIK_Const[0])
            cmds.setAttr('%s:R_armBlend_CON.FKIKBlend' %self.nsChar , 1)
            cmds.setAttr('%s:L_armBlend_CON.FKIKBlend' %self.nsChar , 1)
            cmds.setAttr('%s:R_legBlend_CON.FKIKBlend' %self.nsChar , 1)
            cmds.setAttr('%s:L_legBlend_CON.FKIKBlend' %self.nsChar , 1)  

    def SkintoHIK(self): # constraint Source Char
        for i in range(len(self.HIKJoint_list)):
            self.toSkin_Const = cmds.parentConstraint( "%s:%s" %(self.nsChar,self.moduleJoint_list[i]) ,"%s:%s" %(self.nsChar,self.HIKJoint_list[i]), mo = 1 , w = 1 )
            self.delConstraints.append(self.toSkin_Const[0])  

    def importHIK(self):
        if self.rig_RDB.isChecked() == True:
            self.getNamespace()
            cmds.file('/dexter/Cache_DATA/CRT/RiggingRnD/baseRig/templates/HIKJoint/HIKJoint.ma' , i = True , type = 'mayaAscii' , ra = True , mergeNamespacesOnClash = True , namespace = self.nsChar , options = 'v=0')
            
            HIKJoint_constraint_list = []
            for i in range(len(self.HIKJoint_list)):
                temp_point_con = cmds.pointConstraint( "%s:%s" %(self.nsChar,self.moduleJoint_list[i]) ,"%s:%s" %(self.nsChar,self.HIKJoint_list[i]), mo = 0 , w = 1 )
                HIKJoint_constraint_list.append(temp_point_con[0])
            cmds.delete(HIKJoint_constraint_list)

            if self.targetChar_RDB.isChecked() == True:
                self.targetNS.append(self.nsChar)
                if self.IK_RDB.isChecked() == True:
                    self.HIKtoIK()
                else:
                    self.HIKtoFK()
            else:
                self.SkintoHIK()    
        else:
            cmds.file('/dexter/Cache_DATA/CRT/RiggingRnD/baseRig/templates/HIKJoint/humanType01_humanIK.ma' , i = True , type = 'mayaAscii' , ra = True ,options = 'v=0')

    def reloadHIKtoList(self):   #, QtGui.QListWidget):
        self.HIK_list = cmds.ls(type = 'HIKCharacterNode')
        self.HIK_list_WGT.clear()
        self.HIK_list_WGT.addItems(self.HIK_list)

    def getSourceHIK(self):
        gSHIK = str(self.HIK_list_WGT.currentItem().text())
        if len( self.getSourceHIK_list ) == 0:
            self.getSourceHIK_list.append(gSHIK)
        else:
            del self.getSourceHIK_list[0:len(self.getSourceHIK_list)]
            self.getSourceHIK_list.append(gSHIK)
        if self.rig_RDB.isChecked() == True:
            mel.eval('$gHIKCurrentCharacter  = "%s"' %self.getSourceHIK_list[0])
            mel.eval('hikToggleLockDefinition();')
        SCHIK = self.getSourceHIK_list
        TGHIK = self.getTargetHIK_list
        mel.eval('refreshAllCharacterLists();')
        mel.eval('mayaHIKsetCharacterInput("%s","%s");' %(TGHIK[0],SCHIK[0]))

        if self.IK_RDB.isChecked() == True:
            self.IKPOVBake()

    def getTargetHIK(self):
        gTHIK = str(self.HIK_list_WGT.currentItem().text())
        if len( self.getTargetHIK_list ) == 0:
            self.getTargetHIK_list.append(gTHIK)
        else:
            del self.getTargetHIK_list[0:len(self.getTargetHIK_list)]
            self.getTargetHIK_list.append(gTHIK)
        mel.eval('$gHIKCurrentCharacter  = "%s"' %self.getTargetHIK_list[0])
        mel.eval('hikToggleLockDefinition();')

    def IKPOVBake(self):
 
        nsChar = self.targetNS
        POV_set_List = ['LeftLeg' , 'RightLeg' , 'LeftArm' , 'RightArm' ]
        decomposedMatrix_list = []
        plusMinusAverage_list = []
        multiplyDivide_list = []

        # joint part : 4
        for i in range(len(POV_set_List)):
            del decomposedMatrix_list[0:len(decomposedMatrix_list)]
            del plusMinusAverage_list[0:len(plusMinusAverage_list)]
            del multiplyDivide_list[0:len(multiplyDivide_list)]
            # decomposed_Node : 4
            for x in range(len(self.IKPOV_list)):
                decomposed_node = cmds.createNode('decomposeMatrix',n ='%s:%s_%s_DCM' %(nsChar[0],POV_set_List[i],x+1)  ) 
                decomposedMatrix_list.append(decomposed_node)
                self.delConstraints.append(decomposed_node)
            # plusMinusAverage_Node : 6
            for y in range(len(self.IKPOV_list)+2):
                plusMinusAverage_node = cmds.createNode('plusMinusAverage',n ='%s:%s_%s_PMA' %(nsChar[0],POV_set_List[i],y+1)  ) 
                if y <= 3:
                    cmds.setAttr('%s.operation' %plusMinusAverage_node , 2 )
                plusMinusAverage_list.append(plusMinusAverage_node)
                self.delConstraints.append(plusMinusAverage_node)
            # multiplyDivide_Node : 2
            for z in range(len(self.IKPOV_list)-2):
                multiplyDivide_node = cmds.createNode('multiplyDivide',n ='%s:%s_%s_MPD' %(nsChar[0],POV_set_List[i],z+1)  ) 
                cmds.setAttr('%s.input2X' %multiplyDivide_node , 2)
                cmds.setAttr('%s.input2Y' %multiplyDivide_node , 2)
                cmds.setAttr('%s.input2Z' %multiplyDivide_node , 2)
                if z <= 0:
                    cmds.setAttr('%s.operation' %multiplyDivide_node , 2 )
                multiplyDivide_list.append(multiplyDivide_node)
                self.delConstraints.append(multiplyDivide_node)
            # composeMatrix : 1
            composeMatrix_node = cmds.createNode('composeMatrix',n ='%s:%s_%s_CPM' %(nsChar[0],POV_set_List[i],i+1)) 
            self.delConstraints.append(composeMatrix_node)
            # multiMatrix : 1
            multMatrix_node = cmds.createNode('multMatrix',n ='%s:%s_%s_MMX' %(nsChar[0],POV_set_List[i],i+1)) 
            self.delConstraints.append(multMatrix_node)

            # connectAttr 
            for a in range(3):
                cmds.connectAttr('%s:%s.worldMatrix' %(nsChar[0],self.IKPOV_list[i][a]), '%s.inputMatrix' %decomposedMatrix_list[a] )
                cmds.connectAttr('%s.outputTranslate' %decomposedMatrix_list[a] , '%s.input3D[0]' %plusMinusAverage_list[a] )
            cmds.connectAttr('%s.output3D' %plusMinusAverage_list[0] , '%s.input3D[0]' %plusMinusAverage_list[4] )
            cmds.connectAttr('%s.output3D' %plusMinusAverage_list[2] , '%s.input3D[1]' %plusMinusAverage_list[4] )
            cmds.connectAttr('%s.output3D' %plusMinusAverage_list[4] , '%s.input1' %multiplyDivide_list[0] )
            cmds.connectAttr('%s.output' %multiplyDivide_list[0]  , '%s.input3D[1]' %plusMinusAverage_list[3] )
            cmds.connectAttr('%s.output3D' %plusMinusAverage_list[1]  , '%s.input3D[0]' %plusMinusAverage_list[3] )
            cmds.connectAttr('%s.output3D' %plusMinusAverage_list[3] , '%s.input1' %multiplyDivide_list[1] )
            cmds.connectAttr('%s.output' %multiplyDivide_list[1] , '%s.input3D[0]' %plusMinusAverage_list[5] )
            cmds.connectAttr('%s.output' %multiplyDivide_list[0]  , '%s.input3D[1]' %plusMinusAverage_list[5] )
            cmds.connectAttr('%s.output3D' %plusMinusAverage_list[5] , '%s.inputTranslate' %composeMatrix_node)
            cmds.connectAttr('%s.outputMatrix' %composeMatrix_node ,'%s.matrixIn[0]' %multMatrix_node )
            cmds.connectAttr('%s.matrixSum' %multMatrix_node ,'%s.inputMatrix' %decomposedMatrix_list[3] )
            cmds.connectAttr('%s.outputTranslate' %decomposedMatrix_list[3] , '%s:%s.translate' %(nsChar[0],self.IKPOV_list[i][3]))
            cmds.connectAttr('%s:%s.parentInverseMatrix' %(nsChar[0],self.IKPOV_list[i][3]) , '%s.matrixIn[1]' %multMatrix_node )       ## IK poleVector Bake

    def attatchWorldCon(self):
        root_CON = ['%s:root_CON' %self.targetNS[0]]
        temp_Loc = cmds.spaceLocator(n = 'temp_root_LOC')
        cmds.parentConstraint("%s:root_CON" %self.targetNS[0] , temp_Loc, mo=0)
        cmds.select(temp_Loc,r=1)
        cmds.bakeResults( simulation=True, t=( int(self.minCurrent), int(self.maxCurrent) ), sampleBy=1, dic=True, pok=True, sac=False, ral=False, bol=False, mr=True, controlPoints=False, shape=False )
        cmds.select( temp_Loc , r=1)
        cmds.select( "%s:move_CON" %self.targetNS[0], add=1)
        p4Con = cmds.pointConstraint(mo=1, skip= "y" ,w=1)
        self.delConstraints.append(p4Con[0])
        self.delConstraints.append(temp_Loc[0])
        cmds.select(cl=True)

    def mirrorAnim(self, item):
        nsChar = self.targetNS
        self.currentItem = item
        # print self.currentItem
        if self.currentItem == 'On':
            cmds.setAttr ("%s:HIKproperties1.Mirror" %nsChar[0], 1)
        else:
            cmds.setAttr ("%s:HIKproperties1.Mirror" %nsChar[0], 0)

    def bakeIKControl(self):
        nsChar = self.targetNS
        cmds.select(cl=True)
        if self.worldCon_CKB.isChecked() == True:
            self.attatchWorldCon()
        for i in range(len(self.IKController_list)):
            print self.IKController_list[i]
            cmds.select('%s:%s' %(nsChar[0],self.IKController_list[i]), add=True)
        cmds.select("%s:move_CON" %nsChar[0] , add=True )
        cmds.currentTime(self.minCurrent)
        cmds.bakeResults( simulation=True, t=( int(self.minCurrent), int(self.maxCurrent) ), sampleBy=1, dic=True, pok=True, sac=False, ral=False, bol=False, mr=True, controlPoints=False, shape=False )
        cmds.select(cl=True)

    def bakeFKControl(self):
        nsChar = self.targetNS
        cmds.select(cl=True)
        if self.worldCon_CKB.isChecked() == True:
            self.attatchWorldCon()
        for i in range(len(self.FKController_list)):
            print self.FKController_list[i]
            cmds.select('%s:%s' %(nsChar[0],self.FKController_list[i]), add=True)
        cmds.select("%s:move_CON" %nsChar[0] , add=True )
        cmds.currentTime(self.minCurrent)
        cmds.bakeResults( simulation=True, t=( int(self.minCurrent), int(self.maxCurrent) ), sampleBy=1, dic=True, pok=True, sac=False, ral=False, bol=False, mr=True, controlPoints=False, shape=False )
        cmds.select(cl=True)

    def doSmartBake(self):
        sourceNS = str(self.getSourceHIK_list[0]).split(':')[0]
        targetNS = self.targetNS[0]
        if cmds.getAttr('%s:L_armBlend_CON.FKIKBlend' %sourceNS) == 1:
            fromList = self.IKController_list 
            targetList = self.IKController_list 
        if cmds.getAttr('%s:L_armBlend_CON.FKIKBlend' %sourceNS) == 0:
            fromList = self.FKController_list 
            targetList = self.FKController_list 
        if cmds.getAttr('%s:L_armBlend_CON.FKIKBlend' %sourceNS) == cmds.getAttr('%s:L_armBlend_CON.FKIKBlend' %targetNS):
            # get query Curve Attr 
            for i in range(len(fromList)):
                cmds.select('%s:%s' %(sourceNS,fromList[i]), r=True)
                cmds.selectKey(k=True)
                cmds.filterCurve()
                cmds.select('%s:%s' %(targetNS,targetList[i]), r=True)
                cmds.selectKey(k=True)
                cmds.filterCurve()
                cmds.selectKey(k=True)
                # keyframe
                kf_tx = cmds.keyframe('%s:%s.tx' %(sourceNS,fromList[i]) , q=True, tc=True)
                kf_ty = cmds.keyframe('%s:%s.ty' %(sourceNS,fromList[i]) , q=True, tc=True)
                kf_tz = cmds.keyframe('%s:%s.tz' %(sourceNS,fromList[i]) , q=True, tc=True)
                kf_rx = cmds.keyframe('%s:%s.rx' %(sourceNS,fromList[i]) , q=True, tc=True)
                kf_ry = cmds.keyframe('%s:%s.ry' %(sourceNS,fromList[i]) , q=True, tc=True)
                kf_rz = cmds.keyframe('%s:%s.rz' %(sourceNS,fromList[i]) , q=True, tc=True)
                # Cutkey 
                for j in range(len(kf_tx)):
                    int_kf_tx = int(kf_tx[j])
                    cmds.selectKey('%s:%s.tx' %(targetNS,targetList[i]) , rm=True, k=True , t=(kf_tx[j],kf_tx[j]))
                for j in range(len(kf_ty)):
                    int_kf_ty = int(kf_ty[j])
                    cmds.selectKey('%s:%s.ty' %(targetNS,targetList[i]) , rm=True, k=True , t=(kf_ty[j],kf_ty[j]))
                for j in range(len(kf_tz)):
                    int_kf_tz = int(kf_tz[j])
                    cmds.selectKey('%s:%s.tz' %(targetNS,targetList[i]) , rm=True, k=True , t=(kf_tz[j],kf_tz[j]))
                for j in range(len(kf_rx)):
                    int_kf_rx = int(kf_rx[j])
                    cmds.selectKey('%s:%s.rx' %(targetNS,targetList[i]) , rm=True, k=True , t=(kf_rx[j],kf_rx[j]))
                for j in range(len(kf_ry)):
                    int_kf_ry = int(kf_ry[j])
                    cmds.selectKey('%s:%s.ry' %(targetNS,targetList[i]) , rm=True, k=True , t=(kf_ry[j],kf_ry[j]))
                for j in range(len(kf_rz)):
                    int_kf_rz = int(kf_rz[j])
                    cmds.selectKey('%s:%s.rz' %(targetNS,targetList[i]) , rm=True, k=True , t=(kf_rz[j],kf_rz[j]))
                cmds.cutKey(cl=True , an='keys')
                # make blank list
                at_tx = [] ; at_ty = [] ; at_tz = [] ; at_rx = [] ; at_ry = [] ; at_rz = [] 
            
                del at_tx[0:len(at_tx)] ; del at_ty[0:len(at_ty)] ; del at_tz[0:len(at_tz)] ;  del at_rx[0:len(at_rx)] ; del at_ry[0:len(at_ry)] ; del at_rz[0:len(at_rz)]
        else:
            cmds.warning('"Need same IK / FK status."')

    def runRetargeting(self):
        if self.timeSlider_RDB.isChecked() == True:
            self.minCurrent = cmds.playbackOptions( q=1,min=True ) - 1
            self.maxCurrent = cmds.playbackOptions( q=1,max=True ) + 1
            if self.IK_RDB.isChecked() == True:
                self.bakeIKControl()
            else:
                self.bakeFKControl()
        if self.startEnd_RDB.isChecked() == True:
            self.minCurrent = self.start_LIN.text()
            self.maxCurrent = self.end_LIN.text()
            if self.IK_RDB.isChecked() == True:
                self.bakeIKControl()
            else:
                self.bakeFKControl()
        if self.delConstraints == None:
            pass
        else:
            cmds.delete( self.delConstraints )
            cmds.delete('*:HIKJoint_LOC')
            cmds.delete('*:HIK*')
            cmds.delete('*HIK*')
        if self.mocap_RDB.isChecked() == True:
            cmds.delete('humanType01_humanIK_mocap_char_GRP') 
            """
        if cmds.objExists('*:HIKJoint_LOC') == True:
            cmds.delete('*:HIKJoint_LOC')
            cmds.delete('*:HIK*')
            cmds.delete('*HIK*')
            """
        cmds.select(cl=True)
        


#--------------------------------------------------------------------------------------------
def OPEN():
    window_name     = 'HIK_retargeting'
    dock_control     = 'HIK_retargeting_Dock'
    
    if cmds.window( window_name, exists=True ):
        cmds.deleteUI( window_name )

    Window = uiMainWindow()
    Window.show()

    Window.setObjectName(window_name)
 

    if (cmds.dockControl(dock_control, q=True, ex=True)):
        cmds.deleteUI(dock_control)
    AllowedAreas = ['right', 'left']
    cmds.dockControl(dock_control, aa=AllowedAreas, a='left', floating=False, content=window_name, label='HIK_retargeting')
  
