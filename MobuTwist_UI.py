from pyfbsdk import *
from pyfbsdk_additions import *
from MobuTwist import *

def DoTwistToggle():
    
    SetName = 'Twist_Set'
    ChkSet = True
    DelSets = []
    for Set in FBSystem().Scene.Sets:
        if SetName in Set.LongName:
            DelSets.append(Set)
            ChkSet=False
    
    for DelSet in DelSets:
        DelItems = DelSet.Components
        for i in range(len(DelItems)):
            DelItems[0].FBDelete()
        DelSet.FBDelete()           
            
    if ChkSet:
        RootLists = []
        for TopNode in FBSystem().Scene.RootModel.Children:
            if TopNode.Name=='root':
                RootLists.append(TopNode.LongName)
        for RootList in RootLists:
            try:
                DoTwist(RootList)
            except:
                continue



def BtnCallbackSwitchBtn(control, event):
    global stat
    stat = 1-stat
    SwitchBtn.Caption = SwitchCaption[stat]
    DoTwistToggle()

def PopulateTool(t):
    
    SetName = 'Twist_Set'
    global SwitchCaption
    SwitchCaption = ['Status : None','Status : Twist']
    global stat
    stat = 0
    for Set in FBSystem().Scene.Sets:
        if SetName in Set.LongName:
            stat = 1
    
    global SwitchBtn
    SwitchBtn = FBButton()
    x = FBAddRegionParam(15,FBAttachType.kFBAttachNone,"")
    y = FBAddRegionParam(10,FBAttachType.kFBAttachNone,"")
    w = FBAddRegionParam(120,FBAttachType.kFBAttachNone,"")
    h = FBAddRegionParam(30,FBAttachType.kFBAttachNone,"")
    t.AddRegion("SwitchBtn","SwitchBtn", x, y, w, h)
     
    t.SetControl("SwitchBtn", SwitchBtn)
    SwitchBtn.Visible  = True
    SwitchBtn.ReadOnly = False
    SwitchBtn.Enabled  = True
    SwitchBtn.Hint     = "Twist & Static Toggle"
    SwitchBtn.Caption  = SwitchCaption[stat]
    SwitchBtn.State    = stat
    SwitchBtn.Style    = FBButtonStyle.kFB2States
    SwitchBtn.Justify  = FBTextJustify.kFBTextJustifyCenter
    SwitchBtn.Look     = FBButtonLook.kFBLookColorChange
    SwitchBtn.SetStateColor(FBButtonState.kFBButtonState0,FBColor(0.164,0.164,0.164))
    SwitchBtn.SetStateColor(FBButtonState.kFBButtonState1,FBColor(0.0, 0.0, 0.0))
    SwitchBtn.OnClick.Add(BtnCallbackSwitchBtn)

 
def TwistCreateTool():
    t = FBCreateUniqueTool("MobuTwist")
    t.StartSizeX    = 155
    t.StartSizeY    = 70
    PopulateTool(t)
    ShowTool(t)


TwistCreateTool()