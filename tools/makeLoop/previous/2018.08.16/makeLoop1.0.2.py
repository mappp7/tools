
# encoding=utf-8
# !/usr/bin/env python

# -------------------------------------------------------------------------------
#   LOOP MAKER
#   Dexter Rigging Team
#
#		Taewoo.Lim
#
#	2018.08.10
# -------------------------------------------------------------------------------
import os
import site
import subprocess
from xml.dom import minidom, Node

import re
import time
import getpass

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
        self.selMesh = None
        self.path = None
        self.confirm = None
        self.ssname = None

        self.sList = []

    def createConnections(self):

        # connection method

        self.ui.meshSelect_BTN.clicked.connect(self.MeshSelect)
        self.ui.path_BTN.clicked.connect(self.pathSelect)
        self.ui.makeLoop_BTN.clicked.connect(self.runLoop)

        self.connect(self.ui.sourceFrame_LWG, SIGNAL("itemClicked( QListWidgetItem *)"),
            self.contactShape)

        self.ui.loopRange_LED.valueChanged.connect(self.loopConfirm(self.ssname))
        self.ui.loopRange2_LED.valueChanged.connect(self.loopConfirm(self.ssname))

    def contactShape(self,item):
        textQuery = item.text()
        self.ssname= textQuery.split(':')[0]
        cmds.select(self.ssname)

    def loopConfirm(self,sName):

        if self.ssname:
            minF = self.ui.loopRange_LED.value()
            maxF = self.ui.loopRange2_LED.value()
            start_ = cmds.getAttr('{}.sourceStart'.format(self.info_dict_[sName][0]))
            end_ = cmds.getAttr('{}.sourceEnd'.format(self.info_dict_[sName][0]))

            min_limit = (end_ - start_ +1)/5
            max_limit = end_ - min_limit

            if minF >= min_limit and maxF < max_limit :
                self.ui.confirm_LED.setText('Availiable')
                self.ui.confirm_LED.setStyleSheet("color: rgb(0, 255, 0);")

            elif minF < min_limit or maxF >= max_limit :
                self.ui.confirm_LED.setText('{0}△ ~ {1}▽'.format(min_limit , max_limit))
                self.ui.confirm_LED.setStyleSheet("color: rgb(255, 0, 0);")

        else:
            pass


########################################################UI Start

