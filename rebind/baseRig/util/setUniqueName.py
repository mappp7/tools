import maya.cmds as cmds
import maya.mel as mel

def setUniqueName(name,typ):
    i=0
    while i>=0:
        if i is 0:
            if cmds.objExists (name+'_'+typ) is False:
                res=cmds.rename (name,name+'_'+typ)
                break
            else:
                i=i+1
                
    
        elif cmds.objExists (name+str(i)+'_'+typ) is False:
            res=cmds.rename (name,name+str(i)+'_'+typ)
            break
        else:
            i=i+1 
    return res