
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

        self.sList = []
        self.sf_list = []
        self.ef_list = []

    def createConnections(self):

        # connection method

        self.ui.meshSelect_BTN.clicked.connect(self.MeshSelect)
        self.ui.path_BTN.clicked.connect(self.pathSelect)
        self.ui.makeLoop_BTN.clicked.connect(self.runLoop)

        self.ui.loopRange_LED.valueChanged.connect(self.loopConfirm)

    def loopConfirm(self):
        loopRg = self.ui.loopRange_LED.value()

        print loopRg
        self.confirm = ((min(self.ef_list)-max(self.sf_list)) +1) * 2/3

        if loopRg >= self.confirm:
            self.ui.confirm_LED.setText('Impossible')
            self.ui.confirm_LED.setStyleSheet("color: rgb(255, 0, 0);")
        elif loopRg < self.confirm:
            self.ui.confirm_LED.setText('Possible')
            self.ui.confirm_LED.setStyleSheet("color: rgb(0, 255, 0);")

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
            self.sf_list.append(sf_)

            ef_ = cmds.getAttr('{}.sourceEnd'.format(self.info_dict_[i][1]))
            self.ef_list.append(ef_)

            info_Final.append('{0} : {1} ~ {2}'.format(i+'_cacheBlend',sf_,ef_))

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
                try:
                    self.ui.loopRange_LED.setEnabled(False)
                    self.ui.confirm_LED.setEnabled(False)
                    self.ui.makeLoop_BTN.setEnabled(False)
                except:
                    pass

                self.info_dict_ = {}
                for i in self.selMesh:
                    sn = cmds.listRelatives(i ,s=True)[0]
                    self.shape = sn
                    self.sList.append(sn)
                    self.info_dict_[self.shape] = [self.shape + 'A_cache',self.shape + 'B_cache',self.shape + '_cacheBlend']

            else:
                if os.path.exists(cacheFolder +'/'+ i):
                    try:
                        self.ui.loopRange_LED.setEnabled(True)
                        self.ui.confirm_LED.setEnabled(True)
                        self.ui.makeLoop_BTN.setEnabled(True)
                    except:
                        pass

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
                    try:
                        self.ui.loopRange_LED.setEnabled(False)
                        self.ui.confirm_LED.setEnabled(False)
                        self.ui.makeLoop_BTN.setEnabled(False)
                    except:
                        pass


    def loopFunction(self,cache1,cache2,cbNode,frameRange):

        n_sE = frameRange * 3/2

        y = cmds.getAttr('%s.sourceStart' %cache1)

        cmds.setAttr('%s.sourceEnd' %cache1 , int(y + n_sE -1))
        cmds.setAttr('%s.sourceEnd' %cache2 , int(y + n_sE -1))
        x = cmds.getAttr('%s.sourceEnd' %cache1)
        z = x - y + 1

        sf1_att = -(z/3) + 1

        sf2_att = z + 2*(sf1_att-1)

        cmds.setAttr('%s.startFrame' %cache1 ,sf1_att)
        cmds.setAttr('%s.startFrame' %cache2 ,sf2_att)

        #setKey cacheBlend
        cmds.currentTime((y + n_sE -1 )* 1/3)
        cmds.setAttr('{}.cacheData[0].weight'.format(cbNode),1)
        cmds.setAttr('{}.cacheData[1].weight'.format(cbNode),0)
        cmds.setKeyframe('{}.cacheData[0].weight'.format(cbNode))
        cmds.setKeyframe('{}.cacheData[1].weight'.format(cbNode))

        cmds.currentTime((y + n_sE -1) * 2/3)
        cmds.setAttr('{}.cacheData[0].weight'.format(cbNode),0)
        cmds.setAttr('{}.cacheData[1].weight'.format(cbNode),1)
        cmds.setKeyframe('{}.cacheData[0].weight'.format(cbNode))
        cmds.setKeyframe('{}.cacheData[1].weight'.format(cbNode))
        #set playbackoptions
        cmds.playbackOptions(min = y , max = self.ui.loopRange_LED.value() -1)

    def runLoop(self):
        loopRg = self.ui.loopRange_LED.value()

        if loopRg >= self.confirm:
            print "check loopRange"

        elif loopRg < self.confirm:
            for i in self.sList:

                a = self.info_dict_[i]
                self.loopFunction(a[0],a[1],a[2],loopRg)

################################## MAKE LOOP ########################

def OPEN():
    global Window
    try:
        Window.close()
        Window.deleteLater()
    except: pass
    Window = makeLoop()
    Window.ui.show()
