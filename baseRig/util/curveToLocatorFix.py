import maya.cmds as cmds

def curveToLocatorFix( curveObject ):
    spineCurve = curveObject#cmds.ls( selection = True )
    
    spineCurveShape = cmds.listRelatives(spineCurve,s=1)
    spans = cmds.getAttr(spineCurveShape[0]+'.spans')
    degree = cmds.getAttr(spineCurveShape[0]+'.degree')
    cvCount = range(spans + degree)
    
    locatorList = []
    
    for cv in range(len(cvCount)):
        print cv
        cvPosition = cmds.pointPosition( '%s.cv[%s]' % (spineCurve, cv) )
        #controller = controller( 'path%s_CON' % cv, 'cube', 'yellow' )
        
        curveN = curveObject.split('1_')
        nodeName = curveN[-1].replace( curveN[-1], 'LOC' )

        locator = cmds.spaceLocator( n='%s%s_%s' % ( curveN[0], str(cv+1), nodeName ) )
        locatorList.append(locator[0])
        
        cmds.move( cvPosition[0],cvPosition[1],cvPosition[2] )
        
        # matrix connetion
        MMX = cmds.createNode( 'multMatrix', name=locator[0].replace( locator[0].split('_')[-1], 'MMX' ) )
        DCM = cmds.createNode( 'decomposeMatrix', name=locator[0].replace( locator[0].split('_')[-1], 'DCM' ) )
        
        cmds.connectAttr( '%s.worldInverseMatrix[0]' % spineCurve, '%s.matrixIn[1]' % MMX )
        cmds.connectAttr( '%s.worldMatrix[0]' % locator[0], '%s.matrixIn[0]' % MMX )
        cmds.connectAttr( '%s.matrixSum' % MMX, '%s.inputMatrix' % DCM )
        cmds.connectAttr( '%s.outputTranslate' % DCM, '%s.controlPoints[%s]' % (spineCurveShape[0], cv) )
        
    return locatorList