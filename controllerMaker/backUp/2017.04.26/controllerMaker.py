#encoding=utf-8
#!/usr/bin/env python

#-------------------------------------------------------------------------------
#
#   Dexter Rigging Team
#
#       yunhyuk.jung
#
#   2016.06.03.v01.w12
#-------------------------------------------------------------------------------

import os

from PySide import QtCore, QtGui

from shiboken import wrapInstance

import maya.cmds as cmds
import maya.OpenMayaUI as omui
import maya.mel as mel 
import json

import xml.etree.ElementTree as xml
import pysideuic
from cStringIO import StringIO

# import undoCommand
from util.undoCommand import undo
from util.homeNul import*

# ui Path Setting
basePath = os.path.abspath( __file__ + '/../' )
print basePath
uiFile   = os.path.join( basePath, 'controllerMaker.ui' )
print uiFile

# sys Path setting
# import sys
# scriptDir = '/home/yunhyuk.jung/JYH_Local/Scripts'
# if not scriptDir in sys.path:
#     sys.path.append(scriptDir)

def maya_main_window():
    '''
    Return the Maya main window widget as a Python object
    '''
    main_window_ptr = omui.MQtUtil.mainWindow()
    return wrapInstance(long(main_window_ptr), QtGui.QWidget)

def loadUiType(uiFile):
    """
    Pyside lacks the "loadUiType" command, so we have to convert the ui file to py code in-memory first
    and then execute it in a special frame to retrieve the form_class.
    """
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

        self.ButtonConnection()
        self.makerIcon()
        self.temp_CON = []
        self.mayaFolder = cmds.workspace(q=True, dir=True)
        if self.mayaFolder:
            #setPath = self.browseForFolderCallback(mayaFolder[0])
            self.expConPath_LIE.setText( self.mayaFolder )

