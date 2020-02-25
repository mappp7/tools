#encoding:utf-8
#==============================
#
#
#==============================

import maya.cmds as cmds
import maya.mel as mel
from util.defaultGroupNode import*
from util.fkControllerMaker import*
from util.setUniqueName import*
from util.homeNul import*
from manual.biped.setSkinJoint import *

class setFinger():
    
    def __init__(self):
        z=defaultGroupNode()
        z.createGroupNode()
          
        return
    
    
    def setFK(self,jnt):
        copied=[]
        
        for e in jnt:
            name=e.split('_')[0]+'_FK_'+e.split('_')[2]

            dup= cmds.duplicate (e,n=name,rr=True,rc=True)
            tmp=setUniqueName(dup[0],'JNT')
            par= cmds.listRelatives (tmp,p=True,typ='joint')
            chi= cmds.listRelatives (tmp,c=True,typ='joint')

            if par is not None:
                if len(copied) is not 0:    
                    cmds.parent (tmp,copied[-1])
                    if cmds.connectionInfo (tmp+'.inverseScale',id=True) is False:
                        cmds.connectAttr (copied[-1]+'.scale',tmp+'.inverseScale',f=True)
            if chi is not None:
                cmds.delete (chi)
                
            copied.append(tmp)    
            
        cmds.parent(copied[0],'FKJoint_GRP') 
        con=fkControllerMaker( 'octagon', 'yellow', copied )
        for s in con[0]:
            sha= cmds.listRelatives (s,s=True,typ='nurbsCurve')
            cmds.rotate (0,0,90,sha[0]+'.cv[*]',os=1)
            cmds.scale (0.25,0.25,0.25,sha[0]+'.cv[*]',os=1)
        nul= cmds.listRelatives (con[0][0],p=True)
        cmds.parent (nul,'FKControl_GRP')
                                  
        return con[0]
        
    def setBlend(self,jnt):
        buffer=[]
        copied=[]
        const=[]
        crv=''        
        tmp=cmds.listRelatives (jnt[0],c=1,ad=1)
        c=jnt[0]
        buffer.append(c)
        
        if tmp is not None:    
            for i in range(len(tmp)):
                
                if jnt[-1] in c:
                    break
                else:
                    c=cmds.listRelatives (c,c=True)
                    buffer.append(c[0])

        #조인트 복사 및 중복된 네임 정리   
        for e in buffer:
            name=e.split('_')[0]+'_Blend_'+e.split('_')[2]
            dup= cmds.duplicate (e,n=name,rr=True,rc=True)
            tmp= setUniqueName(dup[0],'JNT')
            par= cmds.listRelatives (tmp,p=True,typ='joint')
            chi= cmds.listRelatives (tmp,c=True,typ='joint')
            
            if par is not None:
                if len(copied) is not 0:    
                    cmds.parent (tmp,copied[-1])
                    if cmds.connectionInfo (tmp+'.inverseScale',id=True) is False:
                        cmds.connectAttr (copied[-1]+'.scale',tmp+'.inverseScale',f=True)
            if chi is not None:
                cmds.delete (chi)
            copied.append(tmp)
        cmds.parent(copied[0],'BlendJoint_GRP')                            
        

        for e in copied:
            if cmds.objExists (e.replace('Blend','FK')) :
                const.append(cmds.parentConstraint (e.replace('Blend','FK'),e,w= 1)[0])
            
            if cmds.objExists (e.replace('Blend','IK')):
                const.append(cmds.parentConstraint (e.replace('Blend','IK'),e,w= 1)[0])
                
        #skin setup
        s=setSkinJoint()
        s.set()
        return copied