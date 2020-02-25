#######################################################################################################################
#                                                                                                                     #
#  propRigTool_v02                                                                                                    #
#   - lock and hide channel ( scale, visibility )                                                                     #
#   - 30. Jan. 2020.                                                                                                  #
#                                                                                                                     #
#######################################################################################################################

import maya.cmds as cmds
import site
site.addsitedir('/dexter/Cache_DATA/CRT/riggingTeamShelf/propRigTool/propRigTool_v02_set')


def organizeChannelBox () :
    cmds.select ('*_CON')
    cmds.select ('place_CON', 'direction_CON', 'move_CON', deselect=1)
    selected_CON = cmds.ls(sl=1)
    for LnH in selected_CON :
        cmds.setAttr ('%s.sx' %LnH, lock=True, keyable=False)
        cmds.setAttr ('%s.sy' %LnH, lock=True, keyable=False)
        cmds.setAttr ('%s.sz' %LnH, lock=True, keyable=False)
        cmds.setAttr ('%s.v' %LnH, lock=True, keyable=False) 
