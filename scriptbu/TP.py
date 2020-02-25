neckPC = { 'PL' : [ 'C_IK_head_JNT', 'C_IK_neck1_JNT', 'C_IK_neck3_JNT', 'C_IK_neck5_JNT' ], 'CL' : [ 'C_FK_head_NUL', 'C_FK_neck1_NUL', 'C_FK_neck2_NUL', 'C_FK_neck3_NUL' ] }

neckP = { 'PL' : [ 'C_FK_head_NUL', 'C_FK_neck3_NUL', 'C_FK_neck2_NUL' ], 'CL' : [ 'C_FK_neck3_NUL', 'C_FK_neck2_NUL', 'C_FK_neck1_NUL' ] }

AA = { 'PL' : [ 'C_IK_head_CON', 'C_IK_neck1_CON', 'C_IK_upBody_CON', 'C_IK_lowBody_CON', 'L_IK_foreLeg_CON', 'R_IK_foreLeg_CON', 'L_IK_hindLeg_CON', 'R_IK_hindLeg_CON' ], 'CL' : [ 'C_IK_headSub_CONShape', 'C_IK_neck1Sub_CONShape', 'C_IK_upBodySub_CONShape', 'C_IK_lowBodySub_CONShape', 'L_foreLeg_inSideRoll_NUL', 'R_foreLeg_inSideRoll_NUL', 'L_hindLeg_inSideRoll_NUL', 'R_hindLeg_inSideRoll_NUL' ] }

conVis = { 'key' : [ [ 'neck_switch', 'C_IK_neck1_CON' ], [ 'spine_switch', 'C_IK_root_CON' ] ], 'attr' : [ 'IK_con_vis', 'FK_con_vis' ], 'vis' : [ [ [ 'C_IK_neckMiddle_CON' ], [ 'C_FK_neck3_NUL_CON', 'C_FK_neck2_NUL_CON' ] ], [ [ 'C_IK_spineMiddle_CON' ], [ 'C_FKsub_spine2_NUL_CON', 'C_FKsub_spine3_NUL_CON' ] ] ] }


attach_list = [ 'C_IK_spine1_NULAttach_NUL', 'C_IK_spine2_NULAttach_NUL', 'C_IK_spine3_NULAttach_NUL', 'C_IK_spine4_NULAttach_NUL', 'C_IK_spine5_NULAttach_NUL', 'C_IK_neck_CRV1_NULAttach_NUL', 'C_IK_neck_CRV2_NULAttach_NUL', 'C_IK_neck_CRV3_NULAttach_NUL', 'C_IK_neck_CRV4_NULAttach_NUL', 'C_IK_neck_CRV5_NULAttach_NUL' ]

noneTrans_list = [ 'C_IK_spine1_stCRV1_LOC', 'C_IK_spine1_stCRV2_LOC', 'C_IK_spine1_stCRV3_LOC', 'C_IK_spine1_stCRV4_LOC', 'C_IK_spine1_stCRV5_LOC', 'C_IK_spine1_stCRV6_LOC', 'C_IK_spine1_stCRV7_LOC', 'C_IK_neck_stCRV1_LOC', 'C_IK_neck_stCRV2_LOC', 'C_IK_neck_stCRV3_LOC', 'C_IK_neck_stCRV4_LOC', 'C_IK_neck_stCRV5_LOC', 'C_IK_neck_stCRV6_LOC', 'C_IK_neck_stCRV7_LOC', 'C_IK_neck_CRV1_NUL', 'C_IK_neck_CRV2_NUL', 'C_IK_neck_CRV3_NUL', 'C_IK_neck_CRV4_NUL', 'C_IK_neck_CRV5_NUL' ]

auxillary_list = [ 'C_IK_neck_HDL', 'C_IK_neck_CRV', 'C_IK_spine1_HDL', 'C_IK_spine1_CRV', 'tail_curve', 'tail_HDL' ]

neck_list = [ 'C_IK_head_NUL', 'C_IK_neck1_NUL', 'C_IK_neckMiddle_NUL', 'C_IK_neck1_JNT', 'C_FK_neck1_NUL', 'C_FK_neck2_NUL_NUL', 'C_FK_neck2_NULAttach_NUL' ]

spine_list = [ 'C_IK_spineMiddle_NUL', 'C_IK_root_JNT', 'C_IK_root_NUL', 'C_IK_lowBody_NUL', 'C_IK_upBody_NUL', 'C_IK_spine1_NUL', 'C_IK_spine2_NUL', 'C_IK_spine3_NUL', 'C_IK_spine4_NUL', 'C_IK_spine5_NUL', 'C_IK_lowBody_NULAttach_NUL', 'C_IK_upBody_NULAttach_NUL', 'C_FKsub_spine1_NUL', 'C_FKsub_spine2_NUL_NUL', 'C_FKsub_spine2_NUL_NULAttach_NUL' ]

L_foreLeg_list = [ 'L_IK_clavicle_JNT', 'L_subIk_clavicle_JNT', 'L_wistRoll_NUL', 'L_IK_edbow_NUL', 'L_IK_clavicle_world_NUL', 'L_subIk_shoulder_PV_NUL', 'L_IK_foreLeg_NUL' ]
R_foreLeg_list = [ 'R_IK_clavicle_JNT', 'R_subIk_clavicle_JNT', 'R_wistRoll_NUL', 'R_IK_edbow_NUL', 'R_IK_clavicle_world_NUL', 'R_subIk_shoulder_PV_NUL', 'R_IK_foreLeg_NUL' ]

