#encoding=utf-8
#!/usr/bin/env python

#-------------------------------------------------------------------------------
#
#   Dexter Rigging Team
#
#       yunhyuk.jung
#
#   2015.12.09.v01.w03
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
        for i in range(1,33):
            eval( "self.color_%s_BTN.clicked.connect(self.overrideColor)" %i )
        # for i in range(1,29):
        #     eval( "self.conMake_%s_BTN.clicked.connect(self.controllerMake)" %i )

# buttonAction def Group
    def ButtonConnection(self):
        self.Shape_Replace_BTN.clicked.connect(self.shapeReplace)
        self.Do_Resize_BTN.clicked.connect(self.controllerResize)
        self.FK_Control_Maker_BTN.clicked.connect(self.FKcontrolMaker)

    @undo      
    def overrideColor(self):
        sender = self.sender()
        btn = sender.objectName()
        btn_number = btn.split('_')
        sel_name = cmds.ls(sl=True)
        for i in sel_name: 
            colorShape =  i 
            cmds.setAttr("%sShape.overrideEnabled" %colorShape, 1)
            cmds.setAttr("%sShape.overrideColor" %colorShape, int(btn_number[1])-1)

    # def controllerMake(self):
    #     sender = self.sender()
    #     btn = sender.objectName()
    #     print btn
    #     btn_number = btn.split('_')

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
            Control = cmds.circle(nr=(1,0,0),c=(0,0,0),r=1, n= jointName.replace(jointName.split('_')[-1],'CRV'))
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
    
    @undo
    def controllerResize(self):
        number = float(self.Do_Resize_DSB.text())
        XYZ = ["X","Y","Z"]
        sel = cmds.ls(sl=True)
        for x in sel:
            curveName = x
            curveShape = cmds.listRelatives( curveName, s=True )[0]
            cvNum = cmds.getAttr( '%s.spans' % curveShape ) + cmds.getAttr( '%s.degree' % curveShape )
            cmds.select( "%s.cv[0:%s]" %(curveName,cvNum))
            cluster = cmds.cluster()
            if number > 0:
                for i in XYZ:
                    cmds.setAttr( "%s.scale%s" %(cluster[1],i), number)
            else:
                nagative_number = 1 - number*(-0.1)
                print nagative_number
                for i in XYZ:
                    cmds.setAttr( "%s.scale%s" %(cluster[1],i), nagative_number)
            cmds.DeleteHistory(cmds.select( sel ))


def OPEN():
    window_name     = 'Control_Creator'
    dock_control     = 'Control_Creator_Dock'

    if cmds.window( window_name, exists=True ):
        cmds.deleteUI( window_name )

    Window = uiMainWindow()
    Window.show()

    Window.setObjectName(window_name)
    
    # if (cmds.dockControl(dock_control, q=True, ex=True)):
    #     cmds.deleteUI(dock_control)
    # AllowedAreas = ['right', 'left']
    # cmds.dockControl(dock_control,aa=AllowedAreas, a='left', floating=False, content=window_name, label='EX Window')
    
