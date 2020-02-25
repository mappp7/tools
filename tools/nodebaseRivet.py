import maya.cmds as cmds
import maya.mel as mel

baseMesh = cmds.ls( sl=True )[0]
targetObject = cmds.ls( sl=True )

baseMeshShape = cmds.listRelatives( baseMesh, s=True )[0]

for i in range(len(targetObject)):
    print i
    # Create Node
    edgeIfo1Node = cmds.createNode( 'curveFromMeshEdge' )
    edgeIfo2Node = cmds.createNode( 'curveFromMeshEdge' )
    loftNode = cmds.createNode( 'loft' )
    surfaceInfoNode = cmds.createNode( 'pointOnSurfaceInfo' )
    fbfMatrixNode = cmds.createNode( 'fourByFourMatrix' )
    deComMatrixNode = cmds.createNode( 'decomposeMatrix' )
    #temp
    deComMatrixNodeTarget = cmds.createNode( 'decomposeMatrix' )
    clPoOnSurf = cmds.createNode( 'closestPointOnSurface' )
    
    clPoOnMesh = cmds.createNode( 'closestPointOnMesh' )
    
    # ConnectAttr
    cmds.connectAttr( '%s.worldMesh[0]' % baseMeshShape, '%s.inputMesh' % edgeIfo1Node )
    cmds.connectAttr( '%s.worldMesh[0]' % baseMeshShape, '%s.inputMesh' % edgeIfo2Node )
    cmds.connectAttr( '%s.outputCurve' % edgeIfo1Node, '%s.inputCurve[0]' % loftNode )
    cmds.connectAttr( '%s.outputCurve' % edgeIfo2Node, '%s.inputCurve[1]' % loftNode )
    
    cmds.connectAttr( '%s.outputSurface' % loftNode, '%s.inputSurface' % surfaceInfoNode )
    
    cmds.connectAttr( '%s.positionX' % surfaceInfoNode, '%s.in30' % fbfMatrixNode )
    cmds.connectAttr( '%s.positionY' % surfaceInfoNode, '%s.in31' % fbfMatrixNode )
    cmds.connectAttr( '%s.positionZ' % surfaceInfoNode, '%s.in32' % fbfMatrixNode )
    
    cmds.connectAttr( '%s.normalX' % surfaceInfoNode, '%s.in00' % fbfMatrixNode )
    cmds.connectAttr( '%s.normalY' % surfaceInfoNode, '%s.in01' % fbfMatrixNode )
    cmds.connectAttr( '%s.normalZ' % surfaceInfoNode, '%s.in02' % fbfMatrixNode )
    
    cmds.connectAttr( '%s.tangentUx' % surfaceInfoNode, '%s.in10' % fbfMatrixNode )
    cmds.connectAttr( '%s.tangentUy' % surfaceInfoNode, '%s.in11' % fbfMatrixNode )
    cmds.connectAttr( '%s.tangentUz' % surfaceInfoNode, '%s.in12' % fbfMatrixNode )
    
    cmds.connectAttr( '%s.tangentVx' % surfaceInfoNode, '%s.in20' % fbfMatrixNode )
    cmds.connectAttr( '%s.tangentVy' % surfaceInfoNode, '%s.in21' % fbfMatrixNode )
    cmds.connectAttr( '%s.tangentVz' % surfaceInfoNode, '%s.in22' % fbfMatrixNode )
    
    cmds.connectAttr( '%s.output' % fbfMatrixNode, '%s.inputMatrix' % deComMatrixNode )
    
    # get UV connection
    cmds.connectAttr( '%s.worldMatrix[0]' % targetObject[i], '%s.inputMatrix' % deComMatrixNodeTarget )
    cmds.connectAttr( '%s.outputTranslate' % deComMatrixNodeTarget, '%s.inPosition' % clPoOnSurf )
    cmds.connectAttr( '%s.outputSurface' % loftNode, '%s.inputSurface' % clPoOnSurf )
    
    cmds.connectAttr( '%s.parameterU' % clPoOnSurf, '%s.parameterU' % surfaceInfoNode )
    cmds.connectAttr( '%s.parameterV' % clPoOnSurf, '%s.parameterV' % surfaceInfoNode )
    
    
    # get face To edeg
    
    cmds.connectAttr( '%s.outputTranslate' % deComMatrixNodeTarget, '%s.inPosition' % clPoOnMesh )
    cmds.connectAttr( '%s.worldMesh[0]' % baseMeshShape, '%s.inMesh' % clPoOnMesh )
    
    closestFaceIndex = cmds.getAttr( '%s.closestFaceIndex' % clPoOnMesh )
    
    
    
    
    
    
    cmds.select( cl=True )
    cmds.select( '%s.f[%s]' % ( baseMesh, closestFaceIndex )  )
    mel.eval('ConvertSelectionToVertices;')
    vtxList = cmds.ls( sl=True, fl=True )
    
    if len( vtxList ) == 3:
        cmds.select( cl=True )
        cmds.select( '%s.f[%s]' % ( baseMesh, closestFaceIndex )  )
        mel.eval('ConvertSelectionToEdges;')
        selEdeg = cmds.ls(sl=True, fl=True)
        cmds.select( cl=True )
        
        getEdeg = selEdeg[::2]
        cmds.select(getEdeg)
        
        get1EdegId = int( getEdeg[0].split('.e[')[1].split(']')[0] )
        get2EdegId = int( getEdeg[1].split('.e[')[1].split(']')[0] )
        
        cmds.setAttr( '%s.edgeIndex[0]' % edgeIfo1Node, get1EdegId )
        cmds.setAttr( '%s.edgeIndex[0]' % edgeIfo2Node, get2EdegId )
        
        
    
    if len( vtxList ) == 4:
        cmds.select( cl=True )
        cmds.select( '%s.f[%s]' % ( baseMesh, closestFaceIndex )  )
        faceCenterP = faceCenter()
        fcLocaor = cmds.spaceLocator()[0]
        cmds.move( faceCenterP[1:][0], faceCenterP[1:][1], faceCenterP[1:][2], fcLocaor )
        
        #cmds.select( '%s.f[%s]' % ( baseMesh, closestFaceIndex )  )
        #mel.eval('ConvertSelectionToVertices;')
        #vtxList = cmds.ls( sl=True, fl=True )
        
        
        
        nearestVtxList = nearestObject( fcLocaor, vtxList )
        cmds.select( nearestVtxList[0::3] )
        mel.eval('ConvertSelectionToContainedEdges;')
        get1Edeg = cmds.ls( sl=True )[0]
        get1EdegId = int( get1Edeg.split('.e[')[1].split(']')[0] )
        cmds.select( cl=True )
        
        
        cmds.select( nearestVtxList[1:-1] )
        mel.eval('ConvertSelectionToContainedEdges;')
        get2Edeg = cmds.ls( sl=True )[0]
        get2EdegId = int( get2Edeg.split('.e[')[1].split(']')[0] )
        cmds.select( cl=True )
        
        
        
        
        
        cmds.setAttr( '%s.edgeIndex[0]' % edgeIfo1Node, get1EdegId )
        cmds.setAttr( '%s.edgeIndex[0]' % edgeIfo2Node, get2EdegId )
        
        cmds.delete( fcLocaor )
        
    else:
        print 'polygon!!!!!!!!'
    
    
    
    
    rivetTransform = cmds.createNode( 'transform', n='rivet' )
    cmds.connectAttr( '%s.outputTranslate' % deComMatrixNode, '%s.translate' % rivetTransform )
    cmds.connectAttr( '%s.outputRotate' % deComMatrixNode, '%s.rotate' % rivetTransform )
    
    
    
    
    # clean up node
    
    cmds.disconnectAttr( '%s.parameterU' % clPoOnSurf, '%s.parameterU' % surfaceInfoNode )
    cmds.disconnectAttr( '%s.parameterV' % clPoOnSurf, '%s.parameterV' % surfaceInfoNode )
    cmds.delete( deComMatrixNodeTarget, clPoOnSurf, clPoOnMesh )
    
    
    
    
    
    # attach target
    cmds.parentConstraint( rivetTransform, targetObject[i], mo=True )
    cmds.scaleConstraint( rivetTransform, targetObject[i], mo=True )








































