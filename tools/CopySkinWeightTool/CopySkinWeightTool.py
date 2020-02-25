
# encoding=utf-8
# !/usr/bin/env python

# -------------------------------------------------------------------------------
#   CopySkinWeightTool
#   Dexter Rigging Team
#
#		Taewoo.Lim
#
#	2017.01.18
# -------------------------------------------------------------------------------
import os
import site

from Qt import QtGui, QtCore, QtWidgets, load_ui

from Qt.QtGui import *
from Qt.QtCore import *
from Qt.QtWidgets import *

from functools import partial

# from PySide import QtCore, QtGui
# from PySide.QtCore import *
# from PySide.QtGui import *

# from shiboken import wrapInstance

import maya.cmds as cmds
import maya.mel as mel

import maya.OpenMayaUI as omui

import xml.etree.ElementTree as xml
#import pysideuic
from cStringIO import StringIO


basePath = os.path.abspath(__file__ + '/../')
print basePath
uiFile = os.path.join(basePath, 'CopySkinWeightTool.ui')
print uiFile

"""
def maya_main_window():

    main_window_ptr = omui.MQtUtil.mainWindow()
    return wrapInstance(long(main_window_ptr), QtGui.QWidget)



def loadUiType(uiFile):
    #
    # Pyside lacks the "loadUiType" command, so we have to convert the ui file to py code in-memory first
    # and then execute it in a special frame to retrieve the form_class.
    #
    parsed = xml.parse(uiFile)
    widget_class = parsed.find('widget').get('class')
    form_class = parsed.find('class').text

    with open(uiFile, 'r') as f:
        o = StringIO()
        frame = {}

        pysideuic.compileUi(f, o, indent=0)
        pyc = compile(o.getvalue(), '<string>', 'exec')
        exec pyc in frame

        # Fetch the base_class and form class based on their type in the xml from designer
        form_class = frame['Ui_%s' % form_class]
        base_class = eval('QtGui.%s' % widget_class)
    return form_class, base_class


# form_class, base_class = loadUiType(uiFile)
"""

class CopySkinWeightTool(QtWidgets.QMainWindow):#form_class, base_class):
    def __init__(self, parent=None):
        super(CopySkinWeightTool, self).__init__(parent)
        #self.setupUi(self)
        self.ui = load_ui(uiFile)

        self.setWindowTitle('CopySkinWeightTool')
        self.createConnections()
        self.baseMeshList = None
        self.targetMeshList= None
        self.assetName = None

    def createConnections(self):

        # connection method

        self.ui.baseMesh_BTN.clicked.connect(self.baseMeshSelect)
        self.ui.targetMesh_BTN.clicked.connect(self.targetMeshSelect)
        self.ui.copySkin_BTN.clicked.connect(self.buttonSignal)
        self.ui.bodyMeshSel_BTN.clicked.connect(self.bodyMeshSel)
        self.ui.copyToBody_BTN.clicked.connect(self.copySkinFromBody)
        self.ui.Another_copySkin_BTN.clicked.connect(self.anotherCopyButton)

        self.connect(self.ui.otherInput_LWG, SIGNAL("itemClicked( QListWidgetItem *)"),
                     self.selRemainMesh)

        self.connect(self.ui.newAddedMesh_LWG, SIGNAL("itemClicked( QListWidgetItem *)"),
                     self.selNewAddedMesh)

        self.connect(self.ui.blendShape_LWG, SIGNAL("itemClicked( QListWidgetItem *)"),
                     self.selBlendMesh)

        self.connect(self.ui.wrap_LWG, SIGNAL("itemClicked( QListWidgetItem *)"),
                     self.selWrapMesh)
########################################################UI Start

