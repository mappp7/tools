
from pyfbsdk import *
from pyfbsdk_additions import*

class rootMotion:

    def __init__(self, axisState):
        self.ROOT_GLOBAL = {}
        self.Axis_State = axisState
        self.BAKE_BONE = "root"
        self.n_s = ""    
    def ClearSelModel(self):
        modelList = FBModelList()
        FBGetSelectedModels (modelList, None, True)
        for model in modelList:
            model.Selected = False

    def mobuMatrixToPython(self,matrix):
        pythonMatrix = [[],[],[],[]]
        for i in matrix:
            for j in range(4):
                if len(pythonMatrix[j]) != 4:
                    pythonMatrix[j].append(i)
                    break
        return pythonMatrix
    
    def TwistSearch(self,node):
        if node.ClassName() == 'FBModelSkeleton':
            if node.Name.find("twist") != -1:
                node.Selected = True
        for child in node.Children:
            self.TwistSearch(child)

    def BakePlotToWhat(self,mode):
        # mode => 0 = skeleton || 1 = crtl Rig
        TheChar = FBApplication().CurrentCharacter
        if TheChar:
            
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
            myPlayerCtrl = FBPlayerControl()
            myPlayerCtrl.Stop()
            if mode == 0:
                TheChar.PlotAnimation(FBCharacterPlotWhere.kFBCharacterPlotOnSkeleton, myPlotOptions)    
            else:
                TheChar.PlotAnimation(FBCharacterPlotWhere.kFBCharacterPlotOnControlRig, myPlotOptions)
            FBSystem().Scene.Evaluate()
            del(TheChar , myPlotOptions , myPlayerCtrl)
        else:
            FBMessageBox( 'Warning', 'Please Connect Character', "Ok" )

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

    def keyClear(self):
        root_obj = self.n_s + self.BAKE_BONE
        system = FBSystem()
        lenLayer_ = system.CurrentTake.GetLayerCount()
        for i in range(lenLayer_):
            system.CurrentTake.SetCurrentLayer(i)
            root_obj.Translation.SetAnimated(True)
            root_obj.Rotation.SetAnimated(True)
            mainAnim = root_obj.AnimationNode
            for transformAnimNode in mainAnim.Nodes:
                for axisAnimNode in transformAnimNode.Nodes:
                    axisAnimNode.FCurve.EditClear()

    def keyBake(self,name,KEY_DATA):
        object  = FBFindModelByLabelName(name)
        object.Translation.SetAnimated(True)
        object.Rotation.SetAnimated(True)
        mainAnim = object.AnimationNode
        start_frame = FBSystem().CurrentTake.LocalTimeSpan.GetStart().GetFrame()
        end_frame = FBSystem().CurrentTake.LocalTimeSpan.GetStop().GetFrame()
        for transformAnimNode in mainAnim.Nodes:
            for axisAnimNode in transformAnimNode.Nodes:
                axisAnimNode.FCurve.EditClear()
        for time in range(start_frame,end_frame+1,1):
            try:
                if KEY_DATA[str(time)]:
                    for transformAnimNode in mainAnim.Nodes:
                        for axisAnimNode in transformAnimNode.Nodes:
                            if transformAnimNode.Name == "Lcl Translation" and axisAnimNode.Name == "X":
                                axisAnimNode.KeyAdd(FBTime(0,0,0,time),KEY_DATA[str(time)][0])
                            if transformAnimNode.Name == "Lcl Translation" and axisAnimNode.Name == "Y":
                                axisAnimNode.KeyAdd(FBTime(0,0,0,time),KEY_DATA[str(time)][1])
                            if transformAnimNode.Name == "Lcl Translation" and axisAnimNode.Name == "Z":
                                axisAnimNode.KeyAdd(FBTime(0,0,0,time),KEY_DATA[str(time)][2])
                            if transformAnimNode.Name == "Lcl Rotation" and axisAnimNode.Name == "X":
                                axisAnimNode.KeyAdd(FBTime(0,0,0,time),KEY_DATA[str(time)][3])
                            if transformAnimNode.Name == "Lcl Rotation" and axisAnimNode.Name == "Y":
                                axisAnimNode.KeyAdd(FBTime(0,0,0,time),KEY_DATA[str(time)][4])
                            if transformAnimNode.Name == "Lcl Rotation" and axisAnimNode.Name == "Z":
                                axisAnimNode.KeyAdd(FBTime(0,0,0,time),KEY_DATA[str(time)][5])
                            FBSystem().Scene.Evaluate()
            except:
                pass
        
        del(object , mainAnim,start_frame,end_frame)

    def settingLayer(self):
        # create overide layer
        system = FBSystem()
        system.CurrentTake.CreateNewLayer()
        lenLayer_ = system.CurrentTake.GetLayerCount()
        system.CurrentTake.SetCurrentLayer(lenLayer_ -1)
        overideLayer = system.CurrentTake.GetLayer(lenLayer_-1)
        overideLayer.LayerMode = FBLayerMode.kFBLayerModeOverride

        root_obj = FBFindModelByLabelName(self.n_s + self.BAKE_BONE)
        root_obj.Translation.SetAnimated(True)
        root_obj.Rotation.SetAnimated(True)
        
        return overideLayer

    def BakeOriginMotion(self):
        TheChar = FBApplication().CurrentCharacter 
        if TheChar: 
            TheChar.ActiveInput = True 
            root = self.n_s + self.BAKE_BONE
            rootm = FBFindModelByLabelName(root)
            self.ClearSelModel()
            rootm.Selected = True
            self.PlotSelected()


    def CreateConstraint(self,Src,Dst,ConstType,Snap):
        
        ConstMngr = FBConstraintManager()
        ParConst = ConstMngr.TypeCreateConstraint(ConstType)
        ParConst.Name = Dst.LongName+'_Constraint'
        ParConst.ReferenceAdd(0,Dst)
        ParConst.ReferenceAdd(1,Src)
        if Snap:
            ParConst.Snap()
        else:
            ParConst.Active = True
        return ParConst

    def BakeRootMotion(self,rotationOption,axis,linearOp):
        
        TheChar = FBApplication().CurrentCharacter
        if TheChar: 
            TheChar.ActiveInput = True
            root = self.n_s + self.BAKE_BONE
            rootm = FBFindModelByLabelName(root)
            pelvis = self.n_s + "pelvis"
            print (self.n_s)
    
            start_frame = FBSystem().CurrentTake.LocalTimeSpan.GetStart().GetFrame()
            end_frame = FBSystem().CurrentTake.LocalTimeSpan.GetStop().GetFrame()
            #save currentFrame Pelvis matrix
            KEY_DATA = {}
            if linearOp == 1:
                linear_frame = end_frame - start_frame
            else:
                linear_frame = 1
           

            marker2 = FBModelMarker('worldroot')
            marker2.PropertyList.Find('Enable Rotation DOF').Data=True
            marker2.PropertyList.Find('RotationOrder').Data=6
            marker2.Translation = FBVector3d(0.0, 0.0, 0.0)
            marker2.Rotation = FBVector3d(0.0, 0.0, 0.0)
            #marker2.PropertyList.Find('Enable Rotation DOF').Data=True
            #marker2.PropertyList.Find('RotationOrder').Data=6
            marker = FBModelMarker('worldPelvis')
            
            marker3 = FBModelMarker('deleteMarker')
            

            for i in range(start_frame , end_frame +1 ,linear_frame):
                FBPlayerControl().Goto(FBTime(0,0,0,i,0))
                #FBSystem().Scene.Evaluate()
                m_ = FBMatrix()
                obj = FBFindModelByLabelName(pelvis)
                obj.GetMatrix(m_)

                pymat = self.mobuMatrixToPython(m_)
                #axis 1 = xz , 2 = z , 3 = x 
                if axis == 3:
                    x = pymat[3][0]
                    y = 0
                    z = 0
                elif axis == 2:
                    x = 0
                    y = 0
                    z = pymat[3][2]# worldUp Y , spaceUp Z
                else:
                    x = pymat[3][0]
                    y = 0
                    z = pymat[3][2]# worldUp Y , spaceUp Z
                if rotationOption == 1:
                    marker.SetMatrix(m_)
                    
                    #Get Rotate Marker and add -> get rotateX
                    rot = FBVector3d()
                    marker.GetVector(rot , FBModelTransformationType.kModelRotation)
                    #marker.FBDelete()
                    # if front reverseY is (-90-90-90) front X is (-180-90-90)
                    if self.Axis_State == 0 :
                        offsetRot = FBVector3d(-90,-90,-90)
                    else:
                        offsetRot = FBVector3d(-180,-90,-90)
                    
                    addRot = FBVector3d(rot[0],0,-90) + offsetRot
                    newrot = addRot[0]
                    
                
                    if i == int(start_frame):
                        marker3.SetVector(FBVector3d(x,y,z), FBModelTransformationType.kModelTranslation)
                        marker3.SetVector(FBVector3d(0 , newrot, 0) , FBModelTransformationType.kModelRotation)                   
                        
                        marker3.PropertyList.Find('Enable Rotation DOF').Data=True
                        marker3.PropertyList.Find('Enable Translation DOF').Data=True
                        marker3.PropertyList.Find('PreRotation').Data = FBVector3d(0,0,90)
                        marker3.PropertyList.Find('TranslationMinY').Data = True
                        marker3.PropertyList.Find('TranslationMaxY').Data = True
                        marker3.PropertyList.Find('RotationMinY').Data = True
                        marker3.PropertyList.Find('RotationMinZ').Data = True
                        marker3.PropertyList.Find('RotationMaxY').Data = True
                        marker3.PropertyList.Find('RotationMaxZ').Data = True
                        marker3.PropertyList.Find('RotationOrder').Data=6
                        Src = FBFindModelByLabelName(self.n_s + "pelvis")
                        Dst = marker3
                        
                        pConst = self.CreateConstraint(Src,Dst,"Position",0)
                        rConst = self.CreateConstraint(Src,Dst,"Rotation",1)
                        
                        marker2.Parent = marker3
                        Src = marker3
                        Dst = rootm
                        rootConst = self.CreateConstraint(Src,Dst,"Parent/Child",1)

                    trs2 = FBVector3d()
                    rot2 = FBVector3d()
                    marker2.GetVector(trs2 , FBModelTransformationType.kModelTranslation , True)
                    marker2.GetVector(rot2 , FBModelTransformationType.kModelRotation , True)
                   
                    KEY_DATA[str(i)] = [trs2[0],trs2[1],trs2[2],0,0,rot2[1]]
                    
                else:
                    KEY_DATA[str(i)] = [x,y,z,0,0,0]

                
                FBSystem().Scene.Evaluate()
            if rotationOption == 1:   
                #self.keyBake(root,KEY_DATA)
                self.ClearSelModel()
                rootm.Selected = True
                self.PlotSelected()
                self.ClearSelModel()
            else:
                self.keyBake(root,KEY_DATA)
            
            if rotationOption == 1:
                marker.FBDelete()
                marker2.FBDelete()
                marker3.FBDelete()
                pConst.FBDelete()
                rConst.FBDelete()
                rootConst.FBDelete()
            self.BakePlotToWhat(0)
            self.BakePlotToWhat(1)

    def ZeroBake(self,rotationOption):
        
        TheChar = FBApplication().CurrentCharacter
        if TheChar.ActiveInput == True:
            root = self.n_s + self.BAKE_BONE
            currentFrame = FBSystem().LocalTime.GetFrame()
            start_frame = FBSystem().CurrentTake.LocalTimeSpan.GetStart().GetFrame()
            end_frame = FBSystem().CurrentTake.LocalTimeSpan.GetStop().GetFrame()
            #save zero transform
            KEY_DATA = {}
            for i in range(start_frame , end_frame+1, 1):
                if rotationOption == 1:
                    FBPlayerControl().Goto(FBTime(0,0,0,i,0))
                    #FBSystem().Scene.Evaluate()
                    m_ = FBMatrix()
                    pelvis = FBFindModelByLabelName(self.n_s + "pelvis")
                    marker = FBModelMarker('worldPelvis')
                    pelvis.GetMatrix(m_)
                    marker.SetMatrix(m_)
                    #Get Rotate Marker and add -> get rotateX
                    rot = FBVector3d()
                    marker.GetVector(rot , FBModelTransformationType.kModelRotation)
                    marker.FBDelete()
                    # if front reverseY is (-90-90-90) front X is (-180-90-90)
                    if self.Axis_State == 0 :
                        offsetRot = FBVector3d(-90,-90,-90)
                    else:
                        offsetRot = FBVector3d(-180,-90,-90)
                    
                    addRot = FBVector3d(rot[0],0,-90) + offsetRot
                    KEY_DATA[str(i)] = [0,0,0,0,0,addRot[0]]
                    
                else:
                    KEY_DATA[str(i)] = [0,0,0,0,0,0] #zero Transform
                    rootObj = FBFindModelByLabelName(self.n_s + self.BAKE_BONE)
                    if rootObj.PropertyList.Find("Enable Rotation DOF").Data == False:
                        rootObj.PropertyList.Find("Enable Rotation DOF").Data = True
                        rootObj.PropertyList.Find("Pre Rotation").Data = FBVector3d(-90,0,0) 
                FBSystem().Scene.Evaluate()
            self.keyBake(root,KEY_DATA)
            FBPlayerControl().Goto(FBTime(0,0,0,currentFrame,0))
            
            
            
        else:
            FBMessageBox( 'Warning', 'Please Connect Character', "Ok" )
