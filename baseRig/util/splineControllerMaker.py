#encoding:utf-8

import maya.cmds as cmds
from util.defaultGroupNode import*
from util.controller import*
from util.homeNul import*
from util.setUpCurve import*
from util.setUniqueName import*




def splineControllerMaker(crv,handle):

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
        
    low= controllerShape('C_IK_lowBody','cube','yellow')
    lowBody=setUniqueName(low,'CON')

    up= controllerShape( 'C_IK_upBody','cube','yellow')   
    upBody=setUniqueName(up,'CON')  
    
    lowNul= homeNul(lowBody)
    upNul= homeNul(upBody)        
    cmds.parent(upNul,lowNul,'IKControl_GRP')

    cmds.delete(cmds.parentConstraint(list[0],lowNul,w=True))
    cmds.delete(cmds.parentConstraint(list[-1],upNul,w=True))
    
    for i in range(len(list)):
        chd= cmds.listRelatives(list[i],c=True)
        cmds.parent(chd[0],w=True)
        if i <= 1:
            mmx=cmds.createNode ('multMatrix')
            dcm=cmds.createNode ('decomposeMatrix')
            cmds.connectAttr (lowBody+'.worldMatrix',mmx+'.matrixIn[0]',f=True)
            cmds.connectAttr (list[i]+'.parentInverseMatrix',mmx+'.matrixIn[1]',f=True)
            cmds.connectAttr (mmx+'.matrixSum',dcm+'.inputMatrix',f=True)
            cmds.connectAttr (dcm+'.outputTranslate',list[i]+'.t',f=True)
            cmds.connectAttr (dcm+'.outputRotate',list[i]+'.r',f=True)
            cmds.parent(chd,list[i])
        else:
            mmx=cmds.createNode ('multMatrix')
            dcm=cmds.createNode ('decomposeMatrix')
            cmds.connectAttr (upBody+'.worldMatrix',mmx+'.matrixIn[0]',f=True)
            cmds.connectAttr (list[i]+'.parentInverseMatrix',mmx+'.matrixIn[1]',f=True)
            cmds.connectAttr (mmx+'.matrixSum',dcm+'.inputMatrix',f=True)
            cmds.connectAttr (dcm+'.outputTranslate',list[i]+'.t',f=True)
            cmds.connectAttr (dcm+'.outputRotate',list[i]+'.r',f=True)    
            cmds.parent(chd,list[i])

    cmds.setAttr (handle+'.dTwistControlEnable',1)
    cmds.setAttr (handle+'.dWorldUpType',4)
    cmds.setAttr (handle+'.dWorldUpVector', 0,0,1)
    cmds.setAttr (handle+'.dWorldUpVectorEnd',0,0,1)
    cmds.connectAttr (lowBody+'.worldMatrix[0]',handle+'.dWorldUpMatrix',f=1)
    cmds.connectAttr (upBody+'.worldMatrix[0]',handle+'.dWorldUpMatrixEnd',f=1)
    
    #FK컨트롤러 생성및 세팅
    sp1= controllerShape('C_IK_upBodyRot1','circle','yellow')
    spine1=setUniqueName(sp1,'CON')
    spNul1= homeNul(spine1)        

    sp2= controllerShape('C_IK_upBodyRot2','circle','yellow')
    spine2=setUniqueName(sp2,'CON')
    spNul2= homeNul(spine2)        

    cmds.delete(cmds.parentConstraint(list[1].replace('NUL','LOC'),spNul1,w=True))
    cmds.delete(cmds.parentConstraint(list[2].replace('NUL','LOC'),spNul2,w=True))
    cmds.parent (spNul2,spine1)
    cmds.parent(spNul1,'IKControl_GRP')

    
    return [lowBody,upBody]