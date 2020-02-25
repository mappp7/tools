#encoding:utf-8
#==============================
#
#
#==============================

import maya.cmds as cmds
import maya.mel as mel
from util.defaultGroupNode import*
from util.setUniqueName import*
from util.homeNul import*
from util.attach import*
from util.spaceBlend import*
from util.setPublishPose import*

from manual.biped.setSpine import *
from manual.biped.setShoulder import *
from manual.biped.setArm import *
from manual.biped.setFinger import *
from manual.biped.setNeck import *
from manual.biped.setLeg import *
from manual.biped.setSkinJoint import *


class bipedRig():

    def __init__(self):

        z=defaultGroupNode()
        z.createGroupNode()

        return


    def build(self):
        #spine
        spine=setSpine()
        IKSpineCon= spine.setIK('C_template_hip_JNT','C_template_spine1_JNT','C_template_spine2_JNT','C_template_spine3_JNT','C_template_chest_JNT')
        spine_joint= spine.setBlend('C_template_hip_JNT','C_template_spine1_JNT','C_template_spine2_JNT','C_template_spine3_JNT','C_template_chest_JNT')

        #shoulder
        Lshoulder=setShoulder()
        FKLshoulderCon= Lshoulder.setFK('L_template_shoulder_JNT')
        Left_shoulder_joint= Lshoulder.setBlend('L_template_shoulder_JNT')

        Rshoulder=setShoulder()
        FKRshoulderCon= Rshoulder.setFK('R_template_shoulder_JNT')
        Right_shoulder_joint= Rshoulder.setBlend('R_template_shoulder_JNT')

        #arm
        Larm=setArm()
        FKLarmCon= Larm.setFK('L_template_upArm_JNT','L_template_foreArm_JNT','L_template_hand_JNT')
        IKLarmCon= Larm.setIK('L_template_upArm_JNT','L_template_foreArm_JNT','L_template_hand_JNT')
        Larm.setBlend(Left_shoulder_joint[0],'L_template_upArm_JNT','L_template_foreArm_JNT','L_template_hand_JNT')


        Rarm=setArm()
        FKRarmCon= Rarm.setFK('R_template_upArm_JNT','R_template_foreArm_JNT','R_template_hand_JNT')
        FKRarmCon= Rarm.setIK('R_template_upArm_JNT','R_template_foreArm_JNT','R_template_hand_JNT')
        Rarm.setBlend(Right_shoulder_joint[0],'R_template_upArm_JNT','R_template_foreArm_JNT','R_template_hand_JNT')

        #finger
        Lfinger=setFinger()
        LthumbCon= Lfinger.setFK(['L_template_thumb1_JNT','L_template_thumb2_JNT','L_template_thumb3_JNT'])
        LindexCon= Lfinger.setFK(['L_template_indexPalm_JNT','L_template_index1_JNT','L_template_index2_JNT','L_template_index3_JNT'])
        LmiddleCon= Lfinger.setFK(['L_template_middlePalm_JNT','L_template_middle1_JNT','L_template_middle2_JNT','L_template_middle3_JNT'])
        LringCon= Lfinger.setFK(['L_template_ringPalm_JNT','L_template_ring1_JNT','L_template_ring2_JNT','L_template_ring3_JNT'])
        LlittleCon= Lfinger.setFK(['L_template_pinkyPalm_JNT','L_template_pinky1_JNT','L_template_pinky2_JNT','L_template_pinky3_JNT'])

        Lfinger.setBlend(['L_template_thumb1_JNT','L_template_thumb2_JNT','L_template_thumb3_JNT'])
        Lfinger.setBlend(['L_template_indexPalm_JNT','L_template_index1_JNT','L_template_index2_JNT','L_template_index3_JNT'])
        Lfinger.setBlend(['L_template_middlePalm_JNT','L_template_middle1_JNT','L_template_middle2_JNT','L_template_middle3_JNT'])
        Lfinger.setBlend(['L_template_ringPalm_JNT','L_template_ring1_JNT','L_template_ring2_JNT','L_template_ring3_JNT'])
        Lfinger.setBlend(['L_template_pinkyPalm_JNT','L_template_pinky1_JNT','L_template_pinky2_JNT','L_template_pinky3_JNT'])

        Rfinger=setFinger()
        RthumbCon= Rfinger.setFK(['R_template_thumb1_JNT','R_template_thumb2_JNT','R_template_thumb3_JNT'])
        RindexCon= Rfinger.setFK(['R_template_indexPalm_JNT','R_template_index1_JNT','R_template_index2_JNT','R_template_index3_JNT'])
        RmiddleCon= Rfinger.setFK(['R_template_middlePalm_JNT','R_template_middle1_JNT','R_template_middle2_JNT','R_template_middle3_JNT'])
        RringCon= Rfinger.setFK(['R_template_ringPalm_JNT','R_template_ring1_JNT','R_template_ring2_JNT','R_template_ring3_JNT'])
        RlittleCon= Rfinger.setFK(['R_template_pinkyPalm_JNT','R_template_pinky1_JNT','R_template_pinky2_JNT','R_template_pinky3_JNT'])

        Rfinger.setBlend(['R_template_thumb1_JNT','R_template_thumb2_JNT','R_template_thumb3_JNT'])
        Rfinger.setBlend(['R_template_indexPalm_JNT','R_template_index1_JNT','R_template_index2_JNT','R_template_index3_JNT'])
        Rfinger.setBlend(['R_template_middlePalm_JNT','R_template_middle1_JNT','R_template_middle2_JNT','R_template_middle3_JNT'])
        Rfinger.setBlend(['R_template_ringPalm_JNT','R_template_ring1_JNT','R_template_ring2_JNT','R_template_ring3_JNT'])
        Rfinger.setBlend(['R_template_pinkyPalm_JNT','R_template_pinky1_JNT','R_template_pinky2_JNT','R_template_pinky3_JNT'])

        #neck
        neck=setNeck()
        IkneckCon= neck.setIK('C_template_neck_JNT','C_template_head_JNT')
        neck.setBlend(spine_joint[-1],'C_template_neck_JNT','C_template_head_JNT')

        #leg
        Lleg=setLeg()
        LFKlegCon= Lleg.setFK('L_template_leg_JNT','L_template_lowLeg_JNT','L_template_foot_JNT','L_template_ball_JNT')
        LIKlegCon= Lleg.setIK('L_template_leg_JNT','L_template_lowLeg_JNT','L_template_foot_JNT','L_template_ball_JNT')
        Lleg.setBlend(spine_joint[0],'L_template_leg_JNT','L_template_lowLeg_JNT','L_template_foot_JNT','L_template_ball_JNT')

        Rleg=setLeg()
        RFKlegCon= Rleg.setFK('R_template_leg_JNT','R_template_lowLeg_JNT','R_template_foot_JNT','R_template_ball_JNT')
        RIKlegCon= Rleg.setIK('R_template_leg_JNT','R_template_lowLeg_JNT','R_template_foot_JNT','R_template_ball_JNT')
        Rleg.setBlend(spine_joint[0],'R_template_leg_JNT','R_template_lowLeg_JNT','R_template_foot_JNT','R_template_ball_JNT')


        #attach transform_GRP & root_NUL
        attachNode( 'move_CON', 'transform_GRP', 'translate', 'rotate','shear')
        cmds.connectAttr( 'place_CON.globalScale', 'transform_GRP.scaleX' )
        cmds.connectAttr( 'place_CON.globalScale', 'transform_GRP.scaleY' )
        cmds.connectAttr( 'place_CON.globalScale', 'transform_GRP.scaleZ' )

        #attach spine
        tmp=attachPart2( 'root_CON', 'C_IK_lowBody_NUL', 'translate','rotate','scale','shear')
        cmds.parent(tmp,'attach_GRP')
        tmp=attachPart2( 'root_CON', 'C_IK_upBodyRot1_NUL', 'translate','rotate','scale','shear')
        cmds.parent(tmp,'attach_GRP')
        tmp=attachPart2( 'C_IK_upBodyRot2_CON', 'C_IK_upBody_NUL', 'translate','rotate','scale','shear')
        cmds.parent(tmp,'attach_GRP')

        #attach shoulder
        tmp=attachPart2( 'C_Blend_chest_JNT', 'L_FK_shoulder_NUL', 'translate','rotate','scale','shear')
        cmds.parent(tmp,'attach_GRP')
        tmp=attachPart2( 'C_Blend_chest_JNT', 'R_FK_shoulder_NUL', 'translate','rotate','scale','shear')
        cmds.parent(tmp,'attach_GRP')

        #attach arm
        tmp=attachPart2( 'L_Blend_shoulder_JNT', 'L_FK_upArm_NUL', 'translate','rotate','scale','shear')
        cmds.parent(tmp,'attach_GRP')
        tmp=attachPart2( 'L_Blend_shoulder_JNT', 'L_armBlend_NUL', 'translate','rotate','scale','shear')
        cmds.parent(tmp,'attach_GRP')
        tmp=attachPart2( 'L_Blend_shoulder_JNT', 'L_IK_upArm_JNT', 'translate')
        cmds.parent(tmp,'attach_GRP')
        tmp=attachPart2( 'R_Blend_shoulder_JNT', 'R_FK_upArm_NUL', 'translate','rotate','scale','shear')
        cmds.parent(tmp,'attach_GRP')
        tmp=attachPart2( 'R_Blend_shoulder_JNT', 'R_armBlend_NUL', 'translate','rotate','scale','shear')
        cmds.parent(tmp,'attach_GRP')
        tmp=attachPart2( 'R_Blend_shoulder_JNT', 'R_IK_upArm_JNT', 'translate')
        cmds.parent(tmp,'attach_GRP')

        #attach finger
        tmp=attachPart2( 'L_Blend_hand_JNT', 'L_FK_thumb1_NUL', 'translate','rotate','scale','shear')
        cmds.parent(tmp,'attach_GRP')
        tmp=attachPart2( 'L_Blend_hand_JNT', 'L_FK_indexPalm_NUL', 'translate','rotate','scale','shear')
        cmds.parent(tmp,'attach_GRP')
        tmp=attachPart2( 'L_Blend_hand_JNT', 'L_FK_middlePalm_NUL', 'translate','rotate','scale','shear')
        cmds.parent(tmp,'attach_GRP')
        tmp=attachPart2( 'L_Blend_hand_JNT', 'L_FK_ringPalm_NUL', 'translate','rotate','scale','shear')
        cmds.parent(tmp,'attach_GRP')
        tmp=attachPart2( 'L_Blend_hand_JNT', 'L_FK_pinkyPalm_NUL', 'translate','rotate','scale','shear')
        cmds.parent(tmp,'attach_GRP')

        tmp=attachPart2( 'R_Blend_hand_JNT', 'R_FK_thumb1_NUL', 'translate','rotate','scale','shear')
        cmds.parent(tmp,'attach_GRP')
        tmp=attachPart2( 'R_Blend_hand_JNT', 'R_FK_indexPalm_NUL', 'translate','rotate','scale','shear')
        cmds.parent(tmp,'attach_GRP')
        tmp=attachPart2( 'R_Blend_hand_JNT', 'R_FK_middlePalm_NUL', 'translate','rotate','scale','shear')
        cmds.parent(tmp,'attach_GRP')
        tmp=attachPart2( 'R_Blend_hand_JNT', 'R_FK_ringPalm_NUL', 'translate','rotate','scale','shear')
        cmds.parent(tmp,'attach_GRP')
        tmp=attachPart2( 'R_Blend_hand_JNT', 'R_FK_pinkyPalm_NUL', 'translate','rotate','scale','shear')
        cmds.parent(tmp,'attach_GRP')


        #attach neck
        tmp=attachPart2( 'C_Blend_chest_JNT', 'C_IK_neck_NUL', 'translate','rotate','scale','shear')
        cmds.parent(tmp,'attach_GRP')
        tmp=attachPart2( 'C_IK_neck_CON', 'C_IK_head_NUL', 'translate','rotate','scale','shear')
        cmds.parent(tmp,'attach_GRP')

        #attach leg
        tmp=attachPart2( 'C_Blend_hip_JNT', 'L_FK_leg_NUL', 'translate','rotate','scale','shear')
        cmds.parent(tmp,'attach_GRP')
        tmp=attachPart2( 'C_Blend_hip_JNT', 'L_IK_leg_JNT', 'translate')
        cmds.parent(tmp,'attach_GRP')
        tmp=attachPart2( 'C_Blend_hip_JNT', 'L_legBlend_NUL', 'translate','rotate','scale','shear')
        cmds.parent(tmp,'attach_GRP')

        tmp=attachPart2( 'C_Blend_hip_JNT', 'R_FK_leg_NUL', 'translate','rotate','scale','shear')
        cmds.parent(tmp,'attach_GRP')
        tmp=attachPart2( 'C_Blend_hip_JNT', 'R_IK_leg_JNT', 'translate')
        cmds.parent(tmp,'attach_GRP')
        tmp=attachPart2( 'C_Blend_hip_JNT', 'R_legBlend_NUL', 'translate','rotate','scale','shear')
        cmds.parent(tmp,'attach_GRP')

        #local/world space blend
        #arm
        sp=spaceBlend()
        sp.rotateBlend('L_FK_shoulder_CON','move_CON','L_FK_upArm_CON')
        sp.rotateBlend('R_FK_shoulder_CON','move_CON','R_FK_upArm_CON')

        #neck
        sp.rotateBlend('C_IK_neck_CON','move_CON','C_IK_head_CON')

        #wrist
        sp.rotateBlend('L_FK_foreArm_CON','root_CON','L_FK_hand_CON')
        sp.rotateBlend('R_FK_foreArm_CON','root_CON','R_FK_hand_CON')

        #ik hand / leg
        sp.parentBlend('C_IK_upBody_CON','move_CON','L_IK_hand_CON')
        sp.parentBlend('C_IK_upBody_CON','move_CON','R_IK_hand_CON')
        sp.parentBlend('L_IK_hand_CON','move_CON','L_IK_handVec_CON')
        sp.parentBlend('R_IK_hand_CON','move_CON','R_IK_handVec_CON')

        sp.parentBlend('root_CON','move_CON','L_IK_foot_CON')
        sp.parentBlend('root_CON','move_CON','R_IK_foot_CON')

        #skin joint
        s=setSkinJoint()
        skinJoints= s.set()

        cmds.setAttr ('templateJoint_GRP.v',0)
        """
        Attrs= cmds.getAttr ('rig_GRP.allControls')

        controls= Attrs+IKSpineCon+FKLshoulderCon+FKRshoulderCon+FKLarmCon+IKLarmCon+FKRarmCon+FKRarmCon+LthumbCon+LindexCon+LmiddleCon+LringCon+LlittleCon+RthumbCon+RindexCon+RmiddleCon+RringCon+RlittleCon+IkneckCon+LFKlegCon+LIKlegCon+RFKlegCon+RIKlegCon

        cmds.setAttr ('rig_GRP.allControls', type='stringArray', *([len(controls)] + controls))

        #publish pose
        con=['root_CON','C_IK_lowBody_CON','C_IK_upBodyRot1_CON','C_IK_upBodyRot2_CON',
            'C_IK_upBody_CON','C_IK_head_CON','C_IK_hip_CON',
            'L_IK_foot_CON','L_IK_footVec_CON',
            'R_IK_foot_CON','R_IK_footVec_CON',
            'L_FK_leg_CON','L_FK_lowLeg_CON','L_FK_foot_CON',
            'R_FK_leg_CON','R_FK_lowLeg_CON','R_FK_foot_CON',
            'L_FK_upArm_CON','L_FK_foreArm_CON','L_FK_hand_CON',
            'R_FK_upArm_CON','R_FK_foreArm_CON','R_FK_hand_CON',
            'L_IK_hand_CON','L_IK_handSub_CON','L_IK_handVec_CON',
            'R_IK_hand_CON','R_IK_handSub_CON','R_IK_handVec_CON',
            'L_FK_thumb1_CON','L_FK_thumb2_CON','L_FK_thumb3_CON',
            'R_FK_thumb1_CON','R_FK_thumb2_CON','R_FK_thumb3_CON',

            'L_FK_index1_CON','L_FK_index2_CON','L_FK_index3_CON',
            'R_FK_index1_CON','R_FK_index2_CON','R_FK_index3_CON',

            'L_FK_middle1_CON','L_FK_middle2_CON','L_FK_middle3_CON',
            'R_FK_middle1_CON','R_FK_middle2_CON','R_FK_middle3_CON',

            'L_FK_ring1_CON','L_FK_ring2_CON','L_FK_ring3_CON',
            'R_FK_ring1_CON','R_FK_ring2_CON','R_FK_ring3_CON',

            'L_FK_pinky1_CON','L_FK_pinky2_CON','L_FK_pinky3_CON',
            'R_FK_pinky1_CON','R_FK_pinky2_CON','R_FK_pinky3_CON',
            ]

        for e in con:
            setPublishPose('rig_GRP',e)
        """

        #Set Controller Color
        Color = { 'red':13, 'blue':6, 'yellow':17 , 'peach':20 }

        cmds.select( 'L_*_*_CON' )
        leftController = cmds.ls( sl=True )
        cmds.select( cl=True )
        cmds.select( 'R_*_*_CON' )
        rightController = cmds.ls( sl=True )
        cmds.select( cl=True )

        cmds.select( '*_*Blend_CON' )
        blendController = cmds.ls( sl=True )
        cmds.select( cl=True )

        for x in range(len(blendController)):
            cmds.setAttr('%s.overrideEnabled' % blendController[x], 1)
            cmds.setAttr('%s.overrideColor' % blendController[x], Color['peach'])

        for x in range(len(leftController)):
            cmds.setAttr('%s.overrideEnabled' % leftController[x], 1)
            cmds.setAttr('%s.overrideColor' % leftController[x], Color['blue'])

            cmds.setAttr('%s.overrideEnabled' % rightController[x], 1)
            cmds.setAttr('%s.overrideColor' % rightController[x], Color['red'])

        # Lock And Hide Attr
        worldController_list = [u'root_CON', u'move_CON', u'direction_CON', u'place_CON']

        fkController_list = [u'L_FK_ball_CON', u'L_FK_foot_CON', u'L_FK_foreArm_CON', u'L_FK_hand_CON', u'L_FK_index1_CON',
                             u'L_FK_index2_CON', u'L_FK_index3_CON', u'L_FK_indexPalm_CON', u'L_FK_leg_CON', u'L_FK_lowLeg_CON',
                             u'L_FK_middle1_CON', u'L_FK_middle2_CON', u'L_FK_middle3_CON', u'L_FK_middlePalm_CON', u'L_FK_pinky1_CON',
                             u'L_FK_pinky2_CON', u'L_FK_pinky3_CON', u'L_FK_pinkyPalm_CON', u'L_FK_ring1_CON', u'L_FK_ring2_CON',
                             u'L_FK_ring3_CON', u'L_FK_ringPalm_CON', u'L_FK_shoulder_CON', u'L_FK_thumb1_CON', u'L_FK_thumb2_CON',
                             u'L_FK_thumb3_CON', u'L_FK_upArm_CON', u'R_FK_ball_CON', u'R_FK_foot_CON', u'R_FK_foreArm_CON',
                             u'R_FK_hand_CON', u'R_FK_index1_CON', u'R_FK_index2_CON', u'R_FK_index3_CON', u'R_FK_indexPalm_CON',
                             u'R_FK_leg_CON', u'R_FK_lowLeg_CON', u'R_FK_middle1_CON', u'R_FK_middle2_CON', u'R_FK_middle3_CON',
                             u'R_FK_middlePalm_CON', u'R_FK_pinky1_CON', u'R_FK_pinky2_CON', u'R_FK_pinky3_CON', u'R_FK_pinkyPalm_CON',
                             u'R_FK_ring1_CON', u'R_FK_ring2_CON', u'R_FK_ring3_CON', u'R_FK_ringPalm_CON', u'R_FK_shoulder_CON',
                             u'R_FK_thumb1_CON', u'R_FK_thumb2_CON', u'R_FK_thumb3_CON', u'R_FK_upArm_CON']

        ikController_list = [u'C_IK_head_CON', u'C_IK_hip_CON', u'C_IK_lowBody_CON', u'C_IK_neck_CON', u'C_IK_upBodyRot1_CON',
                             u'C_IK_upBodyRot2_CON', u'C_IK_upBody_CON', u'L_IK_ballRollUp_CON', u'L_IK_ball_CON', u'L_IK_footRollUp_CON',
                             u'L_IK_footSub_CON', u'L_IK_footVec_CON', u'L_IK_foot_CON', u'L_IK_handSub_CON', u'L_IK_handVec_CON',
                             u'L_IK_hand_CON', u'R_IK_ballRollUp_CON', u'R_IK_ball_CON', u'R_IK_footRollUp_CON', u'R_IK_footSub_CON',
                             u'R_IK_footVec_CON', u'R_IK_foot_CON', u'R_IK_handSub_CON', u'R_IK_handVec_CON', u'R_IK_hand_CON']

        blendController_list = [u'L_armBlend_CON', u'L_legBlend_CON', u'R_armBlend_CON', u'R_legBlend_CON']

        scaleVisibilityLock_list = worldController_list + fkController_list + ikController_list + blendController_list

        r_lock_List = ['L_IK_handVec_CON', 'R_IK_handVec_CON', 'L_IK_footVec_CON', 'R_IK_footVec_CON']

        t_r_lock_List = ['L_armBlend_CON', 'L_legBlend_CON', 'R_armBlend_CON', 'R_legBlend_CON']

        for x in range( len(scaleVisibilityLock_list) ):
            cmds.setAttr( '%s.sx' % scaleVisibilityLock_list[x], lock=True, keyable=False )
            cmds.setAttr( '%s.sy' % scaleVisibilityLock_list[x], lock=True, keyable=False )
            cmds.setAttr( '%s.sz' % scaleVisibilityLock_list[x], lock=True, keyable=False )

            cmds.setAttr( '%s.v' % scaleVisibilityLock_list[x], lock=True, keyable=False )

        for x in range( len(r_lock_List) ):
            cmds.setAttr( '%s.rx' % r_lock_List[x], lock=True, keyable=False )
            cmds.setAttr( '%s.ry' % r_lock_List[x], lock=True, keyable=False )
            cmds.setAttr( '%s.rz' % r_lock_List[x], lock=True, keyable=False )

        for x in range( len(t_r_lock_List) ):
            cmds.setAttr( '%s.tx' % t_r_lock_List[x], lock=True, keyable=False )
            cmds.setAttr( '%s.ty' % t_r_lock_List[x], lock=True, keyable=False )
            cmds.setAttr( '%s.tz' % t_r_lock_List[x], lock=True, keyable=False )

            cmds.setAttr( '%s.rx' % t_r_lock_List[x], lock=True, keyable=False )
            cmds.setAttr( '%s.ry' % t_r_lock_List[x], lock=True, keyable=False )
            cmds.setAttr( '%s.rz' % t_r_lock_List[x], lock=True, keyable=False )

        return
