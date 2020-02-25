import maya.cmds as cmds
list = cmds.ls(sl=1)

A= [u'C_Skin_hip_JNT',
 u'C_Skin_spine1_JNT',
 u'C_Skin_spine2_JNT',
 u'C_Skin_spine3_JNT',
 u'C_Skin_chest_JNT',
 u'R_Skin_shoulder_JNT',
 u'R_Skin_upArm_JNT',
 u'R_Skin_upArmTwist_JNT',
 u'R_Skin_upArmTwist1_JNT',
 u'R_Skin_upArmTwist2_JNT',
 u'R_Skin_upArmTwist3_JNT',
 u'R_Skin_upArmTwist4_JNT',
 u'R_Skin_foreArm_JNT',
 u'R_Skin_foreArmTwist_JNT',
 u'R_Skin_foreArmTwist1_JNT',
 u'R_Skin_foreArmTwist2_JNT',
 u'R_Skin_foreArmTwist3_JNT',
 u'R_Skin_foreArmTwist4_JNT',
 u'R_Skin_hand_JNT']

for i in list:
    if len(i.split('|')) > 0:
        a= i.split('|')[-1]
        A.append(a)

for x in range(len(A)):
    if x > 0:
        y= x+1
        cmds.parent(A[y],A[X])
        


