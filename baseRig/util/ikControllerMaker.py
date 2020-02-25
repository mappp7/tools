#encoding:utf-8

import maya.cmds as cmds
from util.defaultGroupNode import*
from util.controller import*
from util.homeNul import*




def ikControllerMaker(target ,handle):
    
    z=defaultGroupNode()
    z.createGroupNode()
    
    par= cmds.listRelatives (target,p=True)

    loc= cmds.spaceLocator (n=handle.split('_HDL')[0]  + '_LOC')[0]
    loc_nul= cmds.group (loc,n=loc.replace('_LOC','Space_NUL'))
    sub= controllerShape( handle.split('_HDL')[0]  + 'Sub_CON', 'circle', 'yellow' )
    con= controllerShape( handle.split('_HDL')[0]  + '_CON', 'cube', 'yellow' )
    vec= controllerShape( handle.split('_HDL')[0]  + 'Vec_CON', 'sphere', 'yellow' )
    
    snul= homeNul(sub)
    cnul= homeNul(con)
    vnul= homeNul(vec)

    cmds.parent (loc_nul,sub)
    cmds.parent (snul,con)
    
    cmds.delete (cmds.pointConstraint (target,cnul,w=True))
    cmds.delete (cmds.orientConstraint (target,snul,w=True))
    cmds.delete (cmds.orientConstraint (con,loc_nul,w=True))
    cmds.delete (cmds.pointConstraint (par,vnul,w=True))

    cmds.parentConstraint (loc,handle,mo=True)  
    cmds.orientConstraint (loc,target,mo=True)
    cmds.poleVectorConstraint (vec,handle,w=1)
        
    cmds.rotate (0,0,90,sub+'.cv[*]',os=1)
    cmds.setAttr (loc+'.v',0)
    
    cmds.parent (cnul,vnul,'IKControl_GRP')
       
    return [sub,con,vec],[snul,cnul,vnul]
