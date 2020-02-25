#encoding=utf-8
'''
Path         :
Title        :
Description  :
Author       :
Date         :
Notes        :
'''

####################################################################################################
### General ########################################################################################
####################################################################################################


# Import Package Modules
import manual.quadruped.spine.ikSpine as QS    ;   reload( QS )


# Import Python Modules
#import os, sys, re, stat, functools, shutil
import os
import sys
import re
import stat
import functools
import shutil

# Import Maya Modules
#from maya import mel, cmds, OpenMayaUI
import maya.cmds as cmds
import maya.mel as mel
import maya.OpenMayaUI as mui

# Import QT Modules

default = 'none'
try:
    from PyQt4 import *
    from PyQt4 import QtCore
    from PyQt4 import uic
    import sip
    default = 'pyqt4'
    print 'LOAD : pyqt4'
except:
    print 'pyqt4 not found'

try:
    import xml.etree.ElementTree as xml
    from cStringIO import StringIO
    from PySide import QtGui, QtCore
    import pysideuic, shiboken

    default = 'pyside'
    print 'LOAD : pyside'
except:
    print 'pyside not found'

if default == 'none':
    cmds.error( 'no Library found, please install PyQt4 or PySide!')

####################################################################################################
### Utilities ######################################################################################
####################################################################################################

def loadUiType(uiFile):
    if default ==  "pyqt4":
        form_class, base_class =  uic.loadUiType( uiFile )
    else:
        parsed = xml.parse(uiFile)
        widget_class = parsed.find('widget').get('class')
        form_class = parsed.find('class').text

        with open(uiFile, 'r') as f:
            o = StringIO()
            frame = {}

            pysideuic.compileUi(f, o, indent=0)
            pyc = compile(o.getvalue(), '<string>', 'exec')
            exec pyc in frame

            form_class = frame['Ui_%s'%form_class]
            base_class = eval('QtGui.%s'%widget_class)
    return form_class, base_class


basePath = os.path.abspath( __file__ + '/../../../' )
print basePath
qDir     = QtCore.QDir()
uiFile   = os.path.join( basePath, 'ui', 'quadruped.ui' )
print uiFile
ui_path  = os.path.dirname(uiFile)
qDir.setCurrent(ui_path)

#iconPath = os.path.join(basePath, 'icons/' )
#print iconPath

# Load the ui file, and create my class
base_class, form_class = loadUiType(uiFile)



def wrapinstance(ptr, base=None):
    if ptr is None:
        return None
    ptr = long(ptr) #Ensure type
    if globals().has_key('shiboken'):
        if base is None:
            qObj = shiboken.wrapInstance(long(ptr), QtCore.QObject)
            metaObj = qObj.metaObject()
            cls = metaObj.className()
            superCls = metaObj.superClass().className()
            if hasattr(QtGui, cls):
                base = getattr(QtGui, cls)
            elif hasattr(QtGui, superCls):
                base = getattr(QtGui, superCls)
            else:
                base = QtGui.QWidget
        return shiboken.wrapInstance(long(ptr), base)
    elif globals().has_key('sip'):
        base = QtCore.QObject
        return sip.wrapinstance(long(ptr), base)
    else:
        return None
"""
class Control_CreatorUI(Control_CreatorUI_form, Control_CreatorUI_base):
    def __init__(self, parent=None):
        super(Control_CreatorUI, self).__init__(parent)
        self.setupUi(self)

        print '__init__'
"""
####################################################################################################
### Classes ########################################################################################
####################################################################################################

'''
class Name   :
Description  :
Note         :
'''

# Class( base QT )
class Quadruped( base_class, form_class ):
    # MainWindow Type
    def __init__( self ): #getMayaWindow()
        '''A custom window with a demo set of ui widgets'''
        # init our ui using the MayaWindow as parent
        super( base_class, self ).__init__()
        # uic adds a function to our class called setupUi, calling this creates all the widgets from the .ui file
        self.setupUi(self)

        self.createConnections()

    def createConnections( self ):
        self.itqsj_btn.clicked.connect( self.importQuadrupedTemplateSpineJoint )
        self.qs_btn.clicked.connect( self.spineBuild )

    def importQuadrupedTemplateSpineJoint( self ):
        cmds.file( '/dexter/Cache_DATA/CRT/RiggingRnD/baseRig/manual/quadruped/templateJoint/quadrupedTemplateSpineJoint.mb',
                    i=True, type='mayaBinary', mergeNamespacesOnClash=False, rpr='clash', options='v=0', pr=True )
        if cmds.objExists('clash_sceneConfigurationScriptNode'):
            cmds.delete('clash_sceneConfigurationScriptNode')
            cmds.delete('clash_uiConfigurationScriptNode')

    def spineBuild( self ):
        QS.quadrupedSpineRun()



