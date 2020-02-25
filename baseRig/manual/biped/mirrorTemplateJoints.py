#encoding:utf-8
#==============================
#
#
#==============================
import maya.cmds as cmds
import maya.mel as mel

from util.zeroOut import *

class mirrorTemplateJoints():
    '''
    정렬된 L_template 조인트를 반대쪽으로 미러링 / 제로 아웃 한다.
    '''
    
    
    def __init__(self):
        
        
        return
        
    #Left 조인트의 형태대로 Right 조인트를 재 배치 한다    
    def similarPose(self,jnt):
        
        tmp=[]
        parents=[]
        
        #called zeroOut class
        zero=zeroOut()
        
        if 'L_' in jnt:
            tmp = cmds.joint (jnt , n = 'replace_'+jnt)
            cmds.parent (tmp ,w =1)
            cmds.mirrorJoint (tmp , mirrorYZ = True , mirrorBehavior = True , searchReplace = ('L_','R_'))
            ls= cmds.listRelatives (jnt.replace ('L_','R_'),c=True)
            if ls is not None:
                cmds.parent (ls,w=True)
                cmds.delete (cmds.parentConstraint (tmp.replace ('L_','R_'),jnt.replace ('L_','R_'),w = 1))
                cmds.parent (ls,jnt.replace ('L_','R_'))
                cmds.delete (tmp,tmp.replace ('L_','R_'))
                zero.zeroOutJoint(jnt)
                zero.zeroOutJoint(jnt.replace ('L_','R_'))   
            else:
                cmds.delete (cmds.parentConstraint (tmp.replace ('L_','R_'),jnt.replace ('L_','R_'),w = 1))
                cmds.delete (tmp,tmp.replace ('L_','R_'))
                zero.zeroOutJoint(jnt)
                zero.zeroOutJoint(jnt.replace ('L_','R_'))
                         
        else:
            
            zero.zeroOutJoint(jnt)
                            
        return