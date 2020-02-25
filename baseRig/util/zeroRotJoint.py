import maya.cmds as cmds

def zeroRotJoint( jointList ):
    
    for x in range( len(jointList) ):
        
        oX = cmds.getAttr( '%s.rotateX' % jointList[x] )
        oY = cmds.getAttr( '%s.rotateY' % jointList[x] )
        oZ = cmds.getAttr( '%s.rotateZ' % jointList[x] )
            
        cmds.setAttr( '%s.jointOrientX' % jointList[x], oX )
        cmds.setAttr( '%s.jointOrientY' % jointList[x], oY )
        cmds.setAttr( '%s.jointOrientZ' % jointList[x], oZ )
        
        cmds.setAttr( '%s.rotateX' % jointList[x], 0 )
        cmds.setAttr( '%s.rotateY' % jointList[x], 0 )
        cmds.setAttr( '%s.rotateZ' % jointList[x], 0 )