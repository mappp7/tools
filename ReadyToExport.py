from pyfbsdk import *
from MobuTwist import *
import csv

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


def DoConstraint(ChildM,ParentM,Type):
    ConstMngr = FBConstraintManager()
    ParConst = ConstMngr.TypeCreateConstraint(Type)
    ParConst.Name = str(ChildM.Name)+'_'+str(Type)+'Const'
    ParConst.ReferenceAdd(0,ChildM)
    ParConst.ReferenceAdd(1,ParentM)
    ParConst.Active = True
    return ParConst


def ZeroOffset(InputSkeleton):
    InputSkeleton.PropertyList.Find('Rotation Pivot').Data = FBVector3d(0,0,0)
    InputSkeleton.PropertyList.Find('Rotation Offset').Data = FBVector3d(0,0,0)
    InputSkeleton.PropertyList.Find('Scaling Pivot').Data = FBVector3d(0,0,0)
    InputSkeleton.PropertyList.Find('Scaling Offset').Data = FBVector3d(0,0,0)

def GetBranch(InputRoot):
    ReturnList = []
    ReturnList.append(InputRoot)
    Children = InputRoot.Children
    if Children != None:
        for i in Children:
            ReturnList = ReturnList+GetBranch(i)
    return ReturnList

def DelArray(Array):
    for i in reversed(Array):
        i.FBDelete()

def FindSnapWeapon(RootList):

    StartFrame = FBSystem().CurrentTake.LocalTimeSpan.GetStart().GetFrame()
    EndFrame = FBSystem().CurrentTake.LocalTimeSpan.GetStop().GetFrame() + 1
        
    AddNS = ''
    if ':' in RootList:  AddNS = RootList.split(':')[0]+':'

    LHandPJntName = 'ik_hand_p_l'
    LHandPJntM = FBFindModelByLabelName(AddNS+LHandPJntName)
    LHandPJntM.Translation.SetAnimated(True)
    RHandPJntName = 'ik_hand_p_r'
    RHandPJntM = FBFindModelByLabelName(AddNS+RHandPJntName)
    RHandPJntM.Translation.SetAnimated(True)
    
    LHandPJntFCurveTx = LHandPJntM.Translation.GetAnimationNode().Nodes[0].FCurve
    LHandPJntFCurveTy = LHandPJntM.Translation.GetAnimationNode().Nodes[1].FCurve
    LHandPJntFCurveTz = LHandPJntM.Translation.GetAnimationNode().Nodes[2].FCurve

    RHandPJntFCurveTx = RHandPJntM.Translation.GetAnimationNode().Nodes[0].FCurve
    RHandPJntFCurveTy = RHandPJntM.Translation.GetAnimationNode().Nodes[1].FCurve
    RHandPJntFCurveTz = RHandPJntM.Translation.GetAnimationNode().Nodes[2].FCurve
    
    HandGunJntName = 'ik_hand_gun'
    HandGunJntM = FBFindModelByLabelName(AddNS+HandGunJntName)

    WeaponBasePos = LHandPJntM.Translation.Data
    '''    
    for i in range(StartFrame,EndFrame):
        FBPlayerControl().Goto(FBTime (0, 0, 0, i))
        
        if HandGunJntM.PropertyList.Find('Left Weapon').Data:
            LHandPJntFCurveTx.KeyAdd(FBTime(0,0,0,i),0)
            LHandPJntFCurveTy.KeyAdd(FBTime(0,0,0,i),0)
            LHandPJntFCurveTz.KeyAdd(FBTime(0,0,0,i),0)
            RHandPJntFCurveTx.KeyAdd(FBTime(0,0,0,i),WeaponBasePos[0])
            RHandPJntFCurveTy.KeyAdd(FBTime(0,0,0,i),WeaponBasePos[1])
            RHandPJntFCurveTz.KeyAdd(FBTime(0,0,0,i),WeaponBasePos[2])
        else:
            LHandPJntFCurveTx.KeyAdd(FBTime(0,0,0,i),WeaponBasePos[0])
            LHandPJntFCurveTy.KeyAdd(FBTime(0,0,0,i),WeaponBasePos[1])
            LHandPJntFCurveTz.KeyAdd(FBTime(0,0,0,i),WeaponBasePos[2])
            RHandPJntFCurveTx.KeyAdd(FBTime(0,0,0,i),0)
            RHandPJntFCurveTy.KeyAdd(FBTime(0,0,0,i),0)
            RHandPJntFCurveTz.KeyAdd(FBTime(0,0,0,i),0)
    '''

