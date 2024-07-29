from pyfbsdk import*
from pyfbsdk_additions import*

def toggleLock(lock):
    lockList = ['lowerarm_l','lowerarm_r','calf_l','calf_r']
    for i in lockList:
        iModel = FBFindModelByLabelName(i)
        iModel.PropertyList.Find('Enable Rotation DOF').Data = lock
        iModel.PropertyList.Find('RotationMinX').Data = lock
        iModel.PropertyList.Find('RotationMinY').Data = lock
        iModel.PropertyList.Find('RotationMaxX').Data = lock
        iModel.PropertyList.Find('RotationMaxY').Data = lock
        if lock:
            iModel.PropertyList.Find('RotationMax').Data = FBVector3d(0,0,0)
            iModel.PropertyList.Find('RotationMin').Data = FBVector3d(0,0,0)

def resetPlotOption():
    myPlotOptions = FBPlotOptions ()
    myPlotOptions.ConstantKeyReducerKeepOneKey = False
    myPlotOptions.PlotAllTakes = False
    myPlotOptions.PlotOnFrame = True
    myPlotOptions.PlotPeriod = FBTime ( 0, 0, 0, 1 )
    myPlotOptions.PlotTranslationOnRootOnly = False
    myPlotOptions.PreciseTimeDiscontinuities = False
    myPlotOptions.RotationFilterToApply = FBRotationFilter.kFBRotationFilterUnroll
    myPlotOptions.UseConstantKeyReducer = False
    return myPlotOptions

def sendAnimToRig():
    FBApplication().CurrentCharacter.ActiveInput = 0    
    currentTime = FBSystem().LocalTime.GetFrame()
    lCharacter = FBApplication().CurrentCharacter
    if lCharacter:
        if str(lCharacter.InputType)!='kFBCharacterInputStance':
            if not lCharacter.ActiveInput:
                plotOptions = resetPlotOption()
                toggleLock(False)
                FBSystem().Scene.Evaluate()
                
                lCharacter.PlotAnimation(FBCharacterPlotWhere.kFBCharacterPlotOnControlRig, plotOptions)
                ikCtrlList = []
                for id in FBEffectorId.values.values():
                    if id == FBBodyNodeId.kFBReferenceNodeId:
                        continue
                    model = FBApplication().CurrentCharacter.GetEffectorModel(id)
                    if model:
                        ikCtrlList.append(model)
                        model.PropertyList.Find('IK Blend T').Data = 100
                        model.PropertyList.Find('IK Blend R').Data = 100
                                
                toggleLock(True)
                FBSystem().Scene.Evaluate()
                lCharacter.PlotAnimation(FBCharacterPlotWhere.kFBCharacterPlotOnSkeleton, plotOptions)                
                
                for ctrl in ikCtrlList:
                    if ('HipsEffector' not in ctrl.Name) and ('AnkleEffector' not in ctrl.Name):
                        ctrl.PropertyList.Find('IK Blend T').Data = 0
                        ctrl.PropertyList.Find('IK Blend R').Data = 0
                
                FBSystem().Scene.Evaluate()
                lCharacter.PlotAnimation(FBCharacterPlotWhere.kFBCharacterPlotOnControlRig, plotOptions)
    else:
        pass
    FBPlayerControl().Goto(FBTime(0,0,0,currentTime,0))

def boneLockBake():
    lockBakeList = ["subweapon"]
    lockAttrList = [[0,0,13.5,-90,0,160]]
    for i,name in enumerate(lockBakeList):
        object  = FBFindModelByLabelName(name)
        if object:
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
                    for transformAnimNode in mainAnim.Nodes:
                        for axisAnimNode in transformAnimNode.Nodes:
                            if transformAnimNode.Name == "Lcl Translation" and axisAnimNode.Name == "X":
                                axisAnimNode.KeyAdd(FBTime(0,0,0,time),lockAttrList[i][0])
                            if transformAnimNode.Name == "Lcl Translation" and axisAnimNode.Name == "Y":
                                axisAnimNode.KeyAdd(FBTime(0,0,0,time),lockAttrList[i][1])
                            if transformAnimNode.Name == "Lcl Translation" and axisAnimNode.Name == "Z":
                                axisAnimNode.KeyAdd(FBTime(0,0,0,time),lockAttrList[i][2])
                            if transformAnimNode.Name == "Lcl Rotation" and axisAnimNode.Name == "X":
                                axisAnimNode.KeyAdd(FBTime(0,0,0,time),lockAttrList[i][3])
                            if transformAnimNode.Name == "Lcl Rotation" and axisAnimNode.Name == "Y":
                                axisAnimNode.KeyAdd(FBTime(0,0,0,time),lockAttrList[i][4])
                            if transformAnimNode.Name == "Lcl Rotation" and axisAnimNode.Name == "Z":
                                axisAnimNode.KeyAdd(FBTime(0,0,0,time),lockAttrList[i][5])
                            FBSystem().Scene.Evaluate()
                except:
                    pass
def execFuncAllTakes():
    try:
        for take in FBSystem().Scene.Takes:
            FBSystem().CurrentTake = take
            sendAnimToRig()
    except:
        FBMessageBox('Error', 'Send Animation ERROR!', 'Cancel')

def execFuncSelectTakes(take):
    try:
        FBSystem().CurrentTake = take
        sendAnimToRig()
    except:
        FBMessageBox('Error', 'Send Animation ERROR!', 'Cancel')