########################button signal

    def selRemainMesh(self, item):
        self.selRemaintext = item.text()

        self.remainMeshSelect()

    def selNewAddedMesh(self , item):
        self.selNewAddedtext = item.text()

        self.newAddedMeshSelect()

    def selBlendMesh(self, item):
        self.selBlendtext = item.text()

        self.BlendMeshSelect()

    def selWrapMesh(self , item):
        self.selWraptext = item.text()

        self.WrapMeshSelect()

    def remainMeshSelect(self):

        cmds.select(self.selRemaintext)

    def newAddedMeshSelect(self):
        cmds.select(self.selNewAddedtext)

    def BlendMeshSelect(self):
        cmds.select(self.selBlendMesh)

    def wrapMeshSelect(self):
        cmds.select(self.selWrapMesh)

    def blendShapeWrap(self):

        self.blendGroup = []
        self.wrapGroup = []

        try:
            blendSet = cmds.ls('blend*' or '*_BLS')
            wrapSet = cmds.ls('wrap*' or '*_WRP')

            for i in self.plyList:
                if cmds.listConnections(i):#mesh has BlendShape or wrap
                    lcRemaintext = cmds.listConnections(i)
                    setBlend = set(lcRemaintext)
                    if [x for x in blendSet if x in setBlend]:
                        self.ui.blendShape_LWG.addItems(i)
                        self.blendGroup.append(i)

                    if [z for z in wrapSet if z in setBlend]:
                        print 'newAddedMesh OK'

                        self.ui.wrap_LWG.addItems(i)
                        self.wrapGroup.append(i)
            if self.targetMeshList:
                newAddMesh = [y for y in self.targetMeshList if y in self.remainList]
            else:
                tList = cmds.ls(self.targetName + '*_PLY*',type = 'transform')
                newAddMesh = [y for y in tList if y in self.remainList]
            if newAddMesh:
                self.ui.newAddedMesh_LWG.addItems(newAddMesh)

        except:
            pass
    def baseMeshSelect(self):
        baseMeshSel = cmds.ls(sl=True)
        self.selMesh = baseMeshSel[0]
        self.ui.baseMesh_LET.setText(baseMeshSel[0])
        #baseMeshList make
        self.baseMeshList = cmds.ls('*_PLY')
        # baseMeshSel[0].split('_')[0] + '_

    def targetMeshSelect(self):
        targetMeshSel = cmds.ls(sl=True)
        self.ui.targetMesh_LET.setText(targetMeshSel[0])
        #targetMeshList make
        self.assetName = targetMeshSel[0].split(':')[0]
        self.targetMeshList = cmds.ls(self.assetName + ':' + '*_PLY*',type = 'transform')

    def bodyMeshSel(self):
        baseBodySel = cmds.ls(sl=True)
        self.selBody = baseBodySel[0]
        self.ui.bodyMesh_LED.setText(baseBodySel[0])

