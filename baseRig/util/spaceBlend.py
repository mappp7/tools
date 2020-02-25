#encoding=utf-8

import maya.cmds as cmds
from baseRig.util.defaultGroupNode import*
from baseRig.util.setUniqueName import*



class spaceBlend():

    def __init__(self):

        z=defaultGroupNode()
        z.createGroupNode()

        return

    def createMatrixNode(self,base,target):
        name=''

        if '_' in base:
            lst= base.split('_')
            for e in lst[:-1]:
                if len(name) !=0:
                    name =name+'_'+e
                else:
                    name=name+e
            name= name+'Space'
        else:
            name= base+'Space'

        tmp= cmds.spaceLocator (n=name)
        loc= setUniqueName (name,'LOC')
        tmp= cmds.group(loc,n=name)
        nul= setUniqueName (name,'NUL')

        mmx= cmds.createNode ('multMatrix')
        dcm= cmds.createNode ('decomposeMatrix')

        cmds.connectAttr (base+'.worldMatrix',mmx+'.matrixIn[0]',f=True)
        cmds.connectAttr (nul+'.parentInverseMatrix',mmx+'.matrixIn[1]',f=True)
        cmds.connectAttr (mmx+'.matrixSum',dcm+'.inputMatrix',f=True)

        cmds.connectAttr (dcm+'.outputTranslate',nul+'.t',f=True)
        cmds.connectAttr (dcm+'.outputRotate',nul+'.r',f=True)
        #cmds.connectAttr (dcm+'.outputScale',nul+'.s',f=True)
        cmds.connectAttr (dcm+'.outputShear',nul+'.shear',f=True)

        cmds.delete(cmds.parentConstraint (target,loc,w=True))

        cmds.parent (nul,'space_GRP')
        return loc

    def connectRotate(self,local,world,target):

        L_mmx= cmds.createNode ('multMatrix')
        L_dcm= cmds.createNode ('decomposeMatrix')

        W_mmx= cmds.createNode ('multMatrix')
        W_dcm= cmds.createNode ('decomposeMatrix')

        blend= cmds.createNode ('pairBlend')
        cmds.setAttr (blend+'.rotInterpolation', 1)

        cmds.connectAttr (local+'.worldMatrix',L_mmx+'.matrixIn[0]',f=True)
        cmds.connectAttr (target+'.parentInverseMatrix',L_mmx+'.matrixIn[1]',f=True)
        cmds.connectAttr (L_mmx+'.matrixSum',L_dcm+'.inputMatrix',f=True)

        cmds.connectAttr (world+'.worldMatrix',W_mmx+'.matrixIn[0]',f=True)
        cmds.connectAttr (target+'.parentInverseMatrix',W_mmx+'.matrixIn[1]',f=True)
        cmds.connectAttr (W_mmx+'.matrixSum',W_dcm+'.inputMatrix',f=True)

        cmds.connectAttr (L_dcm+'.outputRotate',blend+'.inRotate2',f=True)
        cmds.connectAttr (W_dcm+'.outputRotate',blend+'.inRotate1',f=True)

        cmds.connectAttr (blend+'.outRotate',target+'.r',f=True)


        return blend

    def connectTranslate(self,local,world,target):

        L_mmx= cmds.createNode ('multMatrix')
        L_dcm= cmds.createNode ('decomposeMatrix')

        W_mmx= cmds.createNode ('multMatrix')
        W_dcm= cmds.createNode ('decomposeMatrix')

        blend= cmds.createNode ('pairBlend')
        cmds.setAttr (blend+'.rotInterpolation', 1)

        cmds.connectAttr (local+'.worldMatrix',L_mmx+'.matrixIn[0]',f=True)
        cmds.connectAttr (target+'.parentInverseMatrix',L_mmx+'.matrixIn[1]',f=True)
        cmds.connectAttr (L_mmx+'.matrixSum',L_dcm+'.inputMatrix',f=True)

        cmds.connectAttr (world+'.worldMatrix',W_mmx+'.matrixIn[0]',f=True)
        cmds.connectAttr (target+'.parentInverseMatrix',W_mmx+'.matrixIn[1]',f=True)
        cmds.connectAttr (W_mmx+'.matrixSum',W_dcm+'.inputMatrix',f=True)

        cmds.connectAttr (L_dcm+'.outputTranslate',blend+'.inTranslate2',f=True)
        cmds.connectAttr (W_dcm+'.outputTranslate',blend+'.inTranslate1',f=True)

        cmds.connectAttr (blend+'.outTranslate',target+'.t',f=True)


        return blend

    def connectParent(self,local,world,target):

        L_mmx= cmds.createNode ('multMatrix')
        L_dcm= cmds.createNode ('decomposeMatrix')

        W_mmx= cmds.createNode ('multMatrix')
        W_dcm= cmds.createNode ('decomposeMatrix')

        blend= cmds.createNode ('pairBlend')
        cmds.setAttr (blend+'.rotInterpolation', 1)

        cmds.connectAttr (local+'.worldMatrix',L_mmx+'.matrixIn[0]',f=True)
        cmds.connectAttr (target+'.parentInverseMatrix',L_mmx+'.matrixIn[1]',f=True)
        cmds.connectAttr (L_mmx+'.matrixSum',L_dcm+'.inputMatrix',f=True)

        cmds.connectAttr (world+'.worldMatrix',W_mmx+'.matrixIn[0]',f=True)
        cmds.connectAttr (target+'.parentInverseMatrix',W_mmx+'.matrixIn[1]',f=True)
        cmds.connectAttr (W_mmx+'.matrixSum',W_dcm+'.inputMatrix',f=True)

        cmds.connectAttr (L_dcm+'.outputTranslate',blend+'.inTranslate2',f=True)
        cmds.connectAttr (W_dcm+'.outputTranslate',blend+'.inTranslate1',f=True)
        cmds.connectAttr (L_dcm+'.outputRotate',blend+'.inRotate2',f=True)
        cmds.connectAttr (W_dcm+'.outputRotate',blend+'.inRotate1',f=True)

        cmds.connectAttr (blend+'.outTranslate',target+'.t',f=True)
        cmds.connectAttr (blend+'.outRotate',target+'.r',f=True)

        return blend

    def rotateBlend(self,local,world,target):

        name=''

        if '_' in target:
            lst= target.split('_')
            for e in lst[:-1]:
                if len(name) !=0:
                    name =name+'_'+e
                else:
                    name=name+e
            name= name
        else:
            name= target

        tmp= cmds.group (target,n=name+'Space')
        nul= setUniqueName (tmp,'NUL')
        cmds.xform (nul,piv=(0,0,0))
        cmds.addAttr (target,ln ='localSpace',at='double',min= 0 ,max= 1 ,dv= 0)
        cmds.setAttr (target+'.localSpace',e=True,keyable=True)



        locateLocal= self.createMatrixNode (local,target)
        locateWorld= self.createMatrixNode (world,target)

        blend= self.connectRotate(locateLocal,locateWorld,nul)

        cmds.connectAttr (target+'.localSpace',blend+'.weight',f=True)


        return  [locateLocal,locateWorld]

    def translateBlend(self,local,world,target):

        name=''

        if '_' in target:
            lst= target.split('_')
            for e in lst[:-1]:
                if len(name) !=0:
                    name =name+'_'+e
                else:
                    name=name+e
            name= name
        else:
            name= target

        tmp= cmds.group (target,n=name+'Space')
        nul= setUniqueName (tmp,'NUL')
        cmds.xform (nul,piv=(0,0,0))
        cmds.addAttr (target,ln ='localSpace',at='double',min= 0 ,max= 1 ,dv= 0)
        cmds.setAttr (target+'.localSpace',e=True,keyable=True)



        locateLocal= self.createMatrixNode (local,target)
        locateWorld= self.createMatrixNode (world,target)

        blend= self.connectTranslate(locateLocal,locateWorld,nul)

        cmds.connectAttr (target+'.localSpace',blend+'.weight',f=True)


        return
    def parentBlend(self,local,world,target):

        name=''

        if '_' in target:
            lst= target.split('_')
            for e in lst[:-1]:
                if len(name) !=0:
                    name =name+'_'+e
                else:
                    name=name+e
            name= name
        else:
            name= target

        tmp= cmds.group (target,n=name+'Space')
        nul= setUniqueName (tmp,'NUL')
        cmds.xform (nul,piv=(0,0,0))
        cmds.addAttr (target,ln ='localSpace',at='double',min= 0 ,max= 1 ,dv= 0)
        cmds.setAttr (target+'.localSpace',e=True,keyable=True)



        locateLocal= self.createMatrixNode (local,target)
        locateWorld= self.createMatrixNode (world,target)

        blend= self.connectParent (locateLocal,locateWorld,nul)

        cmds.connectAttr (target+'.localSpace',blend+'.weight',f=True)


        return
