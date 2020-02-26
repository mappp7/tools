
# encoding=utf-8
# !/usr/bin/env python

# -------------------------------------------------------------------------------
#   CopySkinWeightTool
#   Dexter Rigging Team
#
#		Taewoo.Lim
#
#	2019.06.11
# -------------------------------------------------------------------------------
import os
import site
basePath = os.path.abspath(__file__ + '/../')
print basePath

import FKconMake as fc; reload(fc)
import divineJoint as dj; reload(dj)
import curveAttachLoc as cl; reload(cl)

from Qt import QtGui, QtCore, QtWidgets, load_ui

from Qt.QtGui import *
from Qt.QtCore import *
from Qt.QtWidgets import *

from functools import partial

import maya.cmds as cmds
import maya.mel as mel
import random

import maya.OpenMayaUI as omui

import xml.etree.ElementTree as xml
#import pysideuic
from cStringIO import StringIO


uiFile = os.path.join(basePath, 'rsToolUI.ui')


class rsTool(QtWidgets.QMainWindow):#form_class, base_class):
    def __init__(self, parent=None):
        super(rsTool, self).__init__(parent)
        #self.setupUi(self)
        self.ui = load_ui(uiFile)

        self.setWindowTitle('rsTool')
        self.createConnections()

    def createConnections(self):

        # connection method

        self.ui.zeroOut_BTN.clicked.connect(self.zeroOut)
        self.ui.copySkin_BTN.clicked.connect(self.copySkin)
        self.ui.addName_BTN.clicked.connect(self.addName)
        self.ui.deleteName_BTN.clicked.connect(self.deleteName)
        self.ui.randomColor_BTN.clicked.connect(self.randomColor)
        self.ui.locatorMatch_BTN.clicked.connect(self.locatorMatch)
        self.ui.posMatch_BTN.clicked.connect(self.posMatch)
        #FK CON MAKE BTN

        self.ui.fkMake_red_BTN.clicked.connect(self.red)
        self.ui.fkMake_blue_BTN.clicked.connect(self.blue)
        self.ui.fkMake_yellow_BTN.clicked.connect(self.yellow)
        self.ui.fkMake_skyBlue_BTN.clicked.connect(self.skyblue)
        self.ui.fkMake_pink_BTN.clicked.connect(self.pink)
        
        self.ui.jointMake_BTN.clicked.connect(self.jointMake)
        self.ui.curveBaseJoint_BTN.clicked.connect(self.curveBaseJoint)

        self.ui.pconstFunc_BTN.clicked.connect(self.pconstFunc)
        self.ui.sconstFunc_BTN.clicked.connect(self.sconstFunc)
        self.ui.aconstFunc_BTN.clicked.connect(self.aconstFunc)

        self.ui.saveUp_BTN.clicked.connect(self.saveUp)
        
    # fk con make
    def red(self):
        self.FKconMake('red')
    def blue(self):
        self.FKconMake('blue')
    def yellow(self):
        self.FKconMake('yellow')
    def skyblue(self):
        self.FKconMake('skyblue')
    def pink(self):
        self.FKconMake('pink')

    def FKconMake(self, color):
        text = self.ui.fk_CBX.currentText()
        colorDict = {'red':13,'blue':6,'yellow':17,'skyblue':18,'pink':20}
        ins = fc.FkConMake()
        ins.launcher(1,text,colorDict[color])

    def jointMake(self):
        dj.ui()
    def curveBaseJoint(self):
        int_ = self.ui.spinBox.value()
        cl.curveAttachLocator(int(int_))
 

    def addName(self):
        lis_ = cmds.ls(sl=1)
        ledText = self.ui.nameSpace_LED.text()
        nul = cmds.group(n= ledText+':NUL' , em=1)

        if ledText != None:           
            for i in lis_:
                newI = cmds.rename(i,ledText+':'+i.split('|')[-1])

                topSel = cmds.ls(newI,dag=True,ni=True,l=True,type='transform')
                print topSel
                lenV = len(topSel)
                for na in range(lenV)[1:]:                   
                    #if topSel[na] != '|'+ newI:
                    cmds.rename(topSel[na] , ledText+':'+topSel[na].split('|')[-1])
                    topSel = cmds.ls(newI,dag=True,ni=True,l=True,type='transform')
            cmds.delete(nul)

    def deleteName(self):
        ledText = cmds.ls(sl=1)[0].split(':')[0]
        
        cmds.namespace(mnp=True,rm = ledText)
        
        
    def zeroOut(self):

        list_ = cmds.ls(sl=1)
        for i in list_:
            if cmds.listRelatives(i,p=1):
                try:
                    top = cmds.listRelatives(i,p=1)[0]
                    cmds.parent(i,w=1)
                except:
                    pass   
            else:
                top = None

            sp = i.split('_')[-1]#CON , NUL
            if len(sp) == 3:
                if top and top.split('_')[-1] == 'NUL':
                    spaceList = cmds.ls(i.replace(sp , 'space_*_NUL'))
                    if spaceList:
                        spaceList.sort()
                        recent = spaceList[-1]
                        intA = int( recent.split('_NUL')[0].split('space_')[-1] ) + 1
                        name = i.replace(sp , 'space_%03d_NUL' %intA)
                    else:
                        name = i.replace(sp , 'space_001_NUL')

                else:
                    name = i.replace(sp , 'NUL')
            else:
                nulList = cmds.ls(i+'_*_NUL')
                if not nulList:
                    name = i + '_001_NUL'
                else:
                    nulList.sort()
                    int_ = int(nulList[-1].split('_NUL')[0].split('_')[-1]) + 1
                    name = i + '_%03d_NUL' %int_ 

            nul = cmds.group(n = 'asdgs_xzhbr_xwrbasd_bcxdfwe' ,em=1)#unique name
            if top:
                cmds.parent(nul,top)
            n_nul = cmds.rename(nul,name)

            cmds.select(i,n_nul)
            mel.eval('delete`parentConstraint`')
            cmds.parent(i,n_nul)


    def locatorMatch (self):
        list_ = cmds.ls(sl=1,fl=1)
        curve_ = list_[0].split('.')[0]
        for i in list_:
            if len(i.split('.')) > 1:
                num = i.split('[')[-1].split(']')[0]
                loc = cmds.spaceLocator(n = i.split('.')[0]+'_catch_%s_LOC'%num)[0]
                locShape = cmds.listRelatives(loc , s=1)[0]
                cShape = cmds.listRelatives( curve_, s=1)[0]
                xf = cmds.xform(i,q=True , t=True)
                cmds.xform(loc,t = (xf[0],xf[1],xf[2]))
                cmds.connectAttr(locShape+'.worldPosition[0]' , cShape + '.controlPoints[%s]'%num ,f=True )

            else:
                print '# select curve vertex #'

    def posMatch(self):
        list_ = cmds.ls(sl=1,fl=1)
        for i in list_[1:]:
            
            cmds.select(list_[0],i)
            mel.eval('delete`parentConstraint`')

    def pconstFunc(self):
        list_ = cmds.ls(sl=1,fl=1)
        for i in list_[1:]:

            cmds.parentConstraint(list_[0],i , mo= True)
    def sconstFunc(self):
        list_ = cmds.ls(sl=1,fl=1)
        for i in list_[1:]:

            cmds.scaleConstraint(list_[0],i , mo= True)
    def aconstFunc(self):
        list_ = cmds.ls(sl=1,fl=1)
        for i in list_[1:]:

            cmds.parentConstraint(list_[0],i , mo= True)
            cmds.scaleConstraint(list_[0],i , mo= True)


    def copySkin(self):
        status = self.ui.CSstat_CBX.currentText()
        lis_ = cmds.ls(sl=True)

        if status == 'BBOX':
            # ORIGIN
            topSelA = cmds.ls(lis_[0],dag=1,ni=1,l=1,type='mesh')
            topHiA = cmds.listRelatives(topSelA ,p=1 ,f=1)
        
            # TARGET
            topSelB = cmds.ls(lis_[1],dag=1,ni=1,l=1,type='mesh')
            topHiB = cmds.listRelatives(topSelB ,p=1 ,f=1)
            # FUNC
            for org in topHiA:
                oBB = cmds.xform(org,worldSpace=True ,query = True, boundingBox = True)
                
                oBB_XYZ = [round((oBB[0] + oBB[3]) / 2.0 ,2), round((oBB[1] + oBB[4]) / 2.0,2) , round((oBB[2] + oBB[5]) / 2.0,2)]
                
                print 'obb : ' + str(oBB_XYZ[0])+' , '+str(oBB_XYZ[1])+' , '+str(oBB_XYZ[2])
                
                for tar in topHiB:
                    
                    tBB = cmds.xform(tar,worldSpace=True ,query = True, boundingBox = True)
                    
                    tBB_XYZ = [round((tBB[0] + tBB[3]) / 2.0,2) , round((tBB[1] + tBB[4]) / 2.0,2) , round((tBB[2] + tBB[5]) / 2.0,2)]
                    
                    print 'tbb : ' + str(tBB_XYZ[0]) +' , '+ str(tBB_XYZ[1]) +' , '+ str(tBB_XYZ[2])
                    if oBB_XYZ == tBB_XYZ:
                        
                        lcSC = cmds.listConnections(mel.eval('findRelatedSkinCluster '+ org) + '.matrix')
                        if lcSC:
                            cmds.select(lcSC , tar)
                            mel.eval('SmoothBindSkin;')
                            cmds.select(org,tar)
                            mel.eval('CopySkinWeights;')
                            mel.eval('performCopySkinWeights false;')
                            mel.eval('copySkinWeights  -noMirror -surfaceAssociation closestPoint -influenceAssociation closestJoint;')
                            
                            break
        else:
            ns = lis_[1].split(':')[0]
            # ORIGIN
            topSelA = cmds.ls(lis_[0],dag=1,ni=1,l=1,type='mesh')
            topHiA = cmds.listRelatives(topSelA ,p=1)

            for org in topHiA:
                lcSC = cmds.listConnections(mel.eval('findRelatedSkinCluster '+ org) + '.matrix')
                if lcSC:
                    cmds.select(lcSC , ns+':'+org)
                    mel.eval('SmoothBindSkin;')
                    cmds.select(org, ns+':'+org)
                    mel.eval('CopySkinWeights;')
                    mel.eval('performCopySkinWeights false;')
                    mel.eval('copySkinWeights  -noMirror -surfaceAssociation closestPoint -influenceAssociation closestJoint;')

    def saveUp(self):

        sceneName = cmds.file(q=True,sn=True)

        _list = sceneName.split('/')[-1].split('.')[0].split('_')
        print _list
        if _list:
            for i in _list:
                if i[0] == 'w' and i[1].isdecimal:
                    wname = i
            print wname
            versionUp = int(wname.split('w')[-1])+1
            anotherName = sceneName.replace(wname , 'w%02d' %versionUp)
            cmds.file(rn = anotherName)
            cmds.file(s=True)
        
    def randomColor(self):

        list_ = cmds.ls(sl=1)
        #create shader
        for i,na in enumerate(list_):
            
            sName = 'tw_random_SHD_' + na
            
            if cmds.objExists(sName):
                cmds.setAttr ("%s.colorR" %sName , random.random())
                cmds.setAttr ("%s.colorG" %sName , random.random())
                cmds.setAttr ("%s.colorB" %sName , random.random())
            
            else:
                shader = cmds.shadingNode("lambert" ,asShader = True)
                newShader = cmds.rename(shader,sName)
                cmds.setAttr ("%s.colorR" %newShader , random.random())
                cmds.setAttr ("%s.colorG" %newShader , random.random())
                cmds.setAttr ("%s.colorB" %newShader , random.random())
            
                cmds.select('%s' %na)
                mel.eval('hyperShade -assign "%s";' %newShader)

            cmds.select(list_)                
                
            







        
########################################################UI Start

########################button signal

    

def OPEN():
    global Window
    try:
        Window.close()
        Window.deleteLater()
    except: pass
    Window = rsTool()
    Window.ui.show()
    """
    if (cmds.dockControl(dock_control, q=True, ex=True)):
        cmds.deleteUI(dock_control)
    AllowedAreas = ['right', 'left']
    cmds.dockControl(dock_control,aa=AllowedAreas, a='left', floating=False, content=window_name, label='EX Window')
    """
