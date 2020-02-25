#encoding=utf-8
#!/usr/bin/env python

#-------------------------------------------------------------------------------
#
#   Dexter Rigging Team
#
#       yunhyuk.jung
#
#   2015.12.23.v01.w03
#-------------------------------------------------------------------------------

import os

from PySide import QtCore, QtGui

from shiboken import wrapInstance

import maya.cmds as cmds
import maya.OpenMayaUI as omui


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

#sys Path setting
import sys
scriptDir = '/home/yunhyuk.jung/JYH_Local/Scripts'
if not scriptDir in sys.path:
    sys.path.append(scriptDir)

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

# buttonAction def Group
    def ButtonConnection(self):
        self.Shape_Replace_BTN.clicked.connect(self.shapeReplace)
        self.Do_Resize_BTN.clicked.connect(self.controllerResize)
        self.FK_Control_Maker_BTN.clicked.connect(self.FKcontrolMaker)
        self.homeNull_BTN.clicked.connect(self.homeNull)
        for i in range(1,33):
            eval( "self.color_%s_BTN.clicked.connect(self.overrideColor)" %i )
        for i in range(1,29):
            eval( "self.conMake_%s_BTN.clicked.connect(self.controllerMake)" %i )

    def overrideColor(self):
        buttonHandle = self.sender()
        btn = buttonHandle.objectName()
        print btn
        btn_number = btn.split('_')
        print btn_number
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

        for i in sel:
            jointName = i
            Control = cmds.circle(nr=(1,0,0),c=(0,0,0),r=1, n= jointName.replace(jointName.split('_')[-1],'CON'))
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
        homeNul( sel[0] , sel[0]+"_NUL")

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

    def controllerMake(self):
        buttonHandle = self.sender()
        btn = buttonHandle.objectName()
        btn_number = btn.split('_')
        n = btn_number[1]

        for i in n:
            # arrow
            if i == '1':
                cmds.curve( d=1 , p =[(5, 0, 0),( 0, 1, -1 ),( 0, 1, 1 ),( 5 ,0, 0 ),( 0 ,-1, 1 ),( 0, 1, 1 ),( 0, 1, -1 ),( 0, -1, -1 ),( 0, -1, 1 ),( 0, -1, -1 ),( 5, 0, 0 )],  k = [0,1,2,3,4,5,6,7,8,9,10] )
            elif i == '2':
                cmds.curve( d=1 , p =[(0, 0, 0 ),( 0, -1, 0 ),( 0.35, -0.4, 0 ),( 0, -0.4, 0 )],  k = [0,1,2,3] )
            elif i == '3':
                cmds.curve( d=1 , p =[(1.5 ,0, 0),( 0.9, 0.3, 0),( 0.9 ,0.15, 0 ),( 0 ,0.15, 0 ),( 0 ,-0.15, 0 ),( 0.9 ,-0.15, 0 ),( 0.9, -0.3, 0 ),( 1.5, 0, 0)],  k = [0,1,2,3,4,5,6,7] )
            # circle
            elif i == '4':
                cmds.circle(nr=(1,0,0), sw=360, r=1, d=3 , ut=0, s=8, ch=1)
            # box
            elif i == '5':
                cmds.curve( d=1, p =[(-1,-1,-1),(-1,-1,1),(1,-1,1),(1,-1,-1),(-1,-1,-1),(-1,1,-1),(-1,1,1),(-1,-1,1),(1,-1,1),(1,1,1),(-1,1,1),(-1,1,-1),(1,1,-1),(1,1,1),(1,-1,1),(1,-1,-1),(1,1,-1)], k =[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16] )

            # # need EDIT low
            # elif i == 6:
            #     cmds.circle(nr=(1,0,0), sw=360, r=1, d=3 , ut=0, s=8, ch=1)
            # elif i == 7:
            #     cmds.circle(nr=(1,0,0), sw=360, r=1, d=3 , ut=0, s=8, ch=1)
            # elif i == 8:
            #     cmds.circle(nr=(1,0,0), sw=360, r=1, d=3 , ut=0, s=8, ch=1)
            # elif i == 9:
            #     cmds.circle(nr=(1,0,0), sw=360, r=1, d=3 , ut=0, s=8, ch=1)
            # elif i == 10:
            #     cmds.circle(nr=(1,0,0), sw=360, r=1, d=3 , ut=0, s=8, ch=1)
            # elif i == 11:
            #     cmds.circle(nr=(1,0,0), sw=360, r=1, d=3 , ut=0, s=8, ch=1)
            # elif i == 12:
            #     cmds.circle(nr=(1,0,0), sw=360, r=1, d=3 , ut=0, s=8, ch=1)
            # elif i == 13:
            #     cmds.circle(nr=(1,0,0), sw=360, r=1, d=3 , ut=0, s=8, ch=1)
            # elif i == 14:
            #     cmds.circle(nr=(1,0,0), sw=360, r=1, d=3 , ut=0, s=8, ch=1)
            # elif i == 15:
            #     cmds.circle(nr=(1,0,0), sw=360, r=1, d=3 , ut=0, s=8, ch=1)
            # elif i == 16:
            #     cmds.circle(nr=(1,0,0), sw=360, r=1, d=3 , ut=0, s=8, ch=1)
            # elif i == 17:
            #     cmds.circle(nr=(1,0,0), sw=360, r=1, d=3 , ut=0, s=8, ch=1)
            # elif i == 18:
            #     cmds.circle(nr=(1,0,0), sw=360, r=1, d=3 , ut=0, s=8, ch=1)
            # elif i == 19:
            #     cmds.circle(nr=(1,0,0), sw=360, r=1, d=3 , ut=0, s=8, ch=1)
            # elif i == 20:
            #     cmds.circle(nr=(1,0,0), sw=360, r=1, d=3 , ut=0, s=8, ch=1)
            # elif i == 21:
            #     cmds.circle(nr=(1,0,0), sw=360, r=1, d=3 , ut=0, s=8, ch=1)
            # elif i == 22:
            #     cmds.circle(nr=(1,0,0), sw=360, r=1, d=3 , ut=0, s=8, ch=1)
            # elif i == 23:
            #     cmds.circle(nr=(1,0,0), sw=360, r=1, d=3 , ut=0, s=8, ch=1)
            # elif i == 24:
            #     cmds.circle(nr=(1,0,0), sw=360, r=1, d=3 , ut=0, s=8, ch=1)
            # elif i == 25:
            #     cmds.circle(nr=(1,0,0), sw=360, r=1, d=3 , ut=0, s=8, ch=1)
            # elif i == 26:
            #     cmds.circle(nr=(1,0,0), sw=360, r=1, d=3 , ut=0, s=8, ch=1)
            # elif i == 27:
            #     cmds.circle(nr=(1,0,0), sw=360, r=1, d=3 , ut=0, s=8, ch=1)
            # else i == 28:
            #     cmds.circle(nr=(1,0,0), sw=360, r=1, d=3 , ut=0, s=8, ch=1)






def OPEN():
    window_name     = 'Control_Creator'
    dock_control     = 'Control_Creator_Dock'

    if cmds.window( window_name, exists=True ):
        cmds.deleteUI( window_name )

    Window = uiMainWindow()
    Window.show()

    Window.setObjectName(window_name)
    """
    if (cmds.dockControl(dock_control, q=True, ex=True)):
        cmds.deleteUI(dock_control)
    AllowedAreas = ['right', 'left']
    cmds.dockControl(dock_control,aa=AllowedAreas, a='left', floating=False, content=window_name, label='EX Window')
    """
