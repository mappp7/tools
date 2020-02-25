import maya.cmds as cmds
import maya.mel as mel

a = cmds.ls(sl=1)

for i in a:
    
    du = cmds.duplicate(i)[0]
    du2 = cmds.duplicate(i)[0]
    
    cmds.select(i.replace('CON','JNT'),du)
    mel.eval('delete`parentConstraint`')
    cmds.blendShape(du2,du,o='world',w=[0,1])
    
    shap = cmds.duplicate(du)[0]
    cmds.delete(du)
    cmds.delete(du2)
    cmds.delete(cmds.listRelatives(i,s=1))
    cmds.select(i.replace('CON','JNT'),i.replace('CON','NUL'))
    mel.eval('delete`parentConstraint`')
    for x in cmds.listRelatives(shap,s=1):
        cmds.parent(x,i,r=1,s=1)
    cmds.delete(shap)
        
