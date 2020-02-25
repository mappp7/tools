#encoding:utf-8
#==============================
#리깅에 필요한 디폴트 그룹을 만든다.
#
#==============================

import maya.cmds as cmds
import maya.mel as mel
from util.controller import *

class defaultGroupNode():

    def __init__(self):
        self.Color = { 'red':13, 'blue':6, 'yellow':17 , 'peach':20 }

    def createGroupNode(self):

        if cmds.objExists ('rig_GRP') is False:
            cmds.group (n= 'rig_GRP',empty= True)
            #cmds.addAttr ('rig_GRP',ln ='allControls', dt ='stringArray')
            #cmds.setAttr ('rig_GRP.allControls', type='stringArray',
            #*([len(['place_CON','direction_CON','move_CON','root_CON'])]
            #+ ['place_CON','direction_CON','move_CON','root_CON']))


        if cmds.objExists ('place_NUL') is False:
            cmds.group (n= 'place_NUL',empty= True)
            cmds.parent('place_NUL','rig_GRP')

        if cmds.objExists ('place_CON') is False:
            cmds.circle (n= 'place_CON',d =3,r=6,nr=[0,1,0],ch=False)
            cmds.parent('place_CON','place_NUL')

            # Global Scale connection
            cmds.addAttr( 'place_CON', ln='globalScale', at='double', dv=1, k=True )

            # cmds.connectAttr( 'place_CON.globalScale', 'place_CON.scaleX' )
            # cmds.connectAttr( 'place_CON.globalScale', 'place_CON.scaleY' )
            # cmds.connectAttr( 'place_CON.globalScale', 'place_CON.scaleZ' )



        if cmds.objExists ('direction_NUL') is False:
            cmds.group (n= 'direction_NUL',empty= True)
            cmds.parent('direction_NUL','place_CON')

        if cmds.objExists ('direction_CON') is False:
            cmds.circle (n= 'direction_CON',d =3,r=5.5,nr=[0,1,0],ch=False)
            cmds.parent('direction_CON','direction_NUL')

        if cmds.objExists ('move_NUL') is False:
            cmds.group (n= 'move_NUL',empty= True)
            cmds.parent('move_NUL','direction_CON')

        if cmds.objExists ('move_CON') is False:
            cmds.circle (n= 'move_CON',d =3,r=5,nr=[0,1,0],ch=False)
            cmds.parent('move_CON','move_NUL')

        if cmds.objExists ('root_NUL') is False:
            cmds.group (n= 'root_NUL',empty= True)
            #cmds.parent('root_NUL','move_CON')

        if cmds.objExists ('root_CON') is False:
            controllerShape('root_CON','root','yellow')
            cmds.parent('root_CON','root_NUL')

        if cmds.objExists ('transform_GRP') is False:
            cmds.group (n= 'transform_GRP',empty= True)
            cmds.parent('transform_GRP','rig_GRP')

        if cmds.objExists ('control_GRP') is False:
            cmds.group (n= 'control_GRP',empty= True)
            cmds.parent('control_GRP','transform_GRP')
            cmds.parent('root_NUL','control_GRP')

        if cmds.objExists ('IKControl_GRP') is False:
            cmds.group (n= 'IKControl_GRP',empty= True)
            cmds.parent('IKControl_GRP','control_GRP')

        if cmds.objExists ('FKControl_GRP') is False:
            cmds.group (n= 'FKControl_GRP',empty= True)
            cmds.parent('FKControl_GRP','control_GRP')

        if cmds.objExists ('otherControl_GRP') is False:
            cmds.group (n= 'otherControl_GRP',empty= True)
            cmds.parent('otherControl_GRP','control_GRP')

        if cmds.objExists ('joint_GRP') is False:
            cmds.group (n= 'joint_GRP',empty= True)
            cmds.parent('joint_GRP','transform_GRP')

        if cmds.objExists ('templateJoint_GRP') is False:
            cmds.group (n= 'templateJoint_GRP',empty= True)
            cmds.parent('templateJoint_GRP','joint_GRP')

        if cmds.objExists ('IKJoint_GRP') is False:
            cmds.group (n= 'IKJoint_GRP',empty= True)
            cmds.setAttr ('IKJoint_GRP.v',0)
            cmds.parent('IKJoint_GRP','joint_GRP')

        if cmds.objExists ('FKJoint_GRP') is False:
            cmds.group (n= 'FKJoint_GRP',empty= True)
            cmds.setAttr ('FKJoint_GRP.v',0)
            cmds.parent('FKJoint_GRP','joint_GRP')

        if cmds.objExists ('BlendJoint_GRP') is False:
            cmds.group (n= 'BlendJoint_GRP',empty= True)
            cmds.setAttr ('BlendJoint_GRP.v',0)
            cmds.parent('BlendJoint_GRP','joint_GRP')

        if cmds.objExists ('SkinJoint_GRP') is False:
            cmds.group (n= 'SkinJoint_GRP',empty= True)
            cmds.parent('SkinJoint_GRP','joint_GRP')

        if cmds.objExists ('attach_GRP') is False:
            cmds.group (n= 'attach_GRP',empty= True)
            cmds.setAttr ('attach_GRP.v',0)
            cmds.parent('attach_GRP','transform_GRP')

        if cmds.objExists ('space_GRP') is False:
            cmds.group (n= 'space_GRP',empty= True)
            cmds.setAttr ('space_GRP.v',0)
            cmds.parent('space_GRP','transform_GRP')

        if cmds.objExists ('stretchy_GRP') is False:
            cmds.group (n= 'stretchy_GRP',empty= True)
            cmds.setAttr ('stretchy_GRP.v',0)
            cmds.parent('stretchy_GRP','transform_GRP')

        if cmds.objExists ('twist_GRP') is False:
            cmds.group (n= 'twist_GRP',empty= True)
            cmds.setAttr ('twist_GRP.v',0)
            cmds.parent('twist_GRP','transform_GRP')

        if cmds.objExists ('roll_GRP') is False:
            cmds.group (n= 'roll_GRP',empty= True)
            cmds.setAttr ('roll_GRP.v',0)
            cmds.parent('roll_GRP','transform_GRP')

        if cmds.objExists ('noneFlip_GRP') is False:
            cmds.group (n= 'noneFlip_GRP',empty= True)
            cmds.setAttr ('noneFlip_GRP.v',0)
            cmds.parent('noneFlip_GRP','transform_GRP')

        if cmds.objExists ('noneTransform_GRP') is False:
            cmds.group (n= 'noneTransform_GRP',empty= True)
            cmds.parent('noneTransform_GRP','rig_GRP')

        if cmds.objExists ('geometry_GRP') is False:
            cmds.group (n= 'geometry_GRP',empty= True)
            cmds.parent('geometry_GRP','noneTransform_GRP')

        if cmds.objExists ('auxillary_GRP') is False:
            cmds.group (n= 'auxillary_GRP',empty= True)
            cmds.setAttr ('auxillary_GRP.v',0)
            cmds.parent('auxillary_GRP','noneTransform_GRP')

        #Set Controller Color
        #Color = { 'red':12, 'blue':6, 'yellow':17 , 'peach':20 }
        cmds.setAttr('%s.overrideEnabled' % 'move_CON', 1)
        cmds.setAttr('%s.overrideColor' % 'move_CON', self.Color['red'])

        cmds.setAttr('%s.overrideEnabled' % 'direction_CON', 1)
        cmds.setAttr('%s.overrideColor' % 'direction_CON', self.Color['yellow'])

        cmds.setAttr('%s.overrideEnabled' % 'place_CON', 1)
        cmds.setAttr('%s.overrideColor' % 'place_CON', self.Color['blue'])
