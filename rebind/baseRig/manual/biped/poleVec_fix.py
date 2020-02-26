import maya.cmds as cmds
import maya.OpenMaya as om

def calculatePosition(objList):
    for i in range(2):
        # calculate polevector position 
        low_Raw = cmds.xform(objList[2], ws=True, q=True, t=True)
        low_Pos = om.MVector(low_Raw[0], low_Raw[1],low_Raw[2])
        mid_Raw = cmds.xform(objList[1], ws=True, q=True, t=True)
        mid_Pos = om.MVector(mid_Raw[0], mid_Raw[1],mid_Raw[2])
        high_Raw = cmds.xform(objList[0], ws=True, q=True, t=True)
        high_Pos = om.MVector(high_Raw[0], high_Raw[1],high_Raw[2])
        midpoint = (low_Pos + high_Pos) / 2
        pvOrigin = mid_Pos - midpoint
        pvRaw = pvOrigin * 2
        pvPos = pvRaw + midpoint
        cmds.move(pvPos.x, pvPos.y, pvPos.z, objList[3][i])
        
def cp_cmd(side):
    # variation
    L_armJoint_list = ['L_Skin_upArm_JNT','L_Skin_foreArm_JNT','L_Skin_hand_JNT',['L_IK_handSpace_LOC', 'moveSpace7_LOC']]
    L_footJoint_list = ['L_Skin_leg_JNT','L_Skin_lowLeg_JNT','L_Skin_foot_JNT',['L_IK_footVecOffsetSpace_LOC', 'moveSpace_LOC']]
    R_armJoint_list = ['R_Skin_upArm_JNT','R_Skin_foreArm_JNT','R_Skin_hand_JNT',['R_IK_handSpace_LOC', 'moveSpace8_LOC']]
    R_footJoint_list = ['R_Skin_leg_JNT','R_Skin_lowLeg_JNT','R_Skin_foot_JNT',['R_IK_footVecOffsetSpace_LOC', 'moveSpace1_LOC']]    
    if side is not 'L':
        calculatePosition(R_armJoint_list)
        calculatePosition(R_footJoint_list)
    else:
        calculatePosition(L_armJoint_list)
        calculatePosition(L_footJoint_list)
    #x = [i.replace('L_','R_') for i in list]





