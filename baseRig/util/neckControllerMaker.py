#encoding:utf-8

import maya.cmds as cmds
from baseRig.util.defaultGroupNode import*
from baseRig.util.controller import*
from baseRig.util.homeNul import*
from baseRig.util.setUpCurve import*
from baseRig.util.setUniqueName import*




def neckControllerMaker(crv,handle):

    list=[]

    #씬안에 필요한 group node생성
    z=defaultGroupNode()
    z.createGroupNode()

    par= cmds.listRelatives (crv,p=True)
    locs= setUpCurve (crv)


    for e in locs:
        tmp= cmds.rename(e,e.replace('_LOC','Attach'))
        name=setUniqueName(tmp,'LOC')
        nul= homeNul(name)
        cmds.parent(nul,'attach_GRP')
        list.append(nul)

    low= controllerShape('C_IK_neck','cube','yellow')
    neck=setUniqueName(low,'CON')

    up= controllerShape( 'C_IK_head','cube','yellow')
    head=setUniqueName(up,'CON')

    neckNul= homeNul(neck)
    headNul= homeNul(head)
    cmds.parent(headNul,neckNul,'IKControl_GRP')

    cmds.delete(cmds.parentConstraint(list[0],neckNul,w=True))
    cmds.delete(cmds.parentConstraint(list[-1],headNul,w=True))

    for i in range(len(list)):
        chd= cmds.listRelatives(list[i],c=True)
        cmds.parent(chd[0],w=True)
        if i == 0:
            mmx=cmds.createNode ('multMatrix')
            dcm=cmds.createNode ('decomposeMatrix')
            cmds.connectAttr (neck+'.worldMatrix',mmx+'.matrixIn[0]',f=True)
            cmds.connectAttr (list[i]+'.parentInverseMatrix',mmx+'.matrixIn[1]',f=True)
            cmds.connectAttr (mmx+'.matrixSum',dcm+'.inputMatrix',f=True)
            cmds.connectAttr (dcm+'.outputTranslate',list[i]+'.t',f=True)
            cmds.connectAttr (dcm+'.outputRotate',list[i]+'.r',f=True)
            cmds.parent(chd,list[i])
        else:
            mmx=cmds.createNode ('multMatrix')
            dcm=cmds.createNode ('decomposeMatrix')
            cmds.connectAttr (head+'.worldMatrix',mmx+'.matrixIn[0]',f=True)
            cmds.connectAttr (list[i]+'.parentInverseMatrix',mmx+'.matrixIn[1]',f=True)
            cmds.connectAttr (mmx+'.matrixSum',dcm+'.inputMatrix',f=True)
            cmds.connectAttr (dcm+'.outputTranslate',list[i]+'.t',f=True)
            cmds.connectAttr (dcm+'.outputRotate',list[i]+'.r',f=True)
            cmds.parent(chd,list[i])

    cmds.setAttr (handle+'.dTwistControlEnable',1)
    cmds.setAttr (handle+'.dWorldUpType',3)
    cmds.setAttr (handle+'.dWorldUpVector', 0,0,1)
    cmds.connectAttr (neck+'.worldMatrix[0]',handle+'.dWorldUpMatrix',f=1)


    return [neck,head]
