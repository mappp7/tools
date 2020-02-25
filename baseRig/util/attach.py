#encoding=utf-8

import maya.cmds as cmds
from util.snap import *
from util.setUniqueName import*


## attachNode ##    
def attachNode( baseNode, targetNode, *TRSS ):
	# node create
	baseNodeMMX = cmds.createNode( 'multMatrix', n=baseNode.replace( baseNode.split('_')[-1], 'MMX' ) )
	baseNodeDCM = cmds.createNode( 'decomposeMatrix', n=baseNode.replace( baseNode.split('_')[-1], 'DCM' ) )

	# conncet node
	cmds.connectAttr( '%s.worldMatrix[0]' % baseNode, '%s.matrixIn[0]' % baseNodeMMX )
	cmds.connectAttr( '%s.parentInverseMatrix[0]' % targetNode, '%s.matrixIn[1]' % baseNodeMMX )

	cmds.connectAttr( '%s.matrixSum' % baseNodeMMX, '%s.inputMatrix' % baseNodeDCM )
	
	if len(TRSS) != 0:
		for x in range(len(TRSS)):
		    cmds.connectAttr( '%s.output%s' % (baseNodeDCM, TRSS[x].capitalize()), '%s.%s' % (targetNode, TRSS[x]) )
	return baseNodeMMX, baseNodeDCM
	
def attachPart( basePart, targetPart, *TRSS ):
    
    #node create
    attachNul = cmds.createNode( 'transform', n='%sAttach_NUL' % targetPart )
    POsnap( attachNul, basePart )
    
    attachLocator = cmds.spaceLocator( n='%sAttach_LOC' % targetPart )
    POsnap( attachLocator, targetPart )
    
    cmds.parent( attachLocator[0],attachNul )
    
    baseNodeMMX = cmds.createNode( 'multMatrix', n=basePart.replace( basePart.split('_')[-1], 'MMX' ) )
    baseNodeDPX = cmds.createNode( 'decomposeMatrix', n=basePart.replace( basePart.split('_')[-1], 'DCM' ) )
    
    targetNodeMMX = cmds.createNode( 'multMatrix', n=targetPart.replace( targetPart.split('_')[-1], 'MMX' ) )
    targetNodeDPX = cmds.createNode( 'decomposeMatrix', n=targetPart.replace( targetPart.split('_')[-1], 'DCM' ) )
    
    #conncet node
    cmds.connectAttr( '%s.worldMatrix[0]' % basePart, '%s.matrixIn[0]' % baseNodeMMX )
    cmds.connectAttr( '%s.parentInverseMatrix[0]' % attachNul, '%s.matrixIn[1]' % baseNodeMMX )
    
    cmds.connectAttr( '%s.matrixSum' % baseNodeMMX, '%s.inputMatrix' % baseNodeDPX )
    
    
    cmds.connectAttr( '%s.worldMatrix[0]' % attachLocator[0], '%s.matrixIn[0]' % targetNodeMMX )
    cmds.connectAttr( '%s.parentInverseMatrix[0]' % targetPart, '%s.matrixIn[1]' % targetNodeMMX )
    
    cmds.connectAttr( '%s.matrixSum' % targetNodeMMX, '%s.inputMatrix' % targetNodeDPX )    
    
    if 'translate' in TRSS:
        cmds.connectAttr( '%s.outputTranslate' % baseNodeDPX, '%s.translate' % attachNul )
        cmds.connectAttr( '%s.outputTranslate' % targetNodeDPX, '%s.translate' % targetPart )
    if 'rotate' in TRSS:
        cmds.connectAttr( '%s.outputRotate' % baseNodeDPX, '%s.rotate' % attachNul )
        cmds.connectAttr( '%s.outputRotate' % targetNodeDPX, '%s.rotate' % targetPart )
    if 'scale' in TRSS:
        cmds.connectAttr( '%s.outputScale' % baseNodeDPX, '%s.scale' % attachNul )
        cmds.connectAttr( '%s.outputScale' % targetNodeDPX, '%s.scale' % targetPart )
    if 'shear' in TRSS:
        cmds.connectAttr( '%s.outputShear' % baseNodeDPX, '%s.shear' % attachNul )
        cmds.connectAttr( '%s.outputShear' % targetNodeDPX, '%s.shear' % targetPart )
    return attachNul

