import maya.cmds as cmds
from manual.biped.nodePVpos import *
from manual.biped.addMatchInfo import *

def addRigCommand():
	# add rig
	cmds.parentConstraint( 'L_FK_upArm_CON', 'L_IK_upArmAttach_LOC' )
	cmds.parentConstraint( 'R_FK_upArm_CON', 'R_IK_upArmAttach_LOC' )
	     
	LH = nodePVconnect( ['L_FK_upArm_JNT', 'L_FK_foreArm_JNT', 'L_FK_hand_JNT'] )
	RH = nodePVconnect( ['R_FK_upArm_JNT', 'R_FK_foreArm_JNT', 'R_FK_hand_JNT'] )

	cmds.setAttr( '%s.translateX' % LH, 0 )
	cmds.setAttr( '%s.translateY' % LH, 0 )
	cmds.setAttr( '%s.translateZ' % LH, 0 )

	cmds.setAttr( '%s.translateX' % RH, 0 )
	cmds.setAttr( '%s.translateY' % RH, 0 )
	cmds.setAttr( '%s.translateZ' % RH, 0 )

	cmds.select( cl=True )

	MLG = cmds.group( em=True, n='match_locator_GRP' )
	cmds.parent( LH, RH, MLG )
	cmds.parent( MLG, 'auxillary_GRP' )

	cmds.setAttr( 'match_locator_GRP.visibility', 0 )

	# fk to ik macth asddInfo
	addMatchInfo( 'L_FK_upArm_CON', 'L_IK_upArm_JNT' )
	addMatchInfo( 'L_FK_foreArm_CON', 'L_IK_foreArm_JNT' )
	addMatchInfo( 'L_FK_hand_CON', 'L_IK_hand_JNT' )

	addMatchInfo( 'R_FK_upArm_CON', 'R_IK_upArm_JNT' )
	addMatchInfo( 'R_FK_foreArm_CON', 'R_IK_foreArm_JNT' )
	addMatchInfo( 'R_FK_hand_CON', 'R_IK_hand_JNT' )

	# ik to fk macth asddInfo
	addMatchInfo( 'L_IK_hand_CON', 'L_FK_hand_JNT' )
	addMatchInfo( 'L_IK_handVec_CON', 'L_FK_foreArm_pv_LOC' )

	addMatchInfo( 'R_IK_hand_CON', 'R_FK_hand_JNT' )
	addMatchInfo( 'R_IK_handVec_CON', 'R_FK_foreArm_pv_LOC' )
