#######################################################################################################################
#                                                                                                                     #
#  propRigTool_v02                                                                                                    #
#   - lineWidth
#   - 30. Jan. 2020.                                                                                                  #
#                                                                                                                     #
#######################################################################################################################

import maya.cmds as cmds

def control_lineWidth (lw) :
    lw = cmds.floatField ('lw', q = 1, v = 1)
    sel = cmds.ls ( sl = 1 )
    for c in range ( len ( sel ) ) :
        selShape = cmds.listRelatives ( sel[c], s = 1)
        cmds.setAttr ( ' %s.lineWidth ' %selShape[0], lw )



    
