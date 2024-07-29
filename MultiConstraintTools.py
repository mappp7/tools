from pyfbsdk import *
from pyfbsdk_additions import *

def MCAlign( pModel, pAlignTo):

    lAlignTransPos = FBVector3d();
    lModelTransPos = FBVector3d();
    lAlignRotPos = FBVector3d();
    lModelRotPos = FBVector3d();   
    
    pAlignTo.GetVector(lAlignTransPos)
    pModel.GetVector(lModelTransPos)
    
    pAlignTo.GetVector(lAlignRotPos, FBModelTransformationType.kModelRotation )
    pModel.GetVector(lModelRotPos, FBModelTransformationType.kModelRotation)
    
    lModelTransPos[0] = lAlignTransPos[0]
    lModelTransPos[1] = lAlignTransPos[1]
    lModelTransPos[2] = lAlignTransPos[2]
    
    lModelRotPos[0] = lAlignRotPos[0]
    lModelRotPos[1] = lAlignRotPos[1]
    lModelRotPos[2] = lAlignRotPos[2]        
         
    pModel.SetVector(lModelTransPos)
    pModel.SetVector(lModelRotPos, FBModelTransformationType.kModelRotation)

def MCCreateConst(Dst):
    CurrentTime = FBSystem().LocalTime.GetFrame()
    
    ConstMngr = FBConstraintManager()
    ParConst = ConstMngr.TypeCreateConstraint('Parent/Child')
    ParConst.Name = 'TT_'+Dst.LongName.replace(':','>')+'_'+FBSystem().CurrentTake.LongName.replace(':','>')+'_Constraint'
    ParConst.ReferenceAdd(0,Dst)
    
    ParConstWeight = ParConst.PropertyList.Find('Weight')
    ParConstWeight.SetAnimated(True)
    ParConstWeight.Data=100
    ParConstWeight.GetAnimationNode().KeyCandidate(FBTime(0, 0, 0, 0))
    ParConstWeight.SetLocked(True)
    return ParConst

def MCChangeConst(ConstList,Idx):
    for i in range(len(ConstList)):
        ConstWeight = ConstList[i].PropertyList.Find('Weight')
        ConstWeight.SetLocked(False)
        ConstWeight.SetAnimated(True)
        if i==Idx:  ConstWeight.Data=100
        else:   ConstWeight.Data=0
        ConstWeight.GetAnimationNode().KeyCandidate(FBTime(0, 0, 0, 0))
        ConstWeight.SetLocked(True)

def SetKeyCandidate(pAnimationNode):
    CurrentTime = FBSystem().LocalTime.GetFrame()
    if len(pAnimationNode.Nodes) == 0:
        pAnimationNode.KeyCandidate(FBTime(0, 0, 0,CurrentTime))
    else:
        for lNode in pAnimationNode.Nodes:
            SetKeyCandidate(lNode)

def KeyInterpolate(AnimNode):
    FCrv = AnimNode.FCurve
    keyList = FCrv.Keys
    for i in range(len(keyList)):
        FCrv = keyList[i]
        FCrv.Interpolation = FBInterpolation.values[0]
        FCrv.TangentMode = FBTangentMode.values[0]
        FCrv.TangentConstantMode = FBTangentConstantMode.values[0]
        FCrv.LeftDerivative = 0.0
        FCrv.RightDerivative = 0.0
        FCrv.LeftTangentWeight = 0.333333343267
        FCrv.RightTangentWeight = 0.333333343267

def MCSetKey(Const,Snap,Idx):
    Tgt = Const.ReferenceGet(0,0)
    SrcLen = Const.ReferenceGetCount(True)
    for i in range(0,SrcLen):
        KeyProperty = []
        KeyProperty.append('Offset T')
        KeyProperty.append('Offset R')
        KeyProperty.append('Offset S')
        KeyProperty.append('Weight')
        
        Src = Const.ReferenceGet(1,i)
        for KeyProp in KeyProperty:
            Const.PropertyList.Find(Src.LongName+'.'+KeyProp).SetAnimated(True)

        if Snap and Idx==i:
            MCAlign(Tgt,Src)
        
        Const.Active = False
        Const.Snap()
        
        for Property in KeyProperty:
            AnimNodes = Const.PropertyList.Find(Src.LongName+'.'+Property).GetAnimationNode()
            if len(AnimNodes.Nodes) != 0:
                for AnimNode in AnimNodes.Nodes:
                    SetKeyCandidate(AnimNode)
                    KeyInterpolate(AnimNode)
            else:
                WeightVal = Const.PropertyList.Find(Src.LongName+'.'+Property)
                
                if Idx==i:  WeightVal.Data = 100
                else:   WeightVal.Data = 0
                
                SetKeyCandidate(AnimNodes)
                KeyInterpolate(AnimNodes)