# script that returns the center point of selected polygon faces. 
# owen burgess 2009

import maya.OpenMaya as OpenMaya
import math

def faceCenter():

    faceCenter = []

    selection = OpenMaya.MSelectionList()
    OpenMaya.MGlobal.getActiveSelectionList(selection)
    print ("Number of objects in selection: %s " % selection.length())

    iter = OpenMaya.MItSelectionList (selection, OpenMaya.MFn.kMeshPolygonComponent)

    while not iter.isDone():
        #status = OpenMaya.MStatus
        dagPath = OpenMaya.MDagPath()
        component = OpenMaya.MObject()

        iter.getDagPath(dagPath, component)

        polyIter = OpenMaya.MItMeshPolygon(dagPath, component)

        while not polyIter.isDone():

            i = 0
            i = polyIter.index()
            faceInfo = [0]
            faceInfo[0] = ("The center point of face %s is:" %i)
            faceCenter+=faceInfo

            center = OpenMaya.MPoint
            center = polyIter.center(OpenMaya.MSpace.kWorld)
            point = [0.0,0.0,0.0]
            point[0] = center.x
            point[1] = center.y
            point[2] = center.z
            faceCenter += point
            
            polyIter.next()
            
        iter.next()
        
    return faceCenter
# end of script

def getDistance( pos1, pos2 ):
    distance = ( ( pos1[0] - pos2[0] ) **2 + ( pos1[1] - pos2[1] ) **2 + ( pos1[2] - pos2[2] ) **2 ) **0.5
    distance = round( distance, 4 )
    return distance

def nearestObject( base, objList ):
    nDisList = []
    disList = []
    for x in range( len( objList ) ):
        basePos = cmds.xform( base, ws=True, t=True, q=True )
        pos = cmds.xform( objList[x], ws=True, t=True, q=True )
        dis = getDistance( basePos, pos )
        print str(dis) + ' : ' + objList[x]
        disList.append( dis )
    for i in range( len( disList ) ):
        if len( disList ) != 0:
            disIndex = disList.index( min( disList ) )
            nDisList.append( objList[ disIndex ] )
            #print objList[ disIndex ]
            del disList[ disIndex ]
            del objList[ disIndex ]
            
    return nDisList
