import maya.cmds as cmds
import maya.mel as mel


def autoSmothSkin( influenceJointList, localIterator, globalIterator ):

    mel.eval( 'ArtPaintSkinWeightsToolOptions;')
    mel.eval( 'artAttrPaintOperation artAttrSkinPaintCtx Smooth; ' )
    
    for x in range( globalIterator ):
        print x
        for x in range( len( skinJointList ) - 1 ):
            mel.eval( 'artSkinInflListChanging "%s" 0;' % skinJointList[x] )
            mel.eval( 'artSkinInflListChanging "%s" 1;' % skinJointList[x+1] )
            mel.eval( 'artSkinInflListChanged artAttrSkinPaintCtx;' )
        
            for x in range( localIterator ):
                mel.eval('artAttrSkinPaintCtx -e -clear `currentCtx`;')
        
        skinJointList.reverse()  
        for x in range( len( skinJointList ) - 1 ):
            mel.eval( 'artSkinInflListChanging "%s" 0;' % skinJointList[x] )
            mel.eval( 'artSkinInflListChanging "%s" 1;' % skinJointList[x+1] )
            mel.eval( 'artSkinInflListChanged artAttrSkinPaintCtx;' )
        
            for x in range( localIterator ):
                mel.eval('artAttrSkinPaintCtx -e -clear `currentCtx`;')




skinMesh = cmds.ls( sl=True )


for x in range( len(skinMesh) ):
    skinMeshShape = cmds.listRelatives( skinMesh[x], s=True, ni=True )
    skinClusterNode = cmds.listConnections( skinMeshShape, type='skinCluster' )

    skinJointList = cmds.skinCluster( skinClusterNode[0], q=True, influence=True )
    
    cmds.select( cl=True )
    
    cmds.select( skinMesh[x] )
    
    autoSmothSkin( skinJointList, 5, 1 )
    
    cmds.select( cl=True )