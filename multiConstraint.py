# !/usr/bin/env python
# -*- coding: utf-8 -*-
#-----------------------------------------------------------------------------------------------
import os
import inspect
import webbrowser
import importlib
curPath = inspect.getfile(lambda: None)
curPath = os.path.abspath(curPath + '/../')
# import Module
try:
    from PySide import  QtGui as widgets
    from PySide import QtGui as gui
    from PySide import QtCore, QtUiTools
    
except:
    from PySide2 import  QtWidgets as widgets
    from PySide2 import QtGui as gui
    from PySide2 import QtCore, QtUiTools
import shiboken2
from functools import partial
import MultiConstraintTools as mc;importlib.reload(mc)
from pyfbsdk import*
from pyfbsdk_additions import*

class nativeWidgetHolder(FBWidgetHolder):
    def WidgetCreate(self, pWidgetParent):
        self.motionBuilderMain = MainUI(shiboken2.wrapInstance(pWidgetParent, widgets.QWidget))
        return shiboken2.getCppPointer(self.motionBuilderMain)[0]

class NativeQtWidgetTool(FBTool):
    def __init__(self, name):
        FBTool.__init__(self, name)
        self.mNativeWidgetHolder = nativeWidgetHolder()
        self.BuildLayout()
        #UI size
        self.StartSizeX = 700
        self.StartSizeY = 800
        self.StartPosX = 700
        self.StartPosY = 180

    def BuildLayout(self):
        x = FBAddRegionParam(0, FBAttachType.kFBAttachLeft, "")
        y = FBAddRegionParam(0, FBAttachType.kFBAttachTop, "")
        w = FBAddRegionParam(0, FBAttachType.kFBAttachRight, "")
        h = FBAddRegionParam(0, FBAttachType.kFBAttachBottom, "")
        self.AddRegion("main", "main", x, y, w, h)
        self.SetControl("main", self.mNativeWidgetHolder)

