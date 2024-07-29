# -*- coding: utf-8 -*-
import inspect
try:
    from PySide import  QtGui as widgets
    from PySide import QtGui as gui
    from PySide import QtCore, QtUiTools
except:
    from PySide2 import  QtWidgets as widgets
    from PySide2 import QtGui as gui
    from PySide2 import QtCore, QtUiTools

import shiboken2
from pyfbsdk import*
from pyfbsdk_additions import*
import os

curPath = inspect.getfile(lambda: None)
curPath = os.path.abspath(curPath + '/../')

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
        self.StartSizeX = 400
        self.StartSizeY = 300
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
        self.buildUI()
        self.defaultSet()
        self.connectSignal()
  
    def loadUIWidget(self, uiFileName, parent=None):
        loader = QtUiTools.QUiLoader()
        uiFile = QtCore.QFile(uiFileName)
        uiFile.open(QtCore.QFile.ReadOnly)
        ui = loader.load(uiFile, parent)
        uiFile.close()
        return ui

    def buildUI(self):
        self.parent().setLayout(widgets.QVBoxLayout())
        uiFile = curPath + '\\rigBatch.ui'
        self.ui = self.loadUIWidget(uiFile)
        self.parent().layout().addWidget(self.ui)

    
    # Default UI setting 
    def defaultSet(self):
        self.srcPath = ""
        self.dstPath = ""
        self.rigPath = ""
        

    def setProgress(self,pgbItem,value):
        pgbItem.setValue(value)
        QtCore.QCoreApplication.processEvents()
        FBSystem().Scene.Evaluate()

    def connectSignal(self):

        
        self.ui.sourcefolder_BTN.clicked.connect(self.srcBrowser)

        self.ui.newrig_BTN.clicked.connect(self.rigBrowser)
        
        self.ui.batchrig_BTN.clicked.connect(self.main)
       

    def srcBrowser(self):
        self.expPath = widgets.QFileDialog.getExistingDirectory(self, 'Select export directory ...','/home/',
                                                        widgets.QFileDialog.DontUseNativeDialog )
        self.ui.sourcefolder_LED.setText(self.expPath)
        self.srcPath = str(self.ui.sourcefolder_LED.text())
        self.dstPath = self.srcPath.replace("/"+ self.srcPath.rpartition("/")[-1] , "/rigbatch_dst")
        print(self.dstPath)
        if not os.path.exists(self.dstPath):
            os.makedirs(self.dstPath)
        

    def rigBrowser(self):
        self.expPath = widgets.QFileDialog.getOpenFileName(self, 'Select rig file ...','Z:/P4V/LLL/LllArt/Rigging',
                                                        "Files(*.fbx)" )
        
        self.ui.newrig_LED.setText(self.expPath[0])
        self.rigPath = str(self.ui.newrig_LED.text())
        

    def openBrowser(self):
        expPath = str(self.ui.expPath_LIE.text())
        os.startfile(expPath)

    def characterRootFind(self):
        
        pList = FBApplication().CurrentCharacter.GetModel(FBBodyNodeId.kFBHipsNodeId)
        
        asset = pList
        while asset.Parent:
            asset = asset.Parent
        return asset
    
    def GetBranch(self,InputRoot):
        ReturnList = []
        ReturnList.append(InputRoot)
        try:
            Children = InputRoot.Children
        except:
            Children = None
            
        if Children != None:
            for i in Children:
                ReturnList = ReturnList+self.GetBranch(i)
        return ReturnList

    def delBranch(self,list_):
        
        for i in reversed(list_):    
            i.FBDelete()

    def selectBranch(self,root):
        
        root.Selected = True 
        for child in root.Children:
            if child.ClassName() == "FBModelSkeleton":
                child.Selected = True
            
            self.selectBranch(child)

    def ClearSelModel(self):
        modelList = FBModelList()
        FBGetSelectedModels (modelList, None, True)
        for model in modelList:
            model.Selected = False

    def skinfind(self,modelList):
        for i in modelList:
            skinlist = FBModelList()
            if i.ClassName() == "FBModelSkeleton":
                i.GetSkinModelList(skinlist)

            else:    
                i.FBDelete()

            for ii in skinlist:
                ii.Selected = True

    def CreateParentConstraint(self,parent, child, offset): 
        ##Get Object By Name
        
        
        ##Set Parent Object    
        objParent = parent
        ##Set Child Object
        objChild = child
        
        ##Create "Parent/Child" Constraint 
        for i in range( FBConstraintManager().TypeGetCount() ):
            if "Parent/Child" in FBConstraintManager().TypeGetName(i):
                lMyConstraint = FBConstraintManager().TypeCreateConstraint(i)
            
        #for index, element in enumerate(selected_objects):
        lMyConstraint.ReferenceAdd (0, objChild)
        lMyConstraint.ReferenceAdd (1, objParent)
        
        #Snap if user desires
        if offset == True:
            lMyConstraint.Snap()

        ##Activate Constraint
        lMyConstraint.Active = True
    
    def PlotSelected(self):
        lOptions = FBPlotOptions () 
        lOptions.ConstantKeyReducerKeepOneKey = False#True
        lOptions.PlotAllTakes = True
        lOptions.PlotOnFrame = True
        lOptions.PlotPeriod = FBTime ( 0, 0, 0, 1 ) 
        lOptions.PlotTranslationOnRootOnly = False 
        lOptions.PreciseTimeDiscontinuities = False 
        lOptions.RotationFilterToApply = FBRotationFilter.kFBRotationFilterUnroll
        lOptions.UseConstantKeyReducer = False
        FBSystem().CurrentTake.PlotTakeOnSelected(lOptions )
        FBSystem().Scene.Evaluate()
        del(lOptions)

    def main(self):
        oApp=FBApplication()
        saveOption = 1
        srcPath = self.srcPath
        dstPath = self.dstPath
        rigPath = self.rigPath
        lastone = None
        self.setProgress(self.ui.inprogress_PGB , 0)
        int_ = 0
        
        add_ = int(100/len(os.listdir(srcPath)))
        
        for oFile in os.listdir(srcPath):
            oFbOp=FBFbxOptions(True)
            oFbOp.SetAll(FBElementAction.kFBElementActionAppend,True)
            oFbOp.BaseCameras = True
            oFbOp.CameraSwitcherSettings = True
            oFbOp.CurrentCameraSettings = True
            oFbOp.TransportSettings = True
            oFbOp.GlobalLightingSettings = True
            print("file : " , oFile)
            int_ = int_+add_
            self.setProgress(self.ui.inprogress_PGB , int(int_* 0.75))
            if oFile.endswith(".fbx"):
                FbxFile=os.path.join(srcPath,oFile)
                oApp.FileNew()
                self.setProgress(self.ui.inprogress_PGB , int(int_* 0.77))
                oApp.FileOpen(FbxFile,False,oFbOp)
                
                for i in FBSystem().Scene.Takes:
                    print(i.Name)


                characters = FBSystem().Scene.Characters
                charList = [x.LongName for x in characters]
                controlRigs = FBSystem().Scene.ControlSets
                reference=characters[0].GetCtrlRigModel(FBBodyNodeId.kFBReferenceNodeId)
                matList = FBSystem().Scene.Materials
                nameSpace = ""     
                conNameSpace = ""
                charNameSpace = ""
                skinNameSpace = ""
                rigNameSpace = ""
                matNameSpace = ""

                addNS = "rebuild_for_retarget"
               
                #############################################
                if len(charList) == 1:
                    FBApplication().CurrentCharacter = characters[0]
                    root_ = self.characterRootFind()
                    if root_.LongName.find(":") != -1:
                        nameSpace = root_.LongName.split(":")[0]
                    if controlRigs[0].LongName.find(":") != -1:
                        conNameSpace = controlRigs[0].LongName.split(":")[0]
                    if characters[0].LongName.find(":") != -1:
                        charNameSpace = characters[0].LongName.split(":")[0]    
                    if reference.LongName.find(":") != -1:
                        rigNameSpace = reference.LongName.split(":")[0]    
                    if matList[0].LongName.find(":") != -1:
                        matNameSpace = matList[0].LongName.split(":")[0]    
                    self.ClearSelModel()
                    self.selectBranch(root_)
                    
                    selectedModels = FBModelList()
                    FBGetSelectedModels(selectedModels,None , True,True)
                    #FBGetSelectedModels(self.selectedModels)
                    #skel , con, char select
                    self.ClearSelModel()
                    self.skinfind(selectedModels)
                    
                    skinModels = FBModelList()
                    FBGetSelectedModels(skinModels,None , True,True)
                    if skinModels[0].LongName.find(":") != -1:
                        skinNameSpace = skinModels[0].LongName.split(":")[0]

                    if nameSpace:
                        root_.ProcessNamespaceHierarchy(FBNamespaceAction.kFBRemoveAllNamespace, nameSpace)
                    if charNameSpace:
                        characters[0].ProcessNamespaceHierarchy(FBNamespaceAction.kFBRemoveAllNamespace, charNameSpace)
                    if conNameSpace:
                        controlRigs[0].ProcessNamespaceHierarchy(FBNamespaceAction.kFBRemoveAllNamespace, conNameSpace)
                    if skinNameSpace:
                        for x in skinModels:
                            x.ProcessNamespaceHierarchy(FBNamespaceAction.kFBRemoveAllNamespace, skinNameSpace)
                    if rigNameSpace:
                        reference.ProcessNamespaceHierarchy(FBNamespaceAction.kFBRemoveAllNamespace, rigNameSpace)
                    if matNameSpace:
                        for x in matList:
                            x.ProcessNamespaceHierarchy(FBNamespaceAction.kFBRemoveAllNamespace, matNameSpace)
                    
                    root_.ProcessNamespaceHierarchy(FBNamespaceAction.kFBConcatNamespace, addNS)
                    characters[0].ProcessNamespaceHierarchy(FBNamespaceAction.kFBConcatNamespace, addNS)
                    controlRigs[0].ProcessNamespaceHierarchy(FBNamespaceAction.kFBConcatNamespace, addNS)
                    for x in range(len(skinModels)):
                        if x == 0:
                            parent_ = skinModels[x]
                            parent_.ProcessNamespaceHierarchy(FBNamespaceAction.kFBConcatNamespace, addNS)
                            while parent_.Parent:
                                parent_ = parent_.Parent
                                parent_.ProcessNamespaceHierarchy(FBNamespaceAction.kFBConcatNamespace, addNS)
                        else:
                            skinModels[x].ProcessNamespaceHierarchy(FBNamespaceAction.kFBConcatNamespace, addNS)
                    
                    reference.ProcessNamespaceHierarchy(FBNamespaceAction.kFBConcatNamespace, addNS)
                    for x in matList:
                        x.ProcessNamespaceHierarchy(FBNamespaceAction.kFBConcatNamespace, addNS)
                    
                    
                    #############################################
                    oFbOp2=FBFbxOptions(True,rigPath)
                    for lTakeIndex in range( 0, oFbOp2.GetTakeCount() ):
                        oFbOp2.SetTakeSelect( lTakeIndex, False )

                    oFbOp2.SetAll(FBElementAction.kFBElementActionMerge,True)
                    oFbOp2.TakeSpan = FBTakeSpanOnLoad.kFBLeaveAsIs
                    newTake = FBSystem().CurrentTake.CopyTake("asdiof_jwoiejfoi_wejg_ioajwoie_gjoaiwejgo_iaje_sgo_ij")
                    FBSystem().CurrentTake = newTake

                    print("rig : " ,rigPath)
                    oApp.FileMerge(rigPath,False,oFbOp2)
                    newTake.FBDelete()

                    #############################################
                    characters2 = FBSystem().Scene.Characters
                    FBApplication().CurrentCharacter = characters2[-1]
                    
                    #FBApplication().CurrentCharacter.ActiveInput = 1
                    FBApplication().CurrentCharacter.InputCharacter = characters2[0]

                    FBApplication().CurrentCharacter.InputType = FBCharacterInputType.kFBCharacterInputCharacter
                    
                    character = FBApplication().CurrentCharacter
                    solver = character.GetExternalSolver()
                    active_source = character.PropertyList.Find('Active Source')
                    #left_shoulder_property = solver.PropertyList.Find('Reach Left Shoulder')
                    #right_shoulder_property = solver.PropertyList.Find('Reach Right Shoulder')
                    #left_hand_reach_t_property = character.PropertyList.Find('Left Hand Reach T')
                    #right_hand_reach_t_property = character.PropertyList.Find('Right Hand Reach T')
                    #left_hand_reach_r_property = character.PropertyList.Find('Left Hand Reach R')
                    #right_hand_reach_r_property = character.PropertyList.Find('Right Hand Reach R')

                    active_source.Data = True
                    #left_shoulder_property.Data = 100.0 
                    #right_shoulder_property.Data = 100.0
                    #left_hand_reach_t_property.Data = 100.0
                    #right_hand_reach_t_property.Data = 100.0
                    #left_hand_reach_r_property.Data = 100.0
                    #right_hand_reach_r_property.Data = 100.0
                            
                
                    
                    myPlotOptions = FBPlotOptions ()
                    myPlotOptions.PlotTangentMode = FBPlotTangentMode.kFBPlotTangentModeAuto
                    myPlotOptions.ConstantKeyReducerKeepOneKey = False
                    myPlotOptions.PlotAllTakes = True
                    myPlotOptions.PlotOnFrame = True
                    myPlotOptions.PlotPeriod = FBTime ( 0, 0, 0, 1 )
                    myPlotOptions.PlotTranslationOnRootOnly = False
                    myPlotOptions.PreciseTimeDiscontinuities = False
                    myPlotOptions.RotationFilterToApply = FBRotationFilter.kFBRotationFilterUnroll
                    myPlotOptions.UseConstantKeyReducer = False

                    TheChar = FBApplication().CurrentCharacter
                    TheChar.PlotAnimation(FBCharacterPlotWhere.kFBCharacterPlotOnSkeleton, myPlotOptions)  
                    TheChar.PlotAnimation(FBCharacterPlotWhere.kFBCharacterPlotOnControlRig, myPlotOptions)        

                    #FBApplication().CurrentCharacter = characters2[0]
                    #FBApplication().CurrentCharacter.SetCharacterizeOff()
                    self.setProgress(self.ui.inprogress_PGB , int_)
                    lFBList = [FBSystem().Scene.Constraints, FBSystem().Scene.Handles, FBSystem().Scene.UserObjects,  FBSystem().Scene.Shaders, FBSystem().Scene.Textures, FBSystem().Scene.Folders, FBSystem().Scene.Groups,
                    FBSystem().Scene.ObjectPoses, FBSystem().Scene.CharacterPoses, FBSystem().Scene.KeyingGroups, FBSystem().Scene.Notes, FBSystem().Scene.VideoClips, FBSystem().Scene.RootModel.Children,FBSystem().Scene.Components]
                    singleList = [FBSystem().Scene.ControlSets, FBSystem().Scene.CharacterExtensions,
                    FBSystem().Scene.Characters, FBSystem().Scene.Materials]
                    remove_list = []
                    remove_debug = []
                    self.ClearSelModel()
                    for items in lFBList:
                        for i in items:
                            try:
                                if i.LongName.split(":")[0] == "rebuild_for_retarget":
                                    
                                    while i.Parent:
                                        i = i.Parent

                                    if not i.LongName in remove_debug:

                                        remove_list.extend([i])
                                        remove_debug.append(i.LongName)
                            except:
                                pass
                    for items in singleList:
                        for i in items:
                            try:
                                if i.LongName.split(":")[0] == "rebuild_for_retarget":

                                    if not i.LongName in remove_debug:

                                        remove_list.extend([i])
                                        remove_debug.append(i.LongName)
                            except:
                                pass
                    print(remove_debug)
                   
                    #root bake
                    rootM = FBFindModelByLabelName("root")
                    
                    for i in remove_list:
                        if i.ClassName() != "FBModelSkeleton":
                            self.delBranch(self.GetBranch(i))    
                        else:
                            lastone = i

                    print (lastone.LongName , rootM.LongName)
                    self.CreateParentConstraint(lastone , rootM , False)
                    self.ClearSelModel()
                    rootM.Selected = True
                    self.PlotSelected()

                    self.delBranch(self.GetBranch(lastone))
                    self.setProgress(self.ui.inprogress_PGB , int_)
                    
                    if saveOption ==1:
                        oSaveFilePath=os.path.join(dstPath,oFile)
                        oFbSOp=FBFbxOptions(False)
                        oFbSOp.EmbedMedia=False
                        
                        oApp.FileSave(oSaveFilePath,oFbSOp)
                    
                    del(skinModels,selectedModels,lastone,oFbOp,oFbOp2,newTake,myPlotOptions)
        del(int_ , add_)

        self.setProgress(self.ui.inprogress_PGB , 100)
        FBMessageBox( 'StatusWindow', 'Complete!!', "Ok" )
                   
gToolName = "RIg Batch v1.02"
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

 


