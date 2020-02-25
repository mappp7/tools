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
from util.spaceBlend import *

class noneFlip():
    
    def __init__(self):
        
        z=defaultGroupNode()
        z.createGroupNode()
        
        return
    
    def setup(self,base,target,con):
        name=''
        
        if '_' in con:
            lst= con.split('_')
            for e in lst[:-1]:
                if len(name) !=0:
                    name =name+'_'+e
                else:
                    name=name+e
            name= name   
        else:
            name= con
            
        tmp= cmds.spaceLocator(n=name+'Aim')
        aim_locator= setUniqueName (tmp[0],'LOC')
        aim_nul= homeNul(aim_locator)
        
        tmp= cmds.spaceLocator(n=name+'Target')
        target_locator= setUniqueName (tmp[0],'LOC')
        target_nul= homeNul(target_locator)
        
        tmp= cmds.spaceLocator(n=name+'Offset')
        offset_locator= setUniqueName (tmp[0],'LOC')     
        offset_nul= homeNul(offset_locator)
        
        tmp= cmds.group (aim_nul,target_nul,n=name+'NoneFlip')
        group= setUniqueName (tmp,'GRP')     

        cmds.pointConstraint (base,aim_nul,w=True)
        cmds.pointConstraint (target,target_nul,w=True)
        cmds.delete(cmds.parentConstraint (con,offset_nul,w=True))
        
        
        cmds.aimConstraint (target,aim_locator,w=True,aim=[1,0,0],u=[0,1,0],wut='objectrotation',wu=[1,0,0],wuo=base)

        sp=spaceBlend()
        sp.parentBlend(offset_locator,'move_CON',con)

        
        cmds.parent (offset_nul,aim_locator)
        cmds.parent (group,'noneFlip_GRP')
        
           
        return [aim_locator,target_locator,offset_locator]
        