def DoWeapon(RootList,UpperBody):

    SetName = 'IK_Gun_Set'
    
    AddNS = ''
    if ':' in RootList: AddNS = RootList.split(':')[0]+':'
    WeaponSet = FBSet(SetName)
    if AddNS not in WeaponSet.LongName:
        WeaponSet.ProcessObjectNamespace(FBNamespaceAction.kFBConcatNamespace, AddNS[:-1])
    WeaponSet.Name = SetName

    RootName = 'root'
    SubRootName = 'subroot'
    L_WeaponName = 'weapon_l'
    R_WeaponName = 'weapon_r'
    L_HandName = 'hand_l'
    R_HandName = 'hand_r'
    L_FootName = 'foot_l'
    R_FootName = 'foot_r'
    
    #Get Joint's Model
    RootM = FBFindModelByLabelName(AddNS+RootName)
    SubRootM = []
    if FBFindModelByLabelName(AddNS+SubRootName)==None:
        SubRootM = FBFindModelByLabelName(AddNS+RootName)
    else:
        SubRootM = FBFindModelByLabelName(AddNS+SubRootName)
    L_WeaponM = FBFindModelByLabelName(AddNS+L_WeaponName)
    R_WeaponM = FBFindModelByLabelName(AddNS+R_WeaponName)
    L_HandM = FBFindModelByLabelName(AddNS+L_HandName)
    R_HandM = FBFindModelByLabelName(AddNS+R_HandName)
    L_FootM = FBFindModelByLabelName(AddNS+L_FootName)
    R_FootM = FBFindModelByLabelName(AddNS+R_FootName)
    
    #Scene Cleanup
    if FBFindModelByLabelName(AddNS+'ik_hand_gun_root')!=None:
        DelList = GetBranch(FBFindModelByLabelName(AddNS+'ik_hand_gun_root'))
        DelArray(DelList)

    if FBFindModelByLabelName(AddNS+'ik_foot_root')!=None:
        DelList = GetBranch(FBFindModelByLabelName(AddNS+'ik_foot_root'))
        DelArray(DelList)

    if FBFindModelByLabelName(AddNS+'ik_foot_root')!=None:
        DelList = GetBranch(FBFindModelByLabelName(AddNS+'ik_foot_root'))
        DelArray(DelList)
    
    
    #Set Rig
    #UpperBody IK Rig
    if UpperBody:

        IKHandGunSpineM = FBModelSkeleton(AddNS+'ik_hand_gun_root')
        IKHandGunSpineM.Parent = SubRootM
        IKHandGunSpineM.Translation = FBVector3d(0,0,0)
        IKHandGunSpineM.Rotation = FBVector3d(0,0,0)
        ZeroOffset(IKHandGunSpineM)
        WeaponSet.ConnectSrc(IKHandGunSpineM)

        IKHandGunM = FBModelSkeleton(AddNS+'ik_hand_gun')
        IKHandGunM.Parent = IKHandGunSpineM
        IKHandGunParConst = DoConstraint(IKHandGunM,R_WeaponM,'Parent/Child')
        ZeroOffset(IKHandGunM)
        WeaponSet.ConnectSrc(IKHandGunM)
        WeaponSet.ConnectSrc(IKHandGunParConst)
        

        #Rig Hand_P
        L_IKHandPM = FBModelSkeleton(AddNS+'ik_hand_p_l')
        L_IKHandPM.Parent = IKHandGunM
        ZeroOffset(L_IKHandPM)
        L_IKHandPM.Translation = FBVector3d(0,0,0)
        L_IKHandPM.Rotation = FBVector3d(0,0,0)
        WeaponSet.ConnectSrc(L_IKHandPM)
        
        R_IKHandPM = FBModelSkeleton(AddNS+'ik_hand_p_r')
        R_IKHandPM.Parent = IKHandGunM
        ZeroOffset(R_IKHandPM)
        R_IKHandPM.Translation = FBVector3d(0,0,0)
        R_IKHandPM.Rotation = FBVector3d(0,0,0)
        WeaponSet.ConnectSrc(R_IKHandPM)
        
        
        L_IKHandM = FBModelSkeleton(AddNS+'ik_hand_l')
        L_IKHandM.Parent = L_IKHandPM
        L_IKHandParConst = DoConstraint(L_IKHandM,L_HandM,'Parent/Child')
        WeaponSet.ConnectSrc(L_IKHandM)
        WeaponSet.ConnectSrc(L_IKHandParConst)
        
        R_IKHandM = FBModelSkeleton(AddNS+'ik_hand_r')
        R_IKHandM.Parent = R_IKHandPM
        R_IKHandParConst = DoConstraint(R_IKHandM,R_HandM,'Parent/Child')
        WeaponSet.ConnectSrc(R_IKHandM)
        WeaponSet.ConnectSrc(R_IKHandParConst)


    #IK Foot Bone
    C_IKFootRootM = FBModelSkeleton(AddNS+'ik_foot_root')
    C_IKFootRootM.Parent = SubRootM
    C_IKFootRootM.Translation = FBVector3d(0,0,0)
    C_IKFootRootM.Rotation = FBVector3d(0,0,0)
    WeaponSet.ConnectSrc(C_IKFootRootM)
    
    L_IKFootM = FBModelSkeleton(AddNS+'ik_foot_l')
    L_IKFootM.Parent = C_IKFootRootM
    ZeroOffset(L_IKFootM)
    L_IKFootParConst = DoConstraint(L_IKFootM,L_FootM,'Parent/Child')
    WeaponSet.ConnectSrc(L_IKFootM)
    WeaponSet.ConnectSrc(L_IKFootParConst)
    
    R_IKFootM = FBModelSkeleton(AddNS+'ik_foot_r')
    R_IKFootM.Parent = C_IKFootRootM
    ZeroOffset(R_IKFootM)
    R_IKFootParConst = DoConstraint(R_IKFootM,R_FootM,'Parent/Child')
    WeaponSet.ConnectSrc(R_IKFootM)
    WeaponSet.ConnectSrc(R_IKFootParConst)
    
    
    AddItems = WeaponSet.Components
    for AddItem in AddItems:
        if AddNS not in AddItem.LongName:
            AddItem.ProcessObjectNamespace(FBNamespaceAction.kFBConcatNamespace, AddNS[:-1])



def ClearSets(SetNames):
    
    FindSet = FBSystem().Scene.Sets
    DelSets = []
    for Set in FindSet:
        for SetName in SetNames:
            if SetName in Set.LongName:
                DelSets.append(Set)
                DelItems = Set.Components
                for i in range(len(DelItems)):
                    DelItems[0].FBDelete()
    for DelSet in reversed(DelSets):
        DelSet.FBDelete()


def ReadyToExport(RootList,UpperBody): 

    SetNames = []
    SetNames.append('IK_Gun_Set')
    SetNames.append('Twist_Set')

    ClearSets(SetNames)
    
    DoWeapon(RootList,UpperBody)
    DoTwist(RootList)
    return True
    