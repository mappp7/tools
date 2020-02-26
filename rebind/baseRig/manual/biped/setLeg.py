#encoding:utf-8
#==============================
#
#
#==============================

import maya.cmds as cmds
import maya.mel as mel
from baseRig.util.defaultGroupNode import*
from baseRig.util.controller import *
from baseRig.util.fkControllerMaker import*
from baseRig.util.ikControllerMaker import*
from baseRig.util.ikHandleMaker import*
from baseRig.util.setUniqueName import*
from baseRig.util.homeNul import*
from baseRig.util.connectSwitch import*
from baseRig.util.twistSetUp import *
from baseRig.util.spaceBlend import *
from baseRig.util.addRollingUp import *
from baseRig.util.stretchyLock import *
from baseRig.util.attach import*
from baseRig.util.noneFlip import *
from manual.biped.setSkinJoint import *

class setLeg():

    def __init__(self):
        z=defaultGroupNode()
        z.createGroupNode()

        return


    def setFK(self,*jnt):
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
        self.FkCon=fkControllerMaker( 'octagon', 'yellow', copied )

        for s in self.FkCon[0]:
            sha= cmds.listRelatives (s,s=True,typ='nurbsCurve')
            cmds.rotate (0,0,90,sha[0]+'.cv[*]',os=1)

        nul= cmds.listRelatives (self.FkCon[0][0],p=True)
        cmds.parent (nul,'FKControl_GRP')

        return self.FkCon[0]


    def setIK(self,*jnt):
        buffer=[]
        copied=[]

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

        cmds.parent(copied[0],'IKJoint_GRP')
        tmp= ikHandleMaker( copied[0], copied[-2], 'ikRPsolver' )
        hdl= cmds.rename (tmp[0],copied[-2].replace('JNT','HDL'))
        cmds.setAttr (hdl+'.v',0)
        cmds.parent (hdl,'auxillary_GRP')


        self.IkCon=ikControllerMaker( copied[-2] ,hdl)

        otherCon= fkControllerMaker( 'circle', 'yellow', [copied[-1]] )

        cmds.delete(otherCon[2])
        cmds.orientConstraint (otherCon[0],copied[-1],w=True)

        ballUp= controllerShape(otherCon[0][0].replace('_CON','RollUp_CON'),'hexagon', 'yellow' )
        ballUp_Nul= homeNul (ballUp)
        cmds.delete(cmds.pointConstraint (copied[-1],ballUp_Nul,w=True))
        cmds.rotate (90,0,0,ballUp+'.cv[*]',os=1)

        heelUp= controllerShape(self.IkCon[0][1].replace('_CON','RollUp_CON'),'hexagon', 'yellow' )
        heelUp_Nul= homeNul (heelUp)
        cmds.delete(cmds.pointConstraint (copied[-2],heelUp_Nul,offset=(0,-1,-1),w=True))
        cmds.rotate (90,0,0,heelUp+'.cv[*]',os=1)

        self.IkCon[0].append(str(otherCon[0][0]))
        self.IkCon[1].append(str(otherCon[1][0]))

        cmds.parent (self.IkCon[1][3],ballUp_Nul,heelUp_Nul,self.IkCon[0][0])

        #rolling up
        roll=addRollingUp()
        tmp=roll.rollUp(self.IkCon[0][1].replace('_CON','_LOC'),ballUp,heelUp)
        cmds.parent (tmp,'roll_GRP')

        #attach shoulder
        tmp=attachPart2(heelUp ,self.IkCon[1][3] , 'translate','rotate','scale','shear')
        cmds.parent(tmp,'attach_GRP')

        #connect stretchy
        st=stretchyLock()
        if cmds.objExists (self.IkCon[0][1].replace('_CON','_LOC')) is True:
            st.setStretchyLock(self.IkCon[0][1],self.IkCon[0][2],self.IkCon[0][1].replace('_CON','_LOC'),copied[0],copied[1],copied[2])
        else:
            tempString= cmds.spaceLocator (n=self.IkCon[0][1].replace('_CON','_LOC'))
            cmds.parent (tempString,self.IkCon[0][1].replace('_CON','Sub_CON'))
            st.setStretchyLock(self.IkCon[0][1],self.IkCon[0][2],self.IkCon[0][1].replace('_CON','_LOC'),copied[0],copied[1],copied[2])

        n=noneFlip()
        n.setup(self.IkCon[0][1].replace('_CON','_LOC'),copied[0],self.IkCon[0][2])
        cmds.rotate (90,0,0,self.IkCon[0][3]+'.cv[*]',os=1)

        return self.IkCon[0]

    def setBlend(self,hip,*jnt):
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


        #스위치 콘트롤러 생성
        prefix= copied[0].split('_')[0]
        buf= controllerShape(prefix+'_legBlend','fatCross','yellow')
        sw= setUniqueName(buf,'CON')
        swNul= homeNul(sw)
        sha= cmds.listRelatives (sw,s=True,typ='nurbsCurve')
        cmds.rotate (90,0,0,sha[0]+'.cv[*]',os=1)
        cmds.scale (0.5,0.5,0.5,sha[0]+'.cv[*]',os=1)

        v= cmds.getAttr (copied[0]+'.tx')
        cmds.delete(cmds.pointConstraint (copied[0],swNul,w=True,offset=(v/(abs(v)),1,0)))

        cmds.addAttr (sw,ln ='FKIKBlend',at='double',min= 0 ,max= 1 ,dv= 0)
        cmds.setAttr (sw+'.FKIKBlend',e=True,keyable=True)

        cmds.addAttr (sw,ln ='FKConVis',at='bool')
        cmds.setAttr (sw+'.FKConVis',e=True,keyable=True)

        cmds.addAttr (sw,ln ='IKConVis',at='bool')
        cmds.setAttr (sw+'.IKConVis',e=True,keyable=True)

        cmds.parent (swNul,'otherControl_GRP')

        for e in copied:
            if cmds.objExists (e.replace('Blend','FK')) :
                const.append(cmds.parentConstraint (e.replace('Blend','FK'),e,w= 1)[0])

            if cmds.objExists (e.replace('Blend','IK')):
                const.append(cmds.parentConstraint (e.replace('Blend','IK'),e,w= 1)[0])
        for e in const:
            buf= cmds.parentConstraint (e,q=True,tl=True)
            if len(buf) is 2:
                z=connectSwitch()
                z.FKIKConstraint(sw,e)
            else:
                cmds.delete(swNul)
                break
        for e in self.FkCon[0]:
            z=connectSwitch()
            z.ConnectFKVisibility(sw,e.replace('_CON','_NUL'))
        for e in self.IkCon[0]:
            z=connectSwitch()
            z.ConnectIKVisibility(sw,e.replace('_CON','_NUL'))

        #twist setup
        t=twistSetUp()
        t.blendTwist(hip,copied[0],copied[1],5)
        t.blendTwist(copied[0],copied[1],copied[2],5)

        #skin setup
        s=setSkinJoint()
        s.set()

        return copied
