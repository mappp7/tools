import maya.cmds as cmds

def addMatchInfo( fkobj, ikobj ):

    cmds.addAttr( fkobj, ln='ikMp', at='double3' )
    cmds.addAttr( fkobj, ln ='ikMpX', at='double', p='ikMp' )
    cmds.addAttr( fkobj, ln ='ikMpY', at='double', p='ikMp' )
    cmds.addAttr( fkobj, ln ='ikMpZ', at='double', p='ikMp' )
    
    cmds.addAttr( fkobj, ln='ikMr', at='double3' )
    cmds.addAttr( fkobj, ln ='ikMrX', at='double', p='ikMr' )
    cmds.addAttr( fkobj, ln ='ikMrY', at='double', p='ikMr' )
    cmds.addAttr( fkobj, ln ='ikMrZ', at='double', p='ikMr' )
    
    
    cmds.addAttr( ikobj, ln='fkMp', at='double3' )
    cmds.addAttr( ikobj, ln ='fkMpX', at='double', p='fkMp' )
    cmds.addAttr( ikobj, ln ='fkMpY', at='double', p='fkMp' )
    cmds.addAttr( ikobj, ln ='fkMpZ', at='double', p='fkMp' )
    
    cmds.addAttr( ikobj, ln='fkMr', at='double3' )
    cmds.addAttr( ikobj, ln ='fkMrX', at='double', p='fkMr' )
    cmds.addAttr( ikobj, ln ='fkMrY', at='double', p='fkMr' )
    cmds.addAttr( ikobj, ln ='fkMrZ', at='double', p='fkMr' )
    
    
    # Create Node
    multMfk = cmds.createNode( 'multMatrix', n=fkobj.replace( fkobj.split('_')[-1], 'MMX' ) )
    decomposeMfk = cmds.createNode( 'decomposeMatrix', n=fkobj.replace( fkobj.split('_')[-1], 'DMX' ) )
    
    multMik = cmds.createNode( 'multMatrix', n=ikobj.replace( ikobj.split('_')[-1], 'MMX' ) )
    decomposeMik = cmds.createNode( 'decomposeMatrix', n=ikobj.replace( ikobj.split('_')[-1], 'DMX' ) )
    
    # inPut connections
    cmds.connectAttr( '%s.worldMatrix' % fkobj, '%s.matrixIn[0]' % multMfk )
    cmds.connectAttr( '%s.parentInverseMatrix' % ikobj, '%s.matrixIn[1]' % multMfk )
    
    cmds.connectAttr( '%s.matrixSum' % multMfk, '%s.inputMatrix' % decomposeMfk )
    
    
    cmds.connectAttr( '%s.worldMatrix' % ikobj, '%s.matrixIn[0]' % multMik )
    cmds.connectAttr( '%s.parentInverseMatrix' % fkobj, '%s.matrixIn[1]' % multMik )
    
    cmds.connectAttr( '%s.matrixSum' % multMik, '%s.inputMatrix' % decomposeMik )
    
    # outPut connections
    cmds.connectAttr( '%s.outputTranslate' % decomposeMfk, '%s.fkMp' % ikobj )
    cmds.connectAttr( '%s.outputRotate' % decomposeMfk, '%s.fkMr' % ikobj )
    
    cmds.connectAttr( '%s.outputTranslate' % decomposeMik, '%s.ikMp' % fkobj )
    cmds.connectAttr( '%s.outputRotate' % decomposeMik, '%s.ikMr' % fkobj )