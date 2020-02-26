#encoding=utf-8

import maya.cmds as cmds

## pairBlend ##
# createPairBlendNode( 'joint1', 'joint3', 'joint2', 'test_PBD', 'translate', 'rotate' )
def createPairBlendNode( fistObject, secondObject, lastObject, NAME, *attrs ):
    pairBlendNode = cmds.createNode( 'pairBlend', n=NAME )
    if cmds.objExists( fistObject ):
        for x in range(len(attrs)):
            
            shapeNode = cmds.listRelatives( fistObject, s=True )
            if cmds.nodeType( fistObject ) == 'joint':
                cmds.connectAttr( '%s.%s' % (fistObject, attrs[x]), '%s.in%s1' % (pairBlendNode, attrs[x].capitalize()) )
            else:
                if shapeNode != None:
                    cmds.connectAttr( '%s.%s' % (fistObject, attrs[x]), '%s.in%s1' % (pairBlendNode, attrs[x].capitalize()) )
                if shapeNode == None:
                    cmds.connectAttr( '%s.output%s' % (fistObject, attrs[x].capitalize()), '%s.in%s1' % (pairBlendNode, attrs[x].capitalize()) )
                
            shapeNode = cmds.listRelatives( secondObject, s=True )
            if cmds.nodeType( secondObject ) == 'joint':
                cmds.connectAttr( '%s.%s' % (secondObject, attrs[x]), '%s.in%s2' % (pairBlendNode, attrs[x].capitalize()) )
            else:
                if shapeNode != None:
                    cmds.connectAttr( '%s.%s' % (secondObject, attrs[x]), '%s.in%s2' % (pairBlendNode, attrs[x].capitalize()) )
                    
                if shapeNode == None:
                    cmds.connectAttr( '%s.output%s' % (secondObject, attrs[x].capitalize()), '%s.in%s2' % (pairBlendNode, attrs[x].capitalize()) )
                
                
            cmds.connectAttr( '%s.out%s' % (pairBlendNode, attrs[x].capitalize()), '%s.%s' % (lastObject,attrs[x]) )
    return pairBlendNode
"""
#encoding=utf-8

import maya.cmds as cmds

## pairBlend ##
# createPairBlendNode( 'pCube1', 'pCube2', 'pCube3', 'test_PBD', 'translate', 'rotate' )
def createPairBlendNode( fistObject, secondObject, lastObject, NAME, *attrs ):
    pairBlendNode = cmds.createNode( 'pairBlend', n=NAME )
    if cmds.objExists( fistObject ):
        for x in range(len(attrs)):
            
            shapeNode = cmds.listRelatives( fistObject, s=True )
            if shapeNode != None:
                cmds.connectAttr( '%s.%s' % (fistObject, attrs[x]), '%s.in%s1' % (pairBlendNode, attrs[x].capitalize()) )
            if shapeNode == None:
                cmds.connectAttr( '%s.output%s' % (fistObject, attrs[x].capitalize()), '%s.in%s1' % (pairBlendNode, attrs[x].capitalize()) )
                
            shapeNode = cmds.listRelatives( secondObject, s=True )
            if shapeNode != None:
                cmds.connectAttr( '%s.%s' % (secondObject, attrs[x]), '%s.in%s2' % (pairBlendNode, attrs[x].capitalize()) )
                
            if shapeNode == None:
                cmds.connectAttr( '%s.output%s' % (secondObject, attrs[x].capitalize()), '%s.in%s2' % (pairBlendNode, attrs[x].capitalize()) )
                
                
            cmds.connectAttr( '%s.out%s' % (pairBlendNode, attrs[x].capitalize()), '%s.%s' % (lastObject,attrs[x]) )
    return pairBlendNode
"""