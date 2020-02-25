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
from util.spaceBlend import*

from manual.biped.setSpine import *
from manual.biped.setShoulder import *
from manual.biped.setArm import *
from manual.biped.setFinger import *
from manual.biped.setNeck import *
from manual.biped.setLeg import *
from manual.biped.setSkinJoint import *


class extraRig():
    
    def __init__(self):
        
        z=defaultGroupNode()
        z.createGroupNode()
        
        return
        
    def attachWindow(self):
        
        item = cmds.ls ('*Blend*JNT*',typ='joint')
        win = 'AttachWindow'
        if cmds.window (win,ex=True) is True:
            cmds.deleteUI (win)
        cmds.window (win,t=win,w=250,h=350,s=False)
        
        cmds.columnLayout(adj=True)
        cmds.optionMenuGrp('attachMenu',label='Select ',columnWidth=(1, 50) )
        for e in item:
            cmds.menuItem( label=e )
            
        cmds.setParent('..')
        
        cmds.columnLayout()
        

        cmds.button (l='Build It!',w=250,ann='Build The Extra BipedRig',
        c='eb=extraRig()\neb.build()')

        cmds.setParent('..')
        cmds.showWindow( win ) 
        
        return
        
    def build(self):
        
        selected= cmds.ls(sl=True)
        attach= cmds.optionMenuGrp('attachMenu',q=True,v= True)
            
        if 'neck' in selected[0]:  
            attach= cmds.optionMenuGrp('attachMenu',q=True,v= True)
            #neck
            neck=setNeck()
            IkneckCon= neck.setIK(selected[0],selected[1])
            neck.setBlend(attach,selected[0],selected[1])
            #attach neck    
            tmp=attachPart2( attach, IkneckCon[0].replace('_CON','_NUL'), 'translate','rotate','scale','shear')
            cmds.parent(tmp,'attach_GRP')
            tmp=attachPart2( IkneckCon[0], IkneckCon[1].replace('_CON','_NUL'), 'translate','rotate','scale','shear')
            cmds.parent(tmp,'attach_GRP')
            #local/world space blend
            sp=spaceBlend()
            sp.rotateBlend(IkneckCon[0],'move_CON',IkneckCon[1])
            cmds.parent (selected[0],'templateJoint_GRP')       
            return
        
        elif 'shoulder' in selected[0]:
            attach= cmds.optionMenuGrp('attachMenu',q=True,v= True)
            #shoulder        
            shoulder=setShoulder()
            FKshoulderCon= shoulder.setFK(selected[0])
            Left_shoulder_joint= shoulder.setBlend(selected[0])
            #attach shoulder
            tmp=attachPart2( attach, FKshoulderCon[0].replace('_CON','_NUL'), 'translate','rotate','scale','shear')
            cmds.parent(tmp,'attach_GRP')
            cmds.parent (selected[0],'templateJoint_GRP')       
            return
            
        elif 'upArm' in selected[0]:
            attach= cmds.optionMenuGrp('attachMenu',q=True,v= True)
            #arm
            arm=setArm()
            FKarmCon= arm.setFK(selected[0],selected[1],selected[2])
            IKarmCon= arm.setIK(selected[0],selected[1],selected[2])
            blendCon = arm.setBlend(attach,selected[0],selected[1],selected[2])[-1]
            print blendCon
            #query blendCon Name
            #tmp= cmds.connectionInfo (IKarmCon[0]+'.v',id= True)
            #if tmp is True:
            #    temp= cmds.listConnections (IKarmCon[0]+'.v')[0]
            #    blendCon= cmds.listConnections (temp+'.valueX')[0]
            #attach arm
            tmp=attachPart2( attach, FKarmCon[0].replace('_CON','_NUL'), 'translate','rotate','scale','shear')
            cmds.parent(tmp,'attach_GRP')
            tmp=attachPart2( attach, blendCon.replace('_CON','_NUL'), 'translate','rotate','scale','shear')
            cmds.parent(tmp,'attach_GRP')
            tmp=attachPart2( attach, FKarmCon[0].replace('_CON','_JNT').replace('FK','IK'), 'translate')
            cmds.parent(tmp,'attach_GRP')
            #local/world space blend
            sp=spaceBlend()
            sp.rotateBlend(attach,'move_CON',FKarmCon[0])
            sp.rotateBlend(FKarmCon[0],'root_CON',FKarmCon[2])
            cmds.parent (selected[0],'templateJoint_GRP')       
            return
            
        elif 'thumb' in selected[0]:
            attach= cmds.optionMenuGrp('attachMenu',q=True,v= True)
            #finger
            finger=setFinger()
            thumbCon= finger.setFK(selected)
            finger.setBlend(selected)
            #attach finger
            tmp=attachPart2( attach, thumbCon[0].replace('_CON','_NUL'), 'translate','rotate','scale','shear')
            cmds.parent(tmp,'attach_GRP')
            cmds.parent (selected[0],'templateJoint_GRP')       
            return
            
        elif 'index' in selected[0]:
            attach= cmds.optionMenuGrp('attachMenu',q=True,v= True)
            #finger
            finger=setFinger()
            thumbCon= finger.setFK(selected)
            finger.setBlend(selected)
            #attach finger
            tmp=attachPart2( attach, thumbCon[0].replace('_CON','_NUL'), 'translate','rotate','scale','shear')
            cmds.parent(tmp,'attach_GRP')
            cmds.parent (selected[0],'templateJoint_GRP')       
            return
            
        elif 'middle' in selected[0]:
            attach= cmds.optionMenuGrp('attachMenu',q=True,v= True)
            #finger
            finger=setFinger()
            thumbCon= finger.setFK(selected)
            finger.setBlend(selected)
            #attach finger
            tmp=attachPart2( attach, thumbCon[0].replace('_CON','_NUL'), 'translate','rotate','scale','shear')
            cmds.parent(tmp,'attach_GRP')
            cmds.parent (selected[0],'templateJoint_GRP')       
            return
            
        elif 'ring' in selected[0]:
            attach= cmds.optionMenuGrp('attachMenu',q=True,v= True)
            #finger
            finger=setFinger()
            thumbCon= finger.setFK(selected)
            finger.setBlend(selected)
            #attach finger
            tmp=attachPart2( attach, thumbCon[0].replace('_CON','_NUL'), 'translate','rotate','scale','shear')
            cmds.parent(tmp,'attach_GRP')
            cmds.parent (selected[0],'templateJoint_GRP')       
            return
            
        elif 'pinky' in selected[0]:
            attach= cmds.optionMenuGrp('attachMenu',q=True,v= True)
            #finger
            finger=setFinger()
            thumbCon= finger.setFK(selected)
            finger.setBlend(selected)
            #attach finger
            tmp=attachPart2( attach, thumbCon[0].replace('_CON','_NUL'), 'translate','rotate','scale','shear')
            cmds.parent(tmp,'attach_GRP')
            cmds.parent (selected[0],'templateJoint_GRP')       
            return
            
        elif 'leg' in selected[0]:
            attach= cmds.optionMenuGrp('attachMenu',q=True,v= True)
            #leg
            leg=setLeg()
            FKlegCon= leg.setFK(selected[0],selected[1],selected[2],selected[3])
            IKlegCon= leg.setIK(selected[0],selected[1],selected[2],selected[3])
            leg.setBlend(attach,selected[0],selected[1],selected[2],selected[3])
            #query blendCon Name
            tmp= cmds.connectionInfo (IKlegCon[0]+'.v',id= True)
            if tmp is True:
                temp= cmds.listConnections (IKlegCon[0]+'.v')[0]
                blendCon= cmds.listConnections (temp+'.valueX')[0]
            #attach leg
            tmp=attachPart2( attach, FKlegCon[0].replace('_CON','_NUL'), 'translate','rotate','scale','shear')
            cmds.parent(tmp,'attach_GRP')
            tmp=attachPart2( attach, FKlegCon[0].replace('_CON','_JNT').replace('FK','IK'), 'translate')
            cmds.parent(tmp,'attach_GRP')
            tmp=attachPart2( attach, blendCon.replace('_CON','_NUL'), 'translate','rotate','scale','shear')
            cmds.parent(tmp,'attach_GRP')
            cmds.parent (selected[0],'templateJoint_GRP')       
            return
                 
            
        return
        

