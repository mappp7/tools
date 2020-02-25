# ------------------------------------------------------------------------------
# Import
# ------------------------------------------------------------------------------
from Qt import QtGui, QtCore, QtWidgets, load_ui

from Qt.QtGui import *
from Qt.QtCore import *
from Qt.QtWidgets import *

from functools import partial

import os

# from PyQt4.QtGui import *
# from PyQt4.QtCore import *
# from PyQt4.uic import *

import maya.OpenMayaUI as mui
import maya.cmds as cmds
import maya.mel as mel

basePath = os.path.abspath(__file__ + '/../')
print basePath

uiFile = os.path.join(basePath, 'copySkinWeightsTool.ui')
print uiFile


# form_class, base_class = loadUiType(uiFile)

class scGUI(QtWidgets.QMainWindow):
    def __init__(self, parent=None):

        # Initialize abstract classes
        super(scGUI, self).__init__(parent)
        # self.setupUi(self)
        self.ui = load_ui(uiFile)

        # self.ui.setObjectName('WIN')
        self.ui.setWindowTitle('Copy Skin Weights Tool')

        self.createConnections()

    def createConnections(self):

        self.connect(self.ui.originSelectAdd_btn, SIGNAL('clicked()'), self.addOriginMesh)
        self.connect(self.ui.multiSelectAdd_btn, SIGNAL('clicked()'), partial(self.addMesh, self.ui.listWidget))

        self.connect(self.ui.copySkinWeights_btn, SIGNAL('clicked()'), self.copySkinWeights)

    def addOriginMesh(self):

        self.originMesh = cmds.ls(sl=1)

        if not self.originMesh:
            cmds.warning('Please select a originMesh.')
            self.ui.lineEdit.clear()

        elif self.originMesh:
            self.ui.lineEdit.setText(self.originMesh[0])

    def addMesh(self, QListWidget):

        self.objects = cmds.ls(sl=1)
        QListWidget.clear()
        QListWidget.addItems(self.objects)

    def jointsSkinCopys(self):

        # self.Shape = cmds.listRelatives( self.originMesh[0], s=True )
        # self.Cluster = cmds.listConnections( self.Shape[0] + '.inMesh' )
        self.Cluster = mel.eval('findRelatedSkinCluster ' + self.originMesh[0])
        self.joints = cmds.listConnections(self.Cluster + '.matrix')
        print self.joints

        cmds.select(cl=True)
        for x in self.joints:
            cmds.select(x, add=True)

        cmds.select(self.objects, add=True)
        cmds.SmoothBindSkin()

        for x in self.objects:
            cmds.select(self.originMesh)
            cmds.select(x, add=True)
            cmds.CopySkinWeights()
            cmds.select(cl=True)

    def copySkinWeights(self):
        if len(self.objects) > 0:
            self.jointsSkinCopys()
        else:
            cmds.warning('Choose to copy the mesh.')


def Open():
    # global win
    # if cmds.window('WIN', query=True, exists=True):
    #     cmds.deleteUI('WIN', window=True)
    # win = GUI()
    # win.ui.show()
    global win
    try:
        win.close()
        win.deleteLater()
    except:
        pass
    win = scGUI()
    win.ui.show()