#===================================
#attachPart의 수정버젼 
#===================================
def attachPart2( basePart, targetPart, *TRSS ):
    
    #=======================
    #추가된 부분 (이름 관련 하여)
    #=======================
    TargetName=''
    buffer= targetPart.split('_')[:-1]
    for i in range(len(buffer)):
        if i is 0:
            TargetName=buffer[i]
        else:
            TargetName=TargetName+'_'+buffer[i]   

    #node create
    tmp1 = cmds.createNode( 'transform', n=TargetName+'Attach')
    attachNul=setUniqueName(tmp1,'NUL')

    POsnap( attachNul, basePart )
    
    tmp2 = cmds.spaceLocator( n=TargetName+'Attach')
    attachLocator=setUniqueName(tmp2[0],'LOC')

    POsnap( attachLocator, targetPart )
    
    cmds.parent( attachLocator,attachNul )
    
    baseNodeMMX = cmds.createNode( 'multMatrix', n=basePart.replace( basePart.split('_')[-1], 'MMX' ) )
    baseNodeDPX = cmds.createNode( 'decomposeMatrix', n=basePart.replace( basePart.split('_')[-1], 'DCM' ) )
    
    targetNodeMMX = cmds.createNode( 'multMatrix', n=targetPart.replace( targetPart.split('_')[-1], 'MMX' ) )
    targetNodeDPX = cmds.createNode( 'decomposeMatrix', n=targetPart.replace( targetPart.split('_')[-1], 'DCM' ) )
    
    #conncet node
    cmds.connectAttr( '%s.worldMatrix[0]' % basePart, '%s.matrixIn[0]' % baseNodeMMX )
    cmds.connectAttr( '%s.parentInverseMatrix[0]' % attachNul, '%s.matrixIn[1]' % baseNodeMMX )
    
    cmds.connectAttr( '%s.matrixSum' % baseNodeMMX, '%s.inputMatrix' % baseNodeDPX )
    
    
    cmds.connectAttr( '%s.worldMatrix[0]' % attachLocator, '%s.matrixIn[0]' % targetNodeMMX )
    cmds.connectAttr( '%s.parentInverseMatrix[0]' % targetPart, '%s.matrixIn[1]' % targetNodeMMX )
    
    #=======================
    #attachPart와 달라진 부분 
    #=======================
    cmds.connectAttr( '%s.matrixSum' % targetNodeMMX, '%s.inputMatrix' % targetNodeDPX )    
    cmds.connectAttr( '%s.outputTranslate' % baseNodeDPX, '%s.translate' % attachNul )
    cmds.connectAttr( '%s.outputRotate' % baseNodeDPX, '%s.rotate' % attachNul )
    cmds.connectAttr( '%s.outputScale' % baseNodeDPX, '%s.scale' % attachNul )
    cmds.connectAttr( '%s.outputShear' % baseNodeDPX, '%s.shear' % attachNul )
    #~여기까지
    #=======================
    
    if 'translate' in TRSS:
        cmds.connectAttr( '%s.outputTranslate' % targetNodeDPX, '%s.translate' % targetPart )
    if 'rotate' in TRSS:
        cmds.connectAttr( '%s.outputRotate' % targetNodeDPX, '%s.rotate' % targetPart )
    if 'scale' in TRSS:
        cmds.connectAttr( '%s.outputScale' % targetNodeDPX, '%s.scale' % targetPart )
    if 'shear' in TRSS:
        cmds.connectAttr( '%s.outputShear' % targetNodeDPX, '%s.shear' % targetPart )
        
    return attachNul   