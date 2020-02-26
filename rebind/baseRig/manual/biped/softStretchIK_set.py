import maya.cmds as cmds

class softStretchIKSet():
    
    def __init__(self):
        self.xyz = ['x','y','z']

    def setSoftIK(self):
        #softIK and StretchIK
        softIK_asset = ''
        stretchIK_asset = ''
        tempRef = {
                   1:['L_template_hand_JNT','L_template_foreArm_JNT','L_template_upArm_JNT'],
                   2:['R_template_hand_JNT','R_template_foreArm_JNT','R_template_upArm_JNT'],
                   3:['L_template_foot_JNT','L_template_lowLeg_JNT','L_template_leg_JNT'],
                   4:['R_template_foot_JNT','R_template_lowLeg_JNT','R_template_leg_JNT']
                  }
        refPos = dict()
        for i in range(1,5):
            refPos[i] = dict()
            for j in range(len(tempRef[i])):
                print j
                rN = tempRef[i][j].replace('template','ref')
                rNA = rN.replace('JNT','LOC')
                refPos[i][rNA] = dict()
                tempPos = cmds.xform(tempRef[i][j],q=1,t=1,ws=1)
                for t in range(len(tempPos)):
                    tempPos[t] = round(tempPos[t],5)
                refPos[i][rNA] = tempPos

        for i in range(1,5):
            for j in refPos[i]:
                print j
                print refPos[i][j]
                tempLoc = cmds.spaceLocator(n='%s' %j )[0]
                cmds.setAttr('%s.tx' %tempLoc , refPos[i][j][0])
                cmds.setAttr('%s.ty' %tempLoc , refPos[i][j][1])
                cmds.setAttr('%s.tz' %tempLoc , refPos[i][j][2])
                cmds.CenterPivot(tempLoc)
        self.softIKDefaultSet('L')
        self.softIKDefaultSet('R')
        self.setDistanceConnect('L')
        self.setDistanceConnect('R')
        self.deleteAttr('L')
        self.deleteAttr('R')
        self.setHierachyGroup()
                     
    def softIKDefaultSet(self,side):
        # parent motion control locator
        # ARM part
        arm_strh = cmds.duplicate('%s_ref_hand_LOC' %side , n='%s_arm_stretchIK_output_LOC' %side)
        arm_soft = cmds.duplicate('%s_ref_hand_LOC' %side , n='%s_arm_softIK_output_LOC' %side)
        arm_aim = cmds.duplicate('%s_ref_upArm_LOC' %side , n='%s_arm_aim_LOC' %side)
        arm_space = cmds.duplicate('%s_ref_upArm_LOC' %side , n='%s_arm_space_LOC' %side)
        arm_upVec = cmds.duplicate('%s_ref_upArm_LOC' %side , n='%s_arm_softIK_upVec_LOC' %side)
        cmds.setAttr('%s.ty' %arm_upVec[0], 5)
        cmds.select('%s_IK_hand_LOC' %side , arm_aim , r=1)
        cmds.aimConstraint(mo=0 , wut='object' , wuo='%s_arm_softIK_upVec_LOC' %side )

        cmds.parent(arm_strh,arm_soft)
        cmds.parent(arm_soft,arm_aim)
        cmds.parent(arm_aim,arm_space)
        cmds.parent(arm_upVec,arm_space)
        for i in self.xyz:
            cmds.setAttr('%s_arm_softIK_output_LOC.r%s' %(side,i) , 0)
            cmds.setAttr('%s_arm_softIK_output_LOC.r%s' %(side,i) , 0)
            cmds.setAttr('%s_arm_softIK_output_LOC.r%s' %(side,i) , 0)
        
        # LEG part
        leg_strh = cmds.duplicate('%s_ref_foot_LOC' %side , n='%s_leg_stretchIK_output_LOC' %side)
        leg_soft = cmds.duplicate('%s_ref_foot_LOC' %side , n='%s_leg_softIK_output_LOC' %side)
        leg_aim = cmds.duplicate('%s_ref_leg_LOC' %side , n='%s_leg_aim_LOC' %side)
        leg_space = cmds.duplicate('%s_ref_leg_LOC' %side , n='%s_leg_space_LOC' %side)
        leg_upVec = cmds.duplicate('%s_ref_leg_LOC' %side , n='%s_leg_softIK_upVec_LOC' %side)
        cmds.setAttr('%s.tz' %leg_upVec[0], 5)
        cmds.select('%s_IK_foot_LOC' %side , leg_aim , r=1)
        cmds.aimConstraint(mo=0 , wut='object' , wuo='%s_leg_softIK_upVec_LOC' %side )
        
        cmds.parent(leg_strh,leg_soft)
        cmds.parent(leg_soft,leg_aim)
        cmds.parent(leg_aim,leg_space)
        cmds.parent(leg_upVec,leg_space)
        
        # parent ref locator 
        cmds.parent('%s_ref_hand_LOC' %side,'%s_ref_foreArm_LOC' %side)
        cmds.parent('%s_ref_foreArm_LOC' %side,'%s_ref_upArm_LOC' %side)
        cmds.parent('%s_ref_foot_LOC' %side,'%s_ref_lowLeg_LOC' %side)
        cmds.parent('%s_ref_lowLeg_LOC' %side,'%s_ref_leg_LOC' %side)
        for i in self.xyz:
            cmds.setAttr('%s_leg_softIK_output_LOC.r%s' %(side,i) , 0)
            cmds.setAttr('%s_leg_softIK_output_LOC.r%s' %(side,i) , 0)
            cmds.setAttr('%s_leg_softIK_output_LOC.r%s' %(side,i) , 0)
        # parent IK handle
        cmds.delete('%s_IK_hand_HDL_parentConstraint1' %side)
        cmds.delete('%s_IK_foot_HDL_parentConstraint1' %side)
        cmds.parent('%s_IK_hand_HDL' %side , arm_strh)
        cmds.parent('%s_IK_foot_HDL' %side , leg_strh)
        #cmds.parentConstraint('%s_IK_foot_LOC' %side , '%s_IK_foot_HDL' %side , mo=1) # need to foot roll set
        # add Attr 
        cmds.addAttr('%s_IK_hand_CON' %side , ln='softIK' , min=0 , max=1 , at ='double' )
        cmds.setAttr('%s_IK_hand_CON.softIK' %side, e=1 , k=1 )
        cmds.addAttr('%s_IK_hand_CON' %side , ln='stretchIK' , min=0 , max=1 , at ='double' )
        cmds.setAttr('%s_IK_hand_CON.stretchIK' %side, e=1 , k=1 )
        cmds.addAttr('%s_IK_foot_CON' %side , ln='softIK' , min=0 , max=1 , at ='double' )
        cmds.setAttr('%s_IK_foot_CON.softIK' %side, e=1 , k=1 )
        cmds.addAttr('%s_IK_foot_CON' %side , ln='stretchIK' , min=0 , max=1 , at ='double' )
        cmds.setAttr('%s_IK_foot_CON.stretchIK' %side, e=1 , k=1 )
        
    def setDistanceConnect(self,side):
        # set arm length 
        # createNode
        upArmLenDis = cmds.createNode('distanceBetween' , n='%s_upArm_DIS' %side)
        foreArmLenDis = cmds.createNode('distanceBetween' , n='%s_foreArm_DIS' %side)
        ArmLenPMA = cmds.createNode('plusMinusAverage' , n='%s_ArmLen_PMA' %side)
        armCtrlLenDis = cmds.createNode('distanceBetween' , n='%s_armCtrlLen_DIS' %side)
        armStretch_mult_ctrlVal = cmds.createNode('multiplyDivide' , n='%s_arm_stretch_mult_ctrlVal_MPD' %side)
        armMMX = cmds.createNode('multMatrix', n='%s_armCtrlLen_MMX' %side)
        armDCM = cmds.createNode('decomposeMatrix', n='%s_armCtrlLen_DCM' %side)
        
        arm_init_space = cmds.createNode('transform' , n= '%s_arm_init_space_NUL' %side)
        upArm_MMX = cmds.createNode('multMatrix' , n='%s_ref_upArm_MMX' %side)
        foreArm_MMX = cmds.createNode('multMatrix' , n='%s_ref_foreArm_MMX' %side)
        hand_MMX = cmds.createNode('multMatrix' , n='%s_ref_hand_MMX' %side)
        upArm_DCM = cmds.createNode('decomposeMatrix' , n='%s_ref_upArm_DCM' %side)
        foreArm_DCM = cmds.createNode('decomposeMatrix' , n='%s_ref_foreArm_DCM' %side)
        hand_DCM = cmds.createNode('decomposeMatrix' , n='%s_ref_hand_DCM' %side)
        # length connection
        cmds.parentConstraint('%s_FK_upArmAttach_LOC' %side, '%s' %arm_init_space, mo=0)
        for i in self.xyz:
            cmds.connectAttr('place_CON.globalScale', '%s.s%s' %(arm_init_space , i))
        cmds.connectAttr('%s.scale' %arm_init_space , '%s_ref_upArm_LOC.scale' %side)
        #cmds.connectAttr('%s.scale' %arm_init_space , '%s_arm_space_LOC.scale' %side)
        cmds.parentConstraint(arm_init_space,'%s_ref_upArm_LOC' %side, mo=1)
        cmds.parentConstraint(arm_init_space,'%s_arm_space_LOC' %side, mo=1)
        cmds.parent('%s_arm_space_LOC' %side,arm_init_space)
        
        cmds.connectAttr('%s_ref_upArm_LOC.worldMatrix[0]' %side , '%s.matrixIn[0]' %upArm_MMX)
        cmds.connectAttr('%s.worldInverseMatrix[0]' %arm_init_space , '%s.matrixIn[1]' %upArm_MMX)
        cmds.connectAttr('%s_ref_foreArm_LOC.worldMatrix[0]' %side , '%s.matrixIn[0]' %foreArm_MMX)
        cmds.connectAttr('%s.worldInverseMatrix[0]' %arm_init_space , '%s.matrixIn[1]' %foreArm_MMX)
        cmds.connectAttr('%s_ref_hand_LOC.worldMatrix[0]' %side , '%s.matrixIn[0]' %hand_MMX)
        cmds.connectAttr('%s.worldInverseMatrix[0]' %arm_init_space , '%s.matrixIn[1]' %hand_MMX)
        
        cmds.connectAttr('%s.matrixSum' %upArm_MMX , '%s.inputMatrix' %upArm_DCM   )
        cmds.connectAttr('%s.matrixSum' %foreArm_MMX , '%s.inputMatrix' %foreArm_DCM   )
        cmds.connectAttr('%s.matrixSum' %hand_MMX , '%s.inputMatrix' %hand_DCM   )
        
        cmds.connectAttr('%s.outputTranslate' %foreArm_DCM , '%s.point2' %upArmLenDis)
        cmds.connectAttr('%s.outputTranslate' %foreArm_DCM , '%s.point1' %foreArmLenDis)
        cmds.connectAttr('%s.outputTranslate' %hand_DCM , '%s.point2' %foreArmLenDis)    
        cmds.connectAttr('%s.outputTranslate' %upArm_DCM , '%s.point1' %upArmLenDis) 
         
        cmds.connectAttr('%s.outputTranslate' %upArm_DCM , '%s.point1' %armCtrlLenDis)
        cmds.connectAttr('%s_IK_hand_CON.worldMatrix[0]' %side , '%s.matrixIn[0]' %armMMX)
        cmds.connectAttr('%s.worldInverseMatrix[0]' %arm_init_space , '%s.matrixIn[1]' %armMMX)
        cmds.connectAttr('%s.matrixSum' %armMMX , '%s.inputMatrix' %armDCM)
        cmds.connectAttr('%s.outputTranslate' %armDCM , '%s.point2' %armCtrlLenDis)

        cmds.connectAttr('%s.distance' %upArmLenDis, '%s.input1D[0]' %ArmLenPMA)
        cmds.connectAttr('%s.distance' %foreArmLenDis, '%s.input1D[1]' %ArmLenPMA)
        

                         
        # set leg length 
        upLegLenDis = cmds.createNode('distanceBetween' , n='%s_upLeg_DIS' %side)
        lowLegLenDis = cmds.createNode('distanceBetween' , n='%s_lowLeg_DIS' %side)
        legLenPMA = cmds.createNode('plusMinusAverage' , n='%s_legLen_PMA' %side)
        legCtrlLenDis = cmds.createNode('distanceBetween' , n='%s_legCtrlLen_DIS' %side)
        legStretch_mult_ctrlVal = cmds.createNode('multiplyDivide' , n='%s_leg_stretch_mult_ctrlVal_MPD' %side)
        legMMX = cmds.createNode('multMatrix', n='%s_legCtrlLen_MMX' %side)
        legDCM = cmds.createNode('decomposeMatrix', n='%s_legCtrlLen_DCM' %side)
        
        leg_init_space = cmds.createNode('transform' , n= '%s_leg_init_space_NUL' %side)
        leg_MMX = cmds.createNode('multMatrix' , n='%s_ref_leg_MMX' %side)
        lowLeg_MMX = cmds.createNode('multMatrix' , n='%s_ref_lowLeg_MMX' %side)
        foot_MMX = cmds.createNode('multMatrix' , n='%s_ref_foot_MMX' %side)
        leg_DCM = cmds.createNode('decomposeMatrix' , n='%s_ref_leg_DCM' %side)
        lowLeg_DCM = cmds.createNode('decomposeMatrix' , n='%s_ref_lowLeg_DCM' %side)
        foot_DCM = cmds.createNode('decomposeMatrix' , n='%s_ref_foot_DCM' %side)

        cmds.parentConstraint('%s_FK_legAttach_LOC' %side, '%s' %leg_init_space, mo=0)
        for i in self.xyz:
            cmds.connectAttr('place_CON.globalScale', '%s.s%s' %(leg_init_space , i))
        cmds.connectAttr('%s.scale' %leg_init_space , '%s_ref_leg_LOC.scale' %side)
        #cmds.connectAttr('%s.scale' %leg_init_space , '%s_leg_space_LOC.scale' %side)
        cmds.parentConstraint(leg_init_space,'%s_ref_leg_LOC' %side, mo=1)
        cmds.parentConstraint(leg_init_space,'%s_leg_space_LOC' %side, mo=1)
        cmds.parent('%s_leg_space_LOC' %side,leg_init_space)
        # ----
        cmds.connectAttr('%s_ref_leg_LOC.worldMatrix[0]' %side , '%s.matrixIn[0]' %leg_MMX)
        cmds.connectAttr('%s.worldInverseMatrix[0]' %leg_init_space , '%s.matrixIn[1]' %leg_MMX)
        cmds.connectAttr('%s_ref_lowLeg_LOC.worldMatrix[0]' %side , '%s.matrixIn[0]' %lowLeg_MMX)
        cmds.connectAttr('%s.worldInverseMatrix[0]' %leg_init_space , '%s.matrixIn[1]' %lowLeg_MMX)
        cmds.connectAttr('%s_ref_foot_LOC.worldMatrix[0]' %side , '%s.matrixIn[0]' %foot_MMX)
        cmds.connectAttr('%s.worldInverseMatrix[0]' %leg_init_space , '%s.matrixIn[1]' %foot_MMX)
        
        cmds.connectAttr('%s.matrixSum' %leg_MMX , '%s.inputMatrix' %leg_DCM   )
        cmds.connectAttr('%s.matrixSum' %lowLeg_MMX , '%s.inputMatrix' %lowLeg_DCM   )
        cmds.connectAttr('%s.matrixSum' %foot_MMX , '%s.inputMatrix' %foot_DCM   )
        
        cmds.connectAttr('%s.outputTranslate' %lowLeg_DCM , '%s.point2' %upLegLenDis)
        cmds.connectAttr('%s.outputTranslate' %lowLeg_DCM , '%s.point1' %lowLegLenDis)
        cmds.connectAttr('%s.outputTranslate' %foot_DCM , '%s.point2' %lowLegLenDis)    
        cmds.connectAttr('%s.outputTranslate' %leg_DCM , '%s.point1' %upLegLenDis) 
         
        cmds.connectAttr('%s.outputTranslate' %leg_DCM , '%s.point1' %legCtrlLenDis)
        cmds.connectAttr('%s_IK_foot_LOC.worldMatrix[0]' %side , '%s.matrixIn[0]' %legMMX)
        cmds.connectAttr('%s.worldInverseMatrix[0]' %leg_init_space , '%s.matrixIn[1]' %legMMX)
        cmds.connectAttr('%s.matrixSum' %legMMX , '%s.inputMatrix' %legDCM)
        cmds.connectAttr('%s.outputTranslate' %legDCM , '%s.point2' %legCtrlLenDis)
        #-----
        cmds.connectAttr('%s.distance' %upLegLenDis, '%s.input1D[0]' %legLenPMA)
        cmds.connectAttr('%s.distance' %lowLegLenDis, '%s.input1D[1]' %legLenPMA)
        

        # import asset 
        softIK_ast_path = '/dexter/Cache_DATA/CRT/riggingTeamShelf/bumbleBee/asset/softIK_asset.ma'
        stretchIK_ast_path = '/dexter/Cache_DATA/CRT/riggingTeamShelf/bumbleBee/asset/stretchIK_asset.ma'
        cmds.file(softIK_ast_path , i=True, type='mayaAscii', iv=True, ra=True ,mnc=False ,rpr='%s_arm' %side)
        cmds.file(stretchIK_ast_path , i=True, type='mayaAscii', iv=True, ra=True ,mnc=False ,rpr='%s_arm' %side)
        cmds.file(softIK_ast_path , i=True, type='mayaAscii', iv=True, ra=True ,mnc=False ,rpr='%s_leg' %side)
        cmds.file(stretchIK_ast_path , i=True, type='mayaAscii', iv=True, ra=True ,mnc=False ,rpr='%s_leg' %side)     

        unusedNode = [u'L_leg_uiConfigurationScriptNode1',
                      u'L_leg_uiConfigurationScriptNode',
                      u'L_leg_sceneConfigurationScriptNode1',
                      u'L_leg_sceneConfigurationScriptNode',
                      u'L_arm_uiConfigurationScriptNode1',
                      u'L_arm_uiConfigurationScriptNode',
                      u'L_arm_sceneConfigurationScriptNode1',
                      u'L_arm_sceneConfigurationScriptNode',
                      u'L_leg_defaultRenderLayer1',
                      u'L_leg_defaultRenderLayer',
                      u'L_arm_defaultRenderLayer1',
                      u'L_arm_defaultRenderLayer']
        try:
            for i in unusedNode:
                if side == 'L':
                    cmds.delete(i)
                else:
                    i = i.replace('L_','R_')
                    cmds.delete(i)
        except:
            pass
        
        # set Connection 
            # arm ---- input ---------------------------------------------------------------------------------------------
        cmds.connectAttr('%s.output1D' %ArmLenPMA , '%s_arm_softIK_AST.armLen' %side, f=1)
        cmds.connectAttr('%s.distance' %armCtrlLenDis , '%s_arm_softIK_AST.ctrlLen' %side, f=1)
        cmds.connectAttr('%s_IK_hand_CON.softIK' %side , '%s_arm_softIK_AST.softikCtrlValue' %side, f=1)
        cmds.connectAttr('%s_arm_softIK_AST.outputSoftik' %side, '%s_arm_stretchIK_AST.softikLen' %side, f=1)
        cmds.connectAttr('%s.distance' %armCtrlLenDis , '%s_arm_stretchIK_AST.ctrlLen' %side, f=1)
        cmds.connectAttr('%s.distance' %foreArmLenDis , '%s_arm_stretchIK_AST.foreArmLen' %side, f=1)
        cmds.connectAttr('%s.distance' %upArmLenDis , '%s_arm_stretchIK_AST.upArmLen' %side, f=1)
        cmds.connectAttr('%s_IK_hand_CON.stretchIK' %side , '%s_arm_stretchIK_AST.stretchCtrlValue' %side, f=1)
            # arm ---- output ---------------------------------------------------------------------------------------------
        if side is 'L':
            cmds.connectAttr('%s_arm_stretchIK_AST.foreArmStretched' %side , '%s_IK_hand_JNT.translateX' %side, f=1)
            cmds.connectAttr('%s_arm_stretchIK_AST.upArmStretched' %side , '%s_IK_foreArm_JNT.translateX' %side, f=1)
        else:
            foreArm_reverse_MDL = cmds.createNode('multDoubleLinear', n = '%s_foreArm_stretchIK_MDL' %side)
            upArm_reverse_MDL = cmds.createNode('multDoubleLinear', n = '%s_upArm_stretchIK_MDL' %side)
            cmds.setAttr('%s.input2' %foreArm_reverse_MDL , -1)
            cmds.setAttr('%s.input2' %upArm_reverse_MDL , -1)
            cmds.connectAttr('%s_arm_stretchIK_AST.foreArmStretched' %side , '%s.input1' %foreArm_reverse_MDL, f=1)
            cmds.connectAttr('%s.output' %foreArm_reverse_MDL , '%s_IK_hand_JNT.translateX' %side, f=1)
            cmds.connectAttr('%s_arm_stretchIK_AST.upArmStretched' %side , '%s.input1' %upArm_reverse_MDL, f=1)
            cmds.connectAttr('%s.output' %upArm_reverse_MDL , '%s_IK_foreArm_JNT.translateX' %side, f=1)
            
        cmds.connectAttr('%s_arm_stretchIK_AST.stretchCtrlValueOut' %side , '%s.input1X' %armStretch_mult_ctrlVal, f=1)
        cmds.connectAttr('%s_arm_stretchIK_AST.stretchedLen' %side , '%s.input2X' %armStretch_mult_ctrlVal, f=1)
        cmds.connectAttr('%s.outputX' %armStretch_mult_ctrlVal, '%s_arm_stretchIK_output_LOC.tx' %side, f=1)
        cmds.connectAttr('%s_arm_softIK_AST.outputSoftik' %side, '%s_arm_softIK_output_LOC.tx' %side, f=1)
            # leg ---- input ---------------------------------------------------------------------------------------------
        cmds.connectAttr('%s.output1D' %legLenPMA , '%s_leg_softIK_AST.armLen' %side, f=1)
        cmds.connectAttr('%s.distance' %legCtrlLenDis , '%s_leg_softIK_AST.ctrlLen' %side, f=1)
        cmds.connectAttr('%s_IK_foot_CON.softIK' %side , '%s_leg_softIK_AST.softikCtrlValue' %side, f=1)
        cmds.connectAttr('%s_leg_softIK_AST.outputSoftik' %side, '%s_leg_stretchIK_AST.softikLen' %side, f=1)
        cmds.connectAttr('%s.distance' %legCtrlLenDis , '%s_leg_stretchIK_AST.ctrlLen' %side, f=1)
        cmds.connectAttr('%s.distance' %lowLegLenDis , '%s_leg_stretchIK_AST.foreArmLen' %side, f=1)
        cmds.connectAttr('%s.distance' %upLegLenDis , '%s_leg_stretchIK_AST.upArmLen' %side, f=1)
        cmds.connectAttr('%s_IK_foot_CON.stretchIK' %side , '%s_leg_stretchIK_AST.stretchCtrlValue' %side, f=1)
            # leg ---- output ---------------------------------------------------------------------------------------------
        if side is 'L':
            cmds.connectAttr('%s_leg_stretchIK_AST.foreArmStretched' %side , '%s_IK_foot_JNT.translateX' %side, f=1)
            cmds.connectAttr('%s_leg_stretchIK_AST.upArmStretched' %side , '%s_IK_lowLeg_JNT.translateX' %side, f=1)
        else:
            lowLeg_reverse_MDL = cmds.createNode('multDoubleLinear', n = '%s_lowLeg_stretchIK_MDL' %side)
            leg_reverse_MDL = cmds.createNode('multDoubleLinear', n = '%s_leg_stretchIK_MDL' %side)
            cmds.setAttr('%s.input2' %lowLeg_reverse_MDL , -1)
            cmds.setAttr('%s.input2' %leg_reverse_MDL , -1)
            cmds.connectAttr('%s_leg_stretchIK_AST.foreArmStretched' %side , '%s.input1' %lowLeg_reverse_MDL, f=1)
            cmds.connectAttr('%s.output' %lowLeg_reverse_MDL , '%s_IK_foot_JNT.translateX' %side, f=1)
            cmds.connectAttr('%s_leg_stretchIK_AST.upArmStretched' %side , '%s.input1' %leg_reverse_MDL, f=1)
            cmds.connectAttr('%s.output' %leg_reverse_MDL , '%s_IK_lowLeg_JNT.translateX' %side, f=1)
            
        cmds.connectAttr('%s_leg_stretchIK_AST.stretchCtrlValueOut' %side , '%s.input1X' %legStretch_mult_ctrlVal, f=1)
        cmds.connectAttr('%s_leg_stretchIK_AST.stretchedLen' %side , '%s.input2X' %legStretch_mult_ctrlVal, f=1)
        cmds.connectAttr('%s.outputX' %legStretch_mult_ctrlVal, '%s_leg_stretchIK_output_LOC.tx' %side, f=1)
        cmds.connectAttr('%s_leg_softIK_AST.outputSoftik' %side, '%s_leg_softIK_output_LOC.tx' %side, f=1)

    def deleteUnusedNodeCmd(self):
        mm.eval('hyperShadePanelMenuCommand("hyperShadePanel1", "deleteUnusedNodes");')
        # delete turtle Node
        turtleNode = ['TurtleBakeLayerManager', 'TurtleDefaultBakeLayer', 'TurtleRenderOptions', 'TurtleUIOptions']
        rmanList = cmds.ls("rman*")
        rendermanList = cmds.ls("renderMan*")

        if rmanList or rendermanList:
            for rman in rmanList:
                cmds.delete(rman)
            for renderman in rendermanList:
                cmds.delete(renderman)
        for i in turtleNode:
            try:
                cmds.lockNode(i, lock=False)
                cmds.delete(i)
            except:
                pass
        
    def deleteUnknownNode(self):
        # unknownNode = cmds.ls(type = ("unknown", "unknownDag", "unknownTransform"))
        unknownNode = cmds.ls(type=("unknown"))
        for i in unknownNode:
            lockState = cmds.lockNode(i, q=True)[0]

            if lockState:
                cmds.lockNode(i, l=False)
        try:
            cmds.delete(unknownNode)
        except:
            pass

    def deleteAttr(self,side):
        cmds.deleteAttr('%s_IK_hand_CON' %side, at='stretchy')
        cmds.deleteAttr('%s_IK_hand_CON' %side, at='antiPop')
        cmds.deleteAttr('%s_IK_hand_CON' %side, at='lenght1')
        cmds.deleteAttr('%s_IK_hand_CON' %side, at='lenght2')
        cmds.deleteAttr('%s_IK_foot_CON' %side, at='stretchy')
        cmds.deleteAttr('%s_IK_foot_CON' %side, at='antiPop')
        cmds.deleteAttr('%s_IK_foot_CON' %side, at='lenght1')
        cmds.deleteAttr('%s_IK_foot_CON' %side, at='lenght2')
        try:
            self.deleteUnusedNodeCmd()
            self.deleteUnknownNode()
        except:
            pass
    
    def setHierachyGroup(self):
        motionLocator_list = [u'L_ref_upArm_LOC',
                             u'R_ref_upArm_LOC',
                             u'L_ref_leg_LOC',
                             u'R_ref_leg_LOC',
                             u'L_arm_init_space_NUL',
                             u'L_leg_init_space_NUL',
                             u'R_arm_init_space_NUL',
                             u'R_leg_init_space_NUL']
        asset_list = [u'L_arm_softIK_AST',
                     u'L_arm_stretchIK_AST',
                     u'L_leg_softIK_AST',
                     u'L_leg_stretchIK_AST',
                     u'R_arm_softIK_AST',
                     u'R_arm_stretchIK_AST',
                     u'R_leg_softIK_AST',
                     u'R_leg_stretchIK_AST']
        motionSysGrp = cmds.createNode('transform' , n='motionSystem_GRP')
        cmds.select(cl=1)
        assetGrp = cmds.createNode('transform' , n='asset_GRP')
        cmds.select(cl=1)
        cmds.parent(motionSysGrp , 'auxillary_GRP')
        cmds.parent(assetGrp , 'auxillary_GRP')
        cmds.parent(motionLocator_list,motionSysGrp)
        cmds.parent(asset_list , assetGrp)
        cmds.hide(motionLocator_list)
        cmds.hide(assetGrp)
        

#ssIK = softStretchIKSet()
#ssIK.setSoftIK()

