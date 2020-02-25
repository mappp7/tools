#encoding:utf-8
#==============================
#
#
#==============================

import maya.cmds as cmds
import maya.mel as mel
from util.defaultGroupNode import*
from util.setUniqueName import*
from util.homeNul import*
from util.attach import*

class addRollingUp():
    
    def __init__(self):
        z=defaultGroupNode()
        z.createGroupNode()
        return
        
    def rollUp(self,driven,*driver):
        
        sum= cmds.createNode ('multMatrix')
        dcm= cmds.createNode ('decomposeMatrix')
        name=''
        i=0
        result=[]
        pnt= cmds.listRelatives (driven,p=True)[0]
        for e in driver:
            mmx= cmds.createNode ('multMatrix')
            name=''
            
            #이름 추출및 설정
            if '_' in e:
                lst= e.split('_')
                for r in lst[:-1]:
                    if len(name) !=0:
                        name =name+'_'+r
                    else:
                        name=name+r
                name= name
            else:
                name= e
                
            #오프셋 로케이터 생성
            tmp= cmds.spaceLocator (n=name+'Offset')[0]
            offset= setUniqueName (tmp,'LOC')
            tmp= cmds.spaceLocator (n=name+'Reference')[0]
            ref= setUniqueName (tmp,'LOC')
            tmp= cmds.group (offset,ref,n=name+'Space')
            grp= setUniqueName (tmp,'GRP')
            
            cmds.delete (cmds.parentConstraint (driven,offset,w=True))
            cmds.delete (cmds.parentConstraint (driven,ref,w=True))
            
            tmp=attachPart2 (pnt, grp,'translate','rotate','scale','shear')
            cmds.parent(tmp,'attach_GRP')
            
            tmp=attachPart2 (e, offset,'translate','rotate','scale','shear')
            cmds.parent(tmp,'attach_GRP')
            
            cmds.connectAttr (offset+'.worldMatrix[0]',mmx+'.matrixIn[0]',f=True)
            cmds.connectAttr (ref+'.worldInverseMatrix[0]',mmx+'.matrixIn[1]',f=True)
            
            cmds.connectAttr (mmx+'.matrixSum',sum+'.matrixIn['+str(i)+']',f=True)
            result.append(grp)
            i+=1
        cmds.connectAttr (sum+'.matrixSum',dcm+'.inputMatrix',f=True)
        cmds.connectAttr (dcm+'.outputTranslate',driven+'.t',f=True)
        cmds.connectAttr (dcm+'.outputRotate',driven+'.r',f=True)
        
        return   result 


        