class MainUI(widgets.QWidget):
    def __init__(self, parent):
        super(MainUI, self).__init__(parent)
        self.constraintList = []
        self.HUD=None
        self.buildUI()
        self.connectSignal()
        for i in range(3):
            self.HUD_Clear()
        
    def loadUIWidget(self, uiFileName, parent=None):
        loader = QtUiTools.QUiLoader()
        uiFile = QtCore.QFile(uiFileName)
        uiFile.open(QtCore.QFile.ReadOnly)
        ui = loader.load(uiFile, parent)
        uiFile.close()
        return ui

    def buildUI(self):
        self.parent().setLayout(widgets.QVBoxLayout())
        uiFile = curPath + '\\multiConstraint_ui.ui'
        self.ui = self.loadUIWidget(uiFile)
        self.parent().layout().addWidget(self.ui)

    # Default UI setting 

    def constraintListUp(self):
        self.constraintList = []
        self.ui.constraint_CBX.clear()
        lScene = FBSystem().Scene
        lConstraints = lScene.Constraints
        for each in lConstraints:
            if each.ClassName() == "FBConstraint":
                if each.ReferenceGet(0,0).LongName == self.ui.target_BTN.text():
                    if not each.ReferenceGet(0,0).LongName.find(":") == -1:
                        name = each.ReferenceGet(0,0).LongName.replace(":" , ">")
                    else:
                        name = each.ReferenceGet(0,0).LongName
                    if not each.Name.find("TT_"+name) == -1:
                        self.constraintList.append(each)
        for i,c in enumerate(self.constraintList):
            self.ui.constraint_CBX.addItem(c.Name)
        
    def defaultSet(self):
        self.ui.sourceList_TWG.clear()
        self.deleteButtonList=[]
        self.snapKeyList = []
        self.offsetKeyList = []
        
        constraintIndex = self.ui.constraint_CBX.currentIndex()
        if self.constraintList:
            lenParent = self.constraintList[constraintIndex].ReferenceGetCount(1)
            
            self.ui.sourceList_TWG.setRowCount(lenParent+1)
            self.ui.sourceList_TWG.setColumnCount(4)
            self.ui.sourceList_TWG.setHorizontalHeaderLabels(["+-" , "Parent", "Snap Key","Keep Offset"])
            #self.ui.sourceList_TWG.resizeRowsToContents()
            #self.ui.sourceList_TWG.resizeColumnsToContents()
            self.ui.sourceList_TWG.setColumnWidth(0,30)
            self.ui.sourceList_TWG.setColumnWidth(1,200)
            self.ui.sourceList_TWG.setColumnWidth(2,150)
            self.ui.sourceList_TWG.setColumnWidth(3,150)
            #make Button
            for i in range(lenParent):
                sourceModel = self.constraintList[constraintIndex].ReferenceGet(1,i)
                if i == 0:
                    sourceModel.Weight = 100
                else:
                    sourceModel.Weight = 0
                delButton = widgets.QPushButton()
                self.deleteButtonList.append(delButton)
                delButton.setText(" - ")
                delButton.clicked.connect(partial(self.removeButtonFunc , i))

                qbutton = widgets.QPushButton()
                self.snapKeyList.append(qbutton)
                qbutton.setText("SnapKey")
                qbutton.clicked.connect(partial(self.mcSnapKeyFunc , i))

                qbutton2 = widgets.QPushButton()
                self.offsetKeyList.append(qbutton2)
                qbutton2.setText("Keep Offset")
                qbutton2.clicked.connect(partial(self.mcOffsetKeyFunc , i))
            
                self.ui.sourceList_TWG.setCellWidget(i,0,delButton)
                qItem = widgets.QTableWidgetItem(sourceModel.LongName)
                qItem.setFlags(QtCore.Qt.ItemIsEnabled)
                self.ui.sourceList_TWG.setItem(i,1,qItem)
                self.ui.sourceList_TWG.setCellWidget(i,2,qbutton)
                self.ui.sourceList_TWG.setCellWidget(i,3,qbutton2)
            
            self.addButton = widgets.QPushButton()
            self.addButton.setText(" + ")
            self.ui.sourceList_TWG.setCellWidget(lenParent , 0 , self.addButton)
            self.addButton.clicked.connect(self.addButtonFunc)

            #add Button Func
            
    def connectSignal(self):
        self.ui.target_BTN.clicked.connect(self.targetSelect)
        self.ui.constraint_CBX.currentIndexChanged.connect(self.constraintChange)
        
        self.ui.refresh_BTN.clicked.connect(self.refreshFunc)
        self.ui.constDelete_BTN.clicked.connect(self.constDeleteFunc)
        self.ui.constMake_BTN.clicked.connect(self.constMakeFunc)
        self.ui.hudOnOff_BTN.clicked.connect(self.hudOnOffFunc)
        self.ui.sourceList_TWG.cellClicked.connect(self.TableWidgetClicked)
        self.ui.currentKeyDelete_BTN.clicked.connect(self.currentKeyDeleteFunc)
        self.ui.allKeyDelete_BTN.clicked.connect(self.allKeyDeleteFunc)

        self.ui.help_BTN.clicked.connect(self.open_webbrowser)
    ##############################################################################################
    
    ##############################################################################################
    def takeCheck(self):
        status = False
        if self.constraintList:
            index_ = self.ui.constraint_CBX.currentIndex()
            currentTake = FBSystem().CurrentTake.LongName
            model_ = str(self.ui.target_BTN.text())
            if model_.find(":") != -1:
                model_ = model_.replace(":" , ">")
            if currentTake.find(":") != -1:
                currentTake = model_.replace(":" , ">")
            constName = "TT_" + model_ + "_" + currentTake + "_Constraint"
            if self.constraintList[index_].Name == constName:
                status = True 
                self.ui.status_LED.setText("Connect!")
                self.ui.status_LED.setStyleSheet("color : lime")
            else:
                status = False
                self.ui.status_LED.setText('Please Click "Make" or "Find" Button')
                self.ui.status_LED.setStyleSheet("color : red")
        else:
            self.ui.status_LED.setText('Please Click "Make" or "Find" Button')
            self.ui.status_LED.setStyleSheet("color : red")
        return status 
    def open_webbrowser(self):
        # if you want please remember to check its valid url or not
        url = "https://wiki.ncsoft.com/pages/viewpage.action?pageId=511865637#id-%EB%AA%A8%EC%85%98%EB%B9%8C%EB%8D%94%ED%88%B4%EC%A0%9C%EC%9E%91RND-MultiConstraintTool"
        webbrowser.open(url)
    
    def sceneRefresh(self):
        f = FBSystem().LocalTime.GetFrame()
        FBPlayerControl().Goto(FBTime(0,0,0,f+1,0))
        FBPlayerControl().Goto(FBTime(0,0,0,f,0))
        FBSystem().Scene.Evaluate()
    def HUD_Clear(self):
        lScene = FBSystem().Scene
        lConstraints = lScene.Components
        for each in lConstraints:
            if each.ClassName() == "FBHUD":
                each.FBDelete()
            elif each.ClassName() == "FBHUDTextElement":
                each.FBDelete()
            else:
                pass
    def HUD_TextElement(self):
        textElement_list = []
        const = None
        Scene = FBSystem().Scene
        index_ = self.ui.constraint_CBX.currentIndex()
        lConstraints = Scene.Constraints
        for each in lConstraints:
            if each.ClassName() == "FBConstraint":
                try:
                    if each.LongName == self.constraintList[index_].LongName :
                        const = each
                except:
                    pass
        if const:
            len_ = const.ReferenceGetCount(1)
            for i in range(len_):
                name_ = const.ReferenceGet(1,i).LongName
                property_ = name_+".Weight"
                HUDTextElement = FBHUDTextElement("None")
                HUDTextElement.X = 0
                HUDTextElement.Y = -(i * 5)
                HUDTextElement.Justification = FBHUDElementHAlignment.kFBHUDLeft
                HUDTextElement.HorizontalDock = FBHUDElementHAlignment.kFBHUDLeft
                HUDTextElement.VerticalDock = FBHUDElementVAlignment.kFBHUDTop
                HUDTextElement.Content = name_ + " : %d" 
                HUDTextElement.PropertyAddReferenceProperty(const.PropertyList.Find(property_))
                HUDTextElement.Height = 5
                textElement_list.append(HUDTextElement)
        return textElement_list

    def hudOnOffFunc(self):
        #Init
        Scene = FBSystem().Scene
        teList = []
        if not self.HUD:
            teList = self.HUD_TextElement()
            if teList:
                self.HUD = FBHUD("MyHUD")
                Scene.ConnectSrc(self.HUD)          # Connect the HUD to the scene
                #HUDTextElement.Content = "Source1 : %d \nSource2 : %d"
                
                for i in teList:
                    self.HUD.ConnectSrc(i) 
                Scene.Cameras[0].ConnectSrc(self.HUD)
                self.ui.hudOnOff_BTN.setStyleSheet("background-color : green")
        else:
            Scene.DisconnectSrc(self.HUD) 
            Scene.Cameras[0].DisconnectSrc(self.HUD)
            for i in teList:
                i.FBDelete()
            self.HUD.FBDelete()
            del (self.HUD , teList)
            self.HUD = None
            for i in range(3):
                self.HUD_Clear()
            self.ui.hudOnOff_BTN.setStyleSheet("background-color : red")
    def mcSnapKeyFunc(self , i):
        status = self.takeCheck()
        if status:
            if self.constraintList:
                constraintIndex = self.ui.constraint_CBX.currentIndex()
                pModel = self.constraintList[constraintIndex].ReferenceGet(0,0)
                pAlignTo = self.constraintList[constraintIndex].ReferenceGet(1,i)
                
                mc.MCAlign( pModel, pAlignTo)
                self.sceneRefresh()
                mc.MCSetKey(self.constraintList[constraintIndex],False,i)
    def mcOffsetKeyFunc(self , i):
        status = self.takeCheck()
        if status:
            if self.constraintList:
                constraintIndex = self.ui.constraint_CBX.currentIndex()
                mc.MCSetKey(self.constraintList[constraintIndex],False,i)
            
    def TableWidgetClicked(self,row,col):
        if col == 1:
            status = self.takeCheck()
            if status:
                if self.constraintList:
                    constraintIndex = self.ui.constraint_CBX.currentIndex()
                    
                    n = self.constraintList[constraintIndex].ReferenceGet(1,row)
                    self.ClearSelModel()
                    n.Selected = True
    

    def refreshFunc(self):
        self.constraintListUp()
        self.constFindFunc()
        self.defaultSet()
        self.hudOnOffFunc()
        self.hudOnOffFunc()

    def targetSelect(self):
        modelList = FBModelList()
        FBGetSelectedModels (modelList, None, True)
        if len(modelList) == 1:
            if modelList[0].LongName != str(self.ui.target_BTN.text()):
                self.ui.sourceList_TWG.clear()
                self.ui.target_BTN.setText(modelList[0].LongName)
                self.constraintListUp()
                self.constFindFunc()
                self.defaultSet()
                self.takeCheck()

    def constraintChange(self):
        index_ = self.ui.constraint_CBX.currentIndex()
        if self.constraintList:
            
            mc.MCChangeConst(self.constraintList,index_)
        
            self.ClearSelModel()
            self.constraintList[index_].Weight.SetAnimated(True)
            self.constraintList[index_].Selected = True
            
            self.defaultSet()
            self.hudOnOffFunc()
            self.hudOnOffFunc()
            self.takeCheck()
    def constFindFunc(self):
        lSystem = FBSystem()
        lTakeNameCurrent = lSystem.CurrentTake.LongName
        if len(lTakeNameCurrent.split(":")) >= 2 :
            lTakeNameCurrent = lSystem.CurrentTake.LongName.replace(":" , ">")
        else:
            lTakeNameCurrent = lSystem.CurrentTake.LongName
        for i,const in enumerate(self.constraintList):
            
            if const.Name.find(lTakeNameCurrent) != -1 :
                
                mc.MCChangeConst(self.constraintList,i)
                self.ui.constraint_CBX.setCurrentIndex(i)
        self.takeCheck()
        
    def constMakeFunc(self):
        dst = FBFindModelByLabelName(str(self.ui.target_BTN.text()))
        if dst:
            if not str(self.ui.target_BTN.text()).find(":") == -1:
                name = dst.LongName.replace(":" , ">")
            else:
                name = dst.LongName
            if not FBSystem().CurrentTake.LongName.find(":") == -1:
                Tname = FBSystem().CurrentTake.LongName.replace(":" , ">")
            else:
                Tname = FBSystem().CurrentTake.LongName
            confirm = 'TT_'+name+'_'+ Tname +'_Constraint'
            self.constraintListUp()
            constList = []
            for each in self.constraintList:
                if each.ClassName() == "FBConstraint":
                    constList.append(each.Name)
            
            if not confirm in constList:
                mc.MCCreateConst(dst)
                # add string property
                constList.append(confirm)
                self.constraintListUp()
                index = constList.index(confirm)
                mc.MCChangeConst(self.constraintList,index)
                self.defaultSet()
                self.ui.constraint_CBX.setCurrentIndex(index)
            else:
                self.constFindFunc()
            self.takeCheck()

    def constDeleteFunc(self):
        index_ = self.ui.constraint_CBX.currentIndex()
        if self.constraintList:
            self.constraintList[index_].FBDelete()
            self.constraintListUp()
            self.defaultSet()
            self.hudOnOffFunc()
            self.hudOnOffFunc()
            self.takeCheck()

    def addButtonFunc(self):
        status = self.takeCheck()
        if status:
            index_ = self.ui.constraint_CBX.currentIndex()
            modelList = FBModelList()
            FBGetSelectedModels (modelList, None, True)
            
            if len(modelList) == 1:
                if self.constraintList:
                    self.constraintList[index_].Active = False
                    self.constraintList[index_].ReferenceAdd(1 , modelList[0])
                    self.constraintList[index_].Snap()
                    if self.constraintList[index_].ReferenceGetCount(1) == 1:
                        self.constraintList[index_].PropertyList.Find(modelList[0].LongName + ".Weight").Data = 100
                    else:
                        self.constraintList[index_].PropertyList.Find(modelList[0].LongName + ".Weight").Data = 0
                    mc.MCAddParent(self.constraintList[index_])
                    self.defaultSet()
                    self.hudOnOffFunc()
                    self.hudOnOffFunc()
                    #self.constraintList[index_].PropertyCreate(modelList[0].LongName, FBPropertyType.kFBPT_charptr, 'String', False, True, None)

    def removeButtonFunc(self,i):
        status = self.takeCheck()
        if status:
            constraintIndex = self.ui.constraint_CBX.currentIndex()
            sourceModel = self.constraintList[constraintIndex].ReferenceGet(1,i)
            index_ = self.ui.constraint_CBX.currentIndex()
            self.constraintList[index_].ReferenceRemove(1,sourceModel)
            self.defaultSet()
            self.hudOnOffFunc()
            self.hudOnOffFunc()
    
    def currentKeyDeleteFunc(self):
        status = self.takeCheck()
        if status:
            index_ = self.ui.constraint_CBX.currentIndex()
            fcurve_ = mc.MCGetFCrv(self.constraintList[index_])
            mc.MCDelCurrentKey(fcurve_)
            self.sceneRefresh()
            self.hudOnOffFunc()
            self.hudOnOffFunc()

    def allKeyDeleteFunc(self):
        status = self.takeCheck()
        if status:
            saveOffset = []
            weightOnIndex = 0
            index_ = self.ui.constraint_CBX.currentIndex()
            Const = self.constraintList[index_]
            #Tgt = Const.ReferenceGet(0,0)
            len = Const.ReferenceGetCount(1)
            for i in range(len):
                model_ = Const.ReferenceGet(1,i)
                if Const.PropertyList.Find(model_.LongName + ".Weight").Data == 100:
                    weightOnIndex = i
                    KeyProperty = ['Offset T','Offset R','Offset S']
                    
                    Src = Const.ReferenceGet(1,i)
                    for KeyProp in KeyProperty:
                        saveOffset.append(Const.PropertyList.Find(Src.LongName+'.'+KeyProp).Data)
                else:
                    pass
            
            fcurve_ = mc.MCGetFCrv(Const)
            mc.MCClearKey(fcurve_)
            mc.MCEditConstWeight(Const,0)
            Const.PropertyList.Find(Const.ReferenceGet(1,weightOnIndex).LongName + ".Weight").Data = 100
            KeyProperty = ['Offset T','Offset R','Offset S']
            
            Src = Const.ReferenceGet(1,weightOnIndex)
            for i in range(3):
                Const.PropertyList.Find(Src.LongName+'.'+KeyProperty[i]).Data = saveOffset[i]
        
            self.sceneRefresh()
            self.hudOnOffFunc()
            self.hudOnOffFunc()
    
    def ClearSelModel(self):
        modelList = FBModelList()
        FBGetSelectedModels (modelList, None, True)
        for model in modelList:
            model.Selected = False
        if self.constraintList:
            for const in self.constraintList:
                const.Selected = False
                

# -----------------------------------------------------------------------------------------------


gToolName = "Multi Constraint Window"
gDEVELOPMENT = True
if gDEVELOPMENT:
    FBDestroyToolByName(gToolName)
    
if gToolName in FBToolList:
    tool = FBToolList[gToolName]
    ShowTool(tool)
else:
    tool = NativeQtWidgetTool(gToolName)
    FBAddTool(tool)
    if gDEVELOPMENT:
        ShowTool(tool)