def MCGetFCrv(Const):
    SrcLen = Const.ReferenceGetCount(True)
    StartFrame = FBSystem().CurrentTake.LocalTimeSpan.GetStart().GetFrame()
    EndFrame = FBSystem().CurrentTake.LocalTimeSpan.GetStop().GetFrame() + 1
    
    AllAnimNodes = []
    
    for i in range(0,SrcLen):
        
        KeyProperty = []
        KeyProperty.append('Offset T')
        KeyProperty.append('Offset R')
        KeyProperty.append('Offset S')
        KeyProperty.append('Weight')
        
        Src = Const.ReferenceGet(1,i)
        for KeyProp in KeyProperty:
            Const.PropertyList.Find(Src.LongName+'.'+KeyProp).SetAnimated(True)
            AllAnimNodes.append(Const.PropertyList.Find(Src.LongName+'.'+KeyProp).GetAnimationNode())

    AllFCurves = []
    
    for AnimNode in AllAnimNodes:
        if len(AnimNode.Nodes) !=0:
            for Node in AnimNode.Nodes:
                AllFCurves.append(Node.FCurve)
        elif AnimNode.FCurve != 'NoneType':
            AllFCurves.append(AnimNode.FCurve)
    
    return AllFCurves

def MCEditConstWeight(Const,Weight):
    SrcLen = Const.ReferenceGetCount(True)
    for i in range(0,SrcLen):
        Src = Const.ReferenceGet(1,i)
        Const.PropertyList.Find(Src.LongName+'.Weight').Data = Weight

def MCDelRangeKey(AllFCurves,Start,End):
    StartFrame = FBTime(0, 0, 0, Start)
    EndFrame = FBTime(0, 0, 0, End)
    for FCrv in AllFCurves:
        FCrv.KeyDeleteByTimeRange(StartFrame,EndFrame,True)

def MCClearKey(AllFCurves):
    StartFrame = FBTime(0, 0, 0, FBSystem().CurrentTake.LocalTimeSpan.GetStart().GetFrame())
    EndFrame = FBTime(0, 0, 0, FBSystem().CurrentTake.LocalTimeSpan.GetStop().GetFrame() + 1)
    for FCrv in AllFCurves:
        FCrv.KeyDeleteByTimeRange(StartFrame,EndFrame,True)


def MCDelCurrentKey(AllFCurves):
    CurrentFrame = FBSystem().LocalTime.GetFrame()
    for FCrv in AllFCurves:
        CheckFin = True
        for i in range(0, len(FCrv.Keys)):
            KeyTmp = FCrv.Keys[i]
            KeyFrame = KeyTmp.Time.GetFrame()
            if KeyFrame > CurrentFrame:
                FCrv.KeyDeleteByIndexRange(i-1,i-1)
                CheckFin = False
                break
        if CheckFin:
            FCrv.KeyDeleteByIndexRange(len(FCrv.Keys)-1,len(FCrv.Keys)-1)

def MCAddParent(Const):
    SrcLen = Const.ReferenceGetCount(True)
    Src = Const.ReferenceGet(1,0)
    AddSrc = Const.ReferenceGet(1,SrcLen-1)
    if SrcLen>1:
        Const.PropertyList.Find(AddSrc.LongName+'.Weight').SetAnimated(True)
        SrcAnimNode = Const.PropertyList.Find(Src.LongName+'.Weight').GetAnimationNode()
        AddSrcAnimNode = Const.PropertyList.Find(AddSrc.LongName+'.Weight').GetAnimationNode()
        if SrcAnimNode!=None:
            for Key in SrcAnimNode.FCurve.Keys:
                AddSrcAnimNode.FCurve.KeyAdd(Key.Time,0)