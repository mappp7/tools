#encoding:utf-8
#==============================
#조인트1과 조인트 2의트위스트 값을   
#블랜드 하는 클래스.
#==============================

import maya.cmds as cmds
import maya.mel as mel
from util.defaultGroupNode import*
from util.setUniqueName import*
from util.homeNul import*
from util.zeroOut import *

class twistSetUp():
    '''
    트위스트 블랜드 세팅하는 클래스
    '''
    def __init__(self):

        z=defaultGroupNode()
        z.createGroupNode()
        
        return
    
    def blendTwist(self,base,start,end,num):
        
        name=''
        twist=[]
        twistNul=[]
        joints=[]
        

        if '_' in start:
            lst= start.split('_')
            for e in lst[:-1]:
                if len(name) !=0:
                    name =name+'_'+e
                else:
                    name=name+e
            name= name      
        else:
            name= start   
  
        tmp= cmds.spaceLocator (n=name+'Up')
        rotUpVec= setUniqueName (tmp[0],'LOC')
        rotUpNul= homeNul(rotUpVec)   
        cmds.parentConstraint (end,rotUpNul,w=True)
        
        v= cmds.getAttr (end+'.tx')

        #레프트 라이트에따라서 에임되는 수치가 다르다.
        #레프트는 -1 0 0
        #라이트는 1 0 0 이다.
        
        cmds.aimConstraint (start,rotUpVec,w=True,aim=[v/(abs(v))*-1,0,0],u=[0,1,0],wut='none')
        
        #지정된 갯수만큼 블랜드 로케이터를 생성 한다. 
        for i in range(num):
            tmp= cmds.spaceLocator (n=name+'Twist')
            twist.append (setUniqueName (tmp[0],'LOC'))
            twistNul.append (homeNul(twist[i]))
        
            
        tmp= cmds.group (twistNul,n=name+'TwistAim')
        twistAim= setUniqueName (tmp,'NUL')
        
        tmp= cmds.group (twistAim,n=name+'TwistGroup')
        twistGrp= setUniqueName (tmp,'NUL')
                
        cmds.delete(cmds.parentConstraint (start,twistGrp,w=True))
        cmds.parentConstraint (base,twistGrp,mo=True)
        cmds.aimConstraint (end,twistAim,w=True,aim=[v/(abs(v)),0,0],u=[0,1,0],wut='none')
        cmds.pointConstraint (start,twistAim,w=True)
        
        #페어블랜드 노드를 이용하여 
        #조인트의 늘어난 거리만큼 블랜드 로케이터들을 위치 시킨다. 
        for i in range(num):
            pbd= cmds.createNode ('pairBlend')
            cmds.connectAttr (end+'.t',pbd+'.inTranslate2',f= True)
            cmds.connectAttr (pbd+'.outTranslateX',twistNul[i]+'.tx',f= True)
            if i is 0:
                cmds.setAttr (pbd+'.weight',0.01)
            else:    
                cmds.setAttr (pbd+'.weight',(0.99/(num-1))*i)
        
        cmds.aimConstraint (start,twist[-1],w=True,aim=[v/(abs(v))*-1,0,0],u=[0,1,0],wut='objectrotation',wuo= rotUpVec)

        #페어블랜드로 로케이터들의 트위스트값을 
        #나눈다.
        for i in range(num-1):
            pbd= cmds.createNode ('pairBlend')
            cmds.connectAttr (twist[-1]+'.r',pbd+'.inRotate2',f= True)
            cmds.connectAttr (pbd+'.outRotate',twist[i]+'.r',f= True)
            cmds.setAttr (pbd+'.weight',(1.0/(num-1))*i)
            cmds.setAttr (pbd+'.rotInterpolation',1)
            
        
        #트위스트 블랜드 조인트를 생성 하여 
        #트위스트 로케이터와 컨스트레인 한다.
        z=zeroOut()
        for e in twist:
            tmp= cmds.createNode('joint',n= e.replace('_LOC',''))
            jnt= setUniqueName (tmp,'JNT')
            cmds.delete (cmds.parentConstraint (e,jnt,w= True)) 
            z.zeroOutJoint(jnt)
            cmds.parentConstraint (e,jnt,w= True) 
            cmds.parent (jnt,'BlendJoint_GRP')
            joints.append(jnt)
            
        cmds.parent(rotUpNul,twistGrp)
        cmds.parent(twistGrp,'twist_GRP') 
           
        return joints
        
        
