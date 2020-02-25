#encoding:utf-8
#=================================#
#
#
#=================================#

import maya.cmds as cmds
import maya.mel as mel
from util.defaultGroupNode import *

class importTemplate(): 
    '''
    2족 템플릿 조인트를 import 하는 클래스
    
    '''
    def __init__(self):
        z=defaultGroupNode()
        z.createGroupNode()
        return
        
    def simpleBiped(self):
        
        cmds.file ("/dexter/Cache_DATA/CRT/RiggingRnD/baseRig/manual/biped/template/simpleBiped.mb",i=True , loadReferenceDepth= "all")

        cmds.parent ('C_template_hip_JNT','L_template_shoulder_JNT','R_template_shoulder_JNT',
        'R_template_upArm_JNT','L_template_upArm_JNT','C_template_neck_JNT','L_template_leg_JNT',
        'R_template_leg_JNT','templateJoint_GRP')
        return
