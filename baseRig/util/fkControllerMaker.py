import maya.cmds as cmds
from util.controller import*
from util.homeNul import*
from util.snap import*

# fkControllerMaker( 'cube', 'yellow', [LIST] )
                             # colorShape ==> ( 'red', 'blue', 'yellow' )
def fkControllerMaker( conSahpe, colorShape, target ):
    
    conList = []
    constraintList = []
    nulList = []
    
    for x in range( len(target) ):
        controllerName = controllerShape( target[x].split('_JNT')[0]  + '_CON', conSahpe, colorShape )
        POsnap( controllerName, target[x] )
        
        PC = cmds.parentConstraint( controllerName, target[x] )
        
        conList.append( controllerName )
        constraintList.append( PC[0] )
        
    for i in range(len(conList)-1):
        cmds.parent( conList[i+1], conList[i] )
        
    for e in conList: 
        NUL = homeNul( e )
        nulList.append( NUL )
        
    return conList, nulList, constraintList
