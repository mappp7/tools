#encoding:utf-8
#==============================
#
#
#==============================
import maya.cmds as cmds
import maya.mel as mel
from baseRig.util.fkControllerMaker import*

class zeroOut():
    '''
    Translate/Rotate를 zero out한다.
    '''
    def __init__(self):

        return

    def zeroOutJoint(self,jnt):
        pnt=cmds.spaceLocator (n='parent_locator')
        chd=cmds.spaceLocator (n='child_locator')
        cmds.parent (chd,pnt)

        buf=cmds.listRelatives (jnt,p=1)
        if buf is not None:
            cmds.delete (cmds.parentConstraint (buf,pnt,w = 1))

        cmds.delete (cmds.parentConstraint (jnt,chd,w = 1))

        value=cmds.getAttr (chd[0]+'.r')

        cmds.setAttr (jnt+'.r',0,0,0)
        cmds.setAttr (jnt+'.jo',value[0][0],value[0][1],value[0][2])

        cmds.delete (pnt,chd)

        return
