#encoding=utf-8
#!/usr/bin/env python

#-------------------------------------------------------------------------------
#
#   Dexter Rigging Team
#
#       yunhyuk.jung
#
#   2017.11.21   ver.1.2.3
#-------------------------------------------------------------------------------

import os
import site
import maya.cmds as cmds
import maya.OpenMayaUI as omui
import maya.mel as mel 
import json
# add sysPath
#site.addsitedir('/dexter/Cache_DATA/CRT/RiggingRnD/baseRig/')

import xml.etree.ElementTree as xml
from cStringIO import StringIO

from Qt import QtGui, QtCore, QtWidgets, load_ui
from Qt.QtGui import *
from Qt.QtCore import *
from Qt.QtWidgets import *

from util.undoCommand import undo 
from util.homeNul import*

# ui Path Setting
basePath = os.path.abspath( __file__ + '/../' )
print basePath
uiFile   = os.path.join( basePath, 'controllerMaker.ui' )
print uiFile

def maya_main_window():
    '''
    Return the Maya main window widget as a Python object
    '''
    main_window_ptr = omui.MQtUtil.mainWindow()
    return wrapInstance(long(main_window_ptr), QtGui.QWidget)

class uiMainWindow( QtWidgets.QMainWindow ):
    def __init__(self, parent=None):
        super(uiMainWindow, self).__init__(parent)
        self.ui = load_ui(uiFile)
        self.ButtonConnection()
        self.makerIcon()
        self.temp_CON = []
        self.mayaFolder = cmds.workspace(q=True, dir=True)
        if self.mayaFolder:
            self.ui.expConPath_LIE.setText( self.mayaFolder )

