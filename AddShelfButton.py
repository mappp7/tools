# -*- coding: utf-8 -*-

import re
import site
import mobuPath as mp
import ctypes
user32 = ctypes.windll.user32
screensize = user32.GetSystemMetrics(0)

site.addsitedir(mp.envPath)
site.addsitedir("Z:/P4V/LLL/LllArt/Animation/Script/mobu/MB/version_2023/config/Python/envSet")
from pyfbsdk import *
from pyfbsdk_additions import *
############################################################
sys = FBSystem()
app = FBApplication()

#SET MOTION IMPORT SETTING - DOF lock
lconfigApp = FBConfigFile("@Application.txt")
lconfigApp.Set("MotionImportGlobal" , "ImportDOF" , "No")


def OnConnectionStateNotify(control, event):
    if str(event.Action) == 'kFBSelect':
        modelList = FBModelList()
        FBGetSelectedModels (modelList, None, True)
        if len(modelList) == 1:
            ocomBox.setCurrentIndex(modelList[0].PropertyList.Find('Rotation Order').Data)
              

def OnConnectionNotify(control, event):
    if event.SrcPlug:
        if str(event.Action) == 'kFBDisconnect' and str(event.SrcPlug.ClassName()) == "FBAnimationLayer":
            if sys.CurrentTake:
                if not sys.CurrentTake.Selected:
                    for l in sys.Scene.Takes:  
                        l.Selected = False
                    sys.CurrentTake.Selected = True

def Register():
    sys.OnConnectionStateNotify.Add(OnConnectionStateNotify)
    sys.OnConnectionNotify.Add(OnConnectionNotify)
    app.OnFileExit.Add(Unregister)

def Unregister(control=None, event=None):
    sys.OnConnectionStateNotify.Remove(OnConnectionStateNotify)
    sys.OnConnectionNotify.Remove(OnConnectionNotify)
    app.OnFileExit.Remove(Unregister)

Register()

##############################################################
# import ctypes
# user32 = ctypes.windll.user32
# screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
try:
    from PySide import  QtGui as widgets
    #from PySide.QtGui import QColor
    #from PySide.QtGui import QBrush
    from PySide import QtCore
    from PySide.QtCore import *
    from PySide.QtGui import *
except:
    from PySide2.QtWidgets import *
    from PySide2.QtGui import QColor
    from PySide2.QtGui import QBrush
    from PySide2.QtCore import *

class WheelEventFilter(QObject):
    def eventFilter(self, obj, ev):
        if obj.inherits("QComboBox") and ev.type() == QEvent.Wheel:
            return True
        return False

def getDisplayRect(rootwgt):
    if rootwgt:
        # get all Viewer's widgets
        oLyt=rootwgt.layout()
        oMainWgt=oLyt.itemAt(0).widget()
        for oChild in oMainWgt.children():
            for oCChild in oChild.children():
                if oCChild.accessibleName()=="ButtonBarWithRightBar":
                    oUpperWgt=oCChild
                    # get upper Viewer Widget
                    for oCCChild in oCChild.findChildren(QWidget):
                        print(oCCChild.accessibleName())
                        if oCCChild.accessibleName()=="Display":
                            # get Display button layout imformation
                            oDisplayRect=oCCChild.geometry()
                    
                    return oUpperWgt,oDisplayRect
                 
                     
    return None,None

# When press Button 
def HelloWorld():
    QMessageBox.information(win,
                            "button clicked",
                            "Command Test",
                            QMessageBox.Ok)

def executePyFile(path):
    exec(compile(open(path, "rb").read(), path, 'exec'))

# get MotionBuilder window
ptn=re.compile('Mainboard')
for win in QApplication.topLevelWidgets():
    if ptn.search(win.accessibleName()):
        break
    else:
        win=None
# get Viewer window       
if win:
    RootViewer=None
    for cWgt in win.findChildren(QDockWidget):
        if cWgt.windowTitle()=="Viewer":
            RootViewer=cWgt
            break
