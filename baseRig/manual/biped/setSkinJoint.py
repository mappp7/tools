#encoding:utf-8
#==============================
#
#
#==============================

import maya.cmds as cmds
import maya.mel as mel
from baseRig.util.defaultGroupNode import*
from baseRig.util.setUniqueName import*
from baseRig.util.homeNul import*
from baseRig.util.zeroOut import*

class setSkinJoint():

    def __init__(self):
        z=defaultGroupNode()
        z.createGroupNode()

        return


    def set(self):

        list= cmds.ls('*Blend*JNT*',typ='joint')

        skinJoints=[]

        for e in list:
            if cmds.objExists (e.replace('Blend','Skin')) is not True:

                tmp= cmds.createNode ('joint',n= e.replace('Blend','Skin'))
		cmds.delete(cmds.parentConstraint (e,tmp,w= True))
		z=zeroOut()
		z.zeroOutJoint(tmp)
                cmds.parentConstraint (e,tmp,w= True)
                cmds.parent (tmp,'SkinJoint_GRP')
                skinJoints.append(tmp)
            else:
                continue


        return skinJoints
