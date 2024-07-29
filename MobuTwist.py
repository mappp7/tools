from pyfbsdk import *
from pyfbsdk_additions import *
import copy,csv

def GetBranch(InputRoot):
    ReturnList = []
    ReturnList.append(InputRoot)
    Children = InputRoot.Children
    if Children != None:
        for i in Children:
            ReturnList = ReturnList+GetBranch(i)
    return ReturnList


def FindAnimationNode( pParent, pName ): 
    lResult = None 
    for lNode in pParent.Nodes: 
        if lNode.Name == pName: 
            lResult = lNode 
            break 
    return lResult


def ConnectBox(Sender,SenderAttr,Receiver,RecerverAttr):
    SenderOut = FindAnimationNode(Sender.AnimationNodeOutGet(),SenderAttr)
    ReceiverIn = FindAnimationNode(Receiver.AnimationNodeInGet(),RecerverAttr)
    if SenderOut and ReceiverIn:
        FBConnect(SenderOut,ReceiverIn)


def DoRelationConst(Source,Destinations,Ratios,TwistSet):
    PosX = 0
    PosY = 0

    TwistRelation = FBConstraintRelation(str(Source.Name)+'_RelationConst')
    TwistSet.ConnectSrc(TwistRelation)
    TwistRelation.Active = True 
    
    Sender = TwistRelation.SetAsSource(Source)
    Sender.UseGlobalTransforms = False
    TwistRelation.SetBoxPosition(Sender,PosX,PosY)
    
    VecToNumBox = TwistRelation.CreateFunctionBox('Converters','Vector to Number')
    PosX=PosX+400
    TwistRelation.SetBoxPosition(VecToNumBox,PosX,PosY)   
     
    ConnectBox(Sender,'Lcl Rotation',VecToNumBox,'V')

    for Destination,Ratio in zip(Destinations,Ratios):
        if Destination!=None:
            MultiplyBox = TwistRelation.CreateFunctionBox('Number','Multiply (a x b)')
            PosX=PosX+400
            PosY=PosY-200
            TwistRelation.SetBoxPosition(MultiplyBox,PosX,PosY)
            
            NumToVecBox = TwistRelation.CreateFunctionBox('Converters','Number to Vector')
            PosX=PosX+400
            TwistRelation.SetBoxPosition(NumToVecBox,PosX,PosY)
            
            Receiver = TwistRelation.ConstrainObject(Destination)
            Receiver.UseGlobalTransforms = False
            PosX=PosX+400
            TwistRelation.SetBoxPosition(Receiver,PosX,PosY)
            
            ConnectBox(VecToNumBox,'X',MultiplyBox,'a')
            ConnectBox(MultiplyBox,'Result',NumToVecBox,'X')
            ConnectBox(NumToVecBox,'Result',Receiver,'Lcl Rotation')
            PosX=PosX-1200
            PosY=PosY+400
            SetAttr = FindAnimationNode(MultiplyBox.AnimationNodeInGet(), 'b')
            SetAttr.WriteData([Ratio])


def CreateDriver(InputJnt,AddNS,TwistSet,initPose):
    
    InputModel = FBFindModelByLabelName(AddNS+InputJnt)
    InputParentModel = InputModel.Parent
    SphericModel = FBModelSkeleton('')
    SphericParentModel = FBModelNull('')
    
    TwistSet.ConnectSrc(SphericModel)
    TwistSet.ConnectSrc(SphericParentModel)
        
    AddItems = TwistSet.Components
    for AddItem in AddItems:
        if AddNS not in AddItem.LongName:
            AddItem.ProcessObjectNamespace(FBNamespaceAction.kFBConcatNamespace, AddNS[:-1])
    
    SphericParentModel.Name = InputParentModel.Name.split('JNT')[0]+'Spheric_Parent'
    SphericModel.Name = InputModel.Name.split('JNT')[0]+'Spheric'
    SphericModel.PropertyList.Find('Visibility').Data = False
    SphericParentModel.PropertyList.Find('Visibility').Data = False

    ConstMngr = FBConstraintManager()
    
    ParConst = ConstMngr.TypeCreateConstraint('Parent/Child')
    TwistSet.ConnectSrc(ParConst)
    ParConst.Name = str(SphericModel.Name)+'_ParentConst'
    ParConst.ReferenceAdd(0,SphericParentModel)
    ParConst.ReferenceAdd(1,InputParentModel)
    ParConst.Active = True

    SphericModel.Parent = SphericParentModel

    SphericModel.PropertyList.Find('Lcl Translation').Data = InputModel.PropertyList.Find('Lcl Translation').Data
    SphericModel.PropertyList.Find('Lcl Translation').SetLocked(True)
    SphericModel.PropertyList.Find('Enable Rotation DOF').Data = True
    SphericModel.PropertyList.Find('Lcl Rotation').Data   = InputModel.PropertyList.Find('Lcl Rotation').Data
    #SphericModel.PropertyList.Find('Pre Rotation').Data   = PreRotate
    SphericModel.PropertyList.Find('RotationOrder').Data  = 6 #Set Rotation Order SphericXYZ
    SphericModel.PropertyList.Find('Rotation Pivot').Data = FBVector3d(0, 0, 0)
    SphericModel.PropertyList.Find('Scaling Pivot').Data  = FBVector3d(0, 0, 0)

    RotConst = ConstMngr.TypeCreateConstraint('Rotation')
    TwistSet.ConnectSrc(RotConst)
    RotConst.Name = str(SphericModel.Name)+'_RotationConst'
    RotConst.ReferenceAdd(0,SphericModel)
    RotConst.ReferenceAdd(1,InputModel)
    RotConst.Active = True

    #Find UpArm_JNT
    print (initPose)
    InitPoseData = initPose
    GetInitRot = InitPoseData.split(InputJnt)[1].split('[(')[1].split(')]')[0]
    InitRotData = FBVector3d(float(GetInitRot.split(',')[0]),float(GetInitRot.split(',')[1]),float(GetInitRot.split(',')[2]))
    SphericModel.PropertyList.Find('Pre Rotation').Data   = InitRotData

    ######################################
    TwistRigGrpName = 'Twist_Rig_GRP'
    TwistRigGrp = []
    ChkRigGrpName = True

    for Null in FBSystem().Scene.RootModel.Children:

        if Null.LongName == AddNS+TwistRigGrpName:
            ChkRigGrpName = False
            TwistRigGrp = Null
    if ChkRigGrpName:
        TwistRigGrp = FBModelNull('')
        SphericParentModel.Parent = TwistRigGrp
    else:
        SphericParentModel.Parent = TwistRigGrp
        TwistSet.ConnectSrc(TwistRigGrp)
        
    if AddNS not in TwistRigGrp.LongName:   TwistRigGrp.ProcessObjectNamespace(FBNamespaceAction.kFBConcatNamespace, AddNS[:-1])
    TwistRigGrp.Name = TwistRigGrpName
    return SphericModel

