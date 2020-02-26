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
#import test0 as T
import manual.quadruped.quadruped as Q     ;    reload( Q )


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


basePath = os.path.abspath( __file__ + '/../' )
print basePath
qDir     = QtCore.QDir()
uiFile   = os.path.join( basePath, 'ui', 'mainGUI.ui' )
print uiFile
ui_path  = os.path.dirname(uiFile)
qDir.setCurrent(ui_path)

iconPath = os.path.join(basePath, 'icons/' )
print iconPath

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
class Hello( base_class, form_class ):
	# MainWindow Type
	def __init__(self, parent=None): #getMayaWindow()
		'''A custom window with a demo set of ui widgets'''
		# init our ui using the MayaWindow as parent
		super( base_class, self ).__init__( parent )
		# uic adds a function to our class called setupUi, calling this creates all the widgets from the .ui file
		self.setupUi(self)

		#self.setObjectName( WIDGET_NAME )
		#self.setWindowTitle('Hello Tool Window')
		
		self.addToolBarItem()
		
		self.tabWidget.currentChanged.connect(self.addToolBarItem) #changed!
	#	
	#def tapChange(self,i): #changed!
	#	'''
	#	if i == 0:
	#		currentTabTxet = 'TEMPLATES'
	#		print currentTabTxet
	#	if i == 1:
	#		currentTabTxet = 'MODULES'
	#		print currentTabTxet
	#	if i == 2:
	#		currentTabTxet = 'MANUAL'
	#		print currentTabTxet
	#	'''
	#	print ' Tap index is %s ' % i
	#	#self.tabWidget.currentIndex()
	
	def addToolBarItem(self):
		
		if self.tabWidget.currentIndex() == 0:
			print 'MANUAL : ID 0'
			
			self.toolBar.clear()
			self.toolBar.addSeparator()
			
			self.editorAction = QtGui.QAction( QtGui.QIcon( iconPath + 'biped.png' ), 'Biped', self )
			self.toolBar.addAction(self.editorAction)
			self.editorAction. triggered .connect(self.biped)
			
			self.editorAction = QtGui.QAction( QtGui.QIcon( iconPath + 'biped.png' ), 'Quadruped', self )
			self.toolBar.addAction(self.editorAction)
			self.editorAction. triggered .connect(self.quadruped)
			
			self.toolBar.addSeparator()
			
			self.toolBar.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon) # Qt.ToolButtonTextBesideIcon
			
		if self.tabWidget.currentIndex() == 1:
			print 'TEMPLATES : ID 1'
			
			self.toolBar.clear()
			self.toolBar.addSeparator()
			
			self.editorAction = QtGui.QAction( QtGui.QIcon( iconPath + 'biped.png' ), 'Ik Stretch', self )
			self.toolBar.addAction(self.editorAction)
			self.editorAction. triggered .connect(self.editor)
			
			self.toolBar.addSeparator()
			
			self.toolBar.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon) # Qt.ToolButtonTextBesideIcon
			
		if self.tabWidget.currentIndex() == 2:
			print 'MODULES : ID 2'
			
			self.toolBar.clear()
			self.toolBar.addSeparator()
			
			self.editorAction = QtGui.QAction( QtGui.QIcon( iconPath + 'biped.png' ), 'Replace controller Shape', self )
			self.toolBar.addAction(self.editorAction)
			self.editorAction. triggered .connect(self.editor)
			
			self.toolBar.addSeparator()
			
			self.toolBar.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon) # Qt.ToolButtonTextBesideIcon

	# MANUAL button						
	def biped(self):
		self.clearLayout(self.verticalLayout)
		createUI = T.GUI()
		self.verticalLayout.addWidget(createUI)

	def quadruped(self):
		self.clearLayout(self.MANUAL_verticalLayout)
		createUI = Q.Quadruped()
		self.MANUAL_verticalLayout.addWidget(createUI)
	
	# Clear	Layout
	def clearLayout(self, layout):
		while layout.count() > 0:
			item = layout.takeAt(0)
			if not item:
				continue
			
			w = item.widget()
			if w:
				w.deleteLater()





def StartUI():
    if default == "pyqt4":
        MayaWindowPtr = sip.wrapinstance(long( mui.MQtUtil.mainWindow() ), QtCore.QObject)
    else:
        MayaWindowPtr = shiboken.wrapInstance(long(mui.MQtUtil.mainWindow()), QtGui.QMainWindow)
    
    window_name     = 'Control_Creator'
    dock_control     = 'Control_Creator_Dock'
    
    if cmds.window( window_name, exists=True ):
        cmds.deleteUI( window_name )
    Window = Hello(MayaWindowPtr)
    Window.setObjectName(window_name)
    if (cmds.dockControl(dock_control, q=True, ex=True)):
        cmds.deleteUI(dock_control)
    AllowedAreas = ['right', 'left']
    cmds.dockControl(dock_control,aa=AllowedAreas, a='left', floating=False, content=window_name, label='Rig Creator')