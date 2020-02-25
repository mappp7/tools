import maya.cmds as cmds

def getAssetRoot():
    selected = cmds.ls(sl=True)[0]
    
    path=cmds.listRelatives (selected,f=1,p=1)
    if path == None:
        print 'root selected!!'
    
    else :
        
        list=path[0].split('|')
        
        #cmds.select(list[1])
        
        return list[1]