def DoTwist(rootName):
    
    SetName = 'Twist_Set'
    
    if isinstance(rootName,list):   rootName=rootName[0]
    
    AddNS = ''
    if ':' in rootName: AddNS = rootName.split(':')[0]+':'
    TwistSet     = FBSet(SetName)
    TwistSet.ProcessObjectNamespace(FBNamespaceAction.kFBConcatNamespace, AddNS[:-1])
    TwistSet.Name = SetName
    
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
                localTrs = FBFindModelByLabelName(AddNS+matchBone[i]).Translation
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
    if matchBool == False:
        initPose = ''
        FBMessageBox('Skeleton Error', 'Please Check Skeleton.', 'Cancel')
    TwistCharInitPoseFile.close()
    
    
    rootBone = FBFindModelByLabelName(rootName)
    BoneList = GetBranch(rootBone)
    separator='_'
    Ratios=''
    target00=''
    target01=''
    target02=''
    
    for bone in BoneList:
        boneName = bone.Name
        getBoneData = bone.Name.split(separator)
        if len(getBoneData)>1:
            chk = False
            if getBoneData[-2]=='hand' and getBoneData[0]!='ik':
                getBoneData[-2]='lowerarm_twist_00'
                target00=separator.join(getBoneData)
                getBoneData[-2]='lowerarm_twist_01'
                target01=separator.join(getBoneData)
                getBoneData[-2]='lowerarm_twist_02'
                target02=separator.join(getBoneData)

                Ratios = [0, 0.33, 0.66]
                chk = True
                
            elif getBoneData[-2]=='upperarm' and getBoneData[0]!='ik':
                getBoneData[-2]='upperarm_twist_00'
                target00=separator.join(getBoneData)
                getBoneData[-2]='upperarm_twist_01'
                target01=separator.join(getBoneData)
                getBoneData[-2]='upperarm_twist_02'
                target02=separator.join(getBoneData)
                
                Ratios = [-1, -0.66, -0.33]
                chk = True
            elif getBoneData[-2]=='foot' and getBoneData[0]!='ik':
                getBoneData[-2]='calf_twist_00'
                target00=separator.join(getBoneData)
                getBoneData[-2]='calf_twist_01'
                target01=separator.join(getBoneData)
                getBoneData[-2]='calf_twist_02'
                target02=separator.join(getBoneData)
                
                Ratios = [0, 0.33, 0.66]
                chk = True
                
            elif getBoneData[-2]=='thigh' and getBoneData[0]!='ik':
                getBoneData[-2]='thigh_twist_00'
                target00=separator.join(getBoneData)
                getBoneData[-2]='thigh_twist_01'
                target01=separator.join(getBoneData)
                getBoneData[-2]='thigh_twist_02'
                target02=separator.join(getBoneData)
                
                Ratios = [-1, -0.66, -0.33]
                chk = True
           
            if chk:
                print (initPose)
                Source       = CreateDriver(boneName,AddNS,TwistSet,initPose)
        
                Destinations = [FBFindModelByLabelName(AddNS+target00),
                                FBFindModelByLabelName(AddNS+target01),
                                FBFindModelByLabelName(AddNS+target02)]
            
                DoRelationConst(Source,Destinations,Ratios,TwistSet)


    #Add Created Object to Namespace
    AddItems = TwistSet.Components
    for AddItem in AddItems:
        if AddNS not in AddItem.LongName:
            AddItem.ProcessObjectNamespace(FBNamespaceAction.kFBConcatNamespace, AddNS[:-1])