# buttonAction def Group
    def ButtonConnection(self):
        self.ui.Shape_Replace_BTN.clicked.connect(self.shapeReplace)
        self.ui.Do_Resize_BTN.clicked.connect(self.controllerResize)
        self.ui.FK_Control_Maker_BTN.clicked.connect(self.FKcontrolMaker)
        self.ui.homeNull_BTN.clicked.connect(self.homeNull)
        self.ui.mirrorCon_X_BTN.clicked.connect(self.mirrorControl)
        self.ui.mirrorCon_Y_BTN.clicked.connect(self.mirrorControl)
        self.ui.mirrorCon_Z_BTN.clicked.connect(self.mirrorControl)
        self.ui.rotateCon_X_BTN.clicked.connect(self.rotateControl)
        self.ui.rotateCon_Y_BTN.clicked.connect(self.rotateControl)
        self.ui.rotateCon_Z_BTN.clicked.connect(self.rotateControl)
        self.ui.curveClear_BTN.clicked.connect(self.curveClear)
        self.ui.expConPath_BTN.clicked.connect(self.setMayaFolder)
        self.ui.exportCON_BTN.clicked.connect(self.exportCON_JSON)
        self.ui.importCON_BTN.clicked.connect(self.importCON_JSON)
        self.ui.reset_BTN.clicked.connect(self.resetBTN_cmd)
        self.ui.multiSel_BTN.clicked.connect(self.multiSelhierarchy)
        self.ui.chainParent_BTN.clicked.connect(self.chainParents)
        self.ui.crvConnect_BTN.clicked.connect(self.crvConnect)
        for i in range(1,33):
            eval( "self.ui.color_%s_BTN.clicked.connect(self.overrideColor)" %i )
        for i in range(1,29):
            self.con_Make = '%0*d' % ( 2, i )
            eval( "self.ui.conMake_%s_BTN.clicked.connect(self.controllerMake)" %self.con_Make )

    def makerIcon(self):
        setIconPath = '/dexter/Cache_DATA/CRT/riggingTeamShelf/controllerMaker/icon/'
        self.ui.conMake_01_BTN.setIcon(QtGui.QIcon('%sbox.jpg' %setIconPath))
        self.ui.conMake_02_BTN.setIcon(QtGui.QIcon('%scircle.jpg' %setIconPath))
        self.ui.conMake_03_BTN.setIcon(QtGui.QIcon('%svolumeCircle.jpg' %setIconPath))
        self.ui.conMake_04_BTN.setIcon(QtGui.QIcon('%scross.jpg' %setIconPath))
        self.ui.conMake_05_BTN.setIcon(QtGui.QIcon('%sfatCross.jpg' %setIconPath))
        self.ui.conMake_06_BTN.setIcon(QtGui.QIcon('%slocator.jpg' %setIconPath))
        self.ui.conMake_07_BTN.setIcon(QtGui.QIcon('%ssphere.jpg' %setIconPath))
        self.ui.conMake_08_BTN.setIcon(QtGui.QIcon('%soctagon.jpg' %setIconPath))
        self.ui.conMake_09_BTN.setIcon(QtGui.QIcon('%svolumeOctagon.jpg' %setIconPath))
        self.ui.conMake_10_BTN.setIcon(QtGui.QIcon('%srombus.jpg' %setIconPath))
        self.ui.conMake_11_BTN.setIcon(QtGui.QIcon('%sroot.jpg' %setIconPath))
        self.ui.conMake_12_BTN.setIcon(QtGui.QIcon('%shexagon.jpg' %setIconPath))
        self.ui.conMake_13_BTN.setIcon(QtGui.QIcon('%ssquare.jpg' %setIconPath))
        self.ui.conMake_14_BTN.setIcon(QtGui.QIcon('%spyramid.jpg' %setIconPath))
        self.ui.conMake_15_BTN.setIcon(QtGui.QIcon('%sboxPin.jpg' %setIconPath))
        self.ui.conMake_16_BTN.setIcon(QtGui.QIcon('%spin.jpg' %setIconPath))
        self.ui.conMake_17_BTN.setIcon(QtGui.QIcon('%snone.jpg' %setIconPath))
        self.ui.conMake_18_BTN.setIcon(QtGui.QIcon('%snone.jpg' %setIconPath))
        self.ui.conMake_19_BTN.setIcon(QtGui.QIcon('%snone.jpg' %setIconPath))
        self.ui.conMake_20_BTN.setIcon(QtGui.QIcon('%snone.jpg' %setIconPath))
        self.ui.conMake_21_BTN.setIcon(QtGui.QIcon('%snone.jpg' %setIconPath))
        self.ui.conMake_22_BTN.setIcon(QtGui.QIcon('%snone.jpg' %setIconPath))
        self.ui.conMake_23_BTN.setIcon(QtGui.QIcon('%snone.jpg' %setIconPath))
        self.ui.conMake_24_BTN.setIcon(QtGui.QIcon('%snone.jpg' %setIconPath))
        self.ui.conMake_25_BTN.setIcon(QtGui.QIcon('%snone.jpg' %setIconPath))
        self.ui.conMake_26_BTN.setIcon(QtGui.QIcon('%snone.jpg' %setIconPath))
        self.ui.conMake_27_BTN.setIcon(QtGui.QIcon('%snone.jpg' %setIconPath))
        self.ui.conMake_28_BTN.setIcon(QtGui.QIcon('%snone.jpg' %setIconPath))
        #self.ui.homeNull_BTN.setIcon(QtGui.QIcon('%shomeNull.jpg' %setIconPath))

    def overrideColor(self):
        buttonHandle = self.sender()
        btn = buttonHandle.objectName()
        btn_number = btn.split('_')
        sel_name = cmds.ls(sl=True)
        for i in sel_name:
            if self.ui.viewPort_CKB.isChecked() == True:
                try: 
                    if cmds.listRelatives( i, s=True )[0] != None:
                        sel_Shape = cmds.listRelatives( i, s=True )[0]
                        cmds.setAttr("%s.overrideEnabled" %sel_Shape, 1)
                        cmds.setAttr("%s.overrideColor" %sel_Shape, int(btn_number[1])-1)
                except:
                    cmds.setAttr("%s.overrideEnabled" %i, 1)
                    cmds.setAttr("%s.overrideColor" %i, int(btn_number[1])-1)
            if self.ui.outLiner_CKB.isChecked() == True:
                cmds.setAttr('%s.useOutlinerColor' %i, 1)
                self.outLinerCC(i,btn_number[1])

    def outLinerCC(self,obj,number):
        cc_list = {1:[0.3515, 0.3515, 0.3515],
                   2:[0,0,0],
                   3:[0.0497, 0.0497, 0.0497],
                   4:[0.2122, 0.2122, 0.2122],
                   5:[0.602, 0, 0.039],
                   6:[0, 0.005, 0.458],
                   7:[0, 0.284, 1.000],
                   8:[0, 0.447, 0.067],
                   9:[0.165, 0, 0.503],
                   10:[0.812, 0, 0.812],
                   11:[0.674, 0.170, 0.089],
                   12:[0.503, 0.166, 0.143],
                   13:[0.702, 0.041, 0],
                   14:[1.0000, 0, 0],
                   15:[0, 1.0000, 0],
                   16:[0, 0.198, 0.906],
                   17:[1.0000, 1.0000, 1.0000],
                   18:[1.0000, 1.0000, 0],
                   19:[0.1022, 0.7157, 1.0000],
                   20:[0.0561, 1.0000, 0.3613],
                   21:[1.0000, 0.4286, 0.4286],
                   22:[0.923, 0.495, 0.230],   
                   23:[1.0000, 1.0000, 0.1221],  
                   24:[0, 0.685, 0.186],  
                   25:[0.715, 0.443, 0.0],   
                   26:[0.677, 0.696, 0.058],  
                   27:[0.274, 0.696, 0.058],  
                   28:[0.047, 0.552, 0.171],  
                   29:[0.060, 0.713, 0.713],
                   30:[0.074, 0.341, 0.884],
                   31:[0.477, 0.151, 0.851],
                   32:[0.895, 0.074, 0.355],
                   }
        cmds.setAttr('%s.outlinerColor' %obj ,cc_list[int(number)][0],cc_list[int(number)][1],cc_list[int(number)][2] )

    def resetBTN_cmd(self):
        sel_name = cmds.ls(sl=True)
        for i in sel_name:
            if self.ui.viewPort_CKB.isChecked() == True:
                try: 
                    sel_Shape = cmds.listRelatives( i, s=True )[0]
                    cmds.setAttr("%s.overrideEnabled" %sel_Shape, 0)
                except:
                    cmds.setAttr("%s.overrideEnabled" %i, 0)
            if self.ui.outLiner_CKB.isChecked() == True:
                cmds.setAttr('%s.useOutlinerColor' %i, 0)

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
        fkController = list()
        fkNullGroup = list()
        for i in sel:
            jointName = i
            if len(self.temp_CON) == 1:
                Control = cmds.duplicate(self.temp_CON, n= jointName.replace(jointName.split('_')[-1],'CON'))
            else:
                Control = cmds.circle(nr=(1,0,0),c=(0,0,0),r=1, n= jointName.replace(jointName.split('_')[-1],'CON'))
                cmds.DeleteHistory(Control[0])
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

    def homeNull(self):
        sel = cmds.ls(sl=True)
        for i in sel:
            if 'CON' in i:
                homeNul( i )
            else:
                homeNul( i , i+'_NUL' )

    def crvConnect(self):
        sel = cmds.ls(sl=True)
        startName = sel[0]
        endName = sel[1]
        curveName = cmds.curve( d=1, p=[(0,0,0),(0,0,0)], name = startName.replace( startName.split('_')[-1], 'CRV' ) )
        curveShape = cmds.listRelatives( curveName, s=True )[0]
        curveShapeName = cmds.rename( curveShape, '%sShape' % curveName )
        cvNum = cmds.getAttr( '%s.spans' % curveShapeName ) + cmds.getAttr( '%s.degree' % curveShapeName )
        MMX_list = []
        DCM_list = []
        for x in range( cvNum ):
            # Create Node
            MMX = cmds.createNode( 'multMatrix', n=startName.replace( '_%s' % startName.split('_')[-1], '%s_MMX' % (x+1) ) )
            MMX_list.append(MMX)
            DCM = cmds.createNode( 'decomposeMatrix', n=startName.replace( '_%s' % startName.split('_')[-1], '%s_DCM' % (x+1) ) )
            DCM_list.append(DCM)
        # Connection Node
        cmds.connectAttr( '%s.worldMatrix[0]' % startName, '%s.matrixIn[0]' % MMX_list[0] )
        cmds.connectAttr( '%s.matrixSum' % MMX_list[0], '%s.inputMatrix' % DCM_list[0] )
        cmds.connectAttr( '%s.worldInverseMatrix[0]' % curveName, '%s.matrixIn[1]' % MMX_list[0] )
        cmds.connectAttr( '%s.outputTranslate' % DCM_list[0], '%s.controlPoints[0]' %  curveShapeName )
        cmds.connectAttr( '%s.worldMatrix[0]' % endName, '%s.matrixIn[0]' % MMX_list[1] )
        cmds.connectAttr( '%s.matrixSum' % MMX_list[1], '%s.inputMatrix' % DCM_list[1] )
        cmds.connectAttr( '%s.worldInverseMatrix[0]' % curveName, '%s.matrixIn[1]' % MMX_list[1] )
        cmds.connectAttr( '%s.outputTranslate' % DCM_list[1], '%s.controlPoints[1]' %  curveShapeName )

    def chainParents(self):
        sel = cmds.ls(sl=True)
        for x in range(len(sel)-1):
            cmds.parent(sel[x], sel[x+1])

    def multiSelhierarchy(self):
        sel = cmds.ls(sl=True)
        for i in sel:
            cmds.select("%s" %i, hierarchy=True, add=True )

    @undo
    def controllerResize(self):
        number = float(self.ui.Do_Resize_DSB.text())
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
                for i in XYZ:
                    cmds.setAttr( "%s.scale%s" %(cluster[1],i), nagative_number)
            cmds.DeleteHistory(cmds.select( sel ))
    @undo
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
            if self.ui.mirrorCON_world_RDB.isChecked() == True:
                if btn_XYZ[1] == 'X':
                    tempMirrorJoint2 = cmds.mirrorJoint(i , mxy = True , mirrorBehavior=False , searchReplace=('L_', 'R_'))
                    self.mirrorJointList_add.append(tempMirrorJoint2[0])
                elif btn_XYZ[1] == 'Y':
                    tempMirrorJoint2 = cmds.mirrorJoint(i , myz = True , mirrorBehavior=False , searchReplace=('L_', 'R_'))
                    self.mirrorJointList_add.append(tempMirrorJoint2[0])
                elif btn_XYZ[1] == 'Z':
                    tempMirrorJoint2 = cmds.mirrorJoint(i , mxz = True , mirrorBehavior=False , searchReplace=('L_', 'R_'))
                    self.mirrorJointList_add.append(tempMirrorJoint2[0])
            if self.ui.mirrorCON_behavior_RDB.isChecked() == True:
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
        if len(temp_sel) >= 1: 
            for i in range(len(temp_sel)):
                self.chooseConShape(n)
                selMakeCON = cmds.ls(sl=True)
                cmds.delete(cmds.parentConstraint(temp_sel[i],selMakeCON,mo=0,w=1))
                cmds.rename('%s_CON' %temp_sel[i])
                self.homeNull()
        else:
            self.chooseConShape(n)
            #selMakeCON = cmds.ls(sl=True)
            self.homeNull()
        
    def chooseConShape(self,number):
        # box
        n = number 
        if n == '01':
            mel.eval('curve -d 1 -p 0.5 0.5 0.5 -p 0.5 0.5 -0.5 -p -0.5 0.5 -0.5 -p -0.5 -0.5 -0.5 -p 0.5 -0.5 -0.5 -p 0.5 0.5 -0.5 -p -0.5 0.5 -0.5 -p -0.5 0.5 0.5 -p 0.5 0.5 0.5 -p 0.5 -0.5 0.5 -p 0.5 -0.5 -0.5 -p -0.5 -0.5 -0.5 -p -0.5 -0.5 0.5 -p 0.5 -0.5 0.5 -p -0.5 -0.5 0.5  -p -0.5 0.5 0.5 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 -k 9 -k 10 -k 11 -k 12 -k 13 -k 14 -k 15;')
            self.CON_name = 'box'
        # circle 
        elif n == '02':
            mel.eval('circle -c 0 0 0 -nr 0 1 0 -sw 360 -r 0.5 -d 3 -ut 0 -tol 0.01 -s 8 -ch 0')
            self.CON_name = 'circle'
        # volume circle  
        elif n == '03':
            mel.eval('curve -d 1 -p -0.504004 -0.0167178 -1.8995e-06 -p -0.486389 -0.0167178 0.130304 -p -0.436069 -0.0167178 0.251787 -p -0.356385 -0.0167178 0.356383 -p -0.251789 -0.0167178 0.436067 -p -0.130306 -0.0167178 0.486387 -p 0 -0.0167178 0.504002 -p 0.130306 -0.0167178 0.486387 -p 0.251789 -0.0167178 0.436067 -p 0.356385 -0.0167178 0.356383 -p 0.436069 -0.0167178 0.251787 -p 0.486389 -0.0167178 0.130304 -p 0.504004 -0.0167178 -1.8995e-06  -p 0.486389 -0.0167178 -0.130308 -p 0.436069 -0.0167178 -0.251791 -p 0.356385 -0.0167178 -0.356387 -p 0.251789 -0.0167178 -0.436071 -p 0.130306 -0.0167178 -0.486392 -p 0 -0.0167178 -0.504002 -p -0.130306 -0.0167178 -0.486392 -p -0.251789 -0.0167178 -0.436071 -p -0.356385 -0.0167178 -0.356387 -p -0.436069 -0.0167178 -0.251791 -p -0.486389 -0.0167178 -0.130308 -p -0.504004 -0.0167178 -1.8995e-06 -p -0.504004 0.0167178 -1.8995e-06 -p -0.486389 0.0167178 0.130304 -p -0.436069 0.0167178 0.251787 -p -0.356385 0.0167178 0.356383 -p -0.251789 0.0167178 0.436067 -p -0.130306 0.0167178 0.486387 -p 0 0.0167178 0.504002 -p 0 -0.0167178 0.504002 -p 0 0.0167178 0.504002 -p 0.130306 0.0167178 0.486387 -p 0.251789 0.0167178 0.436067 -p 0.356385 0.0167178 0.356383 -p 0.436069 0.0167178 0.251787 -p 0.486389 0.0167178 0.130304 -p 0.504004 0.0167178 -1.8995e-06 -p 0.504004 -0.0167178 -1.8995e-06 -p 0.504004 0.0167178 -1.8995e-06 -p 0.486389 0.0167178 -0.130308 -p 0.436069 0.0167178 -0.251791 -p 0.356385 0.0167178 -0.356387 -p 0.251789 0.0167178 -0.436071 -p 0.130306 0.0167178 -0.486392 -p 0 0.0167178 -0.504002 -p 0 -0.0167178 -0.504002 -p 0 0.0167178 -0.504002 -p -0.130306 0.0167178 -0.486392 -p -0.251789 0.0167178 -0.436071 -p -0.356385 0.0167178 -0.356387 -p -0.436069 0.0167178 -0.251791 -p -0.486389 0.0167178 -0.130308 -p -0.504004 0.0167178 -1.8995e-06 -p -0.504004 -0.0167178 -1.8995e-06 -p -0.504004 0.0167178 -1.8995e-06;')
            self.CON_name = 'volume circle  '
        # cross
        elif n == '04':
            mel.eval('curve -d 1 -p 0.165 0 0.495 -p 0.165 0 0.165 -p 0.495 0 0.165 -p 0.495 0 -0.165 -p 0.165 0 -0.165 -p 0.165 0 -0.495 -p -0.165 0 -0.495 -p -0.165 0 -0.165 -p -0.495 0 -0.165 -p -0.495 0 0.165 -p -0.165 0 0.165 -p -0.165 0 0.495 -p 0.165 0 0.495;')
            self.CON_name = 'cross'
        # fat cross
        elif n == '05':
            mel.eval('curve -d 1 -p 0.25 0 0.5 -p 0.25 0 0.25 -p 0.5 0 0.25 -p 0.5 0 -0.25 -p 0.25 0 -0.25 -p 0.25 0 -0.5 -p -0.25 0 -0.5 -p -0.25 0 -0.25 -p -0.5 0 -0.25 -p -0.5 0 0.25 -p -0.25 0 0.25 -p -0.25 0 0.5 -p 0.25 0 0.5;')
            self.CON_name = 'fat cross'
        # locator
        elif n == '06':
            mel.eval('curve -d 1 -p 0 0 0 -p 0.5 0 0 -p -0.5 0 0 -p 0 0 0 -p 0 0 0.5 -p 0 0 -0.5 -p 0 0 0 -p 0 -0.5 0 -p 0 0.5 0 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8;')
            self.CON_name = 'locator'
        # sphere
        elif n == '07':
            mel.eval('curve -d 1 -p 0 0 0.5 -p 0.353554 0 0.353554 -p 0.5 0 0 -p 0.353554 0 -0.353554 -p 0 0 -0.5 -p -0.353554 0 -0.353554 -p -0.5 0 0 -p -0.353554 0 0.353554 -p 0 0 0.5 -p 0 0.25 0.433013 -p 0 0.433013 0.25 -p 0 0.5 0 -p 0 0.433013 -0.25 -p 0 0.25 -0.433013 -p 0 0 -0.5 -p 0 -0.25 -0.433013 -p 0 -0.433013 -0.25 -p 0 -0.5 0 -p 0 -0.433013 0.25 -p 0 -0.25 0.433013 -p 0 0 0.5 -p 0.353554 0 0.353554 -p 0.5 0 0 -p 0.433013 0.25 0 -p 0.25 0.433013 0 -p 0 0.5 0 -p -0.25 0.433013 0 -p -0.433013 0.25 0 -p -0.5 0 0 -p -0.433013 -0.25 0 -p -0.25 -0.433013 0 -p 0 -0.5 0 -p 0.25 -0.433013 0 -p 0.433013 -0.25 0 -p 0.5 0 0;')
            self.CON_name = 'sphere'
        # octagon
        elif n == '08':
            mel.eval('curve -d 1 -p 0.246168 0 0.492335 -p 0.492335 0 0.246168 -p 0.492335 0 -0.246168 -p 0.246168 0 -0.492335 -p -0.246168 0 -0.492335 -p -0.492335 0 -0.246168 -p -0.492335 0 0.246168 -p -0.246168 0 0.492335 -p 0.246168 0 0.492335;')
            self.CON_name ='octagon'
        # volume octagon
        elif n == '09':
            mel.eval('curve -d 1 -p 0.246503 -0.044 0.493007 -p 0.493007 -0.044 0.246503 -p 0.493007 -0.044 -0.246503 -p 0.246503 -0.044 -0.493007 -p -0.246503 -0.044 -0.493007 -p -0.493007 -0.044 -0.246503 -p -0.493007 -0.044 0.246503 -p -0.246503 -0.044 0.493007 -p 0.246503 -0.044 0.493007 -p 0.246503 0.044 0.493007 -p 0.493007 0.044 0.246503 -p 0.493007 -0.044 0.246503 -p 0.493007 0.044 0.246503 -p 0.493007 0.044 -0.246503 -p 0.493007 -0.044 -0.246503 -p 0.493007 0.044 -0.246503 -p 0.246503 0.044 -0.493007 -p 0.246503 -0.044 -0.493007 -p 0.246503 0.044 -0.493007 -p -0.246503 0.044 -0.493007 -p -0.246503 -0.044 -0.493007 -p -0.246503 0.044 -0.493007 -p -0.493007 0.044 -0.246503 -p -0.493007 -0.044 -0.246503 -p -0.493007 0.044 -0.246503 -p -0.493007 0.044 0.246503 -p -0.493007 -0.044 0.246503 -p -0.493007 0.044 0.246503 -p -0.246503 0.044 0.493007 -p -0.246503 -0.044 0.493007 -p -0.246503 0.044 0.493007 -p 0.246503 0.044 0.493007 -p 0.246503 -0.044 0.493007;')
            self.CON_name = 'volume octagon'
        # rombus
        elif n == '10':
            mel.eval('curve -d 1 -p 0 0.5 0 -p 0.5 0 0 -p 0 0 0.5 -p -0.5 0 0 -p 0 0 -0.5 -p 0 0.5 0 -p 0 0 0.5 -p 0 -0.5 0 -p 0 0 -0.5 -p 0.5 0 0 -p 0 0.5 0 -p -0.5 0 0 -p 0 -0.5 0 -p 0.5 0 0;')
            self.CON_name = 'rombus'
        # root
        elif n == '11':
            mel.eval('curve -d 3 -p 0 0 0.514016 -p 0.215045 0 0.43009 -p 0.215045 0 0.43009 -p 0.215045 0 0.43009 -p 0.107523 0 0.43009 -p 0.107523 0 0.43009 -p 0.107523 0 0.43009 -p 0.107523 0 0.43009 -p 0.107523 0 0.348839 -p 0.107523 0 0.348839 -p 0.107523 0 0.348839 -p 0.165418 0 0.3301 -p 0.269267 0 0.268173 -p 0.330916 0 0.164045 -p 0.348514 0 0.107561 -p 0.348514 0 0.107561 -p 0.348514 0 0.107561 -p 0.348514 0 0.107561 -p 0.43009 0 0.107523 -p 0.43009 0 0.107523 -p 0.43009 0 0.107523 -p 0.43009 0 0.215045 -p 0.43009 0 0.215045 -p 0.43009 0 0.215045 -p 0.514016 0 0 -p 0.514016 0 0 -p 0.514016 0 0 -p 0.43009 0 -0.215045 -p 0.43009 0 -0.215045 -p 0.43009 0 -0.215045 -p 0.43009 0 -0.215045 -p 0.43009 0 -0.107523 -p 0.43009 0 -0.107523 -p 0.43009 0 -0.107523 -p 0.34749 0 -0.107523 -p 0.34749 0 -0.107523 -p 0.34749 0 -0.107523 -p 0.330753 0 -0.16432 -p 0.268043 0 -0.270089 -p 0.161744 0 -0.33227 -p 0.103842 0 -0.349651 -p 0.103842 0 -0.349651 -p 0.103842 0 -0.349651 -p 0.107523 0 -0.43009 -p 0.107523 0 -0.43009 -p 0.107523 0 -0.43009 -p 0.215045 0 -0.43009 -p 0.215045 0 -0.43009 -p 0.215045 0 -0.43009 -p 0 0 -0.514016 -p 0 0 -0.514016 -p 0 0 -0.514016 -p -0.215045 0 -0.43009 -p -0.215045 0 -0.43009 -p -0.215045 0 -0.43009 -p -0.215045 0 -0.43009 -p -0.107523 0 -0.43009 -p -0.107523 0 -0.43009 -p -0.107523 0 -0.43009 -p -0.107523 0 -0.43009 -p -0.106926 0 -0.348711 -p -0.106926 0 -0.348711 -p -0.106926 0 -0.348711 -p -0.106926 0 -0.348711 -p -0.163653 0 -0.331148 -p -0.268767 0 -0.269043 -p -0.330943 0 -0.163999 -p -0.348078 0 -0.107523 -p -0.348078 0 -0.107523 -p -0.348078 0 -0.107523 -p -0.348078 0 -0.107523 -p -0.43009 0 -0.107523 -p -0.43009 0 -0.107523 -p -0.43009 0 -0.107523 -p -0.43009 0 -0.215045 -p -0.43009 0 -0.215045 -p -0.43009 0 -0.215045 -p -0.43009 0 -0.215045 -p -0.514016 0 0 -p -0.514016 0 0 -p -0.514016 0 0 -p -0.514016 0 0 -p -0.43009 0 0.215045 -p -0.43009 0 0.215045 -p -0.43009 0 0.215045 -p -0.43009 0 0.215045 -p -0.43009 0 0.107523 -p -0.43009 0 0.107523 -p -0.43009 0 0.107523 -p -0.43009 0 0.107523 -p -0.347279 0 0.107523 -p -0.347279 0 0.107523 -p -0.347279 0 0.107523 -p -0.347279 0 0.107523 -p -0.331036 0 0.163843 -p -0.269226 0 0.268353 -p -0.164939 0 0.330385 -p -0.109006 0 0.348061 -p -0.109006 0 0.348061 -p -0.109006 0 0.348061 -p -0.109006 0 0.348061 -p -0.107523 0 0.43009 -p -0.107523 0 0.43009 -p -0.107523 0 0.43009 -p -0.107523 0 0.43009 -p -0.215045 0 0.43009 -p -0.215045 0 0.43009 -p -0.215045 0 0.43009 -p 0 0 0.514016 -p 0 0 0.514016 -p 0 0 0.514016 -p 0 0 0.514016;')
            self.CON_name = 'root'
        # hexagon
        elif n == '12':
            mel.eval('curve -d 1 -p -0.257187 0 0.445461 -p 0.257187 0 0.445461 -p 0.514375 0 2.51218e-07 -p 0.257187 0 -0.445461 -p -0.257187 0 -0.445461 -p -0.514375 0 1.69509e-07 -p -0.257187 0 0.445461;')
            self.CON_name = 'hexagon'
        # square
        elif n == '13':
            mel.eval('curve -d 1 -p -0.5 0 0.5 -p 0.5 0 0.5 -p 0.5 0 -0.5 -p -0.5 0 -0.5 -p -0.5 0 0.5;')
            self.CON_name = 'square'
        # pyramid
        elif n == '14':
            mel.eval('curve -d 1 -p 0 0.405941 -0.405941 -p 0 0.405941 0.405941 -p 0 -0.405941 0.405941 -p 2.029703 0 0 -p 0 0.405941 0.405941 -p 0 0.405941 -0.405941 -p 2.029703 0 0 -p 0 -0.405941 -0.405941 -p 0 0.405941 -0.405941 -p 0 0.405941 0.405941 -p 0 -0.405941 0.405941 -p 0 -0.405941 -0.405941 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 -k 9 -k 10 -k 11 ;')
            self.CON_name = 'pyramid'
        # boxPin
        elif n == '15':
            mel.eval('curve -d 1 -p 0 0.521014 0 -p 0 0.370427 0.150588 -p 0 0.370427 0.301176 -p 0 -0.231927 0.301176 -p 0 -0.231927 -0.301176 -p 0 0.370427 -0.301176 -p 0 0.370427 -0.150588 -p 0 0.521014 0 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 ;')
            self.CON_name = 'boxPin'
        # pin
        elif n == '16':
            mel.eval('curve -d 1 -p 0 -0.402236 0 -p 0 0.330789 0 -p 0 0.351072 0.128059 -p 0 0.409934 0.243582 -p 0 0.501614 0.335262 -p 0 0.617137 0.394124 -p 0 0.745196 0.414406 -p 0 0.873254 0.394124 -p 0 0.988778 0.335262 -p 0 1.080458 0.243582 -p 0 1.13932 0.128059 -p 0 1.159602 0 -p 0 1.13932 -0.128059 -p 0 1.080458 -0.243582 -p 0 0.988778 -0.335262 -p 0 0.873255 -0.394124 -p 0 0.745196 -0.414406 -p 0 0.617137 -0.394124 -p 0 0.501614 -0.335262 -p 0 0.409934 -0.243582 -p 0 0.351072 -0.128059 -p 0 0.330789 0 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 -k 9 -k 10 -k 11 -k 12 -k 13 -k 14 -k 15 -k 16 -k 17 -k 18 -k 19 -k 20 -k 21 ;')
            self.CON_name = 'pin'
        self.ui.curveClear_BTN.setText(self.CON_name)
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
        
    def curveClear(self):
        self.CON_name = 'Controller Maker'
        del self.temp_CON[0:len(self.temp_CON)]
        self.ui.curveClear_BTN.setText(self.CON_name)

    def setFilename(self):
        self.JsonName = str(self.ui.fileName_LIE.text())
        return self.JsonName

    def setMayaFolder(self):
        # #cmds.workspace (dir=startFolder)
        self.mayaFolder = cmds.fileDialog2(fm=3, caption = "Set")[0]
        # print self.mayaFolder
        # # When you press cancel or close, mayaFolder would be None and not running this code.
        if self.mayaFolder:
            #setPath = self.browseForFolderCallback(mayaFolder[0])
            self.ui.expConPath_LIE.setText( self.mayaFolder )

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
            for j in curveShapeKeys:
                controlPoints = self.loadedData[i][j]
                cmds.setAttr("%s.controlPoints[%s].xValue" %(i,j), controlPoints[0])
                cmds.setAttr("%s.controlPoints[%s].yValue" %(i,j), controlPoints[1])
                cmds.setAttr("%s.controlPoints[%s].zValue" %(i,j), controlPoints[2])

#------------------------------------------------------------------------------------------------------------------------

def OPEN():
    global Window
    try:
        Window.close()
        Window.deleteLater()
    except: pass
    Window = uiMainWindow()
    Window.ui.show()
