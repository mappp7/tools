#encoding:utf-8
#==============================
#
#
#==============================

import maya.cmds as cmds
import maya.mel as mel
from baseRig.util.defaultGroupNode import*
from baseRig.util.ikHandleMaker import*
from baseRig.util.setUniqueName import*
from baseRig.util.controller import*
from baseRig.util.splineControllerMaker import*
from baseRig.util.connectSwitch import*
from baseRig.util.splineStretchy import*

from manual.biped.setSkinJoint import *


class setSpine():

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
            if i is 0:
                continue
            elif copied[i] is copied[1]:
                tmp=cmds.curve (n='C_IK_spineCurve',d=3,p=pos)
                crv= setUniqueName(tmp,'CRV')
            else:
                cmds.curve (crv,a=True,p=pos)

        cmds.parent(copied[0],'IKJoint_GRP')
        tmp= ikHandleMaker( copied[1], copied[-1], 'ikSplineSolver' ,crv )
        hdl= cmds.rename (tmp[0],copied[0].replace('JNT','HDL'))

        cmds.parent (crv,hdl,'auxillary_GRP')

        #컨트롤러 생성 / 스플라인 커브 컨트롤 셋
        cons=splineControllerMaker(crv,hdl)

        #스플라인 스트레치 연결
        st=splineStretchy()
        st.stretchy(cons[1],crv,copied[1],copied[2],copied[3])


        #힙 컨트롤러 생성
        buf=controllerShape('C_IK_hip','square','yellow')
        hip=setUniqueName(buf,'CON')
        hipNul= homeNul(hip)
        cmds.delete(cmds.parentConstraint(cons[0],hipNul,w=True))
        cmds.parentConstraint(hip,copied[0],mo=True)

        cmds.parent (hipNul,cons[0])

        cmds.orientConstraint(cons[1],copied[-1],mo=True)


        #루트 컨트롤러 생성
        cmds.delete(cmds.parentConstraint(cons[0],'root_NUL',w=True))


        cons.append(hip)

        #return control curves
        return cons


    def setBlend(self,*jnt):
        buffer=[]
        copied=[]
        const=[]
        crv=''
        tmp=cmds.listRelatives (jnt[0],c=1,ad=1)
        c=jnt[0]
        buffer.append(c)

        z=connectSwitch()

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
