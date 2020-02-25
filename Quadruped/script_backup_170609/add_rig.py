def headSpace():
    
    cmds.addAttr ( 'C_IK_head_CON', ln='local_space', at='double',  min=0, max=10, dv=0 )
    cmds.setAttr ( 'C_IK_head_CON.local_space', e=1, keyable=1 )
    
    setRange_Node = cmds.rename ( ( cmds.createNode ('setRange') ), 'head_space_setRange' )
    PBD_node = cmds.rename ( ( cmds.createNode ('pairBlend' ) ), 'head_space_PBD' )
    
    cmds.setAttr ( setRange_Node+'.maxX', 1 )
    cmds.setAttr ( setRange_Node+'.oldMaxX', 10 )
    
    cmds.connectAttr ( 'C_IK_head_CON.local_space', setRange_Node+'.value.valueX' )
    cmds.connectAttr ( setRange_Node+'.outValue.outValueX', PBD_node+'.weight' )
    
    SPC_NUL = cmds.group ( em=1, n='C_IK_head_SPC_NUL' )
    cmds.delete ( cmds.parentConstraint ( 'C_IK_head_CON', SPC_NUL ) )
    cmds.parent ( SPC_NUL, 'C_IK_head_extra_NUL' )
    cmds.parent ( 'C_IK_head_CON', SPC_NUL )
    
    cmds.disconnectAttr ( 'C_FK_head_DCM.outputRotate', 'C_IK_head_extra_NUL.rotate' )
    cmds.connectAttr ( 'C_FK_head_DCM.outputRotate', PBD_node+'.inRotate1' )
    
    cmds.connectAttr (  )
    
    

headSpace()