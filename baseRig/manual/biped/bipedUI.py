#encoding:utf-8
#==============================
#
#
#==============================
import maya.cmds as cmds
from manual.biped.importTemplate import *
from manual.biped.mirrorTemplateJoints import *
from manual.biped.bipedRig import *
from manual.biped.extraJoint import *
from manual.biped.extraRig import *


class bipedUI():
   
        
    
    def __init__(self):
        
        return
    
    def mainUI(self):
        

        
        win= 'bipedRig_V01'
        
        if cmds.window (win,ex=True) is True:
            cmds.deleteUI (win)
	
        cmds.window (win,t=win,w=200,h=350,s=False)
        
        cmds.columnLayout (w=200,h=350,adj=False)
        
        cmds.frameLayout (l='Biped ')
        
        cmds.button (l='ImportTemplate',w=200,ann='Import The Biped Template Joint',
        c='i=importTemplate()\ni.simpleBiped()')
        
        cmds.button (l='Select MirrorJoint/ZeroOut',w=200,ann='ZeroOut The Selected Joints',
        c='m=mirrorTemplateJoints()\nls=cmds.ls(sl=True)\nfor e in ls:\n\tcmds.refresh()\n\tm.similarPose(e)')
        
        cmds.button (l='Build It!',w=200,ann='Build The BipedRig',
        c='b=bipedRig()\nb.build()')
        cmds.setParent ('..')
        
        cmds.frameLayout (l='Extra Joints')

        cmds.button (l='Create Extra Neck',w=200,
        c='ex=extraJoint()\nex.neck()')

        cmds.button (l='Create Extra Shoulder',w=200,
        c='ex=extraJoint()\nex.shoulder()')
                
        cmds.button (l='Create Extra Arm',w=200,
        c='ex=extraJoint()\nex.arm()')
        
        cmds.button (l='Create Extra Finger',w=200,
        c='ex=extraJoint()\nex.finger()')

        cmds.button (l='Create Extra Leg',w=200,
        c='ex=extraJoint()\nex.leg()')
        
        cmds.frameLayout (l='Extra Rig')

        cmds.button (l='Create Extra Rig',w=200,bgc=(1,1,1),
        c='er=extraRig()\ner.attachWindow()')
                
        cmds.showWindow (win)
        
        
        return
