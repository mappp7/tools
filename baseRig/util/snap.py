#encoding=utf-8

import maya.cmds as cmds

## SNAP ##        
def POsnap( object, targetObject ):
    cmds.delete( cmds.parentConstraint( targetObject, object ) )
    
def Psnap( object, targetObject ):
    cmds.delete( cmds.pointConstraint( targetObject, object, offset=(0, 0, 0), weight=1 ) )
    
def Osnap( object, targetObject ):
    cmds.delete( cmds.orientConstraint( targetObject, object, offset=(0, 0, 0), weight=1 ) )
