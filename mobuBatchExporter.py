# !/usr/bin/env python
# -*- coding: utf-8 -*-

#-----------------------------------------------------------------------------------------------
import os
import stat
import inspect
import importlib
import csv
import json
import socket
curPath = inspect.getfile(lambda: None)
curPath = os.path.abspath(curPath + '/../')
# import Module
import CLS_rootMotion as rm;importlib.reload(rm)
import ReadyToExport as RTE;importlib.reload(RTE)
import CLS_sendBoneAniToRig as ar;importlib.reload(ar)

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
        self.StartSizeX = 1000
        self.StartSizeY = 1000
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
        self.fingerExtract = ["thumb_04_r","index_04_r","middle_04_r","ring_04_r","pinky_04_r",
                            "thumb_04_l","index_04_l","middle_04_l","ring_04_l","pinky_04_l"]
        
        self.weaponPlotList = ["ik_hand_gun_root" , "ik_hand_gun" ,"ik_hand_p_l" ,"ik_hand_l" , "ik_hand_p_r" , "ik_hand_r"]
        self.armExtract = ["clavicle_l" , "clavicle_r" , "spine_04_extra02_r" , "spine_04_extra01_l"]
        self.check_characterize = ['pelvis','clavicle_l','upperarm_l','lowerarm_l','hand_l','calf_l','thigh_l','foot_l']


    def loadUIWidget(self, uiFileName, parent=None):
        loader = QtUiTools.QUiLoader()
        uiFile = QtCore.QFile(uiFileName)
        uiFile.open(QtCore.QFile.ReadOnly)
        ui = loader.load(uiFile, parent)
        uiFile.close()
        return ui

    def buildUI(self):
        self.parent().setLayout(widgets.QVBoxLayout())
        uiFile = curPath + '\\mobuBatchExporter_ui.ui'
        self.ui = self.loadUIWidget(uiFile)
        self.parent().layout().addWidget(self.ui)

    def characterListSetting(self):
        self.ui.Asset_LWG.clear()
        CharInScene = []
        for character in FBSystem().Scene.Characters:
            CharInScene.append(character.LongName)
        self.ui.Asset_LWG.addItems(CharInScene)
        if CharInScene:
            self.ui.Asset_LWG.setCurrentRow(0)
            self.AssetName = self.ui.Asset_LWG.currentItem().text()
            index_ = self.ui.Asset_LWG.selectedIndexes()[0]
            row = index_.row()
            FBApplication().CurrentCharacter = FBSystem().Scene.Characters[row]
            confirm_ = self.characterRootFind(FBApplication().CurrentCharacter).LongName
            confirm_len = confirm_.split(":")
            if len(confirm_len) > 1 :
                self.n_s = confirm_len[0]+":"

    # Default UI setting 
    def handleButton(self,state,checkbox):
    
        if state == 2:
            for ii,name in enumerate(self.checkBoxList):
                if checkbox == name:
                    modifiers = widgets.QApplication.keyboardModifiers()
                    if modifiers == QtCore.Qt.ShiftModifier:
                        if self.stack != None:
                            if self.stack < ii:
                                for iii in range(self.stack , ii+1):
                                    self.checkBoxList[iii].setChecked(True)
                                
                        else:
                            self.stack = ii
                    else:
                        self.stack = ii
                        
    def defaultSet(self):
        
        self.stack = None
        
        self.checkState = 0
        self.current_OutputPath = None
        self.BAKE_BONE = "root"
        self.n_s = ""
        
        self.AssetName = None
        save_path = QtCore.QDir.homePath()
        self.buPath = os.path.join(save_path , "MOBU_TEMP_PATH.json")
        
        if os.path.exists(self.buPath):
            with open(self.buPath) as f:
                json_object = json.load(f)
                self.current_OutputPath = json_object["expPath"]
                self.ui.expPath_LIE.setText(self.current_OutputPath)
               
        else:
            json_object = {
                "expPath" : None
            }
            with open(self.buPath, 'w') as f:
                json.dump(json_object, f, indent=2)
            
        self.characterListSetting()
        self.checkBoxList = []
        self.progressList = []
        self.lineEdit2List = []

        self.current_take = FBSystem().Scene.Takes
        self.listTakeName = [x.Name for x in self.current_take]
        self.ui.FbxList_TWG.setRowCount(len(self.listTakeName))
        self.ui.FbxList_TWG.setColumnCount(3)
        self.ui.FbxList_TWG.setHorizontalHeaderLabels(["/", "Takes Name","Progress"])

        for i,v in enumerate(self.listTakeName):
            
            ckbox = widgets.QCheckBox()
            print(ckbox)
            ckbox.setStyleSheet("QCheckBox::indicator { width:20px; height: 20px;} QCheckBox::indicator::checked {image: url(Z:/P4V/LLL/LllArt/Animation/Script/Asset/icon/checkBox.png);} QCheckBox::indicator::unchecked {image: url(Z:/P4V/LLL/LllArt/Animation/Script/Asset/icon/uncheckBox.png);}")
            ckbox.setChecked(True)
            self.checkBoxList.append(ckbox)

            le2 = widgets.QLineEdit()
            le2.setText(v)
            le2.adjustSize()
            self.lineEdit2List.append(le2)
            pgb = widgets.QProgressBar()
            self.progressList.append(pgb)
            self.ui.FbxList_TWG.setCellWidget(i,0,ckbox)
            #self.ui.FbxList_TWG.setItem(i,1,widgets.QTableWidgetItem(v))
            self.ui.FbxList_TWG.setCellWidget(i,1,le2)
            self.ui.FbxList_TWG.setCellWidget(i,2,pgb)
            for x in self.progressList:
                x.reset()
                x.setEnabled(False)
        
        self.ui.FbxList_TWG.setSortingEnabled(False)
        self.ui.FbxList_TWG.resizeRowsToContents()
        self.ui.FbxList_TWG.resizeColumnsToContents()
        self.ui.FbxList_TWG.setColumnWidth(0,20)
        self.ui.FbxList_TWG.setColumnWidth(1,300)
        self.ui.FbxList_TWG.setColumnWidth(2,40)
        
        for ii ,name in enumerate(self.checkBoxList):
            name.stateChanged.connect(lambda state , checkbox = self.checkBoxList[ii]: self.handleButton(state, checkbox))
        for i ,name in enumerate(self.lineEdit2List):
            name.textChanged.connect(lambda: self.textChange(i))
    
                  
    def textChange(self , i):
        for i,take in enumerate(FBSystem().Scene.Takes):
            if take.Name == self.listTakeName[i] or take.Name == "1":

                take.Name = str(self.lineEdit2List[i].text())
                self.listTakeName[i] = str(self.lineEdit2List[i].text())
                
    def connectSignal(self):

        self.ui.Asset_LWG.itemClicked.connect(self.selectCharFunc)
        
        self.ui.FbxList_TWG.horizontalHeader().sectionClicked.connect(self.sectionClickedFunc)

        self.ui.Export_BTN.clicked.connect(self.doExport)

        self.ui.openDir_BTN.clicked.connect(self.openBrowser)
        
        self.ui.expPath_BTN.clicked.connect(self.setExpFolder)
        
        self.ui.refresh_BTN.clicked.connect(self.refreshBtn_func)
        self.ui.expPath_LIE.textChanged.connect(self.expPathChange)
        self.ui.plot_BTN.clicked.connect(self.doPlot)

    def expPathChange(self):
        path = str(self.ui.expPath_LIE.text()).replace("\\" , "/")
        self.current_OutputPath = path
        with open(self.buPath) as f:
            json_object = json.load(f)
            json_object["expPath"] = path
        with open(self.buPath , 'w' ) as f:
            json.dump(json_object, f, indent=2)

    def refreshBtn_func(self):      
        self.defaultSet()

    def openBrowser(self):
        expPath = str(self.ui.expPath_LIE.text())
        os.startfile(expPath)

    def ClearSelModel(self):
        modelList = FBModelList()
        FBGetSelectedModels (modelList, None, True)
        for model in modelList:
            model.Selected = False

    def characterRootFind(self,FBcharacter):
        pList = FBcharacter.PropertyList.Find("HipsLink")
        asset = pList[0]
        while asset.Parent:
            asset = asset.Parent
        return asset

    def SelectBranch(self,topModel):
        
        for childModel in topModel.Children:
            self.SelectBranch(childModel)
        topModel.Selected = True
        topModel.PropertyList.Find("Show").Data = True

    def SelectBranchFalse(self,topModel):
        for childModel in topModel.Children:
            self.SelectBranchFalse(childModel)
        topModel.Selected = False

    def SelectBranchDelete(self,topModel):
        self.ClearSelModel()
        self.SelectBranch(topModel)
        self.delete_selected_objects()
        
    def delete_selected_objects(self):
        
        selected_models = FBModelList()
        FBGetSelectedModels(selected_models)
        
        # Iterate through selected models and delete each one
        for model in selected_models:
            model.FBDelete()

    def RootBranchPlot(self):
        self.ClearSelModel()
        rootM = FBFindModelByLabelName(self.n_s + "root")
        self.SelectBranch(rootM)
        self.PlotSelected()
        self.ClearSelModel()

    
    def UE5Renamer(self,boneName):
        ignoreList = []
        matchArr = [('Skin_',''),
                    ('_JNT',''),
                    ('C_',''),
                    ('UpArm','upperarm'),
                    ('LowArm','lowerarm'),
                    ('Thumb00','thumb_01'),
                    ('Thumb01','thumb_02'),
                    ('Thumb02','thumb_03'),
                    ('Thumb03','thumb_04'),
                    ('Index00','index_metacarpal'),
                    ('Middle00','middle_metacarpal'),
                    ('Ring00','ring_metacarpal'),
                    ('Pinky00','pinky_metacarpal'),
                    ('Neck00','neck_01'),
                    ('Neck01','neck_02'),
                    ('Spine00','spine_01'),
                    ('Spine01','spine_02'),
                    ('Spine02','spine_03'),
                    ('Spine03','spine_04'),
                    ('Hand_Gun_Spine','hand_gun_root'),
                    ('Sub_Weapon','subweapon')]
        if boneName not in ignoreList:
            for i in range(0,len(matchArr)):
                boneName = boneName.replace(matchArr[i][0],matchArr[i][1])
            boneName = boneName.lower()
            getNum=0
            for i in range(0,len(boneName)):
                if boneName[i].isdigit():
                    if boneName[i-1]=='_':
                        pass
                    else:
                        getNum=i
                    break
            if getNum!=0:
                boneName=boneName[:getNum]+'_'+boneName[getNum:]
            if boneName[:2]=='l_':
                boneName = boneName[2:]+'_l'
            elif boneName[:2]=='r_':
                boneName = boneName[2:]+'_r'
        return boneName
    
    def doublePlot(self):
        
        myPlotOptions = FBPlotOptions ()
        myPlotOptions.PlotTangentMode = FBPlotTangentMode.kFBPlotTangentModeAuto
        myPlotOptions.ConstantKeyReducerKeepOneKey = False
        myPlotOptions.PlotAllTakes = False
        myPlotOptions.PlotOnFrame = True
        myPlotOptions.PlotPeriod = FBTime ( 0, 0, 0, 1 )
        myPlotOptions.PlotTranslationOnRootOnly = False
        myPlotOptions.PreciseTimeDiscontinuities = False
        myPlotOptions.RotationFilterToApply = FBRotationFilter.kFBRotationFilterUnroll
        myPlotOptions.UseConstantKeyReducer = False

        TheChar = FBApplication().CurrentCharacter
        if TheChar.ActiveInput == True:
            TheChar.PlotAnimation(FBCharacterPlotWhere.kFBCharacterPlotOnSkeleton, myPlotOptions)
            TheChar.PlotAnimation(FBCharacterPlotWhere.kFBCharacterPlotOnControlRig, myPlotOptions)         
        else:
            TheChar.PlotAnimation(FBCharacterPlotWhere.kFBCharacterPlotOnControlRig, myPlotOptions)     
            TheChar.PlotAnimation(FBCharacterPlotWhere.kFBCharacterPlotOnSkeleton, myPlotOptions)

    def PlotCharacter(self):
        
        TheChar = FBApplication().CurrentCharacter

        myPlotOptions = FBPlotOptions ()
        myPlotOptions.ConstantKeyReducerKeepOneKey = False#True
        myPlotOptions.PlotAllTakes = False
        myPlotOptions.PlotOnFrame = True
        myPlotOptions.PlotPeriod = FBTime ( 0, 0, 0, 1 )
        myPlotOptions.PlotTranslationOnRootOnly = False#True
        myPlotOptions.PreciseTimeDiscontinuities = False
        myPlotOptions.RotationFilterToApply = FBRotationFilter.kFBRotationFilterUnroll
        myPlotOptions.UseConstantKeyReducer = False
        # Below two lines are to avoid user plotting the character when the player is running.
        # Go to begining of frame would stop the player

        TheChar.PlotAnimation(FBCharacterPlotWhere.kFBCharacterPlotOnControlRig, myPlotOptions)      
        del(TheChar , myPlotOptions ) 
    

        
    def sectionClickedFunc(self,index = 0):
        if index != 2:
            if self.checkBoxList:
                if self.checkState == 0 :
                    for name in self.checkBoxList:
                        name.setChecked(False)
                        self.checkState = 1
                else:
                    for name in self.checkBoxList:
                        name.setChecked(True)
                        self.checkState = 0
        else:
            for i in self.lineEditList:
                i.setText("0")
            
    def selectCharFunc(self):
        self.AssetName = self.ui.Asset_LWG.currentItem().text()
        index_ = self.ui.Asset_LWG.selectedIndexes()[0]
        row = index_.row()
        FBApplication().CurrentCharacter = FBSystem().Scene.Characters[row]
        root = self.characterRootFind(FBApplication().CurrentCharacter)
        
        if ':' in root.LongName:
            ns = root.LongName.split(':')[0]
            self.n_s = ns + ':'
            
        else:
            ns = ""
            self.n_s = ns
       
    def setExpFolder(self):
    
        if str(self.ui.expPath_LIE.text()) == "":
            self.expPath = widgets.QFileDialog.getExistingDirectory(self, 'Select export directory ...','/home/',
                                                        widgets.QFileDialog.DontUseNativeDialog )
        else:
            self.expPath = widgets.QFileDialog.getExistingDirectory(self, 'Select export directory ...', self.current_OutputPath,
                                                        widgets.QFileDialog.DontUseNativeDialog)
        self.ui.expPath_LIE.setText(self.expPath)
        self.current_OutputPath = str(self.ui.expPath_LIE.text())

        with open(self.buPath) as f:
            json_object = json.load(f)
            json_object["expPath"] = self.current_OutputPath
        with open(self.buPath , 'w' ) as f:
            json.dump(json_object, f, indent=2)

    def check_takeList(self):
        takeList = []
        if self.checkBoxList:
            for i,na in enumerate(self.checkBoxList):
                if na.isChecked():
                    takeList.append(str(self.lineEdit2List[i].text()))
        
        return takeList
        
    def export_Animation_CurrentTake(self,takeName , headSecondary):
        lSystem = FBSystem()
        lApp = FBApplication()
        lSaveTakeNameCurrent = lSystem.CurrentTake.Name
        
        stringList = self.current_OutputPath.split("/")
        newPath = "\\".join(stringList) + "\\"
        lSaveDirRoot = "{}".format(newPath)
        
        lSavePath = lSaveDirRoot

        lSaveFileName = lSaveTakeNameCurrent

        lSaveChrAnim = lSavePath + lSaveFileName + ".fbx"
    
        # Save Animation Options
        lSaveOptions = FBFbxOptions (False) # false = will not save options 
        #lSaveOptions.SaveCharacter = True
        lSaveOptions.UseASCIIFormat = False
        lSaveOptions.SaveSelectedModelsOnly = True
        lSaveOptions.SaveControlSet = False
        lSaveOptions.SaveCharacterExtention = False
        lSaveOptions.ShowFileDialog = False
        lSaveOptions.ShowOptionslDialog = False
        lSaveOptions.BaseCameras = False
        lSaveOptions.CameraSwitcherSettings = False
        lSaveOptions.CurrentCameraSettings = False
        lSaveOptions.GlobalLightingSettings = False
        lSaveOptions.TransportSettings = False
        
        if takeName != None:
            for i in range(lSaveOptions.GetTakeCount()):
                if FBSystem().Scene.Takes[i].Name == takeName:
                    lSaveOptions.SetTakeSelect(i,True)
                else:
                    lSaveOptions.SetTakeSelect(i,False)
        else:
            pass
        
        
        self.ClearSelModel()
        

        rootM = FBFindModelByLabelName("root")
        self.SelectBranch(rootM)
        if not self.characterMode == "PWL":       
            for i in self.fingerExtract:
                i = FBFindModelByLabelName(i)
                if i:
                    i.Selected=False
 
        
        if os.path.isfile(lSaveChrAnim):
            os.chmod( lSaveChrAnim, stat.S_IWRITE )
            os.remove(lSaveChrAnim)
        lApp.FileSave(lSaveChrAnim , lSaveOptions)
        
        if headSecondary:
            if FBFindModelByLabelName("spine_04"):
                lSaveChrAnim_head = lSavePath + lSaveFileName + "_head.fbx"
                self.ClearSelModel()
            
                spineM = FBFindModelByLabelName("spine_04")
                self.SelectBranch(spineM)
                for i in self.armExtract:
                    i = FBFindModelByLabelName(i)
                    if i:
                        self.SelectBranchFalse(i)
                
                lApp.FileSave(lSaveChrAnim_head , lSaveOptions)
        # Save out animation
        #lApp.SaveCharacterRigAndAnimation(lSaveChrAnim, lSaveOptions)
        FBSystem().Scene.Evaluate()
        
        del(lSystem , lApp,lSaveTakeNameCurrent,lSaveOptions)

    def save_constraint_states(self):
        
        constraint_states = {}

        for constraint in FBSystem().Scene.Constraints:
            constraint_states[constraint.Name] = constraint.Active
        
        return constraint_states

    def disable_all_constraints(self):
        
        for constraint in FBSystem().Scene.Constraints:
            constraint.Active = False

    def restore_constraint_states(self,constraint_states):
    
        for constraint in FBSystem().Scene.Constraints:
            if constraint.Name in constraint_states:
                constraint.Active = constraint_states[constraint.Name]


    def PlotSelected(self):
        lOptions = FBPlotOptions () 
        lOptions.ConstantKeyReducerKeepOneKey = False#True
        lOptions.PlotAllTakes = False
        lOptions.PlotOnFrame = True
        lOptions.PlotPeriod = FBTime ( 0, 0, 0, 1 ) 
        lOptions.PlotTranslationOnRootOnly = False 
        lOptions.PreciseTimeDiscontinuities = False 
        lOptions.RotationFilterToApply = FBRotationFilter.kFBRotationFilterUnroll
        lOptions.UseConstantKeyReducer = False
        FBSystem().CurrentTake.PlotTakeOnSelected(lOptions )
        FBSystem().Scene.Evaluate()
        del(lOptions)

    def setProgress(self,pgbItem,value):
        pgbItem.setValue(value)
        QtCore.QCoreApplication.processEvents()
        FBSystem().Scene.Evaluate()
    
    def SetPreRotation(self,mode):
        
        TheChar = FBApplication().CurrentCharacter
        TheChar.ActiveInput =False
        self.PlotCharacter()

        p = FBFindModelByLabelName("pelvis")
        l = FBFindModelByLabelName("clavicle_l")
        r = FBFindModelByLabelName("clavicle_r")
        
        if mode:
            p.PropertyList.Find('PreRotation').Data = FBVector3d(-90,-90,0)
            l.PropertyList.Find('PreRotation').Data = FBVector3d(0,-90,0)
            r.PropertyList.Find('PreRotation').Data = FBVector3d(-180,-90,0)
        else:
            p.PropertyList.Find('PreRotation').Data = FBVector3d(0,0,0)
            l.PropertyList.Find('PreRotation').Data = FBVector3d(0,0,0)
            r.PropertyList.Find('PreRotation').Data = FBVector3d(0,0,0)
        
        self.ClearSelModel()
        p.Selected = True;r.Selected = True;l.Selected = True
    
        self.PlotSelected()
        
        self.ClearSelModel()
        
        TheChar.ActiveInput =False

    def checkInitPose(self):
        #Get InitPose
        TwistCharInitPoseFile = open('Z:\\P4V\\LLL\\LllArt\\Animation\\Script\\mobu\\MB\\Shared\\TwistCharInitPose.csv', 'r')
        rdr = csv.reader(TwistCharInitPoseFile)
        matchBone = []
        matchBoneinitRot = []
        errorLimit = float(0.1)
        initPose = ''
        initPoseTr = ''
        matchIndex = ''
        for line in rdr:
            if line[0]=='Type':
                for i in range(3,len(line)):
                    matchBone.append(line[i])
            else:
                initPose = line[1]
                initPoseTr = line[2]
                matchBool = False
                iChk = 0
                for i in range(0,len(matchBone)):
                    localTrs = FBFindModelByLabelName(self.n_s+matchBone[i]).Translation
                    initTrs = initPoseTr.split(matchBone[i])[1].split('[(')[1].split(')]')[0].split(', ')
                    jChk = 0
                    for j in range(0,len(localTrs)):
                        if (float(localTrs[j])-float(initTrs[j]))<abs(float(errorLimit)):
                            jChk = jChk+1
                        else:
                            break
                    if jChk==3:
                        iChk = iChk+1
                if iChk == len(matchBone):
                    initPose = line[1]
                    matchBool = True
                    break
        return matchBool

    def on_constraints_active_for_extrabone(self):

        bone1 = "spine_04_extra01_l"
        bone2 = "spine_04_extra02_r"
        bone1_ = FBFindModelByLabelName(bone1)
        bone2_ = FBFindModelByLabelName(bone2)
               
        for constraint in FBSystem().Scene.Constraints:
            ref_count = constraint.ReferenceGetCount(0) 
            for i in range(ref_count):
                ref = constraint.ReferenceGet(0, i)
                if ref == bone1_ or  bone2_:
                    if constraint.Active == True:
                        constraint.Active = False

    def off_constraints_active_for_extrabone(self):

        bone1 = "spine_04_extra01_l"
        bone2 = "spine_04_extra02_r"
        bone1_ = FBFindModelByLabelName(bone1)
        bone2_ = FBFindModelByLabelName(bone2)
               
        for constraint in FBSystem().Scene.Constraints:
            ref_count = constraint.ReferenceGetCount(0) 
            for i in range(ref_count):
                ref = constraint.ReferenceGet(0, i)
                if ref == bone1_ or  bone2_:
                    if constraint.Active == False:
                        constraint.Active = True
                    
    

    
    def create_parent_constraint(self,target_name, source_name):
        
        target = FBFindModelByLabelName(target_name)
        source = FBFindModelByLabelName(source_name)
        
        parent_constraint = FBConstraintManager().TypeCreateConstraint('Parent/Child')
        if parent_constraint:

            parent_constraint.ReferenceAdd(0, source)  # 소스 추가 (Parent 역할)
            parent_constraint.ReferenceAdd(1, target)  # 타겟 추가 (Child 역할)

            parent_constraint.Snap = True
            parent_constraint.Active = True
        return parent_constraint

            
    def set_world_transform_direct(self,source_bone, target_bone):
    
        world_translation = FBVector3d()
        world_rotation = FBVector3d()
        world_scaling = FBVector3d()
        
        source_bone.GetVector(world_translation, FBModelTransformationType.kModelTranslation, True)
        source_bone.GetVector(world_rotation, FBModelTransformationType.kModelRotation, True)
        source_bone.GetVector(world_scaling, FBModelTransformationType.kModelScaling, True)
        
        parent_matrix = FBMatrix()
        if target_bone.Parent:
            target_bone.Parent.GetMatrix(parent_matrix, FBModelTransformationType.kModelTransformation)
        else:
            parent_matrix.Identity()

        parent_inverse = FBMatrix()
        FBMatrixInverse(parent_inverse, parent_matrix)

        world_translation_4d = FBVector4d(world_translation[0], world_translation[1], world_translation[2], 1.0)
        local_translation_4d = FBVector4d()
        FBVectorMatrixMult(local_translation_4d, parent_inverse, world_translation_4d)
        
        local_translation = FBVector3d(local_translation_4d[0], local_translation_4d[1], local_translation_4d[2])
        
        target_bone.Translation.Data = local_translation
        target_bone.Rotation.Data = world_rotation
        
    def doPlot(self):
        if self.current_OutputPath:
            result = self.checkInitPose()
            if result:
                
                self.indexingTake = []
                takeList = self.check_takeList()
                #indexing takeList 
                for i,na in enumerate(FBSystem().Scene.Takes):
                    for x in takeList:
                        if na.Name == x:
                            self.indexingTake.append(i)
                
                if self.AssetName:
                    self.AssetName = self.ui.Asset_LWG.currentItem().text()
                    index_ = self.ui.Asset_LWG.selectedIndexes()[0]
                    row = index_.row()
                    FBApplication().CurrentCharacter = FBSystem().Scene.Characters[row]
                    
                    for ind , i in enumerate(self.indexingTake):
                        self.progressList[i].setEnabled(True)
                        self.setProgress(self.progressList[i] , 5)
                        take_ = FBSystem().Scene.Takes[i]
                        FBSystem().CurrentTake = take_

                        self.doublePlot()
                        self.setProgress(self.progressList[i] , 100)
                    for x in self.progressList:
                        x.reset()
                        x.setEnabled(False)

    def doExport(self):

        if self.current_OutputPath:
            # 나중에 어차피 다시 만듬.
            if FBFindModelByLabelName(self.n_s + "ik_foot_root"):
                ik_foot_rootM = FBFindModelByLabelName(self.n_s + "ik_foot_root")
                ik_hand_gun_rootM = FBFindModelByLabelName(self.n_s + "ik_hand_gun_root")
                self.SelectBranchDelete(ik_foot_rootM)
                self.SelectBranchDelete(ik_hand_gun_rootM)

            TheChar = FBApplication().CurrentCharacter

            # Get the list of bones characterized by the character
            bone_names = []
            check_temp_list = []
            # Iterate through standard character bones
            for bone_id in FBBodyNodeId.values:
                bone_model = TheChar.GetModel(FBBodyNodeId(bone_id))
                if bone_model:
                    bone_names.append(bone_model.Name)
            
            for i in self.check_characterize:
                if not i in bone_names:
                    check_temp_list.append(i)
            if check_temp_list:
                self.characterMode = "PWL"
            else:
                self.characterMode = "CHAR"

            if self.characterMode == "CHAR":
                
                TheChar.ActiveInput = False
                self.RootBranchPlot()

                result = self.checkInitPose()
                constraint_states = self.save_constraint_states()
                self.disable_all_constraints()

            elif self.characterMode == "PWL":
                result = True
                
            else:
                result = False
            
            
            # result O : init pose exists / result X : init pose not exists in excel file
            
            if result:
                if self.ui.additive_CBX.isChecked():
                    additiveOp = 0
                else:
                    additiveOp = 1
                
                self.indexingTake = []
                takeList = self.check_takeList()
                #indexing takeList 
                for i,na in enumerate(FBSystem().Scene.Takes):
                    for x in takeList:
                        if na.Name == x:
                            self.indexingTake.append(i)
                
            

                if self.AssetName:
                    self.BAKE_BONE = self.n_s + "root"
                    
                    #Twist and WeaponBone Setting
                    #if nameSpace exsists delete nameSpace
                    char_root = FBFindModelByLabelName(self.BAKE_BONE)
                    if self.n_s != "":
                        
                        char_root.ProcessNamespaceHierarchy(FBNamespaceAction.kFBRemoveAllNamespace, self.n_s)
                    

                    for ind , i in enumerate(self.indexingTake):
                        
                        self.progressList[i].setEnabled(True)
                        self.setProgress(self.progressList[i] , 5)

                        take_ = FBSystem().Scene.Takes[i]
                        FBSystem().CurrentTake = take_
                        take_bu = take_.Name
                        take_.Name = take_.Name+"_copy"
                        take__= FBSystem().CurrentTake.CopyTake(take_bu)
                        FBSystem().CurrentTake = take__

                        if self.ui.rotateLock_CBX.isChecked():
                            ar.execFuncSelectTakes(take__)
                        ar.boneLockBake()
                        
                        if ind == 0 :
                            
                            if self.characterMode == "CHAR":
                                RTE.ReadyToExport(["root"],True)
                                
                            else:
                                RTE.ReadyToExport(["root"],True,True,False)
                                
                        self.setProgress(self.progressList[i] , 12)

                        self.setProgress(self.progressList[i] , 28)
                        
                        rootModel = FBFindModelByLabelName("root")
                        
                        # only ik foot bake not ik hand bake
                        if additiveOp:
                            
                            RTE.FindSnapWeapon("root")

                            self.setProgress(self.progressList[i] , 34)
                        
                            self.ClearSelModel()
                            self.setProgress(self.progressList[i] , 46)
                            
                            self.SelectBranch(rootModel)

                            self.setProgress(self.progressList[i] , 58)
                            self.PlotSelected()
                            self.setProgress(self.progressList[i] , 62)
                            self.ClearSelModel()
                        else:
                           
                            self.ClearSelModel()
                            self.setProgress(self.progressList[i] , 46)
                            self.SelectBranch(rootModel)
                            for removeJ in self.weaponPlotList:
                                removeJ = FBFindModelByLabelName(removeJ)
                                removeJ.Selected = False
                            self.PlotSelected()

                            for name in self.weaponPlotList:
                                object  = FBFindModelByLabelName(name)
                                object.Translation.SetAnimated(True)
                                object.Rotation.SetAnimated(True)
                                mainAnim = object.AnimationNode
                                
                                for transformAnimNode in mainAnim.Nodes:
                                    for axisAnimNode in transformAnimNode.Nodes:
                                        axisAnimNode.FCurve.EditClear()
                                
                                for transformAnimNode in mainAnim.Nodes:
                                    for axisAnimNode in transformAnimNode.Nodes:
                                        if transformAnimNode.Name == "Lcl Translation" and axisAnimNode.Name == "X":
                                            axisAnimNode.KeyAdd(FBTime(0,0,0,0),object.Translation[0])
                                        if transformAnimNode.Name == "Lcl Translation" and axisAnimNode.Name == "Y":
                                            axisAnimNode.KeyAdd(FBTime(0,0,0,0),object.Translation[1])
                                        if transformAnimNode.Name == "Lcl Translation" and axisAnimNode.Name == "Z":
                                            axisAnimNode.KeyAdd(FBTime(0,0,0,0),object.Translation[2])
                                        if transformAnimNode.Name == "Lcl Rotation" and axisAnimNode.Name == "X":
                                            axisAnimNode.KeyAdd(FBTime(0,0,0,0),object.Rotation[0])
                                        if transformAnimNode.Name == "Lcl Rotation" and axisAnimNode.Name == "Y":
                                            axisAnimNode.KeyAdd(FBTime(0,0,0,0),object.Rotation[1])
                                        if transformAnimNode.Name == "Lcl Rotation" and axisAnimNode.Name == "Z":
                                            axisAnimNode.KeyAdd(FBTime(0,0,0,0),object.Rotation[2])
                                        FBSystem().Scene.Evaluate()
                                        
                            self.setProgress(self.progressList[i] , 62)
                            self.ClearSelModel()
                        
                        self.setProgress(self.progressList[i] , 79)
                        self.SetPreRotation(1)
                        #Double Plot
                        self.setProgress(self.progressList[i] , 88)
                        
                        #spine_04 extra bone bake
                        if not self.ui.itemanimation_CBX.isChecked():
                            self.on_constraints_active_for_extrabone()
                            
                            parent_constraint1 = self.create_parent_constraint("weapon_l", "spine_04_extra01_l")
                            parent_constraint2 = self.create_parent_constraint("weapon_r", "spine_04_extra02_r")
                            
                            self.ClearSelModel()
                            FBFindModelByLabelName("spine_04_extra01_l").Selected = True
                            FBFindModelByLabelName("spine_04_extra02_r").Selected = True
                            self.PlotSelected()
                            self.ClearSelModel()
                            
                            parent_constraint1.FBDelete()
                            parent_constraint2.FBDelete()
                            self.off_constraints_active_for_extrabone()
                        
                        if self.ui.headanimation_CBX.isChecked():
                            self.export_Animation_CurrentTake(take_bu,True)
                        else:
                            self.export_Animation_CurrentTake(take_bu,False)
                        
                        
                        self.setProgress(self.progressList[i] , 93)
                        self.setProgress(self.progressList[i] , 98)

                        self.SetPreRotation(0)
                        FBSystem().CurrentTake.FBDelete()

                        take_.Name = take_bu
                        self.setProgress(self.progressList[i] , 100)
                        FBSystem().Scene.Evaluate()
                    if self.characterMode == "CHAR": 
                        
                        self.restore_constraint_states(constraint_states)

                    if additiveOp:
                        if self.characterMode == "CHAR": 
                            RTE.ClearSets(['IK_Gun_Set'])
                            RTE.ClearSets(['Twist_Set'])
                        else:
                            RTE.ClearSets(['IK_Gun_Set'])
                    
                    if self.n_s != "":
                        char_root.ProcessNamespaceHierarchy(FBNamespaceAction.kFBConcatNamespace, self.n_s.split(':')[0])
                    
                    FBMessageBox( 'StatusWindow', 'Complete!!', "Ok" )
                    for x in self.progressList:
                        x.reset()
                        x.setEnabled(False)
                    
            else:
                FBMessageBox( 'Warning', '"Script"폴더 최신 리비전이 필요합니다.', "Ok" )        
        else:
            FBMessageBox( 'Warning', 'Choose Output Path', "Ok" )
        


# -----------------------------------------------------------------------------------------------

CharInScene = []
for character in FBSystem().Scene.Characters:
    pList = character.PropertyList.Find("HipsLink")
    asset = pList[0]
    while asset.Parent:
        asset = asset.Parent
    CharInScene.append(asset.LongName)

if len(CharInScene)>1:
    for i in CharInScene:
        print(i)
        if i.find(":") == -1:
            FBMessageBox( 'Warning', 'More than one character must have a namespace.', "Ok" )
            status = False
            break 
        else:
            status = True 
else:
    status = True

if status == True:

    gToolName = "Mobu Batch Exporter Window"
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

