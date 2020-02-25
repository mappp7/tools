
# encoding=utf-8
# !/usr/bin/env python

# -------------------------------------------------------------------------------
#   CopySkinWeightTool
#   Dexter Rigging Team
#
#		Taewoo.Lim
#
#	2018.08.10
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
uiFile = os.path.join(basePath, 'makeLoop_ui.ui')
print uiFile


class makeLoop(QtWidgets.QMainWindow):#form_class, base_class):
    def __init__(self, parent=None):
        super(makeLoop, self).__init__(parent)
        #self.setupUi(self)
        self.ui = load_ui(uiFile)

        self.setWindowTitle('makeLoop_v1.0.01')
        self.createConnections()

    def createConnections(self):

        pass

        # connection method
        
        self.ui.meshSelect_BTN.clicked.connect(self.MeshSelect)
        self.ui.path_BTN.clicked.connect(self.pathSelect)


        self.connect(self.ui.otherInput_LWG, SIGNAL("itemClicked( QListWidgetItem *)"),
                     self.selRemainMesh)

########################################################UI Start

########################button signal

    def MeshSelect(self, item):
        self.selMeshtext = item.text()

    def pathSelect(self):
        
        cmds.fileDialog2(fileFilter="*.xml" ,fm=3, dialogStyle=2, cap = 'select nCacheFile',okCaption="nCache" )[0] # dir = '%s' %self.Path


 '''#___________________
     def xlmFileInfo( self,filename ):
        ###########################################test


        xml = minidom.parse( filename )
        root = xml.getElementsByTagName( 'Autodesk_Cache_File' )
        allNodes = root[0].childNodes

        for node in allNodes:
            if node.nodeName == 'Channels':
                channels = node.childNodes

                for ch in channels:
                    if re.compile("channel").match(ch.nodeName) != None:
                        channelName = ''
                        for index in range(0, ch.attributes.length):
                            attrName = ch.attributes.item(index).nodeName
                            if attrName == 'ChannelName':
                                channelName = ch.attributes.item(index).nodeValue
        return channelName


    def IG_import (self,iList,cacheFolder):

        #self.importList

        self.IMchar = []
        for x in iList:
            self.IMchar.append(x + '_geoCacheShape.xml')

        xmlList = []
        for i in self.IMchar:

            xmlList.append(i)


        for i in xmlList:
            xmlInfo = self.xlmFileInfo(cacheFolder +'/'+ i)

            if not cmds.objExists('*:*_rig_GRP'):
                preShape = xmlInfo.split('_geoCacheShape')[0]+ 'Shape'
                shape = preShape
            else:
                preShape = xmlInfo.split(':')[-1].split('_geoCacheShape')[0]+ 'Shape'
                assetName = cmds.ls('*:*_rig_GRP')[0].split(':')[0]
                shape = assetName +':'+ preShape

            mcxFile = i.replace('xml','mcx')

            switch = mel.eval('createHistorySwitch("%s", false)'%shape)
            cacheNode = cmds.cacheFile( dir=cacheFolder, f='%s'%mcxFile, ia='%s.inp[0]' % switch, attachFile=True )
            cmds.setAttr('%s.playFromCache' % switch, 1)
        print '\n>>> import success <<<\n'

        '''



##################################Local Time Warp end########################



def OPEN():
    global Window
    try:
        Window.close()
        Window.deleteLater()
    except: pass
    Window = makeLoop()
    Window.ui.show()