# get Viewer window in Display button layout and parent widget.
oParentWgt,oDisplayRect=getDisplayRect(RootViewer)

"""
def setShelfBtn(name,right,width,socket=None):
    execFunc = socket
    if oParentWgt and oDisplayRect:
        oButton = QPushButton(name, oParentWgt)
        x=oDisplayRect.right()+int(right)
        y=oDisplayRect.top()
        w=int(width)
        h=oDisplayRect.bottom()-oDisplayRect.top()
        oButton.setGeometry(x,y,w,h)
        oButton.clicked.connect(execFunc)  
        oButton.show()
# Sample Btn ---------------------------------------------------------------------------------
btnDict = {
            'Save':['Save','5','70','HelloWorld'],
            'DoublePlot':['DoublePlot','1260','82','execDoublePlot'],
            
            }

for k in btnDict:
        b = btnDict
        # print b[k][0]
        # print b[k][1]
        # print b[k][2]
        # print b[k][3]
        setShelfBtn(b[k][0],b[k][1],b[k][2])
"""

# Shelf Btn execFunc ---------------------------------------------------------------------------------
def execRootMake():
    
    import CLS_rootMotion as crm
    rmCLS = crm.rootMotion(1) 
    modelList = FBModelList()
    FBGetSelectedModels (modelList, None, True)
    if len(modelList) == 1:
        if modelList[0].Name.find("root") != -1:
            if len(modelList[0].LongName.split(':')) > 1:
                rmCLS.n_s = modelList[0].LongName.split(':') + ":"
            else:
                rmCLS.n_s = ""
            ind = ocomBox2.currentIndex()
            if ind == 0:
                rmCLS.ZeroBake(0)
            elif ind == 1:
                rmCLS.BakeRootMotion(0,1,0)
            else:
                rmCLS.BakeRootMotion(1,1,0)
        else:
            FBMessageBox( 'Warning', 'Choose Root', "Ok" )
    else:
        FBMessageBox( 'Warning', 'Choose Only One', "Ok" )


def execDoublePlot():
    import DoublePlot as dp
    dp.execFunc()
def execSaveTakeList():
    import SaveTakeList as stl
    stl.execFunc()
def execPreviousTake():
    import TakeMove as tm
    tm.execFunc('PreviousTake')  
def execNextTake():
    import TakeMove as tm
    tm.execFunc('NextTake')
def execDeleteTake():
    import TakeMove as tm
    tm.execFunc('DeleteTake')
def execCheckTake():
    import TakeMove as tm
    tm.execFunc('CheckTake')
def execTpose():
    import controlRig_Tpose as crt
    crt.execFunc()
def execIKZero():
    import setIKBlend as sib
    sib.execFunc(0)
def execIKHundred():
    import setIKBlend as sib
    sib.execFunc()

def execRotationOrder():
    modelList = FBModelList()
    FBGetSelectedModels (modelList, None, True)
    if len(modelList) == 1:
        modelList[0].PropertyList.Find('Rotation Order').Data = ocomBox.currentIndex()

def execBatchExporter():
    myfile = ("Z:/P4V/LLL/LllArt/Animation/Script/mobu/MB/version_2023/config/Python/pyList/mobuBatchExporter.py")
    FBApplication().ExecuteScript(myfile)
def execPoseLibrary():
    myfile = ("Z:/P4V/LLL/LllArt/Animation/Script/mobu/MB/version_2023/config/Python/pyList/PoseLibrary.py")
    FBApplication().ExecuteScript(myfile)
def execPivotTool():
    myfile = ("Z:/P4V/LLL/LllArt/Animation/Script/mobu/MB/version_2023/config/Python/pyList/PivotTool_2018.py")
    FBApplication().ExecuteScript(myfile)
def execNavigationTool():
    myfile = ("Z:/P4V/LLL/LllArt/Animation/Script/mobu/MB/version_2023/config/Python/pyList/NavigationTool.py")
    FBApplication().ExecuteScript(myfile)
