#encoding=utf-8
#!/usr/bin/env python

#-------------------------------------------------------------------------------
#
#   Dexter Rigging Team
#
#       yunhyuk
#
#   2017.1.10 w01
#-------------------------------------------------------------------------------

import os

from PySide import QtCore, QtGui

from shiboken import wrapInstance

import maya.cmds as cmds
import maya.OpenMayaUI as omui
from manual.biped.importTemplate import *
from manual.biped.mirrorTemplateJoints import *
from manual.biped.bipedRig import *
from manual.biped.extraJoint import *
from manual.biped.extraRig import *
from util.zeroOut import *

import xml.etree.ElementTree as xml
import pysideuic
from cStringIO import StringIO

basePath = os.path.abspath( __file__ + '/../' )
print basePath
uiFile   = os.path.join( basePath, 'bumbleBee.ui' )
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

        self.connectSocket()
        self.iconColor()

    def connectSocket(self):
        self.biped_temp_BTN.clicked.connect(self.importBipedTemplete)
        self.biped_build_BTN.clicked.connect(self.buildBiped_cmd)
        self.zeroOut_BTN.clicked.connect(self.zeroOut_cmd)
        self.mirrorJoints_BTN.clicked.connect(self.mirrorJoints_cmd)
        self.biped_ex_neck_BTN.clicked.connect(self.biped_ex_neck_cmd)
        self.biped_ex_shoulder_BTN.clicked.connect(self.biped_ex_shoulder_cmd)
        self.biped_ex_arm_BTN.clicked.connect(self.biped_ex_arm_cmd)
        self.biped_ex_finger_BTN.clicked.connect(self.biped_ex_finger_cmd)
        self.biped_ex_leg_BTN.clicked.connect(self.biped_ex_leg_cmd)
        self.biped_ex_build_BTN.clicked.connect(self.buildExtraRig_cmd)

    def iconColor(self):
        setIconPath = '/dexter/Cache_DATA/CRT/JYH/scripts/Asset/bumbleBee/icon/'
        self.zeroOut_BTN.setIcon(QtGui.QIcon('%szeroOut.jpg' %setIconPath))
        self.mirrorJoints_BTN.setIcon(QtGui.QIcon('%smirrorJoints.jpg' %setIconPath))
        self.biped_build_BTN.setIcon(QtGui.QIcon('%sbuild2.jpg' %setIconPath))
        self.biped_temp_BTN.setIcon(QtGui.QIcon('%simportBipedTemp.jpg' %setIconPath))
        self.biped_ex_build_BTN.setIcon(QtGui.QIcon('%sbuild3.jpg' %setIconPath))
        self.biped_ex_neck_BTN.setIcon(QtGui.QIcon('%sex_neck.jpg' %setIconPath))
        self.biped_ex_finger_BTN.setIcon(QtGui.QIcon('%sex_finger.jpg' %setIconPath))
        self.biped_ex_leg_BTN.setIcon(QtGui.QIcon('%sex_leg.jpg' %setIconPath))
        self.biped_ex_arm_BTN.setIcon(QtGui.QIcon('%sex_arm.jpg' %setIconPath))
        self.biped_ex_shoulder_BTN.setIcon(QtGui.QIcon('%sex_shoulder.jpg' %setIconPath))
        self.quad_temp_BTN.setIcon(QtGui.QIcon('%squad_importTemp.jpg' %setIconPath))
        self.quad_neck_BTN.setIcon(QtGui.QIcon('%squad_neck.jpg' %setIconPath))
        self.quad_spine_BTN.setIcon(QtGui.QIcon('%squad_spine.jpg' %setIconPath))
        self.quad_forelegL_BTN.setIcon(QtGui.QIcon('%squad_foreLeg_L.jpg' %setIconPath))
        self.quad_forelegR_BTN.setIcon(QtGui.QIcon('%squad_foreLeg_L.jpg' %setIconPath))
        self.quad_hindlegL_BTN.setIcon(QtGui.QIcon('%squad_hindLeg_L.jpg' %setIconPath))
        self.quad_hindlegR_BTN.setIcon(QtGui.QIcon('%squad_hindLeg_L.jpg' %setIconPath))
        self.quad_tail_BTN.setIcon(QtGui.QIcon('%squad_tail.jpg' %setIconPath))
        self.quad_setup_BTN.setIcon(QtGui.QIcon('%squad_setup.jpg' %setIconPath))

    def importBipedTemplete(self):
        i = importTemplate()
        i.simpleBiped()

    def buildBiped_cmd(self):
        b=bipedRig()
        b.build()

    def zeroOut_cmd(self):
        z = zeroOut()
        hireSel = []
        sel = cmds.ls(sl=True)
        for i in sel:
            #del hireSel[0:len(hireSel)]
            cmds.select("%s" %i, hierarchy=True, add=True )
            ee = cmds.ls(sl=1)
            for j in ee:
              z.zeroOutJoint(j)
        
    def mirrorJoints_cmd(self):
        m=mirrorTemplateJoints()
        hireSel = []
        sel = cmds.ls(sl=True)
        for i in sel:
            del hireSel[0:len(hireSel)]
            cmds.select("%s" %i, hierarchy=True, add=True )
            ee = cmds.ls(sl=1)
            hireSel.append(ee)
        for e in hireSel[0]:
            cmds.refresh()
            m.similarPose(e)

    def buildExtraRig_cmd(self):
        er=extraRig()
        er.attachWindow()

    def biped_ex_neck_cmd(self):
        ex=extraJoint()
        ex.neck()

    def biped_ex_shoulder_cmd(self):
        ex=extraJoint()
        ex.shoulder()

    def biped_ex_arm_cmd(self):
        ex=extraJoint()
        ex.arm()

    def biped_ex_finger_cmd(self):
        ex=extraJoint()
        ex.finger()

    def biped_ex_leg_cmd(self):
        ex=extraJoint()
        ex.leg()

#---------------------------------------------------------------------------------------------------------------------

def OPEN():
    window_name     = 'BumbleBee'
    dock_control     = 'BumbleBee_Dock'
    
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
    