L_hindLeg_list = [ 'L_IK_hip_JNT', 'L_rig_hip_JNT', 'L_IK_hindLeg_NUL', 'L_IK_hip_NUL', 'L_IK_knee_NUL', 'L_ankleRoll_NUL' ]
R_hindLeg_list = [ 'R_IK_hip_JNT', 'R_rig_hip_JNT', 'R_IK_hindLeg_NUL', 'R_IK_hip_NUL', 'R_IK_knee_NUL', 'R_ankleRoll_NUL' ]

tail_list = [ 'tail1_NUL', 'tail_curve_locator_GRP', 'C_IK_tail1_JNT', 'C_rig_tail1_JNT' ]

delete_list = [ 'L_foreLeg_ballRollTemple', 'L_foreLeg_toeTabTemple', 'L_hindLeg_toeTabTemple', 'R_hindLeg_toeTabTemple' ]

rotate_con_list_A = [ 'C_IK_neckMiddle_CON', 'C_FK_neck3_NUL_CON', 'C_FK_neck2_NUL_CON', 'C_IK_spineMiddle_CON', 'C_FKsub_spine3_NUL_CON', 'C_FKsub_spine2_NUL_CON', 'C_IK_root_CON' ]
rotate_con_list_B = [ 'neck_switch_CON', 'spine_switch_CON' ]


part_connect = { 'PL' : [ 'C_Skin_root_JNT', 'C_Skin_chest_JNT', ], 'CL' : [ [ 'L_IK_hip_NUL', 'R_IK_hip_NUL' ], [ 'L_IK_clavicle_world_NUL', 'R_IK_clavicle_world_NUL', 'C_IK_neck1_NUL', 'L_subIk_shoulder_PV_LOC', 'R_subIk_shoulder_PV_LOC' ] ] }


hide_list = [ 'C_IK_head_aTwist_LOC', 'C_FK_neck2_NULAttach_LOC', 'C_IK_spine4_LOC', 'C_IK_upBody_aTwist_LOC', 'C_IK_spine5_LOC', 'C_IK_upBody_NULAttach_LOC', 'C_IK_spine3_LOC', 'C_IK_spine2_LOC', 'C_FKsub_spine2_NUL_NULAttach_LOC', 'C_IK_lowBody_aTwist_LOC', 'C_IK_spine1_LOC', 'C_IK_lowBody_NULAttach_LOC', 'L_subIk_shoulder_PV_LOC', 'R_subIk_shoulder_PV_LOC', 'L_wistRoll_PV_LOC', 'R_wistRoll_PV_LOC', 'R_IK_hip_RP_HDL', 'L_IK_hip_RP_HDL', 'R_IK_ankle_SC_HDL', 'L_IK_ankle_SC_HDL', 'R_IK_shoulder_RP_HDL', 'L_IK_shoulder_RP_HDL', 'C_IK_neck1_aTwist_LOC', 'neck_up_LOC' ]
hide_list2 = [ 'L_subIk_shoulder_RP_HDL', 'L_IK_wrist_RP_HDL', 'L_IK_foot1_SC_HDL', 'L_IK_foot2_SC_HDL', 'R_subIk_shoulder_RP_HDL', 'R_IK_wrist_RP_HDL', 'R_IK_foot1_SC_HDL', 'R_IK_foot2_SC_HDL', 'L_rig_hip_JNT', 'R_rig_hip_JNT', 'tail*_up_LOC' ]


R_con_list = [ 'R_foreLeg_toeTab_CON', 'R_foreLeg_ballRoll_CON', 'R_foreLeg_footTwist_CON', 'R_foreLeg_toeRoll_CON', 'R_foreLeg_heelRoll_CON', 'R_foreLeg_outSideRoll_CON', 'R_foreLeg_inSideRoll_CON', 'R_IK_foreLeg_CON', 'R_wistRoll_CON', 'R_IK_edbow_CON', 'R_IK_clavicle_CON', 'R_IK_clavicle_world_CON', 'R_IK_hip_CON', 'R_hindLeg_toeTab_CON', 'R_hindLeg_ballRoll_CON', 'R_hindLeg_footTwist_CON', 'R_hindLeg_toeRoll_CON', 'R_hindLeg_heelRoll_CON', 'R_hindLeg_outSideRoll_CON', 'R_hindLeg_inSideRoll_CON', 'R_IK_hindLeg_CON', 'R_IK_knee_CON' ] 

switch_con_list = [ 'neck_switch_CON', 'spine_switch_CON' ]

scale_con_list = [ 'C_IK_upBody_CON', 'C_IK_lowBody_CON', 'C_IK_hip_CON', 'C_IK_neck1_CON', 'C_IK_head_CON', 'C_IK_root_CON', 'R_IK_clavicle_world_CON', 'L_IK_clavicle_world_CON', 'L_IK_hip_CON', 'R_IK_hip_CON', 'C_IK_spineMiddle_CON', 'C_IK_neckMiddle_CON', 'L_IK_foreLeg_CON', 'R_IK_foreLeg_CON', 'L_IK_hindLeg_CON', 'R_IK_hindLeg_CON', 'L_IK_edbow_CON', 'R_IK_edbow_CON', 'L_IK_knee_CON', 'R_IK_knee_CON' ]


parent_list = { 'PL' : [ 'C_IK_hip_CON', 'C_IK_upBody_CON' ], 'CL' : [ [ 'L_IK_hip_NUL', 'R_IK_hip_NUL', 'tail1_NUL', 'C_IK_tail1_JNT' ], [ 'L_IK_clavicle_world_NUL', 'R_IK_clavicle_world_NUL', 'C_IK_neck1_NUL' ] ] }

targetjointList = [ 'L_rig_hip_JNT', 'L_rig_knee_JNT', 'L_rig_ankle_JNT', 'L_rig_ball_JNT', 'R_rig_hip_JNT', 'R_rig_knee_JNT', 'R_rig_ankle_JNT', 'R_rig_ball_JNT' ]
