from util.fkControllerMaker import *
from util.snap import *
from util.homeNul import *
from util.attach import *


def fkAddNeckOP():
    
    fkSpineJointList = [ 'C_FK_neck1_NUL', 'C_FK_neck2_NUL', 'C_FK_neck3_NUL', 'C_FK_head_NUL' ]
    
    fkControllerMaker( 'circle', 'yellow', fkSpineJointList[1:3] )
    
    homeNul( 'C_IK_head_CON', 'C_IK_head_extra_NUL' )
    
    cmds.parentConstraint( 'C_IK_neck1Sub_CON', fkSpineJointList[0], mo=True )
    
    attachNode( 'C_FK_head_NUL', 'C_IK_head_extra_NUL', 'translate', 'rotate', 'scale', 'shear' )
    
    attachPart( 'C_IK_neck1_CON', 'C_FK_neck2_NUL', 'translate', 'rotate', 'scale', 'shear' )
    
    cmds.parent ( 'C_FK_neck1_NUL', w=1 )

