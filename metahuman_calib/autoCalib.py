import logging

import maya.OpenMaya as om
from maya import cmds
import maya.mel as mel

import os
import site
import importlib
basePath = os.path.abspath(__file__ + '/../')
site.addsitedir(basePath)

from PySide2 import QtGui, QtCore, QtWidgets

from PySide2.QtGui import *
from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtUiTools import QUiLoader
import xml.etree.ElementTree as xml

from functools import partial
from os import environ, makedirs
from os import path as ospath
from sys import path as syspath
from sys import platform

site.addsitedir("Z:/P4V/LLL/LllArt/Animation/Script/Asset")

#maya ver : 2023
ROOT_DIR = "Z:/P4V/LLL/LllArt/Animation/Script/Asset/MetaHuman-DNA-Calibration-1.1.0"
ROOT_LIB_DIR = f"{ROOT_DIR}/lib/Maya2023"

if platform == "win32":
    LIB_DIR = f"{ROOT_LIB_DIR}/windows"
elif platform == "linux":
    LIB_DIR = f"{ROOT_LIB_DIR}/linux"
else:
    raise OSError(
        "OS not supported, please compile dependencies and add value to LIB_DIR"
    )

if "MAYA_PLUG_IN_PATH" in environ:
    separator = ":" if platform == "linux" else ";"
    environ["MAYA_PLUG_IN_PATH"] = separator.join([environ["MAYA_PLUG_IN_PATH"], LIB_DIR])
else:
    environ["MAYA_PLUG_IN_PATH"] = LIB_DIR
syspath.insert(0, ROOT_DIR)
syspath.insert(0, LIB_DIR)

from dna import (
    BinaryStreamReader,
    BinaryStreamWriter,
    DataLayer_All,
    FileStream,
    Status,
)
from dnacalib import (
    CommandSequence,
    DNACalibDNAReader,
    SetNeutralJointRotationsCommand,
    SetNeutralJointTranslationsCommand,
    SetVertexPositionsCommand,
    VectorOperation_Add,
    RotateCommand
)
from dna_viewer import DNA, RigConfig, build_rig


