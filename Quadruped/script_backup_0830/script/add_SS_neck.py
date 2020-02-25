import maya.cmds as cmds


def add_SS_neckOP():
    
    ik = 'C_IK_neck_HDL'
    
    jointList = [ 'C_IK_neck1_JNT', 'C_IK_neck2_JNT', 'C_IK_neck3_JNT', 'C_IK_neck4_JNT', 'C_IK_neck5_JNT', 'C_IK_neck6_JNT' ]
    
    globalController = 'place_CON'
    
    
    if 'ikSplineSolver' == cmds.ikHandle( ik, solver=True, q=True ):
        print ik
        # curve
        ikCRV = []
        
        cList=cmds.listConnections( ik, c=True )
        for x in range( len( cList ) ):
            if 'CRV' in cList[x].split( '_' ):
                print cList[x]
                ikCRV.append( cList[x] )
        curveInfo = cmds.arclen( ikCRV[0], ch=True )
        cInfoName = cmds.rename( curveInfo, ikCRV[0].replace( 'CRV', 'CIF' ) )
        ikCurveLength = cmds.getAttr( '%s.arcLength' % cInfoName )
        print 'curve length' + ' : ' + str( ikCurveLength )
        
        # joint
        jointXform = [ 0 ]
        for x in jointList[1:]:
            xValue = cmds.getAttr( '%s.translateX' % x )
            jointXform.append( xValue )
        
        jointLength = sum( jointXform )
        print 'joint length' + ' : ' + str( jointLength )
        
        # divide length
        locatorShapeList = []
        
        for x in range( len( jointList ) ):
            print x
            # create pointOnCurveInfo
            POCI = cmds.createNode( 'pointOnCurveInfo', name=( 'pointOnCurveInfo%s_POINTONCURVEINFO' % (x+1) ) )
            print POCI
            LOC = cmds.spaceLocator( name='%s%s_LOC' % ( ikCRV[0].replace( 'CRV', 'stCRV' ), (x+1)) )
            LOCShape = cmds.listRelatives( LOC[0] )
            locatorShapeList.append( LOCShape[0] )
            print locatorShapeList
            
            cmds.setAttr('%s.template' % LOC[0], 1)
            print LOC
            
            cmds.connectAttr( '%s.position' % POCI, '%s.translate' % LOC[0] )
            cmds.connectAttr( '%s.worldSpace[0]' % cmds.listRelatives( ikCRV[0] )[0], '%s.inputCurve' % POCI )
            
            cmds.setAttr( '%s.parameter' % POCI, x*jointXform[x] )
            
        for x in range( len( jointList ) - 1 ):
            # create node & connections
            DB = cmds.createNode( 'distanceBetween', name='distanceBetween%s_DIS' % (x+1) )
            print DB
            cmds.connectAttr( '%s.worldPosition[0]' % locatorShapeList[ 0:len( jointList ) ][x], '%s.point1' % DB )
            cmds.connectAttr( '%s.worldPosition[0]' % locatorShapeList[ 1:len( jointList ) ][x], '%s.point2' % DB )
            
            wMD = cmds.createNode( 'multiplyDivide', name='globalScaleDivide%s_MPD' % (x+1) )
            cmds.setAttr( '%s.operation' % wMD, 2 )
            
            dMD = cmds.createNode( 'multiplyDivide', name='lengthDivide%s_MPD' % (x+1) )
            cmds.setAttr( '%s.operation' % dMD, 2 )
            cmds.setAttr( '%s.input2X' % dMD, jointXform[x+1] )
            """
            cMD = cmds.createNode( 'multiplyDivide', name='stretchControl%s_MPD' % (x+1) )
            cmds.setAttr( '%s.operation' % cMD, 1 )
    
            cndi = cmds.createNode( 'condition', name='stretchControl%s_CND' % (x+1) )
            cmds.setAttr( '%s.secondTerm' % cndi, 1 )
            cmds.setAttr( '%s.colorIfFalseR' % cndi, 1 )
            cmds.setAttr( '%s.operation' % cndi, 3 )
            """
            #
            cmds.connectAttr( '%s.distance' % DB, '%s.input1X' % wMD )
            cmds.connectAttr( '%s.globalScale' % globalController, '%s.input2X' % wMD )
            
            cmds.connectAttr( '%s.outputX' % wMD, '%s.input1X' % dMD )
            """
            ### setRange
            #cmds.connectAttr( '%s.stretchIk' % animController, '%s.input1X' % cMD ) # value = 0 ~ 1
            cmds.connectAttr( '%s.outputX' % dMD, '%s.input2X' % cMD )
            
            cmds.connectAttr( '%s.outputX' % cMD, '%s.firstTerm' % cndi )
            cmds.connectAttr( '%s.outputX' % cMD, '%s.colorIfTrueR' % cndi )
            """
            # joint connections
            cmds.connectAttr( '%s.outputX' % dMD, '%s.scaleX' % jointList[x] )
            """
            if cmds.objExists( '%sStretch_RNG' % jointList[0].split('_')[-2][:-1] ):
                cmds.connectAttr( '%s.outValueX' % sRNG, '%s.input1X' % cMD )
            else:
                ### setRange ##  # value = 0 ~ 10    
                sRNG = cmds.createNode( 'setRange', n='%sStretch_RNG' % jointList[0].split('_')[-2][:-1] )
                cmds.setAttr( '%s.minX' % sRNG, 0 )
                cmds.setAttr( '%s.maxX' % sRNG, 1 )
                cmds.setAttr( '%s.oldMinX' % sRNG, 0 )
                cmds.setAttr( '%s.oldMaxX' % sRNG, 10 )
                cmds.connectAttr( '%s.stretchIk' % animController, '%s.valueX' % sRNG )  
                cmds.connectAttr( '%s.outValueX' % sRNG, '%s.input1X' % cMD )  
            """
    

