
import os
import sys
import site
import json
import maya.api.OpenMaya as om
import maya.OpenMayaUI as omui
import maya.cmds as cmds
from Qt import QtGui, QtCore, QtWidgets, load_ui

from Qt.QtGui import *
from Qt.QtCore import *
from Qt.QtWidgets import *
from functools import partial

basePath = os.path.abspath(__file__ + '/../')
if not basePath in sys.path:
    site.addsitedir(basePath)
import MTSC_Solver as mtsc ;(reload(mtsc))
import numpy as np
#import module.samplingSim as sS ; reload(sS)

uiFile = os.path.join(basePath, 'DTSCtool.ui')

class MtscTool(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(MtscTool, self).__init__(parent)
        
        self.ui = load_ui(uiFile)
        self.ui.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        # value
        self.mode = 0
        self.skincluster = None
        self.numBones = None
        self.boneList = list()
        self.mesh = None
        self.rest_pose = None
        self.poses = None

        self.setWindowTitle('MTSC_tool')
        self.createConnections()

    def createConnections(self):
        self.ui.mode_CBX.currentIndexChanged.connect(self.modeSelection)
        self.ui.boneList_BTN.clicked.connect(self.InsertBoneList)       
        self.ui.mesh_BTN.clicked.connect(self.InsertMesh)
        self.ui.pose_BTN.clicked.connect(self.InsertPose)
        #self.ui.maxInfluence_SPB
        #self.ui.initIteration_SPB
        
        #self.connect(self.ui.poses_LWG, SIGNAL('itemClicked(QListWidgetItem)') , self.clickPoses)
        
        self.connect(self.ui.posesInsert_BTN, SIGNAL('clicked()') , partial(self.addPoses , self.ui.poses_LWG))
        self.connect(self.ui.posesClear_BTN, SIGNAL('clicked()') , partial(self.clearPoses , self.ui.poses_LWG))
        
        self.ui.updateWeight_BTN.clicked.connect(self.updateWeightFunc)
        self.ui.updateBoneTrasn_BTN.clicked.connect(self.updateBoneTransFunc)

        self.ui.both_BTN.clicked.connect(self.updateBothFunc)
        
        #MTSC(poses, rest_pose, num_bones, sparseness=4, max_iterations=5 , iterations = 3 , mayaMesh = None , jointList = None)


    def modeSelection(self):
        modeIndex = self.ui.mode_CBX.currentIndex()
        self.mode = modeIndex

        if modeIndex == 0 : 
            #vq mode
            #enable
            self.ui.boneNum_SPB.setEnabled(1)
            #disable
            self.ui.boneList_LED.setEnabled(0)
            self.ui.mesh_LED.setEnabled(0)
            
            
        else:
            #vw mode
            #enable
            self.ui.boneList_LED.setEnabled(1)
            self.ui.mesh_LED.setEnabled(1)
            
            #disable
            self.ui.boneNum_SPB.setEnabled(0)

    def InsertBoneList(self):
        sel = cmds.ls(sl=1)
        if len(sel) == 1:
            sel = sel[0]
            bones = cmds.ls(cmds.listRelatives ( sel ,c =1 ,ad=1) , type = 'joint')
            bones.append(sel)
        else:
            print 'please select topLevel Joint'
        self.ui.boneList_LED.setText(str(bones))
        self.boneList = bones

    def InsertMesh(self):
        sel = cmds.ls(sl=1)
        if len(sel) == 1 :
            sel = sel[0]
        else:
            print 'please select one head rest pose mesh' 
        self.ui.mesh_LED.setText(sel)
        self.mesh = sel
        selectionLs = om.MGlobal.getActiveSelectionList()
        self.rest_pose = np.array(om.MFnMesh(selectionLs.getDagPath(0)).getPoints(om.MSpace.kWorld))[:, :3]
        
        #find skinCluster
        skincluster = mel.eval('findRelatedSkinCluster("%s")'%mayaMesh)
        if skincluster:
            self.skincluster = skincluster
        
    
    def InsertPose(self):
        sel = cmds.ls(sl=1)
        if len(sel) == 1 :
            sel = sel[0]
        else:
            print 'please select one pose Mesh(simulation)'
        self.ui.pose_LED.setText(sel)
           

    def addPoses(self, QListWidget):
        items = list()
        for i in xrange(QListWidget.count()):
            items.append(QListWidget.item(i))

        if self.ui.pose_LED and self.ui.simulationRange_min_LED and self.ui.simulationRange_max_LED: 
            #simulation sampling pose 
            min_ = int(self.ui.simulationRange_min_LED.text())
            max_ = int(self.ui.simulationRange_max_LED.text())
            pose = self.ui.pose_LED.text()
            
            simPoses = list()
            for i in range(min_ , max_+1):
                cmds.currentTime(i)
                cmds.select(pose)
                sel = om.MGlobal.getActiveSelectionList()
                simPoses.append(om.MFnMesh(sel.getDagPath(0)).getPoints(om.MSpace.kWorld))
            #self.poses = np.array(simPoses)[:,:,:3]
            
            source = '{pose} : {min} ~ {max}'.format(pose = pose , min = min_ , max = max_)
            
            if not source in items : 
                QListWidget.addItems([source])

        else:
            posesMesh = list()
            if items:
                posesMesh += items
            posesMesh += cmds.ls(sl=1)
            QListWidget.clear()
            for na in posesMesh:
                if not na in items:
                    QListWidget.addItems([na])
            selectionLs = om.MGlobal.getActiveSelectionList()
            num_poses = selectionLs.length()
            self.poses = np.array([om.MFnMesh(selectionLs.getDagPath(i)).getPoints(om.MSpace.kWorld) for i in range(num_poses)])[:, :, :3]
            
    def clearPoses(self,QListWidget):
        self.poses = None
        QListWidget.clear()
        
    def updateWeightFunc(self ):
        self.ui.inprogress_PGB.reset()

        iterations = self.ui.initIteration_SPB.value()
        sparseness = self.ui.maxInfluence_SPB.value()
        maxIterations = self.ui.updateIteration_SPB.value()

        if self.mode == 1:
            bone_transforms, rest_bones_t ,finalBone = mtsc.initialize(self.poses, self.rest_pose, len(self.boneList) ,iterations ,self.mesh ,self.boneList)           
        else:
            bone_transforms, rest_bones_t ,finalBone = mtsc.initialize(self.poses, self.rest_pose, self.ui.boneNum_SPB.value() ,iterations)
            
        for _ in range(maxIterations):
            if self.mode == 1:
                W, bone_transforms, rest_bones_t ,finalBone = mtsc.MTSC(0 ,self.poses, self.rest_pose, bone_transforms , rest_bones_t , finalBone, sparseness ,self.mesh ,self.boneList)
            else:
                W, bone_transforms, rest_bones_t ,finalBone = mtsc.MTSC(0 ,self.poses, self.rest_pose, bone_transforms , rest_bones_t , finalBone, sparseness)
        print W, bone_transforms, rest_bones_t ,finalBone

    def updateBoneTransFunc(self):
        self.ui.inprogress_PGB.reset()
        
        iterations = self.ui.initIteration_SPB.value()
        sparseness = self.ui.maxInfluence_SPB.value()
        maxIterations = self.ui.updateIteration_SPB.value()

        if self.mode == 1:
            bone_transforms, rest_bones_t ,finalBone = mtsc.initialize(self.poses, self.rest_pose, len(self.boneList) ,iterations ,self.mesh ,self.boneList)           
        else:
            bone_transforms, rest_bones_t ,finalBone = mtsc.initialize(self.poses, self.rest_pose, self.ui.boneNum_SPB.value() ,iterations)
            
        for _ in range(maxIterations):
            if self.mode == 1:
                W, bone_transforms, rest_bones_t ,finalBone = mtsc.MTSC(1 ,self.poses, self.rest_pose, bone_transforms , rest_bones_t , finalBone, sparseness ,self.mesh ,self.boneList)
            else:
                W, bone_transforms, rest_bones_t ,finalBone = mtsc.MTSC(1 ,self.poses, self.rest_pose, bone_transforms , rest_bones_t , finalBone, sparseness)
        print W, bone_transforms, rest_bones_t ,finalBone

    def updateBothFunc(self ):
        self.ui.inprogress_PGB.reset()
        
        iterations = self.ui.initIteration_SPB.value()
        sparseness = self.ui.maxInfluence_SPB.value()
        maxIterations = self.ui.updateIteration_SPB.value()

        if self.mode == 1:
            bone_transforms, rest_bones_t ,finalBone = mtsc.initialize(self.poses, self.rest_pose, len(self.boneList) ,iterations ,self.mesh ,self.boneList)           
        else:
            bone_transforms, rest_bones_t ,finalBone = mtsc.initialize(self.poses, self.rest_pose, self.ui.boneNum_SPB.value() ,iterations)
            
        for _ in range(maxIterations):
            if self.mode == 1:
                W, bone_transforms, rest_bones_t ,finalBone = mtsc.MTSC(2 ,self.poses, self.rest_pose, bone_transforms , rest_bones_t , finalBone, sparseness ,self.mesh ,self.boneList)
            else:
                W, bone_transforms, rest_bones_t ,finalBone = mtsc.MTSC(2 ,self.poses, self.rest_pose, bone_transforms , rest_bones_t , finalBone, sparseness)
        print W, bone_transforms, rest_bones_t ,finalBone
    

            
            


def OPEN():
    global Window
    try:
        Window.close()
        Window.deleteLater()
    except:
        pass

    Window = MtscTool()

    Window.ui.show()