class dnaCalibCls(QtWidgets.QMainWindow):#form_class, base_class):
    def __init__(self, parent=None):
        super(dnaCalibCls, self).__init__(parent)
        #self.setupUi(self)
        uiFile = os.path.join(basePath, 'dnaCalib_ui.ui')

        self.ui_ = QFile(uiFile)
        
        self.ui_.open(QFile.ReadOnly)
        loader = QUiLoader()
        self.ui = loader.load(self.ui_)
        self.ui.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        self.ui.close()
        self.setWindowTitle('DNA CALIB TOOL')
        self.createConnections()

        self.CHARACTER_NAME = ""
        
        ROOT_DIR = "Z:/P4V/LLL/LllArt/Animation/Script/Asset/MetaHuman-DNA-Calibration-1.1.0"
        DATA_DIR = f"{ROOT_DIR}/data"
        self.DNA_DIR = f"{DATA_DIR}/dna"
        self.ANALOG_GUI = f"{DATA_DIR}/analog_gui.ma"
        self.GUI = f"{DATA_DIR}/gui.ma"
        self.ADDITIONAL_ASSEMBLE_SCRIPT = f"{DATA_DIR}/additional_assemble_script.py"
        ADD_MESH_NAME_TO_BLEND_SHAPE_CHANNEL_NAME = True

        self.CHARACTER_DNA = f"{ROOT_DIR}/input_dna/{self.CHARACTER_NAME}.dna"
        self.OUTPUT_DIR = f"{ROOT_DIR}/output_dna"
        
        
        self.current_vertices_positions = {}

    def createConnections(self):
        self.ui.dnaFile_BTN.clicked.connect(self.dnaFile_btn_Func)
        self.ui.dnaLoad_BTN.clicked.connect(self.dnaLoad_btn_Func)
        self.ui.newHead_BTN.clicked.connect(self.newHead_btn_Func)
        self.ui.bodyMesh_BTN.clicked.connect(self.bodyMesh_btn_Func)
        self.ui.fittingBone_BTN.clicked.connect(self.fittingBone_btn_Func)
        self.ui.dnaSavePath_BTN.clicked.connect(self.dnaSavePath_btn_Func)
        self.ui.createMetahuman_BTN.clicked.connect(self.create)
        """
        
        
        self.ui.lodSetting_CBX
        self.ui.dnaSavePath_BTN
        """
        #animation 
        self.ui.dnaFile_ani_BTN.clicked.connect(self.dnaFile_ani_btn_Func)
        self.ui.skFile_ani_BTN.clicked.connect(self.skFile_ani_btn_Func)
        self.ui.setRig_BTN.clicked.connect(self.setRigFunc)
        self.ui.aniTool_BTN.clicked.connect(self.aniToolFunc)
        
        
        """
        self.ui.lodSetting_CBX
        self.ui.dnaSavePath_BTN
        """
    def dnaFile_ani_btn_Func(self):
        self.CHARACTER_ANI_DNA = cmds.fileDialog2(fileFilter = "*.dna" , dialogStyle = 2 , fileMode = 1)[0]
        self.ui.dnaFile_ani_LED.setText(str(self.CHARACTER_ANI_DNA))
        self.CHARACTER_ANI_NAME = self.CHARACTER_ANI_DNA.split("/")[-1].split(".dna")[0]
    
    def skFile_ani_btn_Func(self):
        self.SKELETON_ANI_DNA = cmds.fileDialog2(fileFilter = "*.fbx" , dialogStyle = 2 , fileMode = 1)[0]
        self.ui.skFile_ani_LED.setText(str(self.SKELETON_ANI_DNA))
        self.SKELETON_ANI_NAME = self.SKELETON_ANI_DNA.split("/")[-1].split(".fbx")[0]
        
    def setRigFunc(self):
        if self.CHARACTER_ANI_DNA and self.SKELETON_ANI_DNA:
            
            dna = DNA(self.CHARACTER_ANI_DNA)
            config = RigConfig(
                gui_path=self.GUI,
                analog_gui_path=self.ANALOG_GUI,
                aas_path=self.ADDITIONAL_ASSEMBLE_SCRIPT,
            )
            build_rig(dna=dna, config=config)
            
            cmds.file(str(self.SKELETON_ANI_DNA) , r=True , type = "FBX" , mergeNamespacesOnClash = False , namespace = "previewFace" )

            a = cmds.group(em = True)
            cmds.parent("spine_04" , "headRig_grp" , a)
            cmds.xform(a , ro = [90,0,0])
            cmds.xform("headGui_grp" , ro = [0,90,0])
            cmds.hide("head_grp")

            bonegrp = cmds.ls("previewFace:*" , type = "joint")
            cmds.select(bonegrp)
            for i in bonegrp:
                if cmds.objExists(i.split(":")[-1]):
                    cmds.parentConstraint(i.split(":")[-1] , i , mo=1)
            
    def aniToolFunc(self):
        import metahuman_facial_animation_support.metahuman_facial_transfer as ms
        importlib.reload(ms)
        ms.UI()
    def dnaFile_btn_Func(self):
        self.CHARACTER_DNA = cmds.fileDialog2(fileFilter = "*.dna" , dialogStyle = 2 , fileMode = 1)[0]
        self.ui.dnaFile_LED.setText(str(self.CHARACTER_DNA))

        self.CHARACTER_NAME = self.CHARACTER_DNA.split("/")[-1].split(".dna")[0]
        print (self.CHARACTER_DNA)
        print (self.CHARACTER_NAME)
    
    def dnaLoad_btn_Func(self):
        if self.CHARACTER_NAME:
            self.ui.dnaFile_status_LBL.setText("Wait...")
            self.ui.dnaFile_status_LBL.setStyleSheet("color: rgb(255, 255, 0);")
            mel.eval("""setUpAxis "y";""")
            dna = DNA(self.CHARACTER_DNA)
            config = RigConfig(
                gui_path=self.GUI,
                analog_gui_path=self.ANALOG_GUI,
                aas_path=self.ADDITIONAL_ASSEMBLE_SCRIPT,
            )
            build_rig(dna=dna, config=config)

            # this is step 3 sub-step a
            for mesh_index, name in enumerate(dna.meshes.names):
                self.current_vertices_positions[name] = {
                    "mesh_index": mesh_index,
                    "positions": self.get_mesh_vertex_positions_from_scene(name),
                }
            print(self.current_vertices_positions)
            self.ui.dnaFile_status_LBL.setText("Load")
            self.ui.dnaFile_status_LBL.setStyleSheet("color: rgb(85, 255, 0);")
    
    def newHead_btn_Func(self):
        newHead = cmds.fileDialog2(fileFilter = "*.obj" , dialogStyle = 2 , fileMode = 1)[0]
        self.ui.newHead_LED.setText(str(newHead))
        
        beforeImport = cmds.ls("*","*:*" , type = "transform")
        cmds.file(newHead, i=True)
        afterImport = cmds.ls("*","*:*" , type = "transform")
        meshImport = [x for x in afterImport if x not in beforeImport]
        if len(meshImport) > 1:
            self.ui.Newhead_status_LBL.setText("OBJ contain more than 2 object")
            self.ui.Newhead_status_LBL.setStyleSheet("color: rgb(255, 0, 0);")
            cmds.delete(meshImport)
        else:
            self.ui.Newhead_status_LBL.setText("Load")
            self.ui.Newhead_status_LBL.setStyleSheet("color: rgb(85, 255, 0);")

            cmds.rename(meshImport[0] , "NewHead")
    def bodyMesh_btn_Func(self):
        
        bodyMesh = cmds.fileDialog2(fileFilter = "*.fbx" , dialogStyle = 2 , fileMode = 1)[0]
        
        before = set(cmds.ls(type='transform'))
        self.ui.bodyMesh_status_LBL.setText("Wait...")
        self.ui.bodyMesh_status_LBL.setStyleSheet("color: rgb(255, 255, 0);")
        self.ui.bodyMesh_LED.setText(str(bodyMesh))

        cmds.file(bodyMesh, reference=True, iv = True , namespace="bodyRig")
        self.ui.bodyMesh_status_LBL.setText("Load")
        self.ui.bodyMesh_status_LBL.setStyleSheet("color: rgb(85, 255, 0);")

        referenceNode = cmds.file(bodyMesh, query = True ,referenceNode = True)
        after = set(cmds.ls(type='transform'))
        imported = after - before
        
        print (imported)
        print (referenceNode)
        cmds.select(imported)
        if cmds.objExists("bodyRig:root"):
            cmds.xform("bodyRig:root" , ro = [-90,-90,0])
        else:
            self.ui.bodyMesh_status_LBL.setText("ERROR!")
            self.ui.bodyMesh_status_LBL.setStyleSheet("color: rgb(255, 0, 0);")
        
    def fittingBone_btn_Func(self):
        cmds.namespace(add= "DHIhead")
        cmds.select(cl=1)
        cmds.select("spine_04" , hi=1)
        boneList = cmds.ls(sl=1)

        for i in boneList:
            cmds.rename(i , "DHIhead:" + i)
        #Enter Wrapped Head Mesh Name below
        enter_wrapped_mesh_name = "NewHead"
        lod_base_mesh_name = "head_lod0_mesh"
        #Enter folder path below where additional scripts are stored. Do not change slash to forward slash
        #current folder path
        python_folder_path = "Z:/P4V/LLL/LllArt/Animation/Script/Asset/metahuman_rig_transfer"
        # example : DHIhead: if dnareader not import name space.
        name_space = "DHIhead:"

        #Alright lets go

        cmds.select( clear=True )
        cmds.duplicate(name_space + 'spine_04')

        def select_loop_bones():
        
            #giving OG and old mesh a variable name//edit mesh name here
            cmds.select(lod_base_mesh_name)
            ogmesh = cmds.ls( selection=True )

            cmds.select(enter_wrapped_mesh_name)
            newmesh = cmds.ls( selection=True )

            #selecting the bone//edit the bone name here
            cmds.select('spine_04', hierarchy=True)
            bone_List = cmds.ls( selection=True )
            cmds.select( clear=True )

            #Starting bone loop
            boneID = 0
            while boneID < len(bone_List):
                bone = bone_List[boneID]
                
                #run OG_Mesh file
                exec(open('%s/OG_Mesh.py'%python_folder_path).read())
                #run Get_Bone_Data file
                exec(open('%s/Get_Bone_Data.py'%python_folder_path).read())
                #run New_Mesh file
                exec(open('%s/New_Mesh.py'%python_folder_path).read())
                #run Vertex_Offset file
                exec(open('%s/Vertex_Offset.py'%python_folder_path).read())
                #run Set_Bone_data file
                exec(open('%s/Set_Bone_Data.py'%python_folder_path).read())
                
                boneID = boneID+1

        select_loop_bones()
        cmds.select( clear=True )
        unparentList = ['clavicle_pec_l','clavicle_pec_r','spine_04_latissimus_l','spine_04_latissimus_r','clavicle_l','clavicle_r','neck_01',"FACIAL_C_Neck1Root","FACIAL_C_Neck2Root","FACIAL_C_FacialRoot"]
        for i in unparentList:
            cmds.parent(i , w=1)
        for ii in ["spine_04" , "neck_01" , "neck_02" , "head" , "clavicle_r" , "clavicle_l" , "upperarm_l" , "upperarm_r"]:
            cmds.select("bodyRig:" + ii , ii);mel.eval("delete`parentConstraint`")
        x_ = cmds.xform("spine_05" , q=1 ,t=1)[0]/2
        cmds.setAttr("spine_05.translateX" , x_)

        for i in unparentList:
            if i == "FACIAL_C_Neck1Root":
                cmds.parent(i,"neck_01")
            elif i == "FACIAL_C_Neck2Root":
                cmds.parent(i,"neck_02")
            elif i == "FACIAL_C_FacialRoot":
                cmds.parent(i,"head")
            else:
                cmds.parent(i,"spine_05")
        cmds.select('spine_04', hierarchy=True)
        self.RotationZero(toJo=True)

        #blendShape & wrap
        cmds.select(["head_lod3_mesh" , "head_lod4_mesh"]);mel.eval("DeleteHistory;")
        cmds.select(["head_lod3_mesh","head_lod4_mesh" , "head_lod0_mesh"])
        cmds.CreateWrap()
        bs = cmds.blendShape("NewHead" , "head_lod0_mesh" ,before=True )
        cmds.setAttr(bs[0]+".NewHead" , 1)

        cmds.hide("DHIhead:spine_04")

    def RotationZero(self,toJo):
        sel_ = cmds.ls(os=1,type='joint')
        for i in sel_:
            wsRot_ = cmds.xform(i,q=1,ws=1,ro=1)
            cmds.setAttr(i+'.jo',0,0,0,type='float3')
            cmds.xform(i,ws=1,ro=wsRot_)
            if toJo:
                lsRot_ = cmds.getAttr(i+'.r')
                cmds.setAttr(i+'.r',0,0,0,type='float3')
                cmds.setAttr(i+'.jo',lsRot_[0][0],lsRot_[0][1],lsRot_[0][2],type='float3')

    def dnaSavePath_btn_Func(self):
        savePath = cmds.fileDialog2( dialogStyle = 2 , fileMode = 3)[0]
        savePath = savePath.replace("\\" , "/")
        self.OUTPUT_DIR = savePath
        makedirs(self.OUTPUT_DIR, exist_ok=True)
        self.ui.dnaSavePath_LED.setText(str(self.OUTPUT_DIR))
        print 

    def create(self):
        reader = self.load_dna_reader(self.CHARACTER_DNA)
        calibrated = DNACalibDNAReader(reader)

        self.run_joints_command(reader, calibrated)

        for name, item in self.current_vertices_positions.items():
            new_vertices_positions = self.get_mesh_vertex_positions_from_scene(name)
            if new_vertices_positions:
                self.run_vertices_command(
                    calibrated, item["positions"], new_vertices_positions, item["mesh_index"]
                )
        self.run_rotate_command(calibrated)
        self.save_dna(calibrated)
        #mel.eval("""setUpAxis "z";""")
        self.assemble_maya_scene()
        
    def load_dna_reader(self , path):
        stream = FileStream(path, FileStream.AccessMode_Read, FileStream.OpenMode_Binary)
        reader = BinaryStreamReader(stream, DataLayer_All)
        reader.read()
        if not Status.isOk():
            status = Status.get()
            raise RuntimeError(f"Error loading DNA: {status.message}")
        return reader
    
    def save_dna(self , reader):
        self.MODIFIED_CHARACTER_DNA = f"{self.OUTPUT_DIR}/{self.CHARACTER_NAME}_DNACalib"
        stream = FileStream(
            f"{self.MODIFIED_CHARACTER_DNA}.dna",
            FileStream.AccessMode_Write,
            FileStream.OpenMode_Binary,
        )
        writer = BinaryStreamWriter(stream)
        writer.setFrom(reader)
        writer.write()

        print (self.MODIFIED_CHARACTER_DNA)

        if not Status.isOk():
            status = Status.get()
            raise RuntimeError(f"Error saving DNA: {status.message}")
    
    def get_mesh_vertex_positions_from_scene(self,meshName):
        try:
            sel = om.MSelectionList()
            sel.add(meshName)

            dag_path = om.MDagPath()
            sel.getDagPath(0, dag_path)

            mf_mesh = om.MFnMesh(dag_path)
            positions = om.MPointArray()

            mf_mesh.getPoints(positions, om.MSpace.kObject)
            return [
                [positions[i].x, positions[i].y, positions[i].z]
                for i in range(positions.length())
            ]
        except RuntimeError:
            print(f"{meshName} is missing, skipping it")
            return None
        
    def run_joints_command(self,reader, calibrated):
        # Making arrays for joints' transformations and their corresponding mapping arrays
        joint_translations = []
        joint_rotations = []

        for i in range(reader.getJointCount()):
            joint_name = reader.getJointName(i)

            translation = cmds.xform(joint_name, query=True, translation=True)
            joint_translations.append(translation)

            rotation = cmds.joint(joint_name, query=True, orientation=True)
            joint_rotations.append(rotation)

        # this is step 5 sub-step a
        set_new_joints_translations = SetNeutralJointTranslationsCommand(joint_translations)
        # this is step 5 sub-step b
        set_new_joints_rotations = SetNeutralJointRotationsCommand(joint_rotations)

        # Abstraction to collect all commands into a sequence, and run them with only one invocation
        commands = CommandSequence()
        # Add vertex position deltas (NOT ABSOLUTE VALUES) onto existing vertex positions
    
        commands.add(set_new_joints_translations)
        commands.add(set_new_joints_rotations)
        
        commands.run(calibrated)
        # verify that everything went fine
        if not Status.isOk():
            status = Status.get()
            raise RuntimeError(f"Error run_joints_command: {status.message}")

    def run_vertices_command(self,calibrated, old_vertices_positions, new_vertices_positions, mesh_index):
        # making deltas between old vertices positions and new one
        deltas = []
        for new_vertex, old_vertex in zip(new_vertices_positions, old_vertices_positions):
            delta = []
            for new, old in zip(new_vertex, old_vertex):
                delta.append(new - old)
            deltas.append(delta)

        # this is step 5 sub-step c
        new_neutral_mesh = SetVertexPositionsCommand(
            mesh_index, deltas, VectorOperation_Add
        )
        commands = CommandSequence()
        # Add nex vertex position deltas (NOT ABSOLUTE VALUES) onto existing vertex positions
        commands.add(new_neutral_mesh)

        commands.run(calibrated)
        

        # verify that everything went fine
        if not Status.isOk():
            status = Status.get()
            raise RuntimeError(f"Error run_vertices_command: {status.message}")
    
    def run_rotate_command(self,calibrated):
        rot_by_ninty = RotateCommand([0,90,0],[0,0,0])
        #rot_by_ninty = RotateCommand([90,0,90],[0,0,0])
        commands = CommandSequence()
        commands.add(rot_by_ninty)
        commands.run(calibrated)

    def assemble_maya_scene(self):
        dna = DNA(f"{self.MODIFIED_CHARACTER_DNA}.dna")
        config = RigConfig(
            gui_path=self.GUI,
            analog_gui_path=self.ANALOG_GUI,
            aas_path=self.ADDITIONAL_ASSEMBLE_SCRIPT,
        )
        build_rig(dna=dna, config=config)

        cmds.file(rename=f"{self.MODIFIED_CHARACTER_DNA}.mb")
        #cmds.file(save=True)

   



def OPEN():
    global Window
    try:
        Window.close()
        Window.deleteLater()
    except: pass
    Window = dnaCalibCls()
    Window.ui.show()
    
    #ui.show()
    
