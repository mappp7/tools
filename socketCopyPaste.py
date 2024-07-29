from pyfbsdk import *
from pyfbsdk_additions import *
import pyperclip
import re
import simplejson

class MAIN_:
    def __init__(self):
        self.file_type = None
        self.json_data = {}
        self.selList = []
        self.sks = {}
        self.e = FBEdit()
        self.b = FBButton()
        self.e1 = FBEdit()
        self.b1 = FBButton()
        self.l1 = FBLabel()    
        self.b2 = FBButton()
        self.b3 = FBButton()
        self.b4 = FBButton()
        self.b5 = FBButton()
        self.buttonLyt = FBHBoxLayout()
        self.lyt = FBVBoxLayout()
        self.scrollyt = FBScrollBox()
        self.controls = FBList()
        self.controls.Items.append("NULL")
        self.bb1 = FBButton()
        self.bb2 = FBButton()
        
    def filePopup(self):
        self.json_data = {}
        string_ = ""
        lFp = FBFilePopup()
        lFp.Style = FBFilePopupStyle.kFBFilePopupOpen
        lFp.Filter = "*.s*s"
        lFp.Path = r"Z:\LLL\LLL\Content\LllA"
        lRes = lFp.Execute()
        if lRes:
            self.file_type = lFp.FileName.split(".")[-1]
            path = "{}\{}".format(lFp.Path,lFp.FileName)
            with open(path,  'rt', encoding='UTF8') as file:
                for i in file:
                    
                    if i.find("ForceAlwaysAnimated") == -1:
                        string_ = string_ + i
                    else:
                        re = i.replace('true' , '"true"')
                        string_ = string_ + re
            self.json_data = simplejson.loads(string_)
        
        else:
            FBMessageBox( "FBFilePopup example", "Selection canceled", "OK", None, None )
        
        if self.json_data:
            return self.json_data
            
    def importSKS(self,control,event):
        
        self.sks = self.filePopup()
        if self.sks:
            FBPropertyStringList.removeAll(self.controls.Items)
            
            sksInit = self.sks["Sockets"]
            for i in sksInit:            
                self.controls.Items.append(str(i["SocketName"]))
            
            self.scrollyt.SetContentSize(500,len(self.controls.Items) * 25) 
            
    def onChangeFunc(self,control,event):
        self.selList = []
        for i in range(len(self.controls.Items)):
            if self.controls.IsSelected(i):
                self.selList.append(self.controls.Items[i])
                
    def Btn_copyTranslate(self,control,event):
        trans = FBVector3d()
        lModels = FBModelList()
        FBGetSelectedModels(lModels)
        if len(lModels) == 1:
            lModels[0].GetVector(trans,FBModelTransformationType.kModelTranslation,False)
            text_ = "(X={0},Y={1},Z={2})".format(trans[0] ,trans[1]*-1,trans[2])
            self.e.Text = text_
            pyperclip.copy(text_)
        else:
            self.e.Text = "ERROR!!Plese Select One!"
            pyperclip.copy("")
            
    def Btn_copyRotate(self,control,event):
        rotate = FBVector3d()
        lModels = FBModelList()
        FBGetSelectedModels(lModels)
        if len(lModels) == 1:
            lModels[0].GetVector(rotate ,FBModelTransformationType.kModelRotation ,False)
            text_ = "(Pitch={0},Yaw={1},Roll={2})".format(rotate[1] ,rotate[2]*-1,rotate[0])
            self.e1.Text = text_
            pyperclip.copy(text_)
        else:
            self.e1.Text = "ERROR!!Plese Select One!"
            pyperclip.copy("")
    
    def Btn_pasteTranslate(self,control,event):
        lModels = FBModelList()
        FBGetSelectedModels(lModels)
        if len(lModels) ==1:
            text_ = pyperclip.paste()
            print(text_)
            num = re.findall(r"[-+]?(?:\d*\.\d+|\d+)", text_)
            x = float(num[0]);y = float(num[1])*-1;z = float(num[2]);
            lModels[0].SetVector(FBVector3d(x,y,z),FBModelTransformationType.kModelTranslation,False)
        else:
            pass
            
    def Btn_pasteRotate(self,control,event):
        lModels = FBModelList()
        FBGetSelectedModels(lModels)
        if len(lModels) ==1:
            text_ = pyperclip.paste()
            print(text_)
            num = re.findall(r"[-+]?(?:\d*\.\d+|\d+)", text_)
            x = float(num[2]);y = float(num[0])*-1;z = float(num[1])*-1;
            #lModels[0].Rotation = FBVector3d(x,y,z)
            lModels[0].SetVector(FBVector3d(x,y,z) ,FBModelTransformationType.kModelRotation , False )
        else:
            pass
    
    def Btn_Execute(self,control , event):
        print(self.sks)
        parent_grp= None
        if self.file_type == "sms":
            parent_grp = FBModelMarker(str("Zup_group"))
        if self.sks:
            for i in self.sks["Sockets"]:
                if str(i["SocketName"]) in self.selList:
                    marker = FBModelMarker(str(i["SocketName"]))
                    marker.Show = True
                    marker.Size = 300
                    marker.PropertyList.Find('LookUI').Data=2
                    marker.Color = FBColor(0,1,1)
                    if self.file_type == "sms":
                        marker.Parent = parent_grp
                    else:
                        marker.Parent = FBFindModelByLabelName(str(i["BoneName"]))
                    marker.SetVector(self.ueToMobuTranslate(i["RelativeLocation"]),FBModelTransformationType.kModelTranslation,False)
                    marker.SetVector(self.ueToMobuRotate(i["RelativeRotation"]),FBModelTransformationType.kModelRotation,False)
                    #marker.Rotation = self.ueToMobuRotate(i["RelativeRotation"])
        if parent_grp:
            parent_grp.SetVector(FBVector3d(-90,0,0),FBModelTransformationType.kModelRotation,False)
                    
            
    def selectAll(self,control,event):
        if self.controls:
            self.selList = []
            for i in range(len(self.controls.Items)):
                self.controls.Selected(i ,True)
                self.selList.append(self.controls.Items[i])
    def selectClear(self,control,event):
        if self.controls:
            for i in range(len(self.controls.Items)):
                self.controls.Selected(i ,False)
                
            self.selList = []     
                      
    def ueToMobuTranslate(self,data):
        strdata = str(data)
        num = re.findall(r"[-+]?(?:\d*\.\d+|\d+)", strdata)
        x = float(num[0]);y = float(num[1])*-1;z = float(num[2]);
        return FBVector3d(x,y,z)
        
    def ueToMobuRotate(self,data):
        strdata = str(data)
        num = re.findall(r"[-+]?(?:\d*\.\d+|\d+)", strdata)
        x = float(num[2]);y = float(num[0])*-1;z = float(num[1])*-1;
        return FBVector3d(x,y,z)
        
    def PopulateTool(self,t):
        len_ = len(self.controls.Items)
        self.controls.OnChange.Add(self.onChangeFunc)
        x = FBAddRegionParam(5,FBAttachType.kFBAttachLeft,"")
        y = FBAddRegionParam(5,FBAttachType.kFBAttachTop,"")
        w = FBAddRegionParam(-5,FBAttachType.kFBAttachRight,"")
        h = FBAddRegionParam(20,FBAttachType.kFBAttachNone,"")
        t.AddRegion("dirButton","dirButton",x,y,w,h)
        t.SetControl("dirButton" , self.b4)
        self.b4.Caption = "Find Socket File"
        self.b4.OnClick.Add(self.importSKS)
        
        x = FBAddRegionParam(5,FBAttachType.kFBAttachLeft,"")
        y = FBAddRegionParam(5,FBAttachType.kFBAttachBottom,"dirButton")
        w = FBAddRegionParam(-5,FBAttachType.kFBAttachRight,"")
        h = FBAddRegionParam(-265,FBAttachType.kFBAttachBottom,"")
        t.AddRegion("scroll","scroll", x,y,w,h)
        t.SetControl("scroll",self.scrollyt)
        
        self.controls.Style = FBListStyle.kFBVerticalList
        self.controls.MultiSelect = True
        #self.lyt.AllowExpansion = True
        
        x = FBAddRegionParam(0,FBAttachType.kFBAttachLeft,"")
        y = FBAddRegionParam(0,FBAttachType.kFBAttachTop,"")
        w = FBAddRegionParam(0,FBAttachType.kFBAttachRight,"")
        h = FBAddRegionParam(0,FBAttachType.kFBAttachBottom,"")
        self.scrollyt.Content.AddRegion("main","main",x,y,w,h)
        self.scrollyt.Content.SetControl("main",self.lyt)
        self.lyt.Add(self.controls , 500)
        
        self.scrollyt.SetContentSize(500,len_ * 25)
        ###########################
        x = FBAddRegionParam(5,FBAttachType.kFBAttachLeft,"")
        y = FBAddRegionParam(0,FBAttachType.kFBAttachBottom,"scroll")
        w = FBAddRegionParam(-5,FBAttachType.kFBAttachRight,"")
        h = FBAddRegionParam(25,FBAttachType.kFBAttachNone,"")
        t.AddRegion("HLyt","HLyt", x,y,w,h)
        t.SetControl("HLyt",self.buttonLyt)
        
        x = FBAddRegionParam(5,FBAttachType.kFBAttachLeft,"")
        y = FBAddRegionParam(5,FBAttachType.kFBAttachTop,"")
        w = FBAddRegionParam(100,FBAttachType.kFBAttachNone,"")
        h = FBAddRegionParam(25,FBAttachType.kFBAttachNone,"")
        self.buttonLyt.AddRegion("bb1","bb1", x,y,w,h)
        self.buttonLyt.SetControl("bb1",self.bb1)
        self.bb1.Caption = "All Select"
        self.bb1.OnClick.Add(self.selectAll)
        
        x = FBAddRegionParam(5,FBAttachType.kFBAttachRight,"bb1")
        y = FBAddRegionParam(5,FBAttachType.kFBAttachTop,"")
        w = FBAddRegionParam(100,FBAttachType.kFBAttachNone,"")
        h = FBAddRegionParam(25,FBAttachType.kFBAttachNone,"")
        self.buttonLyt.AddRegion("bb2","bb2", x,y,w,h)
        self.buttonLyt.SetControl("bb2",self.bb2)
        self.bb2.Caption = "Clear"
        self.bb2.OnClick.Add(self.selectClear)
        
        #################################
        x = FBAddRegionParam(5,FBAttachType.kFBAttachLeft,"")
        y = FBAddRegionParam(5,FBAttachType.kFBAttachBottom,"HLyt")
        w = FBAddRegionParam(-5,FBAttachType.kFBAttachRight,"")
        h = FBAddRegionParam(25,FBAttachType.kFBAttachNone,"")
        t.AddRegion("execute1","execute1", x,y,w,h)
        t.SetControl("execute1",self.b5)
        self.b5.Caption = "MAKE SOCKET"
        self.b5.Style = FBButtonStyle.kFBPushButton
        self.b5.Look = FBButtonLook.kFBLookColorChange
        self.b5.SetStateColor(FBButtonState.kFBButtonState0,FBColor(0.4,0.4, 0.2))
        self.b5.OnClick.Add(self.Btn_Execute)
        
        x = FBAddRegionParam(5,FBAttachType.kFBAttachLeft,"")
        y = FBAddRegionParam(-30,FBAttachType.kFBAttachTop,"button1")
        w = FBAddRegionParam(-5,FBAttachType.kFBAttachRight,"")
        h = FBAddRegionParam(20,FBAttachType.kFBAttachNone,"")
        t.AddRegion("EditFBEdit","EditFBEdit", x, y, w, h)
        t.SetControl("EditFBEdit",self.e)
        self.e.Text = "(X=NULL,Y=NULL,Z=NULL)"
        self.e.ReadOnly = True
        
        
        x = FBAddRegionParam(5,FBAttachType.kFBAttachLeft,"")
        y = FBAddRegionParam(-30,FBAttachType.kFBAttachTop,"EditFBEdit1")
        w = FBAddRegionParam(-5,FBAttachType.kFBAttachRight,"")
        h = FBAddRegionParam(25,FBAttachType.kFBAttachNone,"")
        t.AddRegion("button1","button1", x, y, w, h)
        t.SetControl("button1",self.b)
        self.b.Caption = "Copy Translate"
        self.b.Style = FBButtonStyle.kFBPushButton
        self.b.Look = FBButtonLook.kFBLookColorChange
        self.b.SetStateColor(FBButtonState.kFBButtonState0,FBColor(0.1,0.4, 0.5))
        self.b.OnClick.Add(self.Btn_copyTranslate)
        
        x = FBAddRegionParam(5,FBAttachType.kFBAttachLeft,"")
        y = FBAddRegionParam(-30,FBAttachType.kFBAttachTop,"button2")
        w = FBAddRegionParam(-5,FBAttachType.kFBAttachRight,"")
        h = FBAddRegionParam(20,FBAttachType.kFBAttachNone,"")
        t.AddRegion("EditFBEdit1","EditFBEdit1", x, y, w, h)
        t.SetControl("EditFBEdit1",self.e1)
        self.e1.Text = "(Pitch=NULL,Yaw=NULL,Roll=NULL)"
        self.e1.ReadOnly = True
        
        x = FBAddRegionParam(5,FBAttachType.kFBAttachLeft,"")
        y = FBAddRegionParam(-30,FBAttachType.kFBAttachTop,"label1")
        w = FBAddRegionParam(-5,FBAttachType.kFBAttachRight,"")
        h = FBAddRegionParam(25,FBAttachType.kFBAttachNone,"")
        t.AddRegion("button2","button2", x, y, w, h)
        t.SetControl("button2",self.b1)
        self.b1.Caption = "Copy Rotate"
        self.b1.Style = FBButtonStyle.kFBPushButton
        self.b1.Look = FBButtonLook.kFBLookColorChange
        self.b1.SetStateColor(FBButtonState.kFBButtonState0,FBColor(0.1,0.4, 0.5))
        self.b1.OnClick.Add(self.Btn_copyRotate)
        
        x = FBAddRegionParam(10,FBAttachType.kFBAttachCenter,"")
        y = FBAddRegionParam(-30,FBAttachType.kFBAttachTop,"button3")
        w = FBAddRegionParam(-5,FBAttachType.kFBAttachRight,"")
        h = FBAddRegionParam(25,FBAttachType.kFBAttachNone,"")
        t.AddRegion("label1","label1", x, y, w, h)
        t.SetControl("label1",self.l1)
        self.l1.Caption = "<====UE TO MOBU====>"
        self.l1.Style = FBTextStyle.kFBTextStyleBold
        self.l1.Justify = FBTextJustify.kFBTextJustifyCenter
        
        x = FBAddRegionParam(5,FBAttachType.kFBAttachLeft,"")
        y = FBAddRegionParam(-30,FBAttachType.kFBAttachTop,"button4")
        w = FBAddRegionParam(-5,FBAttachType.kFBAttachRight,"")
        h = FBAddRegionParam(25,FBAttachType.kFBAttachNone,"")
        t.AddRegion("button3","button3", x, y, w, h)
        t.SetControl("button3",self.b2)
        self.b2.Caption = "Paste Translate"
        self.b2.Style = FBButtonStyle.kFBPushButton
        self.b2.Look = FBButtonLook.kFBLookColorChange
        self.b2.SetStateColor(FBButtonState.kFBButtonState0,FBColor(0.5,0.3, 0.3))
        self.b2.OnClick.Add(self.Btn_pasteTranslate)
        
        x = FBAddRegionParam(5,FBAttachType.kFBAttachLeft,"")
        y = FBAddRegionParam(-30,FBAttachType.kFBAttachBottom,"")
        w = FBAddRegionParam(-5,FBAttachType.kFBAttachRight,"")
        h = FBAddRegionParam(25,FBAttachType.kFBAttachNone,"")
        t.AddRegion("button4","button4", x, y, w, h)
        t.SetControl("button4",self.b3)
        self.b3.Caption = "Paste Rotate"
        self.b3.Style = FBButtonStyle.kFBPushButton
        self.b3.Look = FBButtonLook.kFBLookColorChange
        self.b3.SetStateColor(FBButtonState.kFBButtonState0,FBColor(0.5,0.3, 0.3))
        self.b3.OnClick.Add(self.Btn_pasteRotate)
        
    def CreateTool(self):
        t = FBCreateUniqueTool("Copy Transform Tool")
        t.StartSizeX = 240
        t.StartSizeY = 500
        self.PopulateTool(t)
        ShowTool(t)

mc = MAIN_()
mc.CreateTool()    

        
########################################

    