def execMultiConstraintTool():
    myfile = ("Z:/P4V/LLL/LllArt/Animation/Script/mobu/MB/version_2023/config/Python/pyList/multiConstraint.py")
    FBApplication().ExecuteScript(myfile)
def execPlotSelected():
    myfile = ("Z:/P4V/LLL/LllArt/Animation/Script/mobu/MB/version_2023/config/Python/pyList/selectPlot.py")
    FBApplication().ExecuteScript(myfile)
def execRigBatch():
    myfile = ("Z:/P4V/LLL/LllArt/Animation/Script/mobu/MB/version_2023/config/Python/pyList/rigBatchTool.py")
    FBApplication().ExecuteScript(myfile)

if oParentWgt and oDisplayRect:
    mainL = QHBoxLayout(oParentWgt)
    mainL.setSpacing(0)
    mainL.setContentsMargins(0,0,0,0)#(140,0,150,0)
    
    oScroll1 = QScrollArea(oParentWgt)
    oScroll2 = QScrollArea(oParentWgt)
    oScroll1.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
    oScroll1.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
    oScroll2.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
    oScroll2.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
    oScroll1.horizontalScrollBar().hide()
    oScroll1.setWidgetResizable(True)
    oScroll2.horizontalScrollBar().hide()
    oScroll2.setWidgetResizable(True)
    oScroll1.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
    oScroll2.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
    oScroll1.setStyleSheet("QScrollArea{border:0px;}")
    oScroll2.setStyleSheet("QScrollArea{border:0px;}")
    horizontalScrollBar1 = QScrollBar(Qt.Horizontal, oScroll1)
    horizontalScrollBar2 = QScrollBar(Qt.Horizontal, oScroll2)
    styleSheet = """
    QScrollBar:horizontal
    {
        height: 1px;
        border: 1px transparent #2A2929;
        border-radius: 1px;
    }
    QScrollBar::handle:horizontal
    {
        min-width: 5px;
        border-radius: 1px;
    }
    QScrollBar::add-line:horizontal
    {
        height: 1px;
        subcontrol-position: right;
    }
    QScrollBar::sub-line:horizontal
    {
        height: 1px;
        subcontrol-position: left;
    }
    QScrollBar::add-line:horizontal:hover,QScrollBar::add-line:horizontal:on
    {
        height: 1px;
        subcontrol-position: right;
    }
    QScrollBar::sub-line:horizontal:hover, QScrollBar::sub-line:horizontal:on
    {
        height: 1px;  
        subcontrol-position: left;
    }
    QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal
    {
        background: none;
    }
    QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal
    {
        background: none;
    }
    """
    horizontalScrollBar1.setStyleSheet(styleSheet)
    oScroll1.setHorizontalScrollBar(horizontalScrollBar1)
    oScroll1.show()
    horizontalScrollBar2.setStyleSheet(styleSheet)
    oScroll2.setHorizontalScrollBar(horizontalScrollBar2)
    oScroll2.show()
    
    space = QSpacerItem(140,40,QSizePolicy.Fixed, QSizePolicy.Fixed) 
    mainL.addItem(space)

    wg2 = QWidget()
    lyt = QHBoxLayout()
    wg2.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    lyt.setSpacing(0)
    lyt.setContentsMargins(0,0,0,0)
    wg2.setLayout(lyt)
    mainL.addWidget(wg2)
    lyt.addWidget(oScroll1)

    space = QSpacerItem(260,40,QSizePolicy.Fixed, QSizePolicy.Fixed) 
    mainL.addItem(space)

    wg3 = QWidget()
    lyt2 = QHBoxLayout()
    wg3.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    lyt2.setSpacing(0)
    lyt2.setContentsMargins(0,0,0,0)
    
    wg3.setLayout(lyt2)
    mainL.addWidget(wg3)
    lyt2.addWidget(oScroll2)

    space = QSpacerItem(140,40,QSizePolicy.Fixed, QSizePolicy.Fixed) 
    mainL.addItem(space)

    # HBoxLayout in scrollBox for scroll (1)
    wg1 = QWidget()
    hb1 = QHBoxLayout()
    wg1.setLayout(hb1)
    hb1.setContentsMargins(0,0,0,0)
    hb1.setSpacing(5)

    # area 1 Button
    global ocomBox2
    ocomBox2 = QComboBox(oParentWgt)
    ocomBox2.setView(QListView())
    ocomBox2.addItem('Zero (0,0,0)')
    ocomBox2.addItem('Translate')
    ocomBox2.addItem('Trans + Rotate')

    ocomBox2.setStyleSheet("QListView::item {height:25px;}")
    filter = WheelEventFilter()
    ocomBox2.installEventFilter(filter)
    ocomBox2.setFocusPolicy(Qt.TabFocus)
    x=0
    y=oDisplayRect.top()
    w=100
    h=oDisplayRect.bottom()-oDisplayRect.top()
    #oButton.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
    ocomBox2.setGeometry(x,y,w,h)
    ocomBox2.currentIndexChanged.connect(execRotationOrder)
    ocomBox2.show()
    hb1.addWidget(ocomBox2)

    oButton = QPushButton("Root Make")
    oButton.setStyleSheet("""background-color: rgb(90,10,90);color:  rgb(217,83,79)""")
    x=0#(screensize*0.753)
    y=oDisplayRect.top()
    w=100
    h=oDisplayRect.bottom()-oDisplayRect.top() 
    oButton.setGeometry(x,y,w,h)
    oButton.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
    oButton.clicked.connect(execRootMake)
    oButton.show()
    hb1.addWidget(oButton)

    oButton = QPushButton("Batch Exporter")
    oButton.setStyleSheet("""background-color: rgb(70,159,70);color:  rgb(28,62,28)""")
    x=0#(screensize*0.753)
    y=oDisplayRect.top()
    w=100
    h=oDisplayRect.bottom()-oDisplayRect.top() 
    oButton.setGeometry(x,y,w,h)
    oButton.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
    oButton.clicked.connect(execBatchExporter)
    oButton.show()
    hb1.addWidget(oButton)

    oButton = QPushButton("Pose Library")
    oButton.setStyleSheet("background-color: rgb(51,122,183)")
    x=0
    y=oDisplayRect.top()
    w=100
    h=oDisplayRect.bottom()-oDisplayRect.top()
    oButton.setGeometry(x,y,w,h)
    oButton.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
    oButton.clicked.connect(execPoseLibrary)
    oButton.show()
    hb1.addWidget(oButton)

    oButton = QPushButton("Pivot Tool")
    oButton.setStyleSheet("background-color: rgb(217,83,79)")
    x=0
    y=oDisplayRect.top()
    w=90
    h=oDisplayRect.bottom()-oDisplayRect.top()
    oButton.setGeometry(x,y,w,h)
    oButton.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
    oButton.clicked.connect(execPivotTool)
    oButton.show()
    hb1.addWidget(oButton)

    oButton = QPushButton(" Navigation ")
    oButton.setStyleSheet("background-color: rgb(30,83,79)")
    x=0
    y=oDisplayRect.top()
    w=90
    h=oDisplayRect.bottom()-oDisplayRect.top()
    oButton.setGeometry(x,y,w,h)
    oButton.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
    oButton.clicked.connect(execNavigationTool)
    oButton.show()
    hb1.addWidget(oButton)

    oButton = QPushButton(" MultiConstraint ")
    oButton.setStyleSheet("""background-color: rgb(70,159,30);color:  rgb(28,62,28)""")
    x=0
    y=oDisplayRect.top()
    w=90
    h=oDisplayRect.bottom()-oDisplayRect.top()
    oButton.setGeometry(x,y,w,h)
    oButton.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
    oButton.clicked.connect(execMultiConstraintTool)
    oButton.show()
    hb1.addWidget(oButton)

    oButton = QPushButton(" Rig Batch ")
    oButton.setStyleSheet("""background-color: rgb(250,250,250);color:  rgb(0,0,0)""")
    x=0
    y=oDisplayRect.top()
    w=90
    h=oDisplayRect.bottom()-oDisplayRect.top()
    oButton.setGeometry(x,y,w,h)
    oButton.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
    oButton.clicked.connect(execRigBatch)
    oButton.show()
    hb1.addWidget(oButton)

    
    space = QSpacerItem(20,40,QSizePolicy.Expanding, QSizePolicy.Expanding) 
    hb1.addItem(space)

    oScroll1.setWidget(wg1)

    #@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#
    # HBoxLayout in scrollBox for scroll (2)
    wg2 = QWidget()
    hb2 = QHBoxLayout()
    wg2.setLayout(hb2)
    hb2.setContentsMargins(0,0,0,0)
    hb2.setSpacing(5)

    # area 2 Button
    oButton = QPushButton("Save Take List")
    x=0
    y=oDisplayRect.top()
    w=120
    h=oDisplayRect.bottom()-oDisplayRect.top()
    oButton.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
    oButton.setGeometry(x,y,w,h)
    oButton.clicked.connect(execSaveTakeList)
    oButton.show()
    hb2.addWidget(oButton)

    oButton = QPushButton("T pose")
    x=0
    y=oDisplayRect.top()
    w=70
    h=oDisplayRect.bottom()-oDisplayRect.top()
    oButton.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
    oButton.setGeometry(x,y,w,h)
    oButton.clicked.connect(execTpose)  
    oButton.show()
    hb2.addWidget(oButton)
    # Save System Btn  ---------------------------------------------------------------------------------
    oButton = QPushButton(" Double Plot ", oParentWgt)
    x=0
    y=oDisplayRect.top()
    w=95
    h=oDisplayRect.bottom()-oDisplayRect.top()
    oButton.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
    oButton.setStyleSheet("background-color: rgb(90,40,79)")
    oButton.setGeometry(x,y,w,h)
    oButton.clicked.connect(execDoublePlot)  
    oButton.show()
    hb2.addWidget(oButton)

    oButton = QPushButton(" Plot Selected ", oParentWgt)
    x=0
    y=oDisplayRect.top()
    w=95
    h=oDisplayRect.bottom()-oDisplayRect.top()
    oButton.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
    oButton.setStyleSheet("background-color: rgb(0,90,90)")
    oButton.setGeometry(x,y,w,h)
    oButton.clicked.connect(execPlotSelected)  
    oButton.show()
    hb2.addWidget(oButton)

    global ocomBox
    ocomBox = QComboBox(oParentWgt)
    ocomBox.setView(QListView())
    ocomBox.addItem('Euler XYZ')
    ocomBox.addItem('Euler XZY')
    ocomBox.addItem('Euler YZX')
    ocomBox.addItem('Euler YXZ')
    ocomBox.addItem('Euler ZXY')
    ocomBox.addItem('Euler ZYX')
    ocomBox.addItem('Spheric XYZ')
    ocomBox.setStyleSheet("QListView::item {height:25px;}")
    filter = WheelEventFilter()
    ocomBox.installEventFilter(filter)
    ocomBox.setFocusPolicy(Qt.TabFocus)
    x=0
    y=oDisplayRect.top()
    w=95
    h=oDisplayRect.bottom()-oDisplayRect.top()
    #oButton.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
    ocomBox.setGeometry(x,y,w,h)
    ocomBox.currentIndexChanged.connect(execRotationOrder)
    ocomBox.show()
    hb2.addWidget(ocomBox)
 
    space2 = QSpacerItem(20,40,QSizePolicy.Expanding, QSizePolicy.Expanding) 
    hb2.addItem(space2)

    oScroll2.setWidget(wg2)



