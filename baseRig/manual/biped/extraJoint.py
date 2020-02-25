#encoding:utf-8
#==============================
#엑스트라 조인트를 만드는 스크립트이다.
#실행 명령어는
#ex=extraJoint()
#ex.arm()
#이며 기본 리깅에 추가로 필요한 팔 다리 목 손가락 숄더 조인트를 만든다.
#==============================

import maya.cmds as cmds
import maya.mel as mel
from baseRig.util.defaultGroupNode import*
from baseRig.util.setUniqueName import*


class extraJoint():

    def __init__(self):

        z=defaultGroupNode()
        z.createGroupNode()

        return
    def shoulder(self):
        cmds.select (cl=True)
        tmp= cmds.joint (n='L_template_shoulder',p=(1,13,0))
        shoulder=setUniqueName(tmp,'JNT')
        cmds.mirrorJoint (shoulder , mirrorYZ = True , mirrorBehavior = True , searchReplace = ('L_','R_'))


        return

    def arm(self):

        cmds.select (cl=True)
        tmp= cmds.joint (n='L_template_upArm',p=(2,10,0))
        upArm=setUniqueName(tmp,'JNT')

        tmp= cmds.joint (n='L_template_foreArm',p=(6,10,0))
        cmds.joint (upArm,e=True,zso=True,oj= 'xyz' ,sao='yup')

        foreArm=setUniqueName(tmp,'JNT')

        tmp= cmds.joint (n='L_template_hand',p=(10,10,0))
        hand=setUniqueName(tmp,'JNT')
        cmds.joint (foreArm,e=True,zso=True,oj= 'xyz' ,sao='yup')

        cmds.setAttr (foreArm+'.ry',-10)

        cmds.mirrorJoint (upArm , mirrorYZ = True , mirrorBehavior = True , searchReplace = ('L_','R_'))

        return

    def leg(self):

        cmds.select (cl=True)
        tmp= cmds.joint (n='L_template_leg',p=(1,11,0))
        leg=setUniqueName(tmp,'JNT')

        tmp= cmds.joint (n='L_template_lowLeg',p=(1,6,0))
        lowLeg=setUniqueName(tmp,'JNT')
        cmds.joint (leg,e=True,zso=True,oj= 'xyz' ,sao='yup')

        tmp= cmds.joint (n='L_template_foot',p=(1,1,0))
        foot=setUniqueName(tmp,'JNT')
        cmds.joint (lowLeg,e=True,zso=True,oj= 'xyz' ,sao='yup')

        tmp= cmds.joint (n='L_template_ball',p=(1,0,1))
        ball=setUniqueName(tmp,'JNT')
        cmds.joint (foot,e=True,zso=True,oj= 'xyz' ,sao='yup')

        tmp= cmds.joint (n='L_template_toe',p=(1,0,2))
        toe=setUniqueName(tmp,'JNT')
        cmds.joint (ball,e=True,zso=True,oj= 'xyz' ,sao='yup')

        cmds.setAttr (leg+'.rx',-10)
        cmds.setAttr (lowLeg+'.rx',20)
        cmds.setAttr (foot+'.rx',-10)
        cmds.mirrorJoint (leg , mirrorYZ = True , mirrorBehavior = True , searchReplace = ('L_','R_'))

        return

    def finger(self):
        #thumb
        cmds.select (cl=True)
        tmp= cmds.joint (n='L_template_thumb1',p=(0.1,0,0))
        thumb1=setUniqueName(tmp,'JNT')

        tmp= cmds.joint (n='L_template_thumb2',p=(0.45,0,0))
        thumb2=setUniqueName(tmp,'JNT')
        cmds.joint (thumb1,e=True,zso=True,oj= 'xyz' ,sao='yup')

        tmp= cmds.joint (n='L_template_thumb3',p=(0.75,0,0))
        thumb3=setUniqueName(tmp,'JNT')
        cmds.joint (thumb2,e=True,zso=True,oj= 'xyz' ,sao='yup')
        tmp= cmds.joint (n='L_template_thumb4',p=(1.05,0,0))
        thumb4=setUniqueName(tmp,'JNT')
        cmds.joint (thumb3,e=True,zso=True,oj= 'xyz' ,sao='yup')


        cmds.setAttr(thumb1+'.t',10,10,0.5)
        cmds.setAttr(thumb1+'.jointOrient',80,-10,-30)

        cmds.mirrorJoint (thumb1 , mirrorYZ = True , mirrorBehavior = True , searchReplace = ('L_','R_'))

        #index~pinky
        name= ['index','middle','ring','pinky']
        num= ['Palm','1','2','3','4']
        buffer=[]
        cmds.select (cl=True)
        for i in range(len(name)):
            for n in range(len(num)):
                tmp= cmds.joint (n='L_template_'+name[i]+num[n],p=(0.35,0,0),r=True)
                fin=setUniqueName(tmp,'JNT')
                buffer.append(fin)

            cmds.setAttr(buffer[0]+'.t',10,10,i*-0.2)
            cmds.mirrorJoint (buffer[0] , mirrorYZ = True , mirrorBehavior = True , searchReplace = ('L_','R_'))
            cmds.select (cl=True)
            buffer=[]

        return


    def neck(self):

        cmds.select (cl=True)
        tmp= cmds.joint (n='C_template_neck',p=(0,15,1))
        neck=setUniqueName(tmp,'JNT')

        tmp= cmds.joint (n='C_template_head',p=(0,15.5,1))
        head=setUniqueName(tmp,'JNT')
        cmds.joint (neck,e=True,zso=True,oj= 'xyz' ,sao='yup')

        tmp= cmds.joint (n='C_template_top',p=(0,17,1))
        top=setUniqueName(tmp,'JNT')
        cmds.joint (head,e=True,zso=True,oj= 'xyz' ,sao='yup')

        cmds.setAttr (neck+'.rx',10)
        cmds.setAttr (head+'.rx',-10)
        return
