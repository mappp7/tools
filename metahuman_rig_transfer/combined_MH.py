from maya import cmds
import maya.api.OpenMaya as om
import os 

#Enter Wrapped Head Mesh Name below
enter_wrapped_mesh_name = "NewHead"
lod_base_mesh_name = "head_lod4_mesh"
#Enter folder path below where additional scripts are stored. Do not change slash to forward slash
#current folder path
python_folder_path = "C:/Users/o9o9/Documents/maya/2022/scripts/metahuman_rig_transfer"
# example : DHIhead: if dnareader not import name space.
name_space = "DHIhead:"

#Alright lets go

cmds.select( clear=True )
cmds.duplicate(name_space + 'spine_04')

def select_loop_bones():
    from maya import cmds
    import maya.api.OpenMaya as om
    import os 


    #giving OG and old mesh a variable name//edit mesh name here
    cmds.select(lod_base_mesh_name)
    ogmesh = cmds.ls( selection=True )

    cmds.select(enter_wrapped_mesh_name)
    newmesh = cmds.ls( selection=True )

    #selecting the bone//edit the bone name here
    cmds.select('spine_05', hierarchy=True)
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

def move_constraint():
    #move neck_01 parent bone
    cmds.select(name_space +'neck_01')
    neck_01DHIB = cmds.ls( selection=True )
    cmds.select('neck_01')
    neck_01B = cmds.ls( selection=True )

    neck_01B_XF = cmds.xform(neck_01B,q=1,ws=1,t=1)
    cmds.move( neck_01B_XF[0], neck_01B_XF[1], neck_01B_XF[2], neck_01DHIB, absolute=True, ws=True )

    #move FACIAL_C_Neck1Root parent bone
    cmds.select(name_space +'FACIAL_C_Neck1Root')
    FACIAL_C_Neck1RootDHIB = cmds.ls( selection=True )
    cmds.select('FACIAL_C_Neck1Root')
    FACIAL_C_Neck1RootB = cmds.ls( selection=True )

    FACIAL_C_Neck1RootB_XF = cmds.xform(FACIAL_C_Neck1RootB,q=1,ws=1,t=1)
    cmds.move( FACIAL_C_Neck1RootB_XF[0], FACIAL_C_Neck1RootB_XF[1], FACIAL_C_Neck1RootB_XF[2], FACIAL_C_Neck1RootDHIB, absolute=True, ws=True )

    #move neck_02 parent bone
    cmds.select(name_space +'neck_02')
    neck_02DHIB = cmds.ls( selection=True )
    cmds.select('neck_02')
    neck_02B = cmds.ls( selection=True )

    neck_02B_XF = cmds.xform(neck_02B,q=1,ws=1,t=1)
    cmds.move( neck_02B_XF[0], neck_02B_XF[1], neck_02B_XF[2], neck_02DHIB, absolute=True, ws=True )

    #move FACIAL_C_Neck2Root parent bone
    cmds.select(name_space +'FACIAL_C_Neck2Root')
    FACIAL_C_Neck2RootDHIB = cmds.ls( selection=True )
    cmds.select('FACIAL_C_Neck2Root')
    FACIAL_C_Neck2RootB = cmds.ls( selection=True )

    FACIAL_C_Neck2RootB_XF = cmds.xform(FACIAL_C_Neck2RootB,q=1,ws=1,t=1)
    cmds.move( FACIAL_C_Neck2RootB_XF[0], FACIAL_C_Neck2RootB_XF[1], FACIAL_C_Neck2RootB_XF[2], FACIAL_C_Neck2RootDHIB, absolute=True, ws=True )


    #move head parent bone
    cmds.select(name_space +'head')
    headDHIB = cmds.ls( selection=True )
    cmds.select('head')
    headB = cmds.ls( selection=True )

    headB_XF = cmds.xform(headB,q=1,ws=1,t=1)
    cmds.move( headB_XF[0], headB_XF[1], headB_XF[2], headDHIB, absolute=True, ws=True )

    #move FACIAL_C_FacialRoot parent bone
    cmds.select(name_space +'FACIAL_C_FacialRoot')
    FACIAL_C_FacialRootDHIB = cmds.ls( selection=True )
    cmds.select('FACIAL_C_FacialRoot')
    FACIAL_C_FacialRootB = cmds.ls( selection=True )

    FACIAL_C_FacialRootB_XF = cmds.xform(FACIAL_C_FacialRootB,q=1,ws=1,t=1)
    cmds.move( FACIAL_C_FacialRootB_XF[0], FACIAL_C_FacialRootB_XF[1], FACIAL_C_FacialRootB_XF[2], FACIAL_C_FacialRootDHIB, absolute=True, ws=True )

move_constraint()
cmds.select( clear=True )
