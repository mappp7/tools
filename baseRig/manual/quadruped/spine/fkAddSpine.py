from util.fkControllerMaker import *
from util.snap import *
from util.homeNul import *
from util.attach import *

fkSpineJointList = [ 'C_FKsub_spine1_NUL', 'C_FKsub_spine2_NUL', 'C_FKsub_spine3_NUL', 'C_FKsub_chest_NUL' ]

fkControllerMaker( 'circle', 'yellow', fkSpineJointList[1:3] )

homeNul( 'C_IK_upBody_CON', 'C_IK_upBody_fkSubAttach_NUL' )

cmds.parentConstraint( 'C_IK_lowBodySub_CON', fkSpineJointList[0], mo=True )

attachNode( 'C_FKsub_chest_NUL', 'C_IK_upBody_fkSubAttach_NUL', 'translate', 'rotate', 'scale', 'shear' )

attachPart( 'C_IK_root_CON', 'C_FKsub_spine2_NUL_NUL', 'translate', 'rotate', 'scale', 'shear' )