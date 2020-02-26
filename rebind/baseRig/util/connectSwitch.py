#encoding:utf-8

import maya.cmds as cmds

class connectSwitch():
    def __init__(self):
        self.fkRng=cmds.createNode ('setRange')
        cmds.setAttr (self.fkRng+'.minX', 1)
        cmds.setAttr (self.fkRng+'.oldMaxX', 1)
        self.ikRng=cmds.createNode ('setRange')
        cmds.setAttr (self.ikRng+'.maxX', 1)
        cmds.setAttr (self.ikRng+'.oldMaxX', 1) 
        return
    
    def FKIKConstraint(self,driver,constraint): 
        attr=cmds.parentConstraint (constraint, q=True, wal=True)
        
        cmds.connectAttr (driver+'.FKIKBlend',self.fkRng+'.valueX',f= True)
        cmds.connectAttr (driver+'.FKIKBlend',self.ikRng+'.valueX',f= True)
        
        cmds.connectAttr (self.fkRng+'.outValueX',constraint+'.'+attr[0],f= True)
        cmds.connectAttr (self.ikRng+'.outValueX',constraint+'.'+attr[1],f= True)
     
        return
        
    def ConnectFKVisibility(self,driver,FkCon):
        cmds.connectAttr (driver+'.FKIKBlend',self.fkRng+'.valueX',f= True)
        cmds.connectAttr (driver+'.FKConVis',self.fkRng+'.maxX',f= True)
        cmds.connectAttr (self.fkRng+'.outValueX',FkCon+'.v',f= True)
    
    def ConnectIKVisibility(self,driver,IkCon):
        cmds.connectAttr (driver+'.FKIKBlend',self.ikRng+'.valueX',f= True)
        cmds.connectAttr (driver+'.IKConVis',self.ikRng+'.minX',f= True)
        cmds.connectAttr (self.ikRng+'.outValueX',IkCon+'.v',f= True)     
        return
  