import maya.cmds as cmds

def addLocalSpacetoHandSub(side):

    # set variation
    hand_CON_side = '%s_IK_hand_CON' %side
    handSub_CON_side = '%s_IK_handSub_CON' %side
    handSub_NUL_side = '%s_IK_handSub_local_NUL' %side
    handSub_NUL2_side = '%s_IK_handSub_NUL' %side
    handSubAttatch_local_NUL = '%s_IK_handSubAttatch_local_NUL' %side
    handSubAttatch_local_LOC = '%s_IK_handSubAttatch_local_LOC' %side

    cmds.select(handSub_CON_side,r=1)
    cmds.addAttr(ln='localSpace',at='double',min=0,max=1,dv=0)
    cmds.setAttr('%s.localSpace' %handSub_CON_side ,k=1,e=1)
    tempLocal = cmds.createNode('transform',n=handSub_NUL_side ,parent = handSub_NUL2_side)
    cmds.parent(handSub_CON_side,handSub_NUL_side)

    handSubAttatch_NUL = cmds.group(em = 1 , n = handSubAttatch_local_NUL , parent = hand_CON_side)
    handSubAttatch_LOC = cmds.spaceLocator( n = handSubAttatch_local_LOC)[0]
    cmds.delete(cmds.parentConstraint(hand_CON_side , handSubAttatch_LOC , mo=0 ))
    cmds.parent(handSubAttatch_LOC , handSubAttatch_NUL)
    if side == 'L':
        cmds.setAttr('%s.rotateX' %handSubAttatch_LOC , 90)
    else:
        cmds.setAttr('%s.rotateX' %handSubAttatch_LOC , -90)
    cmds.parent(handSubAttatch_local_NUL , 'attach_GRP')

    toAttNUL_MMX = cmds.createNode('multMatrix', n = handSubAttatch_local_NUL.replace(handSubAttatch_local_NUL.split('_')[-1], '1_MMX'))
    toAttNUL_DCM = cmds.createNode('decomposeMatrix' , n = handSubAttatch_local_NUL.replace(handSubAttatch_local_NUL.split('_')[-1], '1_DCM'))
    toSubNUL_PBD = cmds.createNode('pairBlend' , n = handSubAttatch_local_NUL.replace(handSubAttatch_local_NUL.split('_')[-1], 'PBD'))
    toSubNUL_MMX = cmds.createNode('multMatrix', n = handSubAttatch_local_NUL.replace(handSubAttatch_local_NUL.split('_')[-1], '2_MMX'))
    toSubNUL_DCM = cmds.createNode('decomposeMatrix' , n = handSubAttatch_local_NUL.replace(handSubAttatch_local_NUL.split('_')[-1], '2_DCM'))
    # to Attatch null
    cmds.connectAttr('%s.worldMatrix[0]' %hand_CON_side , '%s.matrixIn[0]' %toAttNUL_MMX , f=1)
    cmds.connectAttr('%s.matrixSum' %toAttNUL_MMX , '%s.inputMatrix' %toAttNUL_DCM , f=1)
    cmds.connectAttr('%s.outputTranslate' %toAttNUL_DCM , '%s.translate' %handSubAttatch_NUL , f=1)
    cmds.connectAttr('%s.outputRotate' %toAttNUL_DCM , '%s.rotate' %handSubAttatch_NUL , f=1)
    cmds.connectAttr('%s.outputScale' %toAttNUL_DCM , '%s.scale' %handSubAttatch_NUL , f=1)
    cmds.connectAttr('%s.outputShear' %toAttNUL_DCM , '%s.shear' %handSubAttatch_NUL , f=1)
    cmds.connectAttr('%s.parentInverseMatrix[0]' %handSubAttatch_NUL , '%s.matrixIn[1]' %toAttNUL_MMX , f=1)
    # to handSub null + pairBlend
    cmds.connectAttr('%s.worldMatrix[0]' %handSubAttatch_LOC , '%s.matrixIn[0]' %toSubNUL_MMX , f=1)
    cmds.connectAttr('%s.matrixSum' %toSubNUL_MMX , '%s.inputMatrix' %toSubNUL_DCM , f=1)
    cmds.connectAttr('%s.outputTranslate' %toSubNUL_DCM , '%s.inTranslate2' %toSubNUL_PBD , f=1)
    cmds.connectAttr('%s.outputRotate' %toSubNUL_DCM , '%s.inRotate2' %toSubNUL_PBD , f=1)

    cmds.connectAttr('%s.localSpace' %handSub_CON_side , '%s.weight' %toSubNUL_PBD , f=1)
    cmds.connectAttr('%s.outTranslate' %toSubNUL_PBD , '%s.translate' %handSub_NUL_side , f=1)
    cmds.connectAttr('%s.outRotate' %toSubNUL_PBD , '%s.rotate' %handSub_NUL_side , f=1)
    cmds.connectAttr('%s.parentInverseMatrix[0]' %handSub_NUL_side , '%s.matrixIn[1]' %toSubNUL_MMX , f=1)
  
#addLocalSpacetoHandSub('L')
#addLocalSpacetoHandSub('R')