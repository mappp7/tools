import maya.cmds as cmds

a = cmds.ls(sl=1)

for i in a:
    
    if cmds.getAttr(i+'.overrideEnabled'):
        shapes = cmds.listRelatives(i,s=1)
        for s in shapes:
            id = cmds.getAttr(i+'.overrideColor')
            cmds.setAttr(s+'.overrideEnabled' , 1)
            cmds.setAttr(s+'.overrideColor' , id)
            cmds.setAttr(i+'.overrideEnabled' , 0)
        
        