# buttonAction def Group
    def ButtonConnection(self):
        self.Shape_Replace_BTN.clicked.connect(self.shapeReplace)
        self.Do_Resize_BTN.clicked.connect(self.controllerResize)
        self.FK_Control_Maker_BTN.clicked.connect(self.FKcontrolMaker)
        self.homeNull_BTN.clicked.connect(self.homeNull)
        self.mirrorCon_X_BTN.clicked.connect(self.mirrorControl)
        self.mirrorCon_Y_BTN.clicked.connect(self.mirrorControl)
        self.mirrorCon_Z_BTN.clicked.connect(self.mirrorControl)
        self.rotateCon_X_BTN.clicked.connect(self.rotateControl)
        self.rotateCon_Y_BTN.clicked.connect(self.rotateControl)
        self.rotateCon_Z_BTN.clicked.connect(self.rotateControl)
        self.curveClear_BTN.clicked.connect(self.curveClear)
        self.expConPath_BTN.clicked.connect(self.setMayaFolder)
        self.exportCON_BTN.clicked.connect(self.exportCON_JSON)
        self.importCON_BTN.clicked.connect(self.importCON_JSON)
        for i in range(1,33):
            eval( "self.color_%s_BTN.clicked.connect(self.overrideColor)" %i )
        for i in range(1,29):
            self.con_Make = '%0*d' % ( 2, i )
            eval( "self.conMake_%s_BTN.clicked.connect(self.controllerMake)" %self.con_Make )

    def makerIcon(self):
        setIconPath = '/dexter/Cache_DATA/CRT/RiggingRnD/baseRig/module/controllerMaker/icon/'
        self.conMake_01_BTN.setIcon(QtGui.QIcon('%sbox.jpg' %setIconPath))
        self.conMake_02_BTN.setIcon(QtGui.QIcon('%scircle.jpg' %setIconPath))
        self.conMake_03_BTN.setIcon(QtGui.QIcon('%svolumeCircle.jpg' %setIconPath))
        self.conMake_04_BTN.setIcon(QtGui.QIcon('%scross.jpg' %setIconPath))
        self.conMake_05_BTN.setIcon(QtGui.QIcon('%sfatCross.jpg' %setIconPath))
        self.conMake_06_BTN.setIcon(QtGui.QIcon('%slocator.jpg' %setIconPath))
        self.conMake_07_BTN.setIcon(QtGui.QIcon('%ssphere.jpg' %setIconPath))
        self.conMake_08_BTN.setIcon(QtGui.QIcon('%soctagon.jpg' %setIconPath))
        self.conMake_09_BTN.setIcon(QtGui.QIcon('%svolumeOctagon.jpg' %setIconPath))
        self.conMake_10_BTN.setIcon(QtGui.QIcon('%srombus.jpg' %setIconPath))
        self.conMake_11_BTN.setIcon(QtGui.QIcon('%sroot.jpg' %setIconPath))
        self.conMake_12_BTN.setIcon(QtGui.QIcon('%shexagon.jpg' %setIconPath))
        self.conMake_13_BTN.setIcon(QtGui.QIcon('%ssquare.jpg' %setIconPath))
        self.conMake_14_BTN.setIcon(QtGui.QIcon('%snone.jpg' %setIconPath))
        self.conMake_15_BTN.setIcon(QtGui.QIcon('%snone.jpg' %setIconPath))
        self.conMake_16_BTN.setIcon(QtGui.QIcon('%snone.jpg' %setIconPath))
        self.conMake_17_BTN.setIcon(QtGui.QIcon('%snone.jpg' %setIconPath))
        self.conMake_18_BTN.setIcon(QtGui.QIcon('%snone.jpg' %setIconPath))
        self.conMake_19_BTN.setIcon(QtGui.QIcon('%snone.jpg' %setIconPath))
        self.conMake_20_BTN.setIcon(QtGui.QIcon('%snone.jpg' %setIconPath))
        self.conMake_21_BTN.setIcon(QtGui.QIcon('%snone.jpg' %setIconPath))
        self.conMake_22_BTN.setIcon(QtGui.QIcon('%snone.jpg' %setIconPath))
        self.conMake_23_BTN.setIcon(QtGui.QIcon('%snone.jpg' %setIconPath))
        self.conMake_24_BTN.setIcon(QtGui.QIcon('%snone.jpg' %setIconPath))
        self.conMake_25_BTN.setIcon(QtGui.QIcon('%snone.jpg' %setIconPath))
        self.conMake_26_BTN.setIcon(QtGui.QIcon('%snone.jpg' %setIconPath))
        self.conMake_27_BTN.setIcon(QtGui.QIcon('%snone.jpg' %setIconPath))
        self.conMake_28_BTN.setIcon(QtGui.QIcon('%snone.jpg' %setIconPath))
        
    def overrideColor(self):
        buttonHandle = self.sender()
        btn = buttonHandle.objectName()
        btn_number = btn.split('_')
        sel_name = cmds.ls(sl=True)
        for i in sel_name:
            colorShape =  i
            sel_Shape = cmds.listRelatives( colorShape, s=True )[0]
            cmds.setAttr("%s.overrideEnabled" %sel_Shape, 1)
            cmds.setAttr("%s.overrideColor" %sel_Shape, int(btn_number[1])-1)

    @undo
    def shapeReplace(self):
        sel = cmds.ls(sl=True)
        sel0_shape = cmds.listRelatives( sel[0], s=True )[0]
        sel1_shape = cmds.listRelatives( sel[1], s=True )[0]
        cmds.parent( sel0_shape , sel[1], r=True, s=True)
        cmds.delete(sel[0])
        cmds.delete(sel1_shape)
        cmds.rename(sel0_shape , "%sShape" %sel[1])

    @undo
    def FKcontrolMaker(self):
        sel = cmds.ls(sl=True)
        fkController = []
        fkNullGroup = []
        print self.temp_CON
        for i in sel:
            jointName = i
            if len(self.temp_CON) == 1:
                Control = cmds.duplicate(self.temp_CON, n= jointName.replace(jointName.split('_')[-1],'CON'))
                print Control
            else:
                Control = cmds.circle(nr=(1,0,0),c=(0,0,0),r=1, n= jointName.replace(jointName.split('_')[-1],'CON'))
                cmds.DeleteHistory(Control[0])
                print Control
            cmds.setAttr("%sShape.overrideEnabled" %Control[0], 1)
            cmds.setAttr("%sShape.overrideColor" %Control[0], 17)
            cmds.DeleteHistory(Control[0])
            cmds.group( Control[0] )
            nullGroup = (cmds.rename(jointName.replace(jointName.split('_')[-1],'NUL')))
            fkController.append("%s" %Control[0])
            fkNullGroup.append("%s" %nullGroup)
            cmds.delete(cmds.parentConstraint(jointName,nullGroup, w=True))
        for x in range(len(sel)-1):
            q = -1-x
            k = -2-x
            cmds.parent(fkNullGroup[q], fkController[k])
        for y in range(len(sel)):
            cmds.parentConstraint(fkController[y], sel[y], mo=1 , w=1)

    @undo
    def homeNull(self):
        sel = cmds.ls(sl=True)
        for i in sel:
            print i 
            if 'CON' in i:
                homeNul( i )
            else:
                homeNul( i , i+'_NUL' )

    @undo
    def controllerResize(self):
        number = float(self.Do_Resize_DSB.text())
        XYZ = ["X","Y","Z"]
        sel = cmds.ls(sl=True)
        for x in sel:
            curveName = x
            curveShape = cmds.listRelatives( curveName, s=True )[0]
            cvNum = cmds.getAttr( '%s.spans' % curveShape ) + cmds.getAttr( '%s.degree' % curveShape )
            conPivot = cmds.xform("%s" %curveName, q=True, ws=True, rp=True)
            cmds.select( "%s.cv[0:%s]" %(curveName,cvNum))
            cluster = cmds.cluster()
            cmds.move( conPivot[0], conPivot[1], conPivot[2], "%s.scalePivot" %cluster[1] , "%s.rotatePivot" %cluster[1],absolute=True)
            if number > 0:
                for i in XYZ:
                    cmds.setAttr( "%s.scale%s" %(cluster[1],i), number)
            else:
                nagative_number = 1 - number*(-0.1)
                print nagative_number
                for i in XYZ:
                    cmds.setAttr( "%s.scale%s" %(cluster[1],i), nagative_number)
            cmds.DeleteHistory(cmds.select( sel ))

    def mirrorControl(self):
        self.mirrorJointList=[]
        self.mirrorJointList_add=[]
        self.parentGroupList=[]
        sel_re = []
        sel=cmds.ls(sl=True)
        for k in sel:
            tempParentGroupList = cmds.listRelatives( k, allParents=True )
            self.parentGroupList.append(tempParentGroupList)
        for i in sel:
            cmds.select(cl=True)
            cmds.select(i ,r=True)
            tempMirrorJoint = cmds.joint(n='%s_temp_JNT' %i )
            cmds.parent(tempMirrorJoint , w=True)
            cmds.parent(i , tempMirrorJoint)
            self.mirrorJointList.append(tempMirrorJoint)
        #  미러조인트 방법이랑 방향 가져와서 세팅     
        buttonXYZ = self.sender()
        btn = buttonXYZ.objectName()
        btn_XYZ = btn.split('_')

        for i in self.mirrorJointList:
            if self.mirrorCON_world_RDB.isChecked() == True:
                if btn_XYZ[1] == 'X':
                    tempMirrorJoint2 = cmds.mirrorJoint(i , mxy = True , mirrorBehavior=False , searchReplace=('L_', 'R_'))
                    self.mirrorJointList_add.append(tempMirrorJoint2[0])
                elif btn_XYZ[1] == 'Y':
                    tempMirrorJoint2 = cmds.mirrorJoint(i , myz = True , mirrorBehavior=False , searchReplace=('L_', 'R_'))
                    self.mirrorJointList_add.append(tempMirrorJoint2[0])
                elif btn_XYZ[1] == 'Z':
                    tempMirrorJoint2 = cmds.mirrorJoint(i , mxz = True , mirrorBehavior=False , searchReplace=('L_', 'R_'))
                    self.mirrorJointList_add.append(tempMirrorJoint2[0])
            if self.mirrorCON_behavior_RDB.isChecked() == True:
                if btn_XYZ[1] == 'X':
                    tempMirrorJoint2 = cmds.mirrorJoint(i , mxy = True , mirrorBehavior=True , searchReplace=('L_', 'R_'))
                    self.mirrorJointList_add.append(tempMirrorJoint2[0])
                elif btn_XYZ[1] == 'Y':
                    tempMirrorJoint2 = cmds.mirrorJoint(i , myz = True , mirrorBehavior=True , searchReplace=('L_', 'R_'))
                    self.mirrorJointList_add.append(tempMirrorJoint2[0])
                elif btn_XYZ[1] == 'Z':
                    tempMirrorJoint2 = cmds.mirrorJoint(i , mxz = True , mirrorBehavior=True , searchReplace=('L_', 'R_'))
                    self.mirrorJointList_add.append(tempMirrorJoint2[0])
        cmds.ungroup(self.mirrorJointList_add)
        cmds.ungroup(self.mirrorJointList)

    def rotateControl(self):
        buttonXYZ = self.sender()
        btn = buttonXYZ.objectName()
        btn_XYZ = btn.split('_')
        sel = cmds.ls(sl=True)
        for i in sel:
            curveName = i
            curveShape = cmds.listRelatives( curveName, s=True )[0]
            cvNum = cmds.getAttr( '%s.spans' % curveShape ) + cmds.getAttr( '%s.degree' % curveShape )
            cmds.select( "%s.cv[0:%s]" %(curveName,cvNum))
            if btn_XYZ[1] == 'X':
                cmds.rotate(90,0,0,r=True,os =True)
            elif btn_XYZ[1] == 'Y':
                cmds.rotate(0,90,0,r=True,os =True)
            elif btn_XYZ[1] == 'Z':
                cmds.rotate(0,0,90,r=True,os =True)
        cmds.select(cl=True)      
        for i in sel:
            cmds.select(i,tgl=True)

    def controllerMake(self):
        temp_sel = cmds.ls(sl=True)
        buttonHandle = self.sender()
        btn = buttonHandle.objectName()
        btn_number = btn.split('_')
        n = btn_number[1]
        # box
        if n == '01':
            mel.eval('curve -d 1 -p 0.5 0.5 0.5 -p 0.5 0.5 -0.5 -p -0.5 0.5 -0.5 -p -0.5 -0.5 -0.5 -p 0.5 -0.5 -0.5 -p 0.5 0.5 -0.5 -p -0.5 0.5 -0.5 -p -0.5 0.5 0.5 -p 0.5 0.5 0.5 -p 0.5 -0.5 0.5 -p 0.5 -0.5 -0.5 -p -0.5 -0.5 -0.5 -p -0.5 -0.5 0.5 -p 0.5 -0.5 0.5 -p -0.5 -0.5 0.5  -p -0.5 0.5 0.5 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 -k 9 -k 10 -k 11 -k 12 -k 13 -k 14 -k 15;')
            self.temp_CON_name = 'box'
        # circle 
        elif n == '02':
            mel.eval('circle -c 0 0 0 -nr 0 1 0 -sw 360 -r 0.5 -d 3 -ut 0 -tol 0.01 -s 8 -ch 0')
            self.temp_CON_name = 'circle'
        # volume circle  
        elif n == '03':
            mel.eval('curve -d 1 -p -0.504004 -0.0167178 -1.8995e-06 -p -0.486389 -0.0167178 0.130304 -p -0.436069 -0.0167178 0.251787 -p -0.356385 -0.0167178 0.356383 -p -0.251789 -0.0167178 0.436067 -p -0.130306 -0.0167178 0.486387 -p 0 -0.0167178 0.504002 -p 0.130306 -0.0167178 0.486387 -p 0.251789 -0.0167178 0.436067 -p 0.356385 -0.0167178 0.356383 -p 0.436069 -0.0167178 0.251787 -p 0.486389 -0.0167178 0.130304 -p 0.504004 -0.0167178 -1.8995e-06  -p 0.486389 -0.0167178 -0.130308 -p 0.436069 -0.0167178 -0.251791 -p 0.356385 -0.0167178 -0.356387 -p 0.251789 -0.0167178 -0.436071 -p 0.130306 -0.0167178 -0.486392 -p 0 -0.0167178 -0.504002 -p -0.130306 -0.0167178 -0.486392 -p -0.251789 -0.0167178 -0.436071 -p -0.356385 -0.0167178 -0.356387 -p -0.436069 -0.0167178 -0.251791 -p -0.486389 -0.0167178 -0.130308 -p -0.504004 -0.0167178 -1.8995e-06 -p -0.504004 0.0167178 -1.8995e-06 -p -0.486389 0.0167178 0.130304 -p -0.436069 0.0167178 0.251787 -p -0.356385 0.0167178 0.356383 -p -0.251789 0.0167178 0.436067 -p -0.130306 0.0167178 0.486387 -p 0 0.0167178 0.504002 -p 0 -0.0167178 0.504002 -p 0 0.0167178 0.504002 -p 0.130306 0.0167178 0.486387 -p 0.251789 0.0167178 0.436067 -p 0.356385 0.0167178 0.356383 -p 0.436069 0.0167178 0.251787 -p 0.486389 0.0167178 0.130304 -p 0.504004 0.0167178 -1.8995e-06 -p 0.504004 -0.0167178 -1.8995e-06 -p 0.504004 0.0167178 -1.8995e-06 -p 0.486389 0.0167178 -0.130308 -p 0.436069 0.0167178 -0.251791 -p 0.356385 0.0167178 -0.356387 -p 0.251789 0.0167178 -0.436071 -p 0.130306 0.0167178 -0.486392 -p 0 0.0167178 -0.504002 -p 0 -0.0167178 -0.504002 -p 0 0.0167178 -0.504002 -p -0.130306 0.0167178 -0.486392 -p -0.251789 0.0167178 -0.436071 -p -0.356385 0.0167178 -0.356387 -p -0.436069 0.0167178 -0.251791 -p -0.486389 0.0167178 -0.130308 -p -0.504004 0.0167178 -1.8995e-06 -p -0.504004 -0.0167178 -1.8995e-06 -p -0.504004 0.0167178 -1.8995e-06;')
            self.temp_CON_name = 'volume circle  '
        # cross
        elif n == '04':
            mel.eval('curve -d 1 -p 0.165 0 0.495 -p 0.165 0 0.165 -p 0.495 0 0.165 -p 0.495 0 -0.165 -p 0.165 0 -0.165 -p 0.165 0 -0.495 -p -0.165 0 -0.495 -p -0.165 0 -0.165 -p -0.495 0 -0.165 -p -0.495 0 0.165 -p -0.165 0 0.165 -p -0.165 0 0.495 -p 0.165 0 0.495;')
            self.temp_CON_name = 'cross'
        # fat cross
        elif n == '05':
            mel.eval('curve -d 1 -p 0.25 0 0.5 -p 0.25 0 0.25 -p 0.5 0 0.25 -p 0.5 0 -0.25 -p 0.25 0 -0.25 -p 0.25 0 -0.5 -p -0.25 0 -0.5 -p -0.25 0 -0.25 -p -0.5 0 -0.25 -p -0.5 0 0.25 -p -0.25 0 0.25 -p -0.25 0 0.5 -p 0.25 0 0.5;')
            self.temp_CON_name = 'fat cross'
        # locator
        elif n == '06':
            mel.eval('curve -d 1 -p 0 0 0 -p 0.5 0 0 -p -0.5 0 0 -p 0 0 0 -p 0 0 0.5 -p 0 0 -0.5 -p 0 0 0 -p 0 -0.5 0 -p 0 0.5 0 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8;')
            self.temp_CON_name = 'locator'
        # sphere
        elif n == '07':
            mel.eval('curve -d 1 -p 0 0 0.5 -p 0.353554 0 0.353554 -p 0.5 0 0 -p 0.353554 0 -0.353554 -p 0 0 -0.5 -p -0.353554 0 -0.353554 -p -0.5 0 0 -p -0.353554 0 0.353554 -p 0 0 0.5 -p 0 0.25 0.433013 -p 0 0.433013 0.25 -p 0 0.5 0 -p 0 0.433013 -0.25 -p 0 0.25 -0.433013 -p 0 0 -0.5 -p 0 -0.25 -0.433013 -p 0 -0.433013 -0.25 -p 0 -0.5 0 -p 0 -0.433013 0.25 -p 0 -0.25 0.433013 -p 0 0 0.5 -p 0.353554 0 0.353554 -p 0.5 0 0 -p 0.433013 0.25 0 -p 0.25 0.433013 0 -p 0 0.5 0 -p -0.25 0.433013 0 -p -0.433013 0.25 0 -p -0.5 0 0 -p -0.433013 -0.25 0 -p -0.25 -0.433013 0 -p 0 -0.5 0 -p 0.25 -0.433013 0 -p 0.433013 -0.25 0 -p 0.5 0 0;')
            self.temp_CON_name = 'sphere'
        # octagon
        elif n == '08':
            mel.eval('curve -d 1 -p 0.246168 0 0.492335 -p 0.492335 0 0.246168 -p 0.492335 0 -0.246168 -p 0.246168 0 -0.492335 -p -0.246168 0 -0.492335 -p -0.492335 0 -0.246168 -p -0.492335 0 0.246168 -p -0.246168 0 0.492335 -p 0.246168 0 0.492335;')
            self.temp_CON_name ='octagon'
        # volume octagon
        elif n == '09':
            mel.eval('curve -d 1 -p 0.246503 -0.044 0.493007 -p 0.493007 -0.044 0.246503 -p 0.493007 -0.044 -0.246503 -p 0.246503 -0.044 -0.493007 -p -0.246503 -0.044 -0.493007 -p -0.493007 -0.044 -0.246503 -p -0.493007 -0.044 0.246503 -p -0.246503 -0.044 0.493007 -p 0.246503 -0.044 0.493007 -p 0.246503 0.044 0.493007 -p 0.493007 0.044 0.246503 -p 0.493007 -0.044 0.246503 -p 0.493007 0.044 0.246503 -p 0.493007 0.044 -0.246503 -p 0.493007 -0.044 -0.246503 -p 0.493007 0.044 -0.246503 -p 0.246503 0.044 -0.493007 -p 0.246503 -0.044 -0.493007 -p 0.246503 0.044 -0.493007 -p -0.246503 0.044 -0.493007 -p -0.246503 -0.044 -0.493007 -p -0.246503 0.044 -0.493007 -p -0.493007 0.044 -0.246503 -p -0.493007 -0.044 -0.246503 -p -0.493007 0.044 -0.246503 -p -0.493007 0.044 0.246503 -p -0.493007 -0.044 0.246503 -p -0.493007 0.044 0.246503 -p -0.246503 0.044 0.493007 -p -0.246503 -0.044 0.493007 -p -0.246503 0.044 0.493007 -p 0.246503 0.044 0.493007 -p 0.246503 -0.044 0.493007;')
            self.temp_CON_name = 'volume octagon'
        # rombus
        elif n == '10':
            mel.eval('curve -d 1 -p 0 0.5 0 -p 0.5 0 0 -p 0 0 0.5 -p -0.5 0 0 -p 0 0 -0.5 -p 0 0.5 0 -p 0 0 0.5 -p 0 -0.5 0 -p 0 0 -0.5 -p 0.5 0 0 -p 0 0.5 0 -p -0.5 0 0 -p 0 -0.5 0 -p 0.5 0 0;')
            self.temp_CON_name = 'rombus'
        # root
        elif n == '11':
            mel.eval('curve -d 3 -p 0 0 0.514016 -p 0.215045 0 0.43009 -p 0.215045 0 0.43009 -p 0.215045 0 0.43009 -p 0.107523 0 0.43009 -p 0.107523 0 0.43009 -p 0.107523 0 0.43009 -p 0.107523 0 0.43009 -p 0.107523 0 0.348839 -p 0.107523 0 0.348839 -p 0.107523 0 0.348839 -p 0.165418 0 0.3301 -p 0.269267 0 0.268173 -p 0.330916 0 0.164045 -p 0.348514 0 0.107561 -p 0.348514 0 0.107561 -p 0.348514 0 0.107561 -p 0.348514 0 0.107561 -p 0.43009 0 0.107523 -p 0.43009 0 0.107523 -p 0.43009 0 0.107523 -p 0.43009 0 0.215045 -p 0.43009 0 0.215045 -p 0.43009 0 0.215045 -p 0.514016 0 0 -p 0.514016 0 0 -p 0.514016 0 0 -p 0.43009 0 -0.215045 -p 0.43009 0 -0.215045 -p 0.43009 0 -0.215045 -p 0.43009 0 -0.215045 -p 0.43009 0 -0.107523 -p 0.43009 0 -0.107523 -p 0.43009 0 -0.107523 -p 0.34749 0 -0.107523 -p 0.34749 0 -0.107523 -p 0.34749 0 -0.107523 -p 0.330753 0 -0.16432 -p 0.268043 0 -0.270089 -p 0.161744 0 -0.33227 -p 0.103842 0 -0.349651 -p 0.103842 0 -0.349651 -p 0.103842 0 -0.349651 -p 0.107523 0 -0.43009 -p 0.107523 0 -0.43009 -p 0.107523 0 -0.43009 -p 0.215045 0 -0.43009 -p 0.215045 0 -0.43009 -p 0.215045 0 -0.43009 -p 0 0 -0.514016 -p 0 0 -0.514016 -p 0 0 -0.514016 -p -0.215045 0 -0.43009 -p -0.215045 0 -0.43009 -p -0.215045 0 -0.43009 -p -0.215045 0 -0.43009 -p -0.107523 0 -0.43009 -p -0.107523 0 -0.43009 -p -0.107523 0 -0.43009 -p -0.107523 0 -0.43009 -p -0.106926 0 -0.348711 -p -0.106926 0 -0.348711 -p -0.106926 0 -0.348711 -p -0.106926 0 -0.348711 -p -0.163653 0 -0.331148 -p -0.268767 0 -0.269043 -p -0.330943 0 -0.163999 -p -0.348078 0 -0.107523 -p -0.348078 0 -0.107523 -p -0.348078 0 -0.107523 -p -0.348078 0 -0.107523 -p -0.43009 0 -0.107523 -p -0.43009 0 -0.107523 -p -0.43009 0 -0.107523 -p -0.43009 0 -0.215045 -p -0.43009 0 -0.215045 -p -0.43009 0 -0.215045 -p -0.43009 0 -0.215045 -p -0.514016 0 0 -p -0.514016 0 0 -p -0.514016 0 0 -p -0.514016 0 0 -p -0.43009 0 0.215045 -p -0.43009 0 0.215045 -p -0.43009 0 0.215045 -p -0.43009 0 0.215045 -p -0.43009 0 0.107523 -p -0.43009 0 0.107523 -p -0.43009 0 0.107523 -p -0.43009 0 0.107523 -p -0.347279 0 0.107523 -p -0.347279 0 0.107523 -p -0.347279 0 0.107523 -p -0.347279 0 0.107523 -p -0.331036 0 0.163843 -p -0.269226 0 0.268353 -p -0.164939 0 0.330385 -p -0.109006 0 0.348061 -p -0.109006 0 0.348061 -p -0.109006 0 0.348061 -p -0.109006 0 0.348061 -p -0.107523 0 0.43009 -p -0.107523 0 0.43009 -p -0.107523 0 0.43009 -p -0.107523 0 0.43009 -p -0.215045 0 0.43009 -p -0.215045 0 0.43009 -p -0.215045 0 0.43009 -p 0 0 0.514016 -p 0 0 0.514016 -p 0 0 0.514016 -p 0 0 0.514016;')
            self.temp_CON_name = 'root'
        # hexagon
        elif n == '12':
            mel.eval('curve -d 1 -p -0.257187 0 0.445461 -p 0.257187 0 0.445461 -p 0.514375 0 2.51218e-07 -p 0.257187 0 -0.445461 -p -0.257187 0 -0.445461 -p -0.514375 0 1.69509e-07 -p -0.257187 0 0.445461;')
            self.temp_CON_name = 'hexagon'
        # square
        elif n == '13':
            mel.eval('curve -d 1 -p -0.5 0 0.5 -p 0.5 0 0.5 -p 0.5 0 -0.5 -p -0.5 0 -0.5 -p -0.5 0 0.5;')
            self.temp_CON_name = 'square'
        # pyramid Arrow
        elif i == '14':
            cmds.curve( d=1 , p =[(5, 0, 0),( 0, 1, -1 ),( 0, 1, 1 ),( 5 ,0, 0 ),( 0 ,-1, 1 ),( 0, 1, 1 ),( 0, 1, -1 ),( 0, -1, -1 ),( 0, -1, 1 ),( 0, -1, -1 ),( 5, 0, 0 )],  k = [0,1,2,3,4,5,6,7,8,9,10] )
            self.temp_CON_name = 'pyramid'
        # elif i == '15':
        #     cmds.circle(nr=(1,0,0), sw=360, r=1, d=3 , ut=0, s=8, ch=1)
        # elif i == '16':
        #     cmds.circle(nr=(1,0,0), sw=360, r=1, d=3 , ut=0, s=8, ch=1)
        # elif i == '17':
        #     cmds.circle(nr=(1,0,0), sw=360, r=1, d=3 , ut=0, s=8, ch=1)
        # elif i == '18':
        #     cmds.circle(nr=(1,0,0), sw=360, r=1, d=3 , ut=0, s=8, ch=1)
        # elif i == '19':
        #     cmds.circle(nr=(1,0,0), sw=360, r=1, d=3 , ut=0, s=8, ch=1)
        # elif i == '20':
        #     cmds.circle(nr=(1,0,0), sw=360, r=1, d=3 , ut=0, s=8, ch=1)
        # elif i == '21':
        #     cmds.circle(nr=(1,0,0), sw=360, r=1, d=3 , ut=0, s=8, ch=1)
        # elif i == '22':
        #     cmds.circle(nr=(1,0,0), sw=360, r=1, d=3 , ut=0, s=8, ch=1)
        # elif i == '23':
        #     cmds.circle(nr=(1,0,0), sw=360, r=1, d=3 , ut=0, s=8, ch=1)
        # pyramid
        # elif n == '24':
        #     cmds.curve( d=1 , p =[(5, 0, 0),( 0, 1, -1 ),( 0, 1, 1 ),( 5 ,0, 0 ),( 0 ,-1, 1 ),( 0, 1, 1 ),( 0, 1, -1 ),( 0, -1, -1 ),( 0, -1, 1 ),( 0, -1, -1 ),( 5, 0, 0 )],  k = [0,1,2,3,4,5,6,7,8,9,10] )
        # # half arrow
        # elif n == '25':
        #     cmds.curve( d=1 , p =[(0, 0, 0 ),( 0, -1, 0 ),( 0.35, -0.4, 0 ),( 0, -0.4, 0 )],  k = [0,1,2,3] )
        # # fat arrow
        # elif n == '26':
        #     cmds.curve( d=1 , p =[(1.5 ,0, 0),( 0.9, 0.3, 0),( 0.9 ,0.15, 0 ),( 0 ,0.15, 0 ),( 0 ,-0.15, 0 ),( 0.9 ,-0.15, 0 ),( 0.9, -0.3, 0 ),( 1.5, 0, 0)],  k = [0,1,2,3,4,5,6,7] )
        # # circle2
        # elif n == '27':
        #     cmds.circle(nr=(1,0,0), sw=360, r=1, d=3 , ut=0, s=8, ch=1)
        # # box2
        # elif n == '28':
        #     cmds.curve( d=1, p =[(-1,-1,-1),(-1,-1,1),(1,-1,1),(1,-1,-1),(-1,-1,-1),(-1,1,-1),(-1,1,1),(-1,-1,1),(1,-1,1),(1,1,1),(-1,1,1),(-1,1,-1),(1,1,-1),(1,1,1),(1,-1,1),(1,-1,-1),(1,1,-1)], k =[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16] )
        self.temp_CON = cmds.ls(sl=True)
        self.curveClear_BTN.setText(self.temp_CON_name)

        if len(temp_sel) == 1:
            cmds.delete(cmds.parentConstraint(temp_sel,self.temp_CON,mo=0,w=1)) 

    def curveClear(self):
        self.temp_CON_name = 'Controller Maker'
        del self.temp_CON[0:len(self.temp_CON)]
        self.curveClear_BTN.setText(self.temp_CON_name)

    def setFilename(self):
        self.JsonName = str(self.fileName_LIE.text())
        return self.JsonName

    def setMayaFolder(self):
        # #cmds.workspace (dir=startFolder)
        self.mayaFolder = cmds.fileDialog2(fm=3, caption = "Set")[0]
        # print self.mayaFolder
        # # When you press cancel or close, mayaFolder would be None and not running this code.
        if self.mayaFolder:
            #setPath = self.browseForFolderCallback(mayaFolder[0])
            self.expConPath_LIE.setText( self.mayaFolder )

    def makeCurveDic(self):
        self.curveDic = {}
        selCurveShape = cmds.ls(sl=True, dag=True, ni=True, type='nurbsCurve')
        cvCountList = []
        for i in range(len(selCurveShape)):
            if cmds.getAttr('%s.f' %selCurveShape[i])==2:
                cvCount = cmds.getAttr( '%s.spans' %selCurveShape[i]) 
            else:
                cvCount = cmds.getAttr( '%s.spans' %selCurveShape[i]) + cmds.getAttr( '%s.degree' % selCurveShape[i] )
            cvCountList.append( cvCount )
        count = 0
        while count < len( cvCountList ):
            self.curveDic[selCurveShape[count]] = {}
            for cvNum in range( cvCountList[count]):
                cvPosition = cmds.pointPosition( '%s.cv[%s]' %( selCurveShape[count], cvNum ) ,l=True)
                self.curveDic[selCurveShape[count]][cvNum] = cvPosition
            count = count + 1 

    def exportCON_JSON(self):
        self.setFilename()
        self.makeCurveDic()
        filePath = self.mayaFolder +'/'+ self.JsonName +'.json'
        # write
        F = open( filePath, 'w' )
        F.write(json.dumps( self.curveDic, indent = 4 ))
        F.close() 

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
            curveShapeKeys = self.loadedData[i].keys()
            print i
            for j in curveShapeKeys:
                print j
                controlPoints = self.loadedData[i][j]
                print controlPoints
                cmds.setAttr("%s.controlPoints[%s].xValue" %(i,j), controlPoints[0])
                cmds.setAttr("%s.controlPoints[%s].yValue" %(i,j), controlPoints[1])
                cmds.setAttr("%s.controlPoints[%s].zValue" %(i,j), controlPoints[2])

#------------------------------------------------------------------------------------------------------------------------

def OPEN():
    window_name     = 'Controller Maker'
    dock_control     = 'Controller Maker Dock'
    if cmds.window( window_name, exists=True ):
        cmds.deleteUI( window_name )
    Window = uiMainWindow()
    Window.show()
    Window.setObjectName(window_name)

    # ----- DOCK -----
    # if (cmds.dockControl(dock_control, q=True, ex=True)):
    #     cmds.deleteUI(dock_control)
    # AllowedAreas = ['right', 'left']
    # cmds.dockControl(dock_control,aa=AllowedAreas, a='left', floating=False, content=window_name, label='Controller Maker')

