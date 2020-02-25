#encoding=utf-8

#------------------------------------------------------------------------------
# Rigging & Simulation Team
#		taehoon.kim@dexterstudios.com
# date : 2017/05/11
#------------------------------------------------------------------------------
# PySide to PySide2 : Convert


# ------------------------------------------------------------------------------
# Import
# ------------------------------------------------------------------------------

import os

from Qt import QtGui, QtCore, QtWidgets, load_ui

from Qt.QtGui import *
from Qt.QtCore import *
from Qt.QtWidgets import *

import maya.OpenMayaUI as mui
import maya.cmds as cmds
import pymel.core as pm

basePath = os.path.abspath(__file__ + '/../')
print basePath

uiFile = os.path.join(basePath, 'jointOrientTool.ui')
print uiFile

#------------------------------------------------------------------------------#

def undo(func):
    def wrapper(*args, **kwargs):
        cmds.undoInfo(openChunk=True)
        try:
            ret = func(*args, **kwargs)
        finally:
            cmds.undoInfo(closeChunk=True)
        return ret
    return wrapper


def undo_pm(func):
    def wrapper(*args, **kwargs):
        pm.undoInfo(openChunk=True)
        try:
            ret = func(*args, **kwargs)
        finally:
            pm.undoInfo(closeChunk=True)
        return ret
    return wrapper

#-------------------------------------------------------------------------------#

class GUI( QtWidgets.QMainWindow ):

	def __init__(self, parent=None):
		
		# Initialize abstract classes
		super(GUI, self).__init__(parent)
		self.ui = load_ui(uiFile)
		
		self.ui.setObjectName('JOT_WIN')
		self.ui.setWindowTitle('JOT Tool')
		
		self.createConnections()
		
	def createConnections(self):
		self.ui.template_pushButton.clicked.connect(self.templateJoint)
		self.ui.reBuild_Joint_pushButton.clicked.connect(self.reBuildJoint)
		self.ui.joint_pushButton.clicked.connect(self.create_joint)
		
	def create_joint(self):
		cmds.JointTool()

	@undo	
	def templateJoint(self):
		
		aimX = int(self.ui.aimX_lineEdit.text())
		aimY = int(self.ui.aimY_lineEdit.text())
		aimZ = int(self.ui.aimZ_lineEdit.text())
		
		upX = int(self.ui.upX_lineEdit.text())
		upY = int(self.ui.upY_lineEdit.text())
		upZ = int(self.ui.upZ_lineEdit.text())
		
		self.jointList = []
		self.tempLocList = []
		self.tempLocNulList = []
		
		self.constraintList = []
		
		selectJoint = cmds.ls( sl=True )
		if selectJoint == []:
			self.noSelection()
		else:
			if cmds.nodeType(selectJoint[0]) == 'joint':
				self.jointList.append(selectJoint[0])
				
				joints = cmds.listRelatives( selectJoint[0], allDescendents=True )
				if joints == None:
					cmds.confirmDialog( message = 'Must use at least bones!' )
				else:
					joints.reverse()
					
					for j in range(len(joints)):
						self.jointList.append(joints[j])
					
					for x in range(len(self.jointList)):
						tempLoc = cmds.spaceLocator( n='Temp%s_LOC' % x )
						self.tempLocList.append(tempLoc[0])
						
						tempLocNul = cmds.group( tempLoc, n='%s_NUL' % tempLoc[0] )
						self.tempLocNulList.append(tempLocNul)
						
						jointP = cmds.xform( self.jointList[x], q=True, ws=True, t=True )
						#print  jointP
						cmds.move( jointP[0], jointP[1], jointP[2], tempLocNul )
						
					fAimCons = cmds.aimConstraint( self.jointList[1], self.tempLocNulList[0], aimVector=[aimX,aimY,aimZ], upVector=[upX,upY,upZ], worldUpType='vector', worldUpVector=[upX,upY,upZ] )
					self.constraintList.append(fAimCons[0])
					for i in range(len(self.jointList)-2):
						mAimCons = cmds.aimConstraint( self.jointList[i+2], self.tempLocNulList[i+1], aimVector=[aimX,aimY,aimZ], upVector=[upX,upY,upZ], worldUpType='objectrotation', worldUpVector=[upX,upY,upZ], worldUpObject=self.tempLocList[i] )
						self.constraintList.append(mAimCons[0])
					lAimCons = cmds.orientConstraint( self.tempLocList[-2], self.tempLocNulList[-1] )
					self.constraintList.append(lAimCons[0])
					#
					cmds.select(self.tempLocList)
					cmds.ToggleLocalRotationAxes()
					cmds.select(self.tempLocList[0])
					
			else:
				self.noSelection()
	@undo
	def reBuildJoint(self):
		cmds.delete( self.constraintList )
		
		cmds.parent( self.jointList[1:], w=True )
		
		for i in range(len(self.jointList)):
			cmds.parent( self.jointList[i], self.tempLocList[i] )
			
			cmds.setAttr( '%s.rotateX' % self.jointList[i], 0 )
			cmds.setAttr( '%s.rotateY' % self.jointList[i], 0 )
			cmds.setAttr( '%s.rotateZ' % self.jointList[i], 0 )
			
			cmds.setAttr( '%s.jointOrientX' % self.jointList[i], 0 )
			cmds.setAttr( '%s.jointOrientY' % self.jointList[i], 0 )
			cmds.setAttr( '%s.jointOrientZ' % self.jointList[i], 0 )
			
		cmds.parent( self.jointList, w=True )
		
		cmds.delete( self.tempLocNulList )
		
		for x in range(len(self.jointList)-1):
			cmds.parent( self.jointList[x+1], self.jointList[x] )
			
	def noSelection(self):
		cmds.confirmDialog(message = 'no joint was selected!')
		
def Open():
    global Window
    if cmds.window('JOT_WIN', query=True, exists=True):
        cmds.deleteUI('JOT_WIN', window=True)
    Window = GUI()
    Window.ui.show()