####################################UI END ########################################

    def skinBind(self,targetL):

        jointList = cmds.ls('*_Skin_*_JNT')

        #cmds.select('*_Skin_*_JNT',self.targetMeshList)
        for i in targetL:
            scl = cmds.skinCluster(jointList , i , tsb=True)
            cmds.skinCluster(scl , e = True , mi =15)
        #mel.eval('SmoothBindSkin;')

    def copySkinWeight(self,baseL):

        self.tempList = []
        self.remainList = [] #other input connect
        self.plyList = []

        for i,name in enumerate(baseL):

            lcSkinC = cmds.listConnections( mel.eval('findRelatedSkinCluster '+ name ) + '.matrix')
            if lcSkinC:
                if self.baseMeshList and self.targetMeshList:
                    if cmds.objExists(self.assetName + ':'+ baseL[i]):

                        cmds.select(name ,self.assetName + ':'+ baseL[i])
                        print name ,self.assetName + ':'+ baseL[i]
                        self.tempList.append(self.assetName + ':'+ baseL[i])
                        self.plyList.append(baseL[i])
                        mel.eval('CopySkinWeights;')
                        mel.eval('performCopySkinWeights false;')
                        mel.eval('copySkinWeights  -noMirror -surfaceAssociation closestPoint -influenceAssociation closestJoint;')
                    else:
                        self.remainList.append(baseL[i])
                else:
                    a = name.replace(self.baseName,self.targetName)
                    print 'a = ' + a
                    if cmds.objExists(a):
                        cmds.select(name ,a)
                        print name , a
                        self.tempList.append(a)

                        self.plyList.append(baseL[i])
                        mel.eval('CopySkinWeights;')
                        mel.eval('performCopySkinWeights false;')
                        mel.eval('copySkinWeights  -noMirror -surfaceAssociation closestPoint -influenceAssociation closestJoint;')
                    else:
                        self.remainList.append(a)
            else:
            # self.tempList.append(self.baseMeshList[i])
                pass

    def copySkinFromBody(self):

        for i in range(len(self.noCopyListNR)):
            if cmds.objExists(self.noCopyListNR[i]):

                cmds.select(self.selBody,self.noCopyListNR[i])
                mel.eval('CopySkinWeights;')
                mel.eval('performCopySkinWeights false;')
                mel.eval('copySkinWeights  -noMirror -surfaceAssociation closestPoint -influenceAssociation closestJoint;')

        self.ui.newAddedMesh_LWG.clear()



    def unbindSkin(self):
        self.unBindList = []
        for z in self.tempList:
            if self.baseMeshList and self.targetMeshList:
                zList = z.split(':')[1]
            else:
                zList = z.replace(self.targetName,self.baseName)
            self.unBindList.append(zList)

        cmds.select(self.unBindList)
        print self.unBindList
        mel.eval('doDetachSkin "2" { "1","1" };')
        #delete func

        '''if self.baseMeshList and self.targetMeshList:
            self.assetList = cmds.ls(self.assetName +':'+ '*_PLY*' , type = 'transform')
        else:
            self.assetList = cmds.ls(self.targetName + '*_PLY*' ,type = 'transform')
        setA = set(self.tempList)
        self.noCopyList = [x for x in self.assetList if x not in setA]

        self.noCopyListMinor = []
        for x in self.noCopyList:
            addList = x.split(':')[1]
            self.noCopyListMinor.append(addList)'''

        self.baseMeshGrp = cmds.listRelatives(self.unBindList[0],fullPath=True)[0].split('geometry_GRP|')[1].split('|')[0]

        #self.visNode = cmds.listConnections('%s.visibility' % self.baseMeshGrp , p=True )

        addInputGroup = cmds.group(n= 'addInput_GRP' , w=True ,em = True)

        #if self.blendGroup:
            #cmds.parent(self.blendGroup, addInputGroup)
        #if self.wrapGroup:
            #cmds.parent(self.wrapGroup, addInputGroup)
        if self.baseMeshList:
            cmds.delete(self.baseMeshGrp)

    def targetGroup(self):
        if self.baseMeshList and self.targetMeshList:
            self.targetMeshGrp = cmds.listRelatives(self.targetMeshList[0],fullPath = True)[0].split('|')[1]

        else:
            self.targetMeshGrp = cmds.listRelatives(self.unBindList[0].replace(self.baseName,self.targetName),fullPath = True)[0].split('|')[1]

        cmds.parent(self.targetMeshGrp,'geometry_GRP')

    def selectTemp (self):
        if self.assetName:
            cmds.namespace( rm= self.assetName , mnp=True)
        '''
        try:
            if self.noCopyListMinor:
                setB = set(self.remainList)
                self.noCopyListNR = [y for y in self.noCopyListMinor if y not in setB]

                self.ui.newAddedMesh_LWG.clear()
                self.ui.newAddedMesh_LWG.addItems(self.noCopyListNR)

            if self.remainList:
                self.ui.otherInput_LWG.clear()
                self.ui.otherInput_LWG.addItems(self.remainList)
        except:
            pass
        '''
            #a = self.targetMeshGrp.split(':')[1]
            #cmds.connectAttr(self.visNode[0] ,'%s.visibility' %a ,f= True)


    def buttonSignal(self):
        self.skinBind(self.targetMeshList)
        self.copySkinWeight(self.baseMeshList)
        self.blendShapeWrap()

        self.unbindSkin()
        self.targetGroup()
        self.selectTemp()
        self.baseMeshList = None
        self.targetMeshList = None

    def anotherCopyButton(self):
        self.targetName = self.ui.anotherTarget_LED.text()
        self.baseName = self.ui.anotherBase_LED.text()
        bN_List = cmds.ls(self.baseName + '*_PLY*' ,type = 'transform')
        print bN_List
        tN_List = cmds.ls(self.targetName + '*_PLY*',type = 'transform')
        print tN_List
        self.skinBind(tN_List)
        self.copySkinWeight(bN_List)
        self.blendShapeWrap()

        self.unbindSkin()
        self.targetGroup()
        self.selectTemp()


##################################Local Time Warp end########################



# def OPEN():
#     window_name = 'MainWindow'
#     dock_control = 'MainWindow_Dock'
#
#     if cmds.window(window_name, exists=True):
#         cmds.deleteUI(window_name)
#
#     Window = CopySkinWeightTool()
#     Window.ui.show()
#
#     Window.setObjectName(window_name)

def OPEN():
    global Window
    try:
        Window.close()
        Window.deleteLater()
    except: pass
    Window = CopySkinWeightTool()
    Window.ui.show()
    """
    if (cmds.dockControl(dock_control, q=True, ex=True)):
        cmds.deleteUI(dock_control)
    AllowedAreas = ['right', 'left']
    cmds.dockControl(dock_control,aa=AllowedAreas, a='left', floating=False, content=window_name, label='EX Window')
    """
