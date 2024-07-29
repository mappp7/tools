import maya.cmds as cmds
import maya.mel as mel 
import pymel.core.general as gn

def main():
    # head mesh 잡고 실행
    headmesh = cmds.ls(sl=1)[0]
    cmds.select( clear=True )


    #Enter Wrapped Head Mesh Name below
    # 매쉬 양식은 아래와 같아야함.
    enter_wrapped_mesh_name = headmesh
    type = headmesh.split("_")[1]

    eye_l_mesh_name = 'ch_%s_eyel_lod0'%type
    eye_r_mesh_name = 'ch_%s_eyer_lod0'%type
    eyeao_mesh_name = 'ch_%s_eyeao_lod0'%type
    eyelash_mesh_name = 'ch_%s_eyelash_lod0'%type
    teeth_mesh_name = 'ch_%s_teeth_lod0'%type



    reference_path = "Z:\\P4V\\LLL\\LllA\\Character\\BNpc\\shared\\Basebody\\sk_ch_nhm_facial.fbx"


    cmds.file(reference_path, reference=True, namespace="copyModel")
    cmds.select("copyModel:root" , hi=1)

    boneList = cmds.ls(sl=1)

    slls=gn.ls(sl=1)
    for sl in slls: 
        if sl.nodeType() != 'joint': continue
        shortNm=sl.split('|')[-1]
        if shortNm[-2:]=='_l':
            shortNm=shortNm[:len(shortNm)-2]
            sl.setAttr('side',1)
        elif shortNm[-2:]=='_r':
            shortNm=shortNm[:len(shortNm)-2]
            sl.setAttr('side',2)
        elif shortNm.find('_L_') != -1:
            shortNm=shortNm.split("_L_")[-1]
            sl.setAttr('side',1)
        elif shortNm.find('_R_') != -1:
            shortNm=shortNm.split("_R_")[-1]
            sl.setAttr('side',2)
        else: 
            sl.setAttr('side',0)
        sl.setAttr('type', 18)
        sl.setAttr('otherType',shortNm.split(':')[-1],type='string')
    cmds.select( clear=True )

    lod_base_mesh_name = "copyModel:ch_head_facial_01"


    #Enter folder path below where additional scripts are stored. Do not change slash to forward slash
    #current folder path
    python_folder_path = "Z:/P4V/LLL/LllArt/Animation/Script/Asset/metahuman_rig_transfer"
    # example : DHIhead: if dnareader not import name space.
    name_space = "copyModel:"

    #Alright lets go

    cmds.duplicate('copyModel:root')

    def select_loop_bones():

        #giving OG and old mesh a variable name//edit mesh name here
        cmds.select(lod_base_mesh_name)
        ogmesh = cmds.ls( selection=True )

        cmds.select(enter_wrapped_mesh_name)
        newmesh = cmds.ls( selection=True )

        #selecting the bone//edit the bone name here
        cmds.select('FACIAL_C_FacialRoot', hierarchy=True)
        bone_List = cmds.ls( selection=True )
        cmds.select( clear=True )

        #Starting bone loop
        boneID = 0
        while boneID < len(bone_List):
            bone = bone_List[boneID]
            if not bone == "FACIAL_C_FacialRoot":
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

    #positioning eye
    select_loop_bones()
    eye_l_list = ['FACIAL_L_EyelidUpperA' , 'FACIAL_L_Eye' , 'FACIAL_L_EyelidLowerA']
    eye_r_list = ['FACIAL_R_EyelidUpperA' , 'FACIAL_R_Eye' , 'FACIAL_R_EyelidLowerA']
    center = cmds.objectCenter(eye_l_mesh_name, gl = True)
    for i in eye_l_list:
        cmds.xform(i , t = center , ws=1)

    center = cmds.objectCenter(eye_r_mesh_name, gl = True)
    for i in eye_r_list:
        cmds.xform(i , t = center , ws=1)

    #facial skin copy
    cmds.select("root" , hi=1)
    bindJoint = cmds.ls(sl=1)
    cmds.select(cl=1)

    cmds.skinCluster(bindJoint, enter_wrapped_mesh_name, toSelectedBones=True)[0]
    cmds.select(cl=True)
    cmds.select(lod_base_mesh_name , enter_wrapped_mesh_name)
    cmds.copySkinWeights(noMirror=True,
                    surfaceAssociation='closestPoint',
                    influenceAssociation='label',
                    uv = ['map1' , 'map1'],
                    normalize=True)
                    
    #eye skinning
    cmds.skinCluster(['FACIAL_R_Eye'], eye_r_mesh_name, toSelectedBones=True)[0]  
    cmds.select(cl=True)
    cmds.skinCluster(['FACIAL_L_Eye'], eye_l_mesh_name, toSelectedBones=True)[0]                 
    cmds.select(cl=True)
    #eyeao skinning
    cmds.skinCluster(bindJoint, eyeao_mesh_name, toSelectedBones=True)[0]
    cmds.select(cl=True)
    cmds.select(enter_wrapped_mesh_name , eyeao_mesh_name)
    cmds.copySkinWeights(noMirror=True,
                    surfaceAssociation='closestPoint',
                    influenceAssociation='label',
                    normalize=True)
                    
    cmds.select(eyeao_mesh_name+".vtx[23]")
    cmds.select(eyeao_mesh_name+".vtx[0:1]" ,eyeao_mesh_name+".vtx[7]" ,eyeao_mesh_name+".vtx[9]",eyeao_mesh_name+".vtx[12]" , eyeao_mesh_name+".vtx[15]" , eyeao_mesh_name+".vtx[19]" ,eyeao_mesh_name+".vtx[21]" ,eyeao_mesh_name+".vtx[23]" ,add=1    )
    mel.eval("WeightHammer;")
    mel.eval("weightHammerVerts;")

    cmds.select(eyeao_mesh_name+".vtx[47]")
    cmds.select(eyeao_mesh_name+".vtx[32:33]" ,eyeao_mesh_name+".vtx[39]" ,eyeao_mesh_name+".vtx[41]",eyeao_mesh_name+".vtx[44]" , eyeao_mesh_name+".vtx[47]" , eyeao_mesh_name+".vtx[51]" ,eyeao_mesh_name+".vtx[53]" ,eyeao_mesh_name+".vtx[55]" ,add=1    )
    mel.eval("WeightHammer;")
    mel.eval("weightHammerVerts;")

    #eyelash skinning
    cmds.skinCluster(bindJoint, eyelash_mesh_name, toSelectedBones=True)[0]
    cmds.select(cl=True)
    cmds.select(eyeao_mesh_name ,eyelash_mesh_name)
    cmds.copySkinWeights(noMirror=True,
                    surfaceAssociation='closestPoint',
                    influenceAssociation='label',
                    normalize=True)
                    
    #teeth skinning
    cmds.skinCluster(bindJoint, teeth_mesh_name, toSelectedBones=True)[0]
    cmds.select(cl=True)
    cmds.select("copyModel:sk_ch_nhm_facial_basefacial_teeth_lod1" , teeth_mesh_name)
    cmds.copySkinWeights(noMirror=True,
                    surfaceAssociation='closestPoint',
                    influenceAssociation='label',
                    uv = ['map1' , 'map1'],
                    normalize=True)


    reference_node = "copyModelRN"
    cmds.file(unloadReference=reference_node)