########################button signal

    def MeshSelect(self):
        self.selMesh = cmds.ls(sl=True)

        self.ui.meshList_LWG.clear()
        self.ui.meshList_LWG.addItems(self.selMesh)

        self.ui.nCache_LED.clear()
        self.ui.sourceFrame_LWG.clear()
        self.ui.loopRange_LED.clear()
        self.ui.confirm_LED.clear()

    def pathSelect(self):

        if len(self.selMesh) == 1:
            pt = cmds.fileDialog2(fileFilter="*.xml" ,fm=1, dialogStyle=2, cap = 'select nCacheFile',okCaption="nCache")[0]
            fileName = pt.split('/')[-1] # dir = '%s' %self.Path
            self.path = pt.split('/' + fileName)[0]

        else:
            self.path = cmds.fileDialog2(fileFilter="*.xml" ,fm=3, dialogStyle=2, cap = 'select nCacheFolder',okCaption="Folder")[0]

        self.IG_import(self.selMesh , self.path)

        info_Final = []
        for i in self.info_dict_:
            sf_ = cmds.getAttr('{}.sourceStart'.format(self.info_dict_[i][1]))

            ef_ = cmds.getAttr('{}.sourceEnd'.format(self.info_dict_[i][1]))

            info_Final.append('{0}: {1} ~ {2}'.format(i,sf_,ef_))

        self.ui.sourceFrame_LWG.clear()
        self.ui.sourceFrame_LWG.addItems(info_Final)


 #___________________
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
        #self.info_cacheList = []
        self.info_dict_ = {}
        self.sList = []

        for x in iList:
            self.IMchar.append( x + 'Shape.xml')

        for i in self.IMchar:
            sn = cmds.listRelatives(i.split('Shape.xml')[0] , s=1)[0]
            if cmds.objExists(sn + '_cacheBlend'):
                self.ui.nCache_LED.setText('>>> Already exists cacheBlend <<<')
                self.ui.nCache_LED.setStyleSheet("color: rgb(255, 255, 0);")
                self.ui.loopRange_LED.clear()
                self.ui.confirm_LED.clear()
                self.info_dict_ = {}
                for i in self.selMesh:
                    sn = cmds.listRelatives(i ,s=True)[0]
                    self.shape = sn
                    self.sList.append(sn)
                    self.info_dict_[self.shape] = [self.shape + 'A_cache',self.shape + 'B_cache',self.shape + '_cacheBlend']

            else:
                if os.path.exists(cacheFolder +'/'+ i):
                    xmlInfo = self.xlmFileInfo(cacheFolder +'/'+ i)

                    #preShape = xmlInfo.split('_geoCacheShape')[0]+ 'Shape'
                    sn = cmds.listRelatives(i.split('Shape.xml')[0] ,s=True)
                    if len(sn) > 1:
                        preShape = sn[1]
                    else:
                        preShape = sn[0]
                    self.shape = preShape
                    self.sList.append(self.shape)

                    mcxFile = i.replace('xml','mcx')

                    switch = mel.eval('createHistorySwitch("%s", false)'%self.shape)
                    CB = cmds.createNode('cacheBlend')
                    CBnode = cmds.rename(CB , self.shape + '_cacheBlend')
                    cacheNode1 = cmds.cacheFile( dir=cacheFolder, f='%s' %mcxFile, ia='%s.inCache[0].vectorArray[0]' % CBnode, attachFile=True )
                    cacheNode2 = cmds.cacheFile( dir=cacheFolder, f='%s' %mcxFile, ia='%s.inCache[0].vectorArray[1]' % CBnode, attachFile=True )
                    #rename
                    cacheNode1 = cmds.rename(cacheNode1 , self.shape + 'A_cache')
                    cacheNode2 = cmds.rename(cacheNode2 , self.shape + 'B_cache')

                    info_cache = cacheNode1
                    #self.info_cacheList.append(info_cache)
                    self.info_dict_[self.shape] = [cacheNode1,cacheNode2,CBnode]


                    #attribute connect
                    cmds.connectAttr('%s.start' %cacheNode1 , '%s.cacheData[0].start' %CBnode, f= 1)
                    cmds.connectAttr('%s.end' %cacheNode1 , '%s.cacheData[0].end' %CBnode, f= 1)
                    cmds.connectAttr('%s.inRange' %cacheNode1 , '%s.cacheData[0].range' %CBnode, f= 1)

                    cmds.connectAttr('%s.start' %cacheNode2 , '%s.cacheData[1].start' %CBnode , f= 1)
                    cmds.connectAttr('%s.end' %cacheNode2 , '%s.cacheData[1].end' %CBnode, f= 1)
                    cmds.connectAttr('%s.inRange' %cacheNode2, '%s.cacheData[1].range' %CBnode, f= 1)

                    cmds.connectAttr('%s.outCacheData[0]' %CBnode , '%s.inp[0]' %switch , f=1)

                    cmds.setAttr('%s.playFromCache' % switch, 1)
                    self.ui.nCache_LED.setText('>>> import success <<<')
                    self.ui.nCache_LED.setStyleSheet("color: rgb(0, 255, 0);")


                else:
                    self.ui.nCache_LED.setText('>>> Check path or file <<<')
                    self.ui.nCache_LED.setStyleSheet("color: rgb(255, 0, 0);")

    def loopFunction(self,cache1,cache2,cbNode):

        cmds.delete('{}_cacheData_1__weight'.format(cbNode))
        cmds.delete('{}_cacheData_0__weight'.format(cbNode))

        getMin = self.ui.loopRange_LED.value()
        n_sE = self.ui.loopRange2_LED.value()

        y = cmds.getAttr('%s.sourceStart' %cache1)

        cmds.setAttr('%s.sourceEnd' %cache1 , n_sE)
        cmds.setAttr('%s.sourceEnd' %cache2 , n_sE)
        x = cmds.getAttr('%s.sourceEnd' %cache1)

        sf1_att = -(getMin-y)

        sf2_att = -(getMin-y) + (n_sE - getMin-1)

        cmds.setAttr('%s.startFrame' %cache1 ,sf1_att)
        cmds.setAttr('%s.startFrame' %cache2 ,sf2_att)

        #setKey cacheBlend
        cmds.currentTime((n_sE-getMin)/2)
        cmds.setAttr('{}.cacheData[0].weight'.format(cbNode),1)
        cmds.setAttr('{}.cacheData[1].weight'.format(cbNode),0)
        cmds.setKeyframe('{}.cacheData[0].weight'.format(cbNode))
        cmds.setKeyframe('{}.cacheData[1].weight'.format(cbNode))

        cmds.currentTime(x)
        cmds.setAttr('{}.cacheData[0].weight'.format(cbNode),0)
        cmds.setAttr('{}.cacheData[1].weight'.format(cbNode),1)
        cmds.setKeyframe('{}.cacheData[0].weight'.format(cbNode))
        cmds.setKeyframe('{}.cacheData[1].weight'.format(cbNode))
        #set playbackoptions
        cmds.playbackOptions(min = y , max = self.ui.loopRange2_LED.value() -1)

    def runLoop(self):

        a = self.info_dict_[self.ssname]
        self.loopFunction(a[0],a[1],a[2])

################################## MAKE LOOP ########################

def OPEN():
    global Window
    try:
        Window.close()
        Window.deleteLater()
    except: pass
    Window = makeLoop()
    Window.ui.show()
