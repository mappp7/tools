#encoding:utf-8
#==============================
#
#
#==============================

import maya.cmds as cmds
import maya.mel as mel
from util.defaultGroupNode import*
from util.ikHandleMaker import*
from util.setUniqueName import*
from util.controller import*
from util.neckControllerMaker import*
from util.twistSetUp import*
from util.spaceBlend import *
from util.splineStretchy import *
from manual.biped.setSkinJoint import *


class setNeck():
    
    def __init__(self):
        z=defaultGroupNode()
        z.createGroupNode()
          
        return
    
    
    def setIK(self,*jnt):
        buffer=[]
        copied=[]
        
        crv=''        
        tmp=cmds.listRelatives (jnt[0],c=1,ad=1)
        c=jnt[0]
        buffer.append(c)
        
        for i in range(len(tmp)):
            
            if jnt[-1] in c:
                break
            else:
                c=cmds.listRelatives (c,c=True)
                buffer.append(c[0])

        #조인트 복사 및 중복된 네임 정리   
        for e in buffer:
            name=e.split('_')[0]+'_IK_'+e.split('_')[2]
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
        
        #커브 그리기
        for i in range(len(copied)):
            pos=cmds.xform(copied[i],q=True,ws=True,t=True)
            if copied[i] is copied[0]:
                tmp=cmds.curve (n='C_IK_spineCurve',d=1,p=pos)
                crv= setUniqueName(tmp,'CRV')
            else:
                cmds.curve (crv,a=True,p=pos)
        
        cmds.parent(copied[0],'IKJoint_GRP')                            
        tmp= ikHandleMaker( copied[0], copied[-1], 'ikSplineSolver' ,crv )
        hdl= cmds.rename (tmp[0],copied[0].replace('JNT','HDL'))
        
        cmds.parent (crv,hdl,'auxillary_GRP')    
        
        #컨트롤러 생성 / 스플라인 커브 컨트롤 셋
        self.IkCon=neckControllerMaker(crv,hdl)
        
        cmds.delete(cmds.orientConstraint (jnt[1],self.IkCon[1].replace('_CON','_NUL'),w=True,o=(0,-90,-90)))        
        cmds.orientConstraint (self.IkCon[1],copied[1],mo=True)
        
        #스플라인 스트레치 연결
        st=splineStretchy()
        st.stretchy(self.IkCon[1],crv,copied[0])
        
        return self.IkCon
        
    def setBlend(self,chest,*jnt):
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
        
        #twist setup        
        t=twistSetUp()
        t.blendTwist(chest,copied[0],copied[1],3) 
        
        #skin setup
        s=setSkinJoint()
        s.set()